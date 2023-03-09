#! /usr/bin/env python

import argparse
import math
import sys


def area_perimeter_ngon(n=3):
  """
  Compute the area and perimeter of a regular N-gon
  inscribed within a cirlce of radius 1.
  """
  # Complain if n<3 because those shapes don't exist
  if n<3:
    raise AssertionError(f"Cannot compute area for ngon when n={n}")
  r = 1 # Radius of our circle
  perimeter = 2*n*r * math.sin(math.pi/n)
  area = 0.5 * n * r**2 * math.sin(2*math.pi/n)
  return area, perimeter


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('n', default=None, type=int, help='Number of angles in our n-gon')
  parser.add_argument('--out', dest='out', default='output.txt', type=str, help='output file')
  options = parser.parse_args()
  area, perimeter = area_perimeter_ngon(options.n)
 
  with open(options.out,'w') as f:
    f.write(f'A {options.n}-gon inscribed within a unit circle has an area of {area:5.3f} and a perimeter of {perimeter:5.3f}\n')
