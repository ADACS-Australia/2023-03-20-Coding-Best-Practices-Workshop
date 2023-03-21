#! /usr/bin/env python
# Demonstrate that we can simulate a catalogue of stars on the sky

# Determine Andromeda location in ra/dec degrees
import math
import numpy as np
import multiprocessing
import sys

NSRC = 1_000_000


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
    #unpack the arguments
    ra, dec, nsrc = args
    # create an empy array for our results
    radec = np.empty((2,nsrc))

    # make nsrc stars within 1 degree of ra/dec
    radec[0,:] = np.random.uniform(ra-1, ra+1, size=nsrc)
    radec[1,:] = np.random.uniform(dec-1, dec+1, size=nsrc)
    
    # return our results
    return radec

def make_stars_parallel(ra, dec, nsrc=NSRC, cores=None):
    
    # By default use all available cores
    if cores is None:
        cores = multiprocessing.cpu_count()
    

    # 20 jobs each doing 1/20th of the sources
    group_size = nsrc//20
    args = [(ra, dec, group_size) for _ in range(20)]


    # start a new process for each task, hopefully to reduce residual
    # memory use
    ctx = multiprocessing.get_context()
    pool = ctx.Pool(processes=cores, maxtasksperchild=1)

    try:
        # call make_posisions(a) for each a in args
        results = pool.map(make_stars, args, chunksize=1)
    except KeyboardInterrupt:
        # stop all the processes if the user calls the kbd interrupt
        print("Caught kbd interrupt")
        pool.close()
        sys.exit(1)
    else:
        # join the pool means wait until there are results
        pool.close()
        pool.join()

        # crete an empty array to hold our results
        radec = np.empty((2,nsrc),dtype=np.float64)

        # iterate over the results (a list of whatever was returned from make_stars)
        for i,r in enumerate(results):
            # store the returned results in the right place in our array
            start = i*group_size
            end = start + group_size
            radec[:,start:end] = r
            
    return radec

if __name__ == "__main__":
    ra,dec = get_radec()
    pos = make_stars_parallel(ra, dec, NSRC, 2)
    # now write these to a csv file for use by my other program
    with open('catalog.csv', 'w') as f:
        print("id,ra,dec", file=f)
        np.savetxt(f, np.column_stack((np.arange(NSRC), pos[0,:].T, pos[1,:].T)),fmt='%07d, %12f, %12f')
