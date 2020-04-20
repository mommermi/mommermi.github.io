---
author: mommermi
date: 2019-06-13 04:41:41+00:00
layout: post
title: Recognizing Asteroid Streaks using a Convolutional Neural Network
description: |
  Asteroid streaks are common in long exposure images from professional
  telescopes. Finding them can improve orbit estimates or even enable the
  discovery of previously unknown objects. Based on simulated data, I
  investigate how hard it is to identify asteroid streaks.
categories:
- astronomy
- deep learning
tags:
- toy project
---

This toy project is aimed at recognizing asteroid streaks - caused by the movement of asteroids against the fixed background in long-exposure astronomical images. This is an important task to discover new asteroids in large survey programs.

{% include image.html url="/images/2019-06-13-recognizing-asteroid-streaks-using-a-convolutional-neural-network/streaks_example.png" description="Some of the synthetic training data used in this project. Linear features resemble asteroid streaks caused by their motion relative to the background, which here only consists of stars and low-level background noise." %}


I have heard about the use of Convolutional Neural Networks for this task before and have been wondering for a while how hard it would be to implement such a model.

The answer is: it is not very hard. Have a look at [this notebook](https://github.com/mommermi/streak_detection/blob/master/Streak_Detection.ipynb) for a simple toy model that is able to correctly identify ~98% of all asteroid streaks in synthetic data!
