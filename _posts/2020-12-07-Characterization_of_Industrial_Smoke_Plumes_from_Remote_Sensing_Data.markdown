---
author: mommermi
date: 2020-12-07
layout: post
title: Characterization of Industrial Smoke Plumes from Remote Sensing Data
description: |
  Greenhouse gas emissions from the industrial economic sector are
  a major driver of the currently observed climate change. We developed
  a deep learning approach to identify and characterize industrial
  smoke plumes. In the future, we will utilize this approach to estimate
  greenhouse gas emissions from remote sensing data on a global scale.
categories:
- Applied Research
tags:
- Earth Observation
- Deep Learning
- Segmentation
- Plumes
- Sentinel-2
---

The major driver of global warming has been identified as the anthropogenic release of greenhouse gas (GHG) emissions from industrial activities. The quantitative monitoring of these emissions is mandatory to fully understand their effect on the Earth's climate and to enforce emission regulations on a large scale. In this work, we investigate the possibility to detect and quantify industrial smoke plumes from globally and freely available multi-band image data from ESA's Sentinel-2 satellites.

{% include image.html
url="/images/2020-12-07-Characterization_of_Industrial_Smoke_Plumes_from_Remote_Sensing_Data/example_panel.png"
description="Example images from our set of 21,350 images of industrial sites. Each column corresponds to one of 624 emitter locations. The top row shows the site during activity (smoke is present) and the bottom row during inactivity (smoke is absent). The origin region of the smoke plume is marked by red circles." %}


### Classification of Smoke Plumes 

Using a modified ResNet-50, we can detect smoke plumes of different sizes with an accuracy of 94.3%. The model correctly ignores natural clouds and focuses on those imaging channels that are related to the spectral absorption from aerosols and water vapor, enabling the localization of smoke.

{% include image.html
url="/images/2020-12-07-Characterization_of_Industrial_Smoke_Plumes_from_Remote_Sensing_Data/activation_example.png"
description="Inference examples from our classification model. For different examples from our test sub-sample (columns), we show the true color RGB image (top row), a false color image (center row), and the activations of some hidden layer in our ResNet implementation (bottom row, sharing the same scaling across the row). We find that the location of smoke correlates in most cases with significant aerosol and water vapor signals and that the hidden layer activations fire based on these signals, leading to good localization of the smoke." %}

### Segmentation of Smoke Plumes

We exploit this localization ability and train a U-Net segmentation model on a labeled sub-sample of our data, resulting in an Intersection-over-Union (IoU) metric of 0.608 and an overall accuracy for the detection of any smoke plume of 94.0%; on average, our model can reproduce the area covered by smoke in an image to within 5.6%. The performance of our model is mostly limited by occasional confusion with surface objects, the inability to identify semi-transparent smoke, and human limitations to properly identify smoke based on RGB-only images. Nevertheless, our results enable us to reliably detect and qualitatively estimate the level of smoke activity in order to monitor activity in industrial plants across the globe. Our data set and code base are publicly available.

{% include image.html
url="/images/2020-12-07-Characterization_of_Industrial_Smoke_Plumes_from_Remote_Sensing_Data/segmentation_example.png"
description="Inference examples from our segmentation model. For different examples from our test sub-sample (columns), we show the RGB image (top row), a false color image (center row), and the footprint of the ground-truth labels (red areas) and predicted labels (green areas). In general, the segmentation model reliably identifies smoke plumes with few limitations." %}


This work was presented at the [``Tackling Climate Change with Machine Learning'' Workshop at the NeurIPS 2020](https://www.climatechange.ai/papers/neurips2020/9) conference and the [2021 NVIDIA GTC](https://www.nvidia.com/en-us/gtc/) conference.
We made the [code](https://github.com/HSG-AIML/IndustrialSmokePlumeDetection) and [data set](https://zenodo.org/record/4250706) from this work available online. 


This work was extended by our PhD student Joelle. Checkout her updates [here]({% post_url 2021-12-14-Estimating_Power_Plant_Greenhouse_Gas_Emissions_from_Satellite_Imagery %}).


# Resources

* Mommert, M., Sigel, M., Neuhausler, M., Scheibenreif, L., Borth, D., "Characterization of Industrial Smoke Plumes from Remote Sensing Data", [Tackling Climate Change with Machine Learning Workshop,
NeurIPS 2020](https://www.climatechange.ai/papers/neurips2020/9). 

* Mommert, M. et al. 2020: [dataset](https://zenodo.org/record/4250706)

* Mommert, M. et al. 2020: [code](https://github.com/HSG-AIML/IndustrialSmokePlumeDetection)


* Mommert, M., "Characterizing Industrial Smoke Plumes from Remote Sensing Data with Deep Learning", oral presentation at [NVIDIA GTC21](https://www.nvidia.com/en-us/gtc/). 
