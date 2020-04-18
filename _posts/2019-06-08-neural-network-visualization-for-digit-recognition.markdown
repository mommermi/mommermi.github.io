---
author: mommermi
date: 2019-06-08 06:10:29+00:00
layout: post
title: Neural Network Visualization for Digit Recognition
description: |
  How do neural networks work? This little project helped me to get a
  better understanding of their workings.
categories:
- deep learning
tags:
- toy project
---

Neural Networks can do amazing things, but they are complex which makes them often hard to understand.

In order to better understand how these machine learning models work, I used a common Neural Network model - a [Multilayer Perceptron](https://en.wikipedia.org/wiki/Multilayer_perceptron) - to recognize hand-written digits and then looked into what the individual neurons in this model are doing. The model I used consisted of 3 dense layers: one hidden layer with 256 neurons, one hidden layer with 64 neurons, and one output layer with 10 different neurons, one for each digit. The training data consisted of the [MNIST](https://en.wikipedia.org/wiki/MNIST_database) database of hand-written digits.

This is what the visualization reveals.

The following animation shows on the far left different versions of the digit "5". Each frame was sent through the trained neural network and it was recorded which neurons reacted - or fired - during this process in each of the layers. The three rightmost plots indicate the three layers of the model. The brighter a pixel, the higher is the output value of the corresponding neuron in the network for corresponding input frame.

![mlp_individualframes](https://michaelmommert.files.wordpress.com/2019/06/mlp_individualframes.gif)

Interestingly, it turned out that for each of the 10 digits only a subset of the neurons fired - and it was more or less always the same subset. In this animation, this is best seen in the second hidden layer, in which more or less the same pixels are colored. It turns out that the first hidden layer pre-processes the pixel data from the original frame. The purpose of the second hidden layer is to find patterns in the output data of the first hidden layer.

Each digit produces a unique fingerprint in the network, thus enabling the recognition of the different hand-written digits with high accuracy.

The code and full explanation for this project is available on [kaggle](https://www.kaggle.com/mommermi/mnist-neural-network-visualization).
