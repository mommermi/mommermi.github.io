---
date: 2026-03-26
title: AI-Based Methods for the Detection and Characterization of Traditional Orchards
tags:
- Remote Sensing
- Deep Learning
- Aerial Imagery
- Orchards
- Vegetation
- Segmentation
---

Traditional orchards are among the most species-rich habitats in Central Europe. Especially in southern Germany, their loosely scattered, tall-trunked fruit trees have shaped the landscape for centuries. Yet these orchards have been in decline for decades.

Although traditional orchards are legally protected, there is still no up-to-date and complete overview of where they can actually be found. But exactly this knowledge would be the basis for protecting and maintaining them in a targeted way. Surveying all orchards on foot is hardly feasible given the vast area involved, and it would be far too expensive.

## Spotting Fruit Trees from the Air

In this work, we developed a method that automatically finds traditional orchards in aerial images. We use only data made freely available by the state of Baden-Württemberg: aerial images with a resolution of 20 cm per pixel, and elevation data from a surface model, from which we can derive the height of trees and buildings.

We trained an artificial intelligence on a diverse area of around 250 square kilometers in the center of Baden-Württemberg, where it learned to recognize trees in aerial images. A further processing step then splits connected tree areas into individual tree crowns and examines how the trees are arranged relative to one another. If at least seven trees stand close together in several rows, the area is classified as a traditional orchard. Smaller groups are classified as tree rows or individual trees.

## What We Found

The AI recognizes trees very reliably, even in areas it never saw during training. For each detected tree, the size and diameter of its crown as well as its height can also be determined. Initial analyses suggest that the images can also be used to roughly estimate how healthy the trees are. However, these results are not yet reliable enough.

{{< image
src="streuobstwiese.png"
descr="The visualization shows a sample aerial image in which traditional orchards were detected. As part of the workflow, individual trees are identified, and for each tree the average NDVI is measured as an indicator of its health. This makes it possible to spot diseased trees even in larger orchards." >}}


Some challenges remain: hedges and rows of trees near orchards are sometimes mistakenly included, very young and small trees are hard to recognize in the images, and in summer some fields can look deceptively similar to trees. In addition, aerial images are only taken every few years and at different times of the year, which makes comparisons difficult. Checking the results is also challenging, as there is currently no up-to-date and error-free reference data.

## Why This Matters

The method shows that traditional orchards can be mapped statewide and at low cost, without expensive drone flights or laser scanning. Since only freely available data is used, the approach can easily be transferred to other regions and applied to other landscape features. In the long term, it could lead to a tool that allows authorities, orchard advisors and farmers to regularly monitor the condition of orchards. We are pursuing this idea further in the ongoing project "miraculix," funded by the German Federal Environmental Foundation (DBU), which focuses on mistletoe and other tree diseases.

## Publication

The results were presented at the annual meeting of the German Society for Photogrammetry, Remote Sensing and Geoinformation (March 25–27, 2026) in Darmstadt. The full paper is available in the conference proceedings:

J. Jäger, M. Mommert, G. Austen, "Einsatz KI-basierter Methoden zur Detektion und Charakterisierung von Streuobstbeständen auf Basis von Open GeoData" [AI-Based Methods for the Detection and Characterization of Traditional Orchards Based on Open GeoData], Annual Meeting of the German Society for Photogrammetry, Remote Sensing and Geoinformation, March 25–27, 2026, Darmstadt, [paper](https://dgpf.de/src/tagung/jt2026/proceedings/paper/20_dgpf2026_Jaeger_et_al.pdf) available.
