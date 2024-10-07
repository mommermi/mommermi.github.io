---
date: 2024-07-12
title: Multimodal Diffusion for Self-Supervised Pretraining
summary: |
  Deep learning models based on diffusion processes have shown great potential in a range of generative tasks, such as image generation. For remote sensing applications, generative models are not that common. The question that we tried to answer is whether diffusion processes can be used to efficiently pretrain models for discriminative tasks?
tags:
- Earth Observation
- Deep Learning
- Diffusion
- Multimodal
- Self-supervised Learning
thumbnail_image: diffusion_qualitative_sample.png
---

Diffusion processes are best known for training image-from-text models. The idea behind diffusion processes is rather simple: you take an image and gradually destroy the information by applied Gaussian noise. A diffusion model will now learn to reconstruct the original information (i.e., remove the noise) between two steps. Fully trained, these models are able to create photo-realistic images from noise.

To create an image from text, the diffusion process has to be conditioned using a text prompt. This is a way to provide additional information to guide the generative process. 

While generative models are not that common in Earth observation, we were wondering, whether we could use a diffusion process to pretrain our models in a self-supervised fashion. 

So we trained a diffusion model on our [*ben-ge* dataset]({{< ref "2023-07-21-Ben-Ge_Extending_Bigearthnet_with_Geographical_and_Environmental_Data" >}}). We provide Sentinel-1 and Sentinel-2 raster data as different bands into the model and we experiment the other data modalities as input for the conditioning mechanism.

Did it work?


{{< image
src="diffusion_qualitative_sample.png"
descr="Synthetic sample generated with our method. The columns show synthetically generated data modalities at different timesteps (top to bottom) of the diffusion process. At the final timestep, realistic and consistent (across the data modalities) scenes emerge from the noise." >}}

As the figure above shows, the model is definitely able to generate realistically looking Sentinel-2 scenes. But more importantly, the Sentinel-1 SAR data that it generates for the same scene, is very consistent with the Sentinel-2 data. This supports the notion that the model learns useful information. But are the learned representations useful for downstream tasks such as land use/land cover classification and segmentation?

The answer seems clear: diffusion pretraining works well for the segmentation task, but not so much for the classification tasks. Furthermore, conditioning of the model seems to improve the results.

For more details, please consult our contribution to IGARSS 2024 (see below).

# Resources

* Alexander Lontke, Michael Mommert, Damian Borth, "*Multi-Modal Diffusion for Self-Supervised Pretraining*", [IEEE International Geoscience and Remote Sensing Symposium 2024](https://ieeexplore.ieee.org/abstract/document/10640509), 2024.
