---
author: mommermi
comments: false
date: 2016-01-08 16:02:51+00:00
layout: post
link: https://michaelmommert.wordpress.com/2016/01/08/a-python-module-to-query-jpl-horizons/
slug: a-python-module-to-query-jpl-horizons
title: A Python Module to Query JPL HORIZONS
wordpress_id: 199
categories:
- python
- software
---

Working on Solar System small bodies, I make frequent use of the [JPL HORIZONS](http://ssd.jpl.nasa.gov/horizons.cgi) system, which provides ephemerides and orbital elements at given times for any Solar System body. HORIZONS provides access through email, telnet, and a website that can be queried manually.

In order to conveniently query and investigate large amounts of data from HORIZONS, I wrote a Python module that provides access to ephemerides and orbital elements by parsing the html source code of the HORIZONS website. This method provides robust and fast access - and it's now part of the [astroquery](https://github.com/astropy/astroquery) module! [Check it out](http://astroquery.readthedocs.io/en/latest/jplhorizons/jplhorizons.html)!
