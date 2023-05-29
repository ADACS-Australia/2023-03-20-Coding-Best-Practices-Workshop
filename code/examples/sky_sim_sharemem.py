#! /usr/bin/env python
# Demonstrate that we can simulate a catalogue of stars on the sky

# Determine Andromeda location in ra/dec degrees
import math
import numpy as np
import multiprocessing
from multiprocessing.shared_memory import SharedMemory
import uuid
import sys

NSRC = 1_000_000
mem_id = None


def init(mem):
    global mem_id
    mem_id = mem
    return


def get_radec():
    # from wikipedia
    ra = '00:42:44.3'
    dec = '41:16:09'

    d, m, s = dec.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = ra.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/math.cos(dec*math.pi/180)
    return ra,dec


def make_stars(args):
    """
    """
    ra, dec, shape, nsrc, job_id = args    
    # Find the shared memory and create a numpy array interface
    shmem = SharedMemory(name=f'radec_{mem_id}', create=False)
    radec = np.ndarray(shape, buffer=shmem.buf, dtype=np.float64)

    # make nsrc stars within 1 degree of ra/dec
    ras = np.random.uniform(ra-1, ra+1, size=nsrc)
    decs = np.random.uniform(dec-1, dec+1, size=nsrc)

    start = job_id * nsrc
    end = start + nsrc
    radec[0, start:end] = ras
    radec[1, start:end] = decs
    return


def make_stars_sharemem(ra, dec, nsrc=NSRC, cores=None):

    # By default use all available cores
    if cores is None:
        cores = multiprocessing.cpu_count()

    # 20 jobs each doing 1/20th of the sources
    args = [(ra, dec, (2, nsrc), nsrc//20, i) for i in range(20)]

    exit = False
    try:
        # set up the shared memory
        global mem_id
        mem_id = str(uuid.uuid4())


        nbytes = 2 * nsrc * np.float64(1).nbytes
        radec = SharedMemory(name=f'radec_{mem_id}', create=True, size=nbytes)

        # creating a new process will start a new python interpreter
        # on linux the new process is created using fork, which copies the memory
        # However on win/mac the new process is created using spawn, which does
        # not copy the memory. We therefore have to initialize the new process
        # and tell it what the value of mem_id is.
        method = 'spawn'
        if sys.platform.startswith('linux'):
            method = 'fork'
        # start a new process for each task, hopefully to reduce residual
        # memory use
        ctx = multiprocessing.get_context(method)
        pool = ctx.Pool(processes=cores, maxtasksperchild=1,
                        initializer=init, initargs=(mem_id,)
                        # ^-pass mem_id to the function 'init' when creating a new process
                        )
        try:
            pool.map_async(make_stars, args, chunksize=1).get(timeout=10_000)
        except KeyboardInterrupt:
            print("Caught kbd interrupt")
            pool.close()
            exit = True
        else:
            pool.close()
            pool.join()
            # make sure to .copy() or the data will dissappear when you unlink the shared memory
            local_radec = np.ndarray((2, nsrc), buffer=radec.buf,
                                     dtype=np.float64).copy()
    finally:
        radec.close()
        radec.unlink()
        if exit:
            sys.exit(1)
    return local_radec


if __name__ == "__main__":
    ra, dec = get_radec()
    pos = make_stars_sharemem(ra, dec, NSRC, 2)
    # now write these to a csv file for use by my other program
    with open('catalog.csv', 'w') as f:
        print("id,ra,dec", file=f)
        np.savetxt(f, np.column_stack((np.arange(NSRC), pos[0, :].T, pos[1, :].T)),fmt='%07d, %12f, %12f')
