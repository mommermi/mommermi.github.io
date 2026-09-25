---
date: 2026-04-30
title: Modeling of Road Traffic Noise using Deep Learning
tags:
- Remote Sensing
- Deep Learning
- Multimodal Data
- Traffic
- Segmentation
---

Deep learning has already proven its potential in many areas of remote sensing. One example is the classification of land use and land cover from satellite and aerial imagery.

But perhaps we can go one step further: once an AI model has learned how certain things are related, can we also ask it "what if?" questions? By deliberately changing the data we feed into the model, we can observe how its output changes. In this way, an AI could serve as a kind of simplified simulator, for example in so-called digital twins. These are virtual replicas of real cities or landscapes in which changes can be tested before they are implemented in the real world.

## Example: Road Traffic Noise

We explore this idea using road traffic noise as an example. In a [previous project]({{< ref "2022-06-20-Traffic_Noise_Estimation_from_Satellite_Imagery_with_Deep_Learning" >}}), we already showed that an AI can estimate road traffic noise exposure based on satellite imagery alone. The satellite images come from the Sentinel-2 satellites, which provide a maximum resolution of 10 m per pixel.

In Sunita Joshi's master's thesis, we are developing this model further. In addition to the satellite images, the AI now also receives information about the elevation of the Earth's surface at every pixel. Such information about the terrain is particularly important when studying noise, because sound does not spread unimpeded: obstacles can block it.

{{< image
src="road_noise_dem_comparison.png"
descr="We show how important elevation data is for correctly simulating the propagation of sound. The satellite image (left) is evaluated by a trained AI model once without additional elevation data and once with the corresponding elevation data in order to determine the actual road traffic noise exposure (center). Both results (right) correctly show the course of the roads, but only the model with elevation data (bottom) is able to reproduce the lower noise exposure in valley structures." >}}

## Testing Noise Barriers on the Computer

The question now is: can an AI trained on noise data be used to test noise protection measures virtually? To do this, we "build" artificial elevations into the elevation map, for example where a noise barrier might be placed. We then check whether the AI predicts less noise behind this barrier, as would be expected in reality.

The qualitative results of the thesis support this hypothesis. The trained model is clearly able to recognize obstacles and simulate the attenuation of sound. A major limitation, however, is that this is not a physically accurate model but a surrogate model.

In further work, we aim to improve and adapt this model so that its results can be brought more closely in line with physical models.

This work was presented at the *National Forum for Remote Sensing and Copernicus* (April 28–30, 2026) in Darmstadt.