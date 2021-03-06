---
author: mommermi
date: 2019-03-04 05:28:42+00:00
layout: post
title: Identifying Stars and Galaxies from Sloan Digital Sky Survey Photometric Data
description: |
  Is it possible to distinguish stars from galaxies based on their photometric
  properties? Yes, and it's actually pretty easy and accurate using machine
  learning.
categories:
- machine learning
- astronomy
tags:
- toy project
---

This is a little toy project that started out of curiosity about what simple machine learning models are able to accomplish and ended up being my contribution to this year's Flagstaff Astronomy Symposium. I hope this project will serve as a motivation for  astronomers to consider machine learning approaches in their work.

## Motivation

The idea behind this project is that object classification is a common problem. Are all these objects [stars](https://en.wikipedia.org/wiki/Star)? Is this a [spiral galaxy](https://en.wikipedia.org/wiki/Spiral_galaxy)? Is that an [elliptical galaxy](https://en.wikipedia.org/wiki/Elliptical_galaxy)? This sounds like a typical classification problem, so it should be easy to implement a machine learning model that is able to distinguish between these object types based on the imaging data, using methods similar to those used in [face recognition](https://en.wikipedia.org/wiki/Facial_recognition_system).

{% include image.html url="https://www.nasa.gov/sites/default/files/styles/full_width_feature/public/thumbnails/image/potw1748a.jpeg" description="Galaxy cluster Abell 2537 as observed with the Hubble Space Telescope and showing a wide range of galaxy types (NASA/ESA/HST)." %}

Given the data volume of large-scale imaging surveys, I was more interested in investigating_ if, instead of running on the actual imaging data, a model could be trained and run on reduced photometric data._ This approach would significantly reduce the data volume as well as the computational complexity of the problem.

## Data

Photometric data obtained with a range of different methods are available from surveys such as the [Sloan Digital Sky Survey](http://www.sdss.org) (SDSS). Luckily, the citizen science project [Galaxy Zoo](https://www.zooniverse.org/projects/zookeeper/galaxy-zoo/) extracted several tens of thousands of galaxy candidates from SDSS images that were then classified by-eye by humans. Using data the classification data from Galaxy Zoo and photometric properties as measured by SDSS, a training set including 62000 elliptical galaxies, 190000 spiral galaxies, and 183000 stars could be assembled for this project.

{% include image.html url="/images/2019-03-04-identifying-stars-and-galaxies-from-sloan-digital-sky-survey-photometric-data/sdss_features.png" description="An example for feature engineering: the left-hand plot shows the quotient of the Petrosian effective radii including 50% or the flux and 90% of the flux for the three different target types, whereas the right-hand plot shows the difference between the two properties. While the quotient nicely splits the three object types across a range of values, the difference allows only to distinguish stars from galaxies in general. The quotient is part of the final feature set used in the modeling." %}

By plotting similar features against each other for the three object types and engineering additional features, I was able to reduce the total number of features to be used in the model to only five.

## Modeling

Providing a level of accuracy very similar to more complex models but performing much faster than them, I decided to go with a simple [Decision Tree classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) as my model of choice.

{% include image.html url="/images/2019-03-04-identifying-stars-and-galaxies-from-sloan-digital-sky-survey-photometric-data/sdss_confusionmatrix.png" description="Best-fit model confusion matrix." %}

The best-fit f1-score for this model is 96.4%, which sound pretty good. A look at the confusion matrix reveals that stars are identified with a 100% confidence, but elliptical galaxies only with 90% confidence. The possible confusion between the two galaxy types is less than 10%, which is still a good result given the simplicity of the model.


## Results


I test the trained model against SDSS of galaxy cluster Abell 1631 and predict target types for each source with reliable photometric properties.

{% include image.html url="/images/2019-03-04-identifying-stars-and-galaxies-from-sloan-digital-sky-survey-photometric-data/sdss_stars.png" description="Objects classified as stars from the Abell 1631 SDSS field using the model described here." %}

As expected, stars are identified without any ambiguity. The example stars shown look almost identical and show a steep brightness gradient as expected for point sources.

{% include image.html url="/images/2019-03-04-identifying-stars-and-galaxies-from-sloan-digital-sky-survey-photometric-data/sdss_ellipticals.png" description="Objects classified as elliptical galaxies from the Abell 1631 SDSS field using the model." %}

Objects that were identified as elliptical galaxies show a significant degree of fuzziness compared to stars, and they lack the steep brightness gradient as is indicated by the shallower scaling of the images. The fuzzy and structure-less appearance is typical for elliptical galaxies.

{% include image.html url="/images/2019-03-04-identifying-stars-and-galaxies-from-sloan-digital-sky-survey-photometric-data/sdss_spirals.png" description="Objects classified as spiral galaxies from the Abell 1631 SDSS field using the model." %}

Finally, objects that the model identifies as spiral galaxies usually show more structure and often a clearly linear orientation, which the elliptical galaxies are lacking. However, there are some cases that could just as well be classified as elliptical galaxies, as suggested by the confusion matrix.


## Conclusions


Given the simplicity of the model, I think that it performs very well. It is definitely possible to distinguish between stars and galaxies, and even some galaxy types, based on the photometric properties alone, which is quite remarkable. Additional tweaking and using a more elaborate modell approach is probably able to improve the model's accuracy and reduce the fractions of false positives.


## Code, Discussion, and Acknowledgments


The code used in this project is available on[ github](https://github.com/mommermi/sdss_stars_galaxies/blob/master/sdss_stars_galaxies.ipynb), together with a more in-depth discussion of the project and its flaws.

This project uses data from [SDSS](http://www.sdss.org) and [Galaxy Zoo](https://www.zooniverse.org/projects/zookeeper/galaxy-zoo/).
