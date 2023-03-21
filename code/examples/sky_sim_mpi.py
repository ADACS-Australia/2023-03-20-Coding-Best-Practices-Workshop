#! /usr/bin/env python
# Demonstrate that we can simulate a catalogue of stars on the sky

# Determine Andromeda location in ra/dec degrees
import math
import numpy as np
from mpi4py import MPI
import glob
import os

NSRC = 1_000_000

comm = MPI.COMM_WORLD
# rank of current process
rank = comm.Get_rank()
# total number of processes that are running
size = comm.Get_size()



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


def make_stars(ra, dec, nsrc, outfile):
    """
    """

    # make nsrc stars within 1 degree of ra/dec
    ras = np.random.uniform(ra-1, ra+1, size=nsrc)
    decs = np.random.uniform(dec-1, dec+1, size=nsrc)
    
    # return our results
    with open('{0}_part{1:03d}'.format(outfile, rank), 'w') as f:
        if rank == 0:
            print("id,ra,dec", file=f)
        np.savetxt(f, np.column_stack((np.arange(nsrc), ras, decs)),fmt='%07d, %12f, %12f')
    return


if __name__ == "__main__":

    ra,dec = get_radec()
    outfile = "catalog_mpi.csv"
    group_size = NSRC // size
    make_stars(ra, dec, group_size, outfile)
    # synchronize before moving on
    comm.Barrier()
    # Select one process to collate all the files
    if rank == 0:
        files = sorted(glob.glob("{0}_part*".format(outfile)))
        with open(outfile,'w') as wfile:
            for rfile in files:
                for l in open(rfile).readlines():
                    print(l.strip(),file=wfile)
                # os.remove(rfile)

