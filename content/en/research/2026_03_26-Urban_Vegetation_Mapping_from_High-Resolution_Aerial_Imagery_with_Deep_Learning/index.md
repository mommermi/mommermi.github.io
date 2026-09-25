---
date: 2026-03-26
title: Urban Vegetation Mapping from High-Resolution Aerial Imagery with Deep Learning
tags:
- Remote Sensing
- Deep Learning
- Aerial Imagery
- Urban Environment
- Vegetation
- Segmentation
---

Trees, parks, lawns and hedges are more than just pleasant to look
at. Urban greenery helps keep cities cool on hot summer days and soaks
up rainwater that would otherwise flood streets and overwhelm
drains. To plan, manage and protect these green spaces, cities need to
know exactly where vegetation grows. Detailed vegetation maps also
feed into computer simulations that help cities prepare for heat waves
and heavy rainfall.

Such maps can be created from aerial and satellite images with the
help of artificial intelligence. Until now, however, most of these
approaches have been complex to set up and required powerful,
expensive computers.

## A simpler approach

In this project, we tested whether vegetation can also be mapped
reliably using readily available AI tools that run on ordinary
hardware. We worked with high-resolution aerial photos of Stuttgart,
in which each pixel covers just 8 by 8 centimeters on the ground. In
addition to normal color information, the images also capture
near-infrared light, which is invisible to the human eye but often
used to detect plants.

To teach the AI what vegetation looks like, we manually marked areas
of tall vegetation (such as trees and bushes) and flat vegetation
(such as lawns and meadows) on almost 4,000 images.

We then trained two different types of AI models. The first classifies
every single pixel of an image according to whether it shows tall
vegetation, flat vegetation or neither. The second performs object
detection, which draws boxes around individual areas of vegetation.

## What we found

Both methods reliably detected vegetation, and their results closely matched what a human sees when looking at the images. The pixel-by-pixel approach proved particularly accurate.

{{< image
src="segmentation_sample_results.png"
descr="We show a sample aerial image (left) and the model predictions (yellow and orange shaded areas) against the ground truth labels (yellow outlines). Low vegetation appears in yellow, tall vegetation in orange. The predictions closely follow the ground truth labels, which supports the model's capability to identiy vegetation in an urban context. Aerial images: (c) 2026 Landeshauptstadt Stuttgart, Stadtmessungsamt." >}}


We also made some useful discoveries along the way. The near-infrared information turned out to be unnecessary: the models performed just as well using only ordinary color images. Small, lightweight versions of the models also delivered solid results, so no specialized computer equipment is needed. The biggest factor limiting accuracy was not the AI itself but the quality of the hand-drawn training examples. Finally, our models also worked well on freely available aerial images of lower resolution that they had never seen during training.

## Why this matters

Our results show that accurate vegetation maps can be created from aerial images using free, easy-to-use AI tools and modest computing power. This makes the technology accessible to a wide range of users, from city administrations and planning offices to researchers and environmental organizations.

## Publication

This work originated as a course project as part of the course "Remote Sensing Studio" in the [Master Photogrammetry and Geoinformation](https://www.hft-stuttgart.com/geomatics/master-photogrammetry-and-geoinformatics) study program at the Stuttgart Technical University of Applied Sciences.  

Results were presented at the annual meeting of the German Society of Photogrammetry, Remote Sensing and Geoinformation (March 25-27, 2026) in Darmstadt. The full paper is available in the proceedings:


K. H. Aung, J. A. Ayala Rico, I. A. Ayibilisah, M. Farhang Khaghan Pour, L. Hakim, S. Joshi, A. K. Rasa,
B. C. Mwimangire, O. M. Mukiri, N. Rahbardarestani, J. D. Velazquez Cupido, Q. Yousufzai, W. Rauser, M. Mommert, "Urban Vegetation Mapping from High-Resolution Aerial Imagery with Deep Learning", Jahrestagung der Deutschen Gesellschaft für Photogrammetrie, Fernerkundung und Geoinformation, 25.-27. März 2026, Darmstadt, [paper](https://dgpf.de/src/tagung/jt2026/proceedings/paper/10_dgpf2026_Aung_et_al.pdf).