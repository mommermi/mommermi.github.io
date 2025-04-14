---
title: Teaching
menu: main
summary: |
  My teaching activities focus on the fields of machine learning/deep learning and remote sensing, but I also teach in other fields, such as photogrammetry, sensor systems and physics. On this page I share some of my teaching resources.
---

## Jupyter Notebooks

Instead of only teaching theoretical basics, I prefer to also cover practical aspects. For this purpose, I use Jupyter Notebooks, which have proven to be very useful for teaching activities, especially when used on cloud-based computing environments such as Binder or Google Colab.

In the following, you find a list of currently available Jupyter Notebooks that are available on my [github teaching repository](https://github.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert). All of these Notebooks are freely available under the MIT Licence, so everyone is invited to use them in their own teaching activities.

The Notebooks are loosely ordered by the following topics. 

### Python

Introductory Notebooks for learning the Python programming language.

* **Basics**: A general introduction into the basics of the the Python programming language. *Interactivity*: low. *Prequisites*: None <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=python%2Fbasics%2Fpython_basics.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/python/basics/python_basics.ipynb)

* **Numpy and Matplotlib**: A more detailed introduction into the Numpy and Matplotlib modules. *Interactivity*: low. *Prequisites*: basic Python <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=python%2Fnumpy-matplotlib%2Fpython_numpy-matplotlib.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/python/numpy-matplotlib/python_numpy-matplotlib.ipynb) 

* **Pandas**: An introduction into Pandas module for data processing and analysis. *Interactivity*: low. *Prequisites*: basic Python <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=python%2Fpandas%2Fpython_pandas.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/python/pandas/python_pandas.ipynb) 


### Data Processing

Noteboks related to the processing of different data modalities.

* **Feature Extraction**: An interactive Notebook introducing different feature extraction techniques for different data modalities. *Interactivity*: high, *Prerequisites*: some experience with Python <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=dataprocessing%2Ffeatureextraction%2Fdataprocessing_featureextraction.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/dataprocessing/featureextraction/dataprocessing_featureextraction.ipynb)


### Clustering

Notebooks related to different clustering applications.

* **Clustering and PCA with sklearn**: A brief introduction into unsupervised learning methods such as clustering and Principal Component Analysis.
*Interactivity*: medium. *Prerequisites*: Numpy experience. <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=clustering%2Fclustering-pca%2Fclustering_clustering-pca.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/clustering/clustering-pca/clustering_clustering-pca.ipynb)

* **Clustering and Segmentation for Sentinel-2 Satellite Imagery**: This example contains segmentation examples based on k-Means clustering and SLIC for a small Sentinel-2 multispectral dataset. *Interactivity*: medium. *Prerequisites*: some experience with Python. <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=clustering%2Fkmeans-slic%2Fsentinel-2%2Fclustering_kmeans-slic_sentinel-2.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/clustering/kmeans-slic/sentinel-2/clustering_kmeans-slic_sentinel-2.ipynb)


### Machine Learning Concepts

Introductions to different supervised learning concepts.

* **Preparing Data for Supervised Learning**: This Notebook serves as an interactive worksheet for preparing a dataset for use in a machine learning model. It will guide you through the steps required to use a dataset in a supervised learning setup. *Interactivity*: high. *Prerequisites*: Numpy experience. <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=mlconcepts%2Fdatapreparation%2Fmlconcepts_datapreparation.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/mlconcepts/datapreparation/mlconcepts_datapreparation.ipynb)

* **Full Supervised Learning Pipeline**: This Notebook combines all the pieces together to perform a classification task with scikit-learn. *Interactivity*: low. *Prerequisites*: some experience with Python. <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=mlconcepts%2Fslpipeline%2Fmlconcepts_slpipeline.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/mlconcepts/slpipeline/mlconcepts_slpipeline.ipynb)

* **Data Labeling**: This tutorial introduces the data labeling process for multiband imaging data. The data are used for a pixel-wise classification of Sentinel-2 data. *Interactivity*: medium. *Prerequisites*: some experience with Python and familiarity with the "Pixel-wise classification with Machine Learning"-Notebook. <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=mlconcepts%2Flabeling%2Fmlconcepts_labeling.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/mlconcepts/labeling/mlconcepts_labeling.ipynb)

* **Data Augmentations**: Building on the "Semantic Segmentation of Sentinel-2 Images with a UNet"-Notebook, this Notebook introduces data augmentations and experiments with a few simple transformations. *Interactivity*: medium. *Prerequisites*: experience with Python and semantic segmentation using a UNet; running this Notebook requires access to a GPU! <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=mlconcepts%2Fdataaugmentations%2Fmlconcepts_dataaugmentations.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/mlconcepts/dataaugmentations/mlconcepts_dataaugmentations.ipynb)

* **Transfer Learning**: Building on the "Image Classification with Convolutional Neural Networks"-Notebook, this Notebook introduces the concept of transfer learning. *Interactivity*: low. *Prerequisites*: experience with Python and semantic segmentation using a UNet; running this Notebook requires access to a GPU! <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=mlconcepts%2Ftransferlearning%2Fmlconcepts_transferlearning.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/mlconcepts/transferlearning/mlconcepts_transferlearning.ipynb)


### Regression

Notebooks related to regression tasks.

* **Regression on the California Housing Dataset**: This is an introductory notebook, featuring different traditional machine learning methods applied to a tabular dataset. *Interactivity*: medium. *Prerequisites*: some experience with Python. <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=regression%2Fml%2Fcaliforniahousing%2Fregression_ml_californiahousing.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/regression/ml/californiahousing/regression_ml_californiahousing.ipynb)


### Pixel-wise Classification

Notebooks related to pixel-wise classification tasks.

* **Pixel-wise Classification with Machine Learning**: This example showcases the use of traditional machine learning methods
for pixel-wise land-use/land-cover classification. Simple data annotation by hand, as well as Maximum likelihood estimation and k-nearest neighbors methods are introduced for this purpose. *Interactivity*: medium. *Prerequisites*: some experience with Python. <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=classification%2Fpixel-wise%2Fml%2Fsentinel-2%2Fclassification_pixel-wise_ml_sentinel-2.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/classification/pixel-wise/ml/sentinel-2/classification_pixel-wise_ml_sentinel-2.ipynb)

* **Pixel-wise Classification with a Multilayer Perceptron**: This tutorial introduces the use of Multilayer Perceptrons for pixel-wise classification for land-use/land-cover classification. *Interactivity*: low. *Prerequisites*: some experience with Python; running this Notebook requires access to a GPU! <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=classification%2Fpixel-wise%2Fmlp%2Fsentinel-2%2Fclassification_pixel-wise_mlp_sentinel-2.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/classification/pixel-wise/mlp/sentinel-2/classification_pixel-wise_mlp_sentinel-2.ipynb)


### Image-wise Classification

Notebooks related to image classification tasks.

* **Image Classification with a Multilayer Perceptron**: In this Notebook we build a Multilayer Perceptron from scratch using Pytorch and train it on a simple image classification task based on the FashionMNIST dataset.  *Interactivity*: low. *Prerequisites*: some experience with Python; running this Notebook requires access to a GPU! <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=classification%2Fimage-wise%2Fmlp%2Ffashionmnist%2Fclassification_image-wise_mlp_fashionmnist.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/classification/image-wise/mlp/fashionmnist/classification_image-wise_mlp_fashionmnist.ipynb)


* **Image Classification with a Convolutional Neural Network**: This example introduces the use of Convolutional Neural Networks for the task of image classification. *Interactivity*: low. *Prerequisites*: some experience with Python, familiarity with the "Pixel-wise classification using machine learning"-Notebook would be useful; running this Notebook requires access to a GPU! <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=classification%2Fimage-wise%2Fcnn%2Fsentinel-2%2Fclassification_image-wise_cnn_sentinel-2.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/classification/image-wise/cnn/sentinel-2/classification_image-wise_cnn_sentinel-2.ipynb)


### Semantic Segmentation

Notebooks related to semantic segmentation tasks.

* **Semantic Segmentation of Sentinel-2 Images with a UNet**: This Notebook introduces the workflow for supervised learning with a UNet architecture available in Pytorch. We will us dense labels available in the *ben-ge-800* dataset for this task. *Interactivity*: low. *Prerequisites*: some experience with Python and familiarity with the "Pixel-wise Classification with a Multilayer Perceptron for Sentinel-2 Satellite Imagery"-Notebook; running this Notebook requires access to a GPU! <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=segmentation%2Funet%2Fsentinel-2%2Fsegmentation_unet_sentinel-2.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/segmentation/unet/sentinel-2/segmentation_unet_sentinel-2.ipynb)


### Object Detection

Notebooks related to object detection tasks.

* **Object Detection with YOLO for Aerial Imagery**: This Notebook introduces object detection using YOLO for aerial imagery. We will detect cars from aerial imagery of the city of Stuttgart. *Interactivity*: low. *Prerequisites*: some experience with Python; running this Notebook requires access to a GPU! <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=objectdetection%2Fyolo%2Faerialimagery%2Fobjectdetection_yolo_aerialimagery.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/objectdetection/yolo/aerialimagery/objectdetection_yolo_aerialimagery.ipynb)

### Remote Sensing

Notebooks related to general remote sensing tasks.

* **Thermal Imaging with flyr**: [Flyr](https://pypi.org/project/flyr/) is a library for extracting thermal data from FLIR images written fully in Python. We use this library to read in, modify and analyse thermograms. *Interactivity*: medium. *Prerequisites*: some experience with Python. <br>[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/main?labpath=remotesensing%2Fthermal%2Fflyr%2Fremotesensing_thermal_flyr.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert/blob/main/remotesensing/thermal/flyr/remotesensing_thermal_flyr.ipynb)


For an up-to-date list of all available Notebooks, please refer to my  [github teaching repository](https://github.com/Hochschule-fuer-Technik-Stuttgart/teaching-mommert).
