#! /usr/bin/env python
"""
Simulate a catalog of stars near to the Andromeda constellation
"""

import argparse
import math
import random

NSRC = 1_000_000

def get_radec():
    """
    Generate the ra/dec coordinates of Andromeda
    in decimal degrees.

    Returns
    -------
    ra : float
        The RA, in degrees, for Andromeda
    dec : float
        The DEC, in degrees for Andromeda
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


def make_positions(ra,dec, nsrc=NSRC):
    """
    Generate NSRC stars within 1 degree of the given ra/dec

    Parameters
    ----------
    ra,dec : float
        The ra and dec in degrees for the central location.
    nsrc : int
        The number of star locations to generate
    
    Returns
    -------
    ras, decs : list
        A list of ra and dec coordinates.
    """
    ras = []
    decs = []
    for _ in range(nsrc):
        ras.append(ra + random.uniform(-1,1))
        decs.append(dec + random.uniform(-1,1))
    return ras, decs


def skysim_parser():
    """
    Configure the argparse for skysim

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for skysim.
    """
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-')
    parser.add_argument('--ra', dest = 'ra', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--dec', dest = 'dec', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help='destination for the output catalog')
    return parser

if __name__ == "__main__":
    parser = skysim_parser()
    options = parser.parse_args()
    if None in [options.ra, options.dec]:
        ra, dec = get_radec()
    else:
        ra = options.ra
        dec = options.dec
    
    ras, decs = make_positions(ra,dec)
    # now write these to a csv file for use by my other program
    with open(options.out,'w') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
    print(f"Wrote {options.out}")