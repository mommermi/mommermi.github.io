---
date: 2021-11-17
title: Commercial Vehicle Traffic Detection from Satellite Imagery with Deep Learning
summary: |
  Can we identify trucks from space and estimate truck traffic rates anywhere on the planet? Yes, we can!
tags:
- Earth Observation
- Deep Learning
- Traffic
- Sentinel-2
featured_image: banner.jpg
thumbnail_image: trucks.png

---

Commercial vehicle traffic is currently responsible for 7% of global CO2 emissions. While road freight will remain the dominant mode of surface freight transportation, its contribution to climate change is likely to increase in the short term. Therefore, the quantitative monitoring of commercial vehicle (CV) traffic is essential for implementing targeted road emission regulations. However, ground monitoring stations are costly and less than half of all countries worldwide collect road freight activity. In this work, we investigate the feasibility of detecting and monitoring CV traffic in freely available
satellite imagery from ESA's Sentinel-2 satellites.

{{< image
src="trucks.png"
descr="Green boxes indicate commercial vehicles (CV) as they move on a Swiss freeway section. Due to a delay in the imaging of the different channels, moving objects exhibit a characteristic rainbow-like appearance in Sentinel-2 images." >}}


{{< image
src="setup.png"
descr="Workflow of this project. We gather satellite imagery and ground-truth traffic count rates for CVs, identify individual CVs with an object detection model and finally train gradient-boosted tree-based models on CV counts to estimate hourly CV traffic rates for the locations considered." >}}

For this task, we obtain [Sentinel-2](https://sentinel.esa.int/web/sentinel/missions/sentinel-2) satellite imagery for 33 locations centered on Swiss freeway sections to identify CVs with a deep learning approach.  We detect CVs with a modified [Faster R-CNN](https://proceedings.neurips.cc/paper/2015/file/14bfa6bb14875e45bba028a21ed38046-Paper.pdf) object detection model by exploiting a characteristic feature of moving objects in Sentinel-2 data: a constant delay between image acquisition in the different channels leads to a characteristic "rainbow-like" appearance for objects that move at sufficient velocity, which is easy to detect. After training our model, we find an average precision score of 72% for the detection of CVs in our imaging data. The model further shows similar performance results for freeway sections outside of Europe (see figure below).

{{< image
src="brazil.png"
descr="We test our object detection approach on out-of-distribution satellite imagery for different continents. In this example, the trained model correctly identifies all CVs on a freeway section in Brazil (extracted detections shown on the right)." >}}

For each freeway section location considered in this project, ground-truth traffic count data is available from [ASTRA](https://www.astra.admin.ch/astra/en/home.html), allowing us to convert snapshot CV counts into hourly traffic rates for CVs. For this purpose, we trained gradient-boosted tree-based regression models in order to predict CV traffic rates from the number of CVs counted per freeway section from our imaging data in addition to other features. We find that it is possible to measure hourly CV traffic volumes for any freeway section in the world within 65% of the actual value or with a root mean square error (RMSE) of ∼160 vehicles per hour. For freeway sections with available but limited ground-truth data, we can predict CV traffic volumes up to within 4% and with an RMSE of ∼60 vehicles per hour. We find that our models are best applied to satellite images with low cloud coverage and for freeway sections above 1 kilometer in length.

{{< image
src="covid.png"
descr="Our combined model approach enables the detection of CV traffic rate variations in 2020 due to Swiss Covid-19 lockdown regulations for different ports of entry. In agreement with ground-truth traffic rates, we find that the border to Italy was most severly affected by a decrease in traffic, while the border to Germany was barely affected." >}}

Additionally, our results enable the estimation of the relative decline in CV
traffic due to lockdown measures during the first wave of the COVID19 pandemic in Switzerland in 2020 (see figure above).

To conclude, our approach enables the estimation of CV traffic rates from remote sensing data only, which makes it applicable on a global scale. The methods presented here constitute a powerful tool to estimate CV traffic rates in areas in which ground-based traffic rate measurements are unavailable.

This project is based on the results of the Master thesis of MBI student Moritz Blattner, who also presented this project at the [ICML 2021 Tackling Climate Change with Machine Learning Workshop](https://www.climatechange.ai/papers/icml2021/19).

# Resources

* Blattner, M., Mommert, M., Borth, D., "Commercial Vehicle Traffic Detection from Satellite Imagery with Deep Learning", ICML 2021 Tackling Climate Change with Machine Learning Workshop [publication (open access)](https://www.climatechange.ai/papers/icml2021/19).