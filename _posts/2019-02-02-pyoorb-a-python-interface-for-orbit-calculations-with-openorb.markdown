---
author: mommermi
date: 2019-02-02 21:37:21+00:00
layout: post
title: pyoorb - A Python interface for orbit calculations with OpenOrb
description: |
  This post introduces pyoorb, a Python interface to the OpenOrb package
  for ephemerides calculations and orbit transformations.
categories:
- software
tags:
- code
---

[OpenOrb](https://github.com/oorb/oorb) is a software suite for performing all sorts of orbit calculations, including orbit integration, ephemerides calculations, and ranging to determine orbit solutions based on observations. Coded in Fortran, OpenOrb is usually compiled locally and run from the command line.

A few years ago, [LSST](https://www.lsst.org/) software developers started working on a Python wrapper for OpenOrb that uses the Fortran code as a library. In the framework of _[sbpy](http://sbpy.org)_, I picked up their excellent groundwork to extend the available functionality for a broader audience.

[_pyoorb_](https://github.com/oorb/oorb/tree/master/python) currently provides functions for orbit integration, ephemerides calculations, as well as orbital element transformations. Orbit ranging will be implemented in the near future. Since _pyoorb_ uses the existing OpenOrb Fortran code as a basis, function input has to follow the specifications meticulously, not offering the dynamic typing that you are used to as a Python user. In order to make _pyoorb_ functions more user-friendly, _sbpy_ provides convenience functions for the use of _pyoorb_.

Consider the following examples, which require _sbpy_ and _pyoorb_ to be installed:
	
  * Calculate the ephemerides of asteroid Ceres for some point in time; we obtain the orbital elements for the same epoch from [JPL Horizons](https://ssd.jpl.nasa.gov/horizons.cgi):


```python
import pyoorb as oo
from astropy.time import Time
from sbpy.data import Orbit, Ephem

# initialize pyoorb
oo.pyoorb.oorb_init()

# obtain current osculating elements for Ceres
orb = Orbit.from_horizons('Ceres')

# define epoch for which ephemerides are to be calculated
epoch = Time('2019-02-01 12:00', format='iso')

# calculate ephemerides
eph = Ephem.from_oo(orb, epoch)
print(eph['epoch', 'RA', 'DEC'])
```
    
      epoch          RA               DEC        
        d           deg               deg        
    --------- ---------------- ------------------
    2458516.0 241.143973372825 -14.38567839898754

	
  * Transform Ceres' Keplerian orbit to cartesian coordinates, comet orbit elements, and back to Keplerian coordinates; we compare the semi-major axis of the original Keplerian orbit with that of the transformed orbit:


```python
import pyoorb as oo
from sbpy.data import Orbit

# initialize pyoorb
oo.pyoorb.oorb_init()

# obtain current osculating elements for Ceres
keporb = Orbit.from_horizons('Ceres')

# transform orbital elements to cartesian coordinates
cartorb = keporb.oo_transform('CART')

# transform cartesian coordinates to comet orbit
comorb = keporb.oo_transform('COM')

# transform comet orbit to Keplerian orbit
keporb2 = comorb.oo_transform('KEP')

print('discrepancy in semi-major axis:', keporb['a']-keporb2['a'])
```
    
    discrepancy in semi-major axis: [0.] AU

	
  * Propagate Ceres' orbit 100 years into the future and compare the result to the orbit derived by JPL Horizons:


```python
import pyoorb as oo
from astropy.time import Time
from sbpy.data import Orbit

# initialize pyoorb
oo.pyoorb.oorb_init()

now = Time.now()

# get current osculating elements from JPL Horizons
orbnow_jpl = Orbit.from_horizons('Ceres')

# propagate orbit 100 years into the future
then_jd = now.jd + 10*365
orbthen = orbnow_jpl.oo_propagate(then_jd)

# compare to JPL Horizons orbit for the same date
orbthen_jpl = Orbit.from_horizons('Ceres', epochs=then_jd)

print('discrepancy in semi-major axis:',
      (orbthen['a']-orbthen_jpl['a']).to('m'))
```
    
    discrepancy in semi-major axis: [51.80632224] m


For more information on _OpenOrb_ and _pyoorb_, check out their [github repo](https://github.com/oorb/oorb). Thanks to[ @bsipocz](https://github.com/bsipocz/), [@mjuric](https://github.com/mjuric/), and [@rhiannonlynne](https://github.com/rhiannonlynne/), _OpenOrb_ and _pyoorb_ are now easily available through conda for Linux and MacOS. Give it a try!

If you are interested in using the _sbpy_ convenience functions, have a look at the [_sbpy_ documentation](https://sbpy.readthedocs.io/en/latest/).


