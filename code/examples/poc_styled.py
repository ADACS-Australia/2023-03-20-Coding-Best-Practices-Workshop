#! /usr/bin/env python
"""
Simulate a catalog of stars near to the Andromeda constellation
"""

import math
import random

NSRC = 1_000_000

def get_radec():
    """
    Generate the ra/dec coordinates of Andromeda
    in decimal degrees.
    """
    # from wikipedia
    andromeda_ra = '00:42:44.3'
    andromeda_dec = '41:16:09'

    d, m, s = andromeda_dec.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = andromeda_ra.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/math.cos(dec*math.pi/180)
    return ra,dec


def make_positions(ra,dec):
    """
    Generate NSRC stars within 1 degree of the given ra/dec
    """
    ras = []
    decs = []
    for _ in range(NSRC):
        ras.append(ra + random.uniform(-1,1))
        decs.append(dec + random.uniform(-1,1))
    return ras, decs


if __name__ == "__main__":
    ra, dec = get_radec()
    ras, decs = make_positions(ra,dec)
    # now write these to a csv file for use by my other program
    with open('catalog.csv','w') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
    print("Wrote catalog.csv")