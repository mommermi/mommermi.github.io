---
author: mommermi
comments: true
date: 2019-03-17 05:41:43+00:00
layout: post
link: https://michaelmommert.wordpress.com/2019/03/16/a-plethora-of-asteroids-in-tess-data/
slug: a-plethora-of-asteroids-in-tess-data
title: A plethora of asteroids in TESS data
wordpress_id: 557
categories:
- data mining
- observations
- software
---

TESS is the [Transiting Exoplanet Survey Satellite](https://tess.mit.edu/), which was launched into space by NASA in 2018 to identify faint brightness variations in stars that are characteristic of planets orbiting around and transiting in front of these stars.

[caption id="" align="aligncenter" width="1200"]![https://upload.wikimedia.org/wikipedia/commons/c/c2/Transiting_Exoplanet_Survey_Satellite_artist_concept_%28transparent_background%29.png](https://upload.wikimedia.org/wikipedia/commons/c/c2/Transiting_Exoplanet_Survey_Satellite_artist_concept_%28transparent_background%29.png) A rendering of the TESS spacecraft. The instrument consists of four imaging cameras, each covering 24° x 24° of the sky.[/caption]

Over the course of its nominal two-year mission, TESS will monitor more than 200,000 stars with the photometric accuracy necessary to identify [exoplanet](https://en.wikipedia.org/wiki/Exoplanet) transits. In order to observe this huge number of stars, TESS points at different "Sectors" in the sky, amounting to a total of 85% of the entire sky. Each Sector spanning 24° x 96°  is observed over a period of about one month.

TESS data are publicly available at [MAST](https://archive.stsci.edu/tess/) - including calibrated Full Frame Images that are stacked over a period of 30 min each. Given the huge field of view of the TESS cameras, there should be an enormous number of asteroids in each frame at any given time. So I went for a data mining fishing expedition...


### Extracting asteroids from TESS data


The idea is conceptually simple:



	
  * download and pre-process the TESS Full Frame images for further analysis ;

	
  * perform a background subtraction to remove stars and other fixed sources to improve the detection of moving objects;

	
  * predict the locations of all known ~800,000 asteroids for the time of the observations in order to be able to identify them in the frames;

	
  * perform photometry and measure their brightness.


Putting all these parts together, we can measure brightness variations of a large number of asteroids over a baseline of up to nearly one month - this is a unique data set that enables the accurate measurement of rotational periods over a continuous period of time that is not accessible from the ground: keep in mind that ground-based observations are restricted to night-time observations only, whereas TESS is able to observe 24/7.

This project is mainly a computational problem: running one out of four cameras per Sector on a desktop machine takes about one day. Multithreading has been implemented where possible to expedite the processing.


### First results


A first cool result is shown in this short video clip:

[vimeo 323253379 w=640 h=274]

This video shows the rotational lightcurve of asteroid 1693 Hertzsprung. The left plot shows a thumbnail image centered on the asteroid and the right plot shows the brightness of the target. As time progresses, the variation in brightness, which is caused by the asteroid's irregular shape and rotation, becomes obvious. This specific asteroid has a rotational period of about 9 hrs. Gaps appear in the lightcurve when the asteroid comes too close to areas affected by image artifacts, which are highlighted with red overlays in the left plot.

I will add more results and visualizations in the near future.


### Current status


Right now, we are working on the publication of a pilot study for this project, as well as a funding proposal to apply our data mining technique to the entire TESS data set.

Stay tuned!


