---
author: mommermi
date: 2020-04-22 
layout: post
title: Automated Cloud Detection with Machine Learning
description: |
  This is a toy project that turned into a real research project and a preparation 
  for my new job as
  research scientist in computer vision: using machine
  learning techniques to identify clouds in all-sky camera images.
categories:
- Astronomy
tags:
- Machine Learning
- Deep Learning
- Allsky-Camera

---

# Motivation

Most (optical) telescopes have to be protected from precipitation to
prevent damage to their optics and electronics. For this reason, most
observatories use all-sky cameras - cheap, but very sensitive CMOS
cameras equipped with fish-eye lenses - that monitor the night sky for
incoming clouds. Telescope operators can observe live streams from these
cameras to make informed decisions as to whether the current weather
situation requires the closing of the telescope dome, or not.

It should be worthwhile to automate this decision-making process so
that, for instance, robotic telescopes can close their enclosures
autonomously if clouds are present without any human intervention. A
very similar system could be used to measure sky quality conditions in
a highly unbiased way.

# Problem

<p align="center">
<iframe src="https://player.vimeo.com/video/410776698" width="500"
height="498" frameborder="0" allow="autoplay; fullscreen"
allowfullscreen></iframe></p>

Unfortunately, the automated detection of clouds in image data is a
non-trivial task. Due to varying illumination conditions and cloud
thickness, the heterogeneous sky background brightness, and other
effects, night sky clouds manifest in different ways in all-sky camera
images, hampering their identification. Additional complications arise
during twilight or during "bright nights", when the Moon is up. These
complications are exemplified in the animation shown above, in which
clouds first appear darker than the clear sky but then brighten
significantly after Moon rise.

My hope was that machine learning models should be able to handle this
level of complexity easily.

# Methods and Data

I tested two different machine learning approaches on this problem:
* a deep learning approach that adopts a
  [ResNet-18](https://arxiv.org/abs/1512.03385) implementation working 
  directly on the image data, and
* a gradient-boosted tree-based model
  ([lightgbm](https://github.com/microsoft/LightGBM)) working on
  preprocessed and extracted features; these features include metrics like
  source count and average background brightness, and time derivatives
  thereof, across a polar grid over each image, as well as additional
  information on the observation circumstances.
  
Both models were trained on a set of 1975 all-sky camera images from Lowell
Observatory's Discovery Telescope (formerly the Discovery Channel Telescope)
that were randomly drawn from a period of 14 consecutive months. In all images of this set, the presence of clouds on a polar grid was labeled manually.

# Results

The results were two-fold:

* The deep learning approach using the *ResNet* implementation was
  only able to reach an accuracy of 85%. This is most likely due to
  the relatively small sample size for this model type. Better results
  are possible with a significantly larger sample size.

* The *lightgbm* model performs much better with an accuracy of ~95%,
  which is not likely to improve for larger sample sizes.

{% include image.html
url="/images/2020-04-22-automated-cloud-detection-with-machine-learning/confusionmatrix.png"
description="Confusion matrix for both model approaches. These matrices underlines the superior performance of the feature-extracted lightgbm approach over the ResNet approach." %}

Another major selling point for the *lightgbm* model is the training
time. While a meaningful model training process for the *lightgbm*
model takes only a matter of seconds, it takes up to an hour for the
*ResNet* approach.

For the full analysis, please refer to the [publication in the
Astronomical Journal](https://iopscience.iop.org/article/10.3847/1538-3881/ab744f) or the [arxiv pre-print version](https://arxiv.org/abs/2003.11109) of this publication.


# Conclusions

I fully recommend the feature-extracted approach, as it easily
outperforms the deep learning approach for this kind of application
while utilizing only a fraction of the resources. Given the high
accuracy of the *lightgbm* and the fact that this seems to be the
maximum achievable accuracy (i.e., it is not limited by sample size)
lets me conclude that this accuracy is only limited by human accuracy
in the manual labeling of the training data.

# Resources

* Mommert, M. 2020, "*Cloud Identification from All-sky Camera Data with Machine Learning*", The Astronomical Journal, 159, 178., [publication](http://doi.org/10.3847/1538-3881/ab744f), [arxiv](http://arxiv.org/abs/2003.11109)

* Mommert, M. 2020: [code and example data](http://doi.org/10.5281/zenodo.3662849)
