---
author: mommermi
date: 2019-02-07 04:28:23+00:00
layout: post
title: How far is Ikea? A data science toy project.
description: |
  This question popped up during a Sunday afternoon walk in the park: It takes
  us two hours to drive to Ikea - is that a lot or not? By combining location
  data and population density estimates I find the answer.
categories:
- data science
tags:
- toy project
---

And now for something completely different...

This toy project is the result of a harmless question that came up during a Sunday afternoon walk in the park:

Living in Flagstaff, Arizona, the closest Ikea location is in Tempe, which is a two-hour drive. _How does this compare to the US population in general? Does the majority of American have to go on a longer drive to get to the closest Ikea? Or is it a shorter drive?_

Answering these questions is not too hard. If you have the right data and tools at hand. Using Python, open data, and open source code I pursue the following approach:



	
  1. Retrieve a list of all Ikea locations in the US.

	
  2. Build a grid across the (continental) US that allows me to...

	
  3. calculate the distance from every cell in this grid to the closest Ikea location.

	
  4. Weight the resulting geographic distance distribution with the local population density.


Let's have a look at some results:

	
  * The following maps shows the distance to the closest Ikea location for any location in the continental US. The black points indicate Ikea locations, the green star indicates the location of Flagstaff. Flagstaff is about 200 km from Ikea in Tempe. There certainly are areas that are farther from the closest Ikea, especially areas in New Mexico and Montana. Some areas of Montana share the longest distance to any Ikea location in the US: 1050 km. ![Ikea_distances](https://michaelmommert.files.wordpress.com/2019/02/ikea_distances-1.png)

	
  * There are obvious cumulations of Ikea locations on the East coast and West coast. Looking at the (logarithmic) population density distribution, it is clear that these ![Ikea_popdist](https://michaelmommert.files.wordpress.com/2019/02/ikea_popdist.png)match with highly populated areas. Also note how the other Ikea locations clearly correlate with densely populated areas.



	
  * By combining the information in the two plots above, we can build a cumulative distribution that shows how far Americans live from their closest Ikeas, weighted by population density: ![Ikea_cumpopdist](https://michaelmommert.files.wordpress.com/2019/02/ikea_cumpopdist.png)
Keep in mind that the curve shown in this plot is cumulative, so it shows for a given distance on the x-axis what fraction of Americans lives within this radius of the closest Ikea location. Flagstaff and the population median are shown in this plot for reference.




### Results


The previous plot enables us to address the questions motivating this project:



	
  * The _US population median distance from any Ikea location is 60 km_; this means that 50% of Americans have to cross a longer distance, the other 50% a shorter distance. Given that the US spans about 4000 km from coast to coast, this is a pretty decent coverage.

	
  * Assuming that people are prepared to drive between 30 min (~50 km) to 1 hr (~100 km) to buy things at Ikea, _what fraction of the population does this cover_? Based on these ranges 46% to 60% are covered.

	
  * And of course the most important question: _What fraction of the US population has a longer drive to Ikea than people living in Flagstaff?_ The answer is: only 20%. Despite the seemingly short distance to Tempe on the above map, only a fifth of the US population has a longer drive to Ikea. This is somewhat depressing...


For details on this analysis and project, have a look at this [jupyter notebook](https://github.com/mommermi/Ikea-distance/blob/master/Ikea-distance.ipynb).
