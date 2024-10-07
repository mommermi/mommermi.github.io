---
date: 2023-07-21
title: Ben-Ge - Extending Bigearthnet with Geographical and Environmental Data
summary: |
  Multimodal datasets for remote sensing are oftentimes limited to two data modalities, such as multispectral and SAR polarization data. In order to experiment with a much wider range of data modalities, we extended the well-known BigEarthNet dataset to includes a wide range of data modalities.
tags:
- Earth Observation
- Deep Learning
- Dataset
- Multimodal
- Self-supervised Learning
thumbnail_image: sample.png
---

Earth observation data are by default multi-modal. Data are being acquired by a wide range of sensors, some of which are passive sensors (e.g., multiband imaging) and others are active sensors (e.g., SAR). In addition to such observational data, archival data are available for most locations on Earth.

Historically, the field of remote sensing and Earth observation has been very active in the combination of different data modalities ("data fusion") in its data analyses. In a data fusion approach, two or more data modalities are combined in an analysis to improve the results over using just a single data modality.

This concept of data fusion has also been used in deep learning applications. However, in most applications, data fusion is limited to two data modalities, which is also reflected by most available datasets. For instance, the widely spread [BigEarthNet](https://bigearth.net/) dataset combines Sentinel-1 SAR with Sentinel-2 multispectral data (BigEarthNet-MM; MM stands for multimodal). While this combination is very powerful for many application, the question remains whether additional information might benefit the learning process. 


{{< image
src="sample.png"
descr="Sample from the ben-ge dataset. The figure shows (from left to right) for a random scene: the Sentinel-2 true color image (which is already part of BigEarthNet), the digital elevation model, the ESAWorldCover land use/land cover map, as well as the scene's climate zone classification, seasonal encoding and air temperature at the time of observation." >}}

To explore the usefulness of different data modalities, we present the *ben-ge* dataset, which supplements the BigEarthNet-MM dataset by compiling freely and globally available geographical and environmental data.

The *ben-ge* (BigEarthNet with Geographical and Environmental data) dataset complements the Sentinel-1 and Sentinel-2 data provided through [BigEarthNet](https://bigearth.net/) with the following:

* elevation data extracted from the [Copernicus Digital Elevation Model GLO-30](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM);
* land-use/land-cover data extracted from [ESA Worldcover](https://esa-worldcover.org/en);
* climate zone information extracted from [Beck et al. 2018](https://www.nature.com/articles/sdata2018214);
* environmental data such as temperature, relative humidity and wind speed concurrent with the Sentinel-1/2 observations from the [ERA-5 global reanalysis](https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5);
* a seasonal encoding ranging from 0 (winter) to 1 (summer).

Based on this dataset, we showcase the value of combining different data modalities for the downstream tasks of patch-based land-use/land-cover classification and land-use/land-cover segmentation. For instance, we find that the performance on these downstream tasks improves with the number of modalities utilized. Naturally, raster data are more beneficial for segmentation tasks as opposed to per-scene data.


*ben-ge* is freely available and expected to serve as a test bed for fully supervised and self-supervised Earth observation applications. 


# Resources

* Michael Mommert, Nicolas Kesseli, Joelle Hanna, Linus Scheibenreif, Damian Borth, Beg&uuml;m Demir, "*Ben-ge: Extending BigEarthNet with Geographical and Environmental Data*",  [IEEE International Geoscience and Remote Sensing Symposium 2023](https://ieeexplore.ieee.org/iel7/10281394/10281399/10282767.pdf) ([open access](https://arxiv.org/pdf/2307.01741.pdf)), 2023.
