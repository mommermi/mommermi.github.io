---
author: mommermi
date: 2016-01-08 16:02:51+00:00
layout: post
title: A Python Module to Query JPL HORIZONS
description: |
  The JPL Horizons system is the standard resource for Solar System
  ephemerides and orbital elements. I created a Python module that
  allows accessing data from this system within Python.
categories:
- astronomy
tags:
- open-source software
---

Working on Solar System small bodies, I make frequent use of the [JPL HORIZONS](http://ssd.jpl.nasa.gov/horizons.cgi) system, which provides ephemerides and orbital elements at given times for any Solar System body. HORIZONS provides access through email, telnet, and a website that can be queried manually.

In order to conveniently query and investigate large amounts of data from HORIZONS, I wrote a Python module that provides access to ephemerides and orbital elements by parsing the html source code of the HORIZONS website. This method provides robust and fast access - and it's now part of the [astroquery](https://github.com/astropy/astroquery) module! [Check it out](http://astroquery.readthedocs.io/en/latest/jplhorizons/jplhorizons.html)!
