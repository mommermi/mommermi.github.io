---
author: mommermi
date: 2021-12-14
layout: post
title: Estimating Power Plant Greenhouse Gas Emissions from Satellite Imagery
description: |
  Tracking Greenhouse Gas emissions will be increasingly important in the future, as power generation from fossil fuels is supposed to fade out. Independent tools to monitor power plants are required for this task. We present a method that uses freely available satellite imagery to estimate power generation and CO2 emission rates on a global scale.
categories:
- Applied Research
tags:
- Earth Observation
- Deep Learning
- Multi-task Learning
- Power Plants
- CO2
- Sentinel-2

---

This project forms the logical extension of our previous project on the [characterization of industrial plumes from remote sensing data](https://mommermi.github.io/applied%20research/2020/12/07/Characterization_of_Industrial_Smoke_Plumes_from_Remote_Sensing_Data.html). Instead of simply identifying and characterizing plumes, we utilize this information to estimate Greenhouse Gas emissions from fossil fuel-firing power plants.

The idea is rather simple: we know that we can segment plumes and robustly distinguish them from natural clouds. For all European power plants, we know for any given time what their power generation rates are. We can therefore train a regression model to estimate the power generation rate from the extent of the observed plume for any given time. However, the apparent size of the plume is not only a function of the power generation process. Instead, it is a highly complex process that relies on environmental variables. To approximate these variables, we provide concurrent weather information, including ambient temperature, air pressure and wind speed to our regression model. 

{% include image.html
url="/images/2021-12-14-Estimating_Power_Plant_Greenhouse_Gas_Emissions_from_Satellite_Imagery/overview.png"
description="Our model architecture. Satellite imagery serves as input to a U-Net backbone. The output feature map serves as input to a multi-task learning approach: we use separate heads to segment the plume, classify the power plant type and predict power generation rates. The latter also accounts for weather variables. The architecture is trained on ground-truth plume masks, power plant type information and power generation rates. We find the results from this multi-task learning approach to outperform models learned on these tasks separately." %}

To improve our power generation rate predictions, we utilize a multi-task learning approach: instead of simply training a model that predicts power generation, we learn additional tasks, namely a power plant classification model (see [here](https://mommermi.github.io/applied%20research/2021/06/16/Power_Plant_Classification_From_Remote_Imaging_With_Deep_Learning) and a plume segmentation model (see [here](https://mommermi.github.io/applied%20research/2020/12/07/Characterization_of_Industrial_Smoke_Plumes_from_Remote_Sensing_Data)). By learning additional tasks, the model generates richer representations of the underlying data, resulting in a more robust training and better performance. This is reflected in our results: the combined multi-task learning approach performs better on each learned tasks than a separately trained model. We can also show the benefit of adding weather data to our model input.

So far, our model is able to estimate power generation rates (with an MAE of 139 MW) - how do we get CO2 emission rates from this result? Our model is also able to identify power plant types; depending on the fuel they use, they emit different amounts of CO2 per MWh into the atmosphere. By approximating these emission factors, we are able to convert our power generation rate estimates into emission rate estimates. 

{% include image.html
url="/images/2021-12-14-Estimating_Power_Plant_Greenhouse_Gas_Emissions_from_Satellite_Imagery/results.png"
description="Prediction results from our multi-task learning approach: power generation rates on the left and CO2 emission rates on the right." %}

Our approach enables the estimation of power generation rates and CO2 emission rates of power plants based on freely available Sentinel-2 satellite imagery. Results have been published at the [Tackling Climate Change with Machine Learning Workshop at NeurIPS 2021](https://www.climatechange.ai/papers/neurips2021/27) and a journal paper with all details is currently in review.



# Resources

* Hanna, J., Mommert, M., Scheibenreif, L. Borth, D., "Multitask Learning for Estimating Power Plant Greenhouse Gas Emissions from Satellite Imagery", NeurIPS 2021 Tackling Climate Change with Machine Learning Workshop; [publication (open access)](https://www.climatechange.ai/papers/neurips2021/27).

* Hanna J. et al. 2021, [code](https://github.com/HSG-AIML/RemoteSensingCO2Estimation)

* Hanna J. et al. 2021, [dataset](https://doi.org/10.5281/zenodo.5644746)