#! /usr/bin/env python
# Demonstrate that we can simulate a catalogue of stars on the sky

# Determine Andromeda location in ra/dec degrees
import math
import numpy as np
import random

# from wikipedia
ra = '00:42:44.3'
dec = '41:16:09'

d, m, s = dec.split(':')
dec = int(d)+int(m)/60+float(s)/3600

h, m, s = ra.split(':')
ra = 15*(int(h)+int(m)/60+float(s)/3600)
ra = ra/math.cos(dec*math.pi/180)

nsrc = 1_000_000

# # make 1000 stars within 1 degree of Andromeda
# ras = []
# decs = []
# for i in range(nsrc):
#     ras.append(ra + random.uniform(-1,1))
#     decs.append(dec + random.uniform(-1,1))

# make 1000 stars within 1 degree of Andromeda
ra_offsets = np.random.uniform(ra-1, ra+1, size=nsrc)
dec_offsets = np.random.uniform(dec-1, dec+1, size=nsrc)

# Results in an effective copy of the offset arrays
ras = ra + ra_offsets
decs = dec + dec_offsets


# now write these to a csv file for use by my other program
with open('catalog.csv', 'w') as f:
    print("id,ra,dec", file=f)
    np.savetxt(f, np.column_stack((np.arange(nsrc), ras, decs)),fmt='%07d, %12f, %12f')
#     for i in range(nsrc):
#         print("{07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)
