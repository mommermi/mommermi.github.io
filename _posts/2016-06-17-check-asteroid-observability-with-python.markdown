---
author: mommermi
comments: false
date: 2016-06-17 18:02:46+00:00
layout: post
link: https://michaelmommert.wordpress.com/2016/06/17/check-asteroid-observability-with-python/
slug: check-asteroid-observability-with-python
title: Check Asteroid Observability with Python
wordpress_id: 295
categories:
- python
- software
---

Observers know the problem: there is a huge list of targets you want to observe - but what is the best time to observe them?

Use this Python script to find out: [check_observability.py](http://134.114.60.45/wordpress/check_observability.py)

The script requires the Python module [CALLHORIZONS](https://pypi.python.org/pypi/CALLHORIZONS) (see [here](https://michaelmommert.wordpress.com/2016/01/08/a-python-module-to-query-jpl-horizons)) that can be easily installed using:

    
    pip install callhorizons


In order to use the script, you have to modify it in three places (you can find those in the code by using a text search, looking for the word 'user'):



	
  1. **Target name list**:
simply create a file listing the names of your targets, one per line. You can use names, numbers, designations; make sure to use underscores in designations, e.g., 2001_AB123 instead of 2001 AB123. Each line can contain additional information on your targets, separated by a blank; this information is ignored by the script. The target name list file has to reside in the same directory as the script, unless you provide its path.

	
  2. **Observation date range and step size**:
The script will query [Horizons](http://ssd.jpl.nasa.gov/horizons.cgi) to obtain your targets' ephemerides. You have to provide a start date ('YYYY-MM-DD'; may include a UT time 'YYYY-MM-DD HH-MM-SS'), end date, and a time step (e.g., '1m' for 1 minute, '2h' for 2 hours, '3d' for 3 days...).

	
  3. **Observability conditions**:
You may want to observe only targets that are brighter than a certain V magnitude, or have a maximum airmass. Enter those conditions here. See below for examples.


Run the script using:

    
    python check_observability.py


The script will output for each target for how many time steps it is observable and write the data into two files:



	
  * **observability.dat** - observability information for each time step

	
  * **peak_observability.dat** - peak brightness information for each target over the entire period


Feel free to use, share, and modify this script. If you have questions or need help modifying the script, send me an email!


### Setting Observability Conditions


You can specify you observability conditions in this line:

    
     observable = eph.data[((eph['V'] < 17.5) & (eph['airmass'] < 2.5))]


The conditions are given in the square brackets indexing eph.data. In the given example, the target is considered observably only in those time steps when V<17.5 and when at the same time the airmass is less than 2.5. You can use all the properties specified [here](http://mommermi.github.io/callhorizons/readme.html#callhorizons.query.get_ephemerides) to setup your observability conditions.

Some examples:

    
    observable = eph.data[((eph['V'] < 20.5) & (eph['airmass'] < 2.0) &
                           (numpy.sqrt(eph['RA_rate']**2 + 
                                       eph['DEC_rate']**2) < 0.1))]


This line also checks for the target's total rate to be less than 0.1 arcsec/sec.

    
    observable = eph.data[((eph['V'] < 18) & 
                          (eph['lunar_presence'] == 'dark'))]


Using this line, the script will only return those ephemerides when the Moon is below the horizon.


