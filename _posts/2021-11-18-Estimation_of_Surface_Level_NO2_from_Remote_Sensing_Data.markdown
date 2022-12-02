---
author: mommermi
date: 2021-11-18
layout: post
title: Estimation of Surface Level NO2 from Remote Sensing Data
description: |
  Air pollution is a major health issue and often also contributes to climate change. Measuring air pollution is costly and therefore only available in some countries. We investigated whether freely available Earth observation data can be utilized to estimate air pollution on the surface level. 
categories:
- Applied Research
tags:
- Earth Observation
- Deep Learning
- Air Pollution
- NO2
- Sentinel-2

---


Exposure to air pollution has been shown to lead to adverse health effects. A major air pollutant is NO2, which, at the surface level, directly affects human health, and, at higher elevations, contributes to acidic rain and represents a precursor to greenhouse gases. While NO2 column densities in the atmosphere can be measured with satellite observations as provided by [Sentinel-5P](https://sentinel.esa.int/web/sentinel/missions/sentinel-5p), it requires in-situ measurements from ground stations to measure NO2 concentrations on the surface level, which is relevant to human exposure.

Our student Linus Scheibenreif investigated whether it would be possible to approximate surface level NO2 from remote sensing observations only, providing a tool to estimate human exposure to NO2 on a useful spatial and temporal scale. In his two publications, Linus showed that

* it is possible to interpolate surface level NO2 exposure between measurements provided by [EEA](https://www.eea.europa.eu/) ground stations based on different types of features ([Scheibenreif et al. 2021a](https://ieeexplore.ieee.org/iel7/9553015/9553016/09554037.pdf)), and
* we can combine satellite imagery with atmospheric trace gas column density measurements to estimate surface level NO2 concentrations with high spatial resolution and intermediate temporal resolution ([Scheibenreif et al. 2021b](https://www.climatechange.ai/papers/icml2021/23)).


{% include image.html
url="/images/2021-11-18-Estimation_of_Surface_Level_NO2_from_Remote_Sensing_Data/figure2.png"
description="Exemplary NO2 predictions based on Sentinel-2 and Sentinel-5P input data from Scheibenreif et al. 2021b." %}

Learn more about Linus' projects in these blog articles: [A Novel Dataset for the Prediction of Surface NO2 Concentrations from Remote Sensing Data](https://hsg-aiml.github.io/2021/04/07/A_Novel_Dataset_for_the_Estimation_of_Surface_NO2_Concentrations_from_Remote_Sensing_Data.html) and [Estimation of Air Pollution with Remote Sensing Data: Revealing Greenhouse Gas Emissions from Space](https://hsg-aiml.github.io/2021/07/23/Estimation_of_Air_Pollution_with_Remote_Sensing_Data.html). 
His results have also been summarized in a IEEE Transactions on Geoscience and Remote Sensing journal paper (see below).


# Resources

* Scheibenreif, L., Mommert, M., Borth, D., "Towards Global Estimation of Ground-Level NO2 Pollution with Deep Learning and Remote Sensing", IEEE Transactions on Geoscience and Remote Sensing, 2022, [publication](https://doi.org/10.1109/TGRS.2022.3160827), [open access](http://www.alexandria.unisg.ch/266586/1/Toward_Global_Estimation_of_Ground-Level_NO2_Pollution_With_Deep_Learning_and_Remote_Sensing.pdf).

* Scheibenreif et al. 2022 Dataset: [zenodo](https://doi.org/10.5281/zenodo.5764262)

* Scheibenreif et al. 2022 Code: [GitHub](https://github.com/HSG-AIML/Global-NO2-Estimation)

* Scheibenreif, L, Mommert, M., Borth, D., "Estimation of Air Pollution with Remote Sensing Data: Revealing Greenhouse Gas Emissions from Space", ICML 2021 Tackling Climate Change with Machine Learning Workshop;
[publication (open access)](https://www.climatechange.ai/papers/icml2021/23).

* Scheibenreif, L. , Mommert, M., Borth, D., "A Novel Dataset and Benchmark for Surface NO2 Prediction from Remote Sensing Data Including COVID Lockdown Measures", IEEE International Geoscience and Remote Sensing Symposium 2021 ([IGARSS 2021](https://igarss2021.com/)); [publication](https://ieeexplore.ieee.org/iel7/9553015/9553016/09554037.pdf).
