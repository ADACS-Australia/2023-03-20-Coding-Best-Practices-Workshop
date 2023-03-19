---
title: "Proof of concept code"
teaching: 30
exercises: 30
questions:
- "Where do we start?"
objectives:
- "Create a common starting point for this workshop"
keypoints:
- A proof of concept is the first thing that works
- A little extra effort can give you a piece of code you can be proud of
---

With the following requirements, we quickly pulled together some code that works.
- Stars should have randomized sky positions around the Andromeda galaxy
- Positions should fall within 1 degree of the central location
- Each star should have a unique ID
- The star ID and position should be saved in a csv file to be analyzed by other programs

The first iteration of our code is shown below.
It was written in a stream-of-conscious mode with a focus on getting a minimum working example that proves that the work can be done.

~~~
# Determine Andromeda location in ra/dec degrees

# from wikipedia
ra = '00:42:44.3'
dec = '41:16:09'

# convert to decimal degrees
from math import *

d, m, s = dec.split(':')
dec = int(d)+int(m)/60+float(s)/3600

h, m, s = ra.split(':')
ra = 15*(int(h)+int(m)/60+float(s)/3600)
ra = ra/cos(dec*pi/180)

nsrc = 1_000_000

# make 1000 stars within 1 degree of Andromeda
from random import *
ras = []
decs = []
for i in range(nsrc):
    ras.append(ra + uniform(-1,1))
    decs.append(dec + uniform(-1,1))


# now write these to a csv file for use by my other program
f = open('catalog.csv','w')
print("id,ra,dec", file=f)
for i in range(nsrc):
    print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)

~~~
{: .language-python}

This code runs without any obvious error, and creates a file called `catalog.csv`.
When we look at the file we see the following first few lines:

~~~
id,ra,dec
0000000,    13.699211,    40.583382
0000001,    14.198856,    40.349619
0000002,    13.514020,    41.903174
0000003,    14.050112,    40.359027
0000004,    13.355615,    41.967990
0000005,    13.258444,    41.896025
0000006,    14.815417,    40.406458
0000007,    13.745500,    41.816140
0000008,    14.641606,    40.451957
0000009,    13.374090,    42.162902
0000010,    14.704210,    41.757121
~~~
{: .output}

We could use another python script, a jupyter notebook, TOPCAT, or even Excel to plot the data above, and use this to further verify that the data are broadly as expected.
The figure below was made with a different python script.

![POC_Catalog]({{ page.root}}{% link fig/POC_Catalog.png %})

Congratulations, we now have a proof of concept code.
It's not perfect, but it proves to us that our ideas could actually work.
Given that this is our first working example of the code, it would be good to set a checkpoint so that if we were to break something in future, we can come back to this version.
We should now think about setting up a project, and keeping our work under version control.

> ## Validate the POC
> Copy the above code into a new file `sky_sim.py`, and verify that it works as intended.
>
> If you have problems let us know in the [etherpad]({{site.ether_pad}})
{: .challenge}

By confirming that the code works we have performed some validation testing. 
We'll look at how to automate this in a later lesson.