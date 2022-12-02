---
layout: page
title: Research
---

My research focuses on the intersection of [computer vision](https://en.wikipedia.org/wiki/Computer_vision) and [Earth observation](https://en.wikipedia.org/wiki/Earth_observation). Computer vision enables computers to "see" and therefore to perform autonomous image analysis methods on large amounts of data. Earth observation data feature unique traits that make them an interesting test bed for computer vision methods: virtually unlimited amounts of multi-modal (different sensors) time-series (observations at different times) data are available for virtually any location on Earth at almost no cost. The combination of these two fields enable me to develop efficient Deep Learning methods for computer vision problems with applications to Earth observation and beyond. 

Some approaches that I am currently interested in include [self-supervised learning](https://en.wikipedia.org/wiki/Self-supervised_learning) in combination with [data fusion](https://en.wikipedia.org/wiki/Data_fusion) methods. Furthermore, I am interested in [weakly supervised learning](https://en.wikipedia.org/wiki/Weak_supervision) methods and applications to real-world problems. 


Some of my recent research results are listed in the following:

<ul>
{% for post in site.posts limit:5 %}
    {%- if post.categories.first != "Astronomy" -%}
	<li>{% include post_preview.html post=post %}	
    {% endif %}
{% endfor %}
</ul>

In my previous research in astronomy, I investigated the physical properties of [asteroids](https://en.wikipedia.org/wiki/Asteroid) and [comets](https://en.wikipedia.org/wiki/Comet) and built open-source scientific software. 

For a more complete list of research projects, please consult the [archive](./archive).


## Team

Research is a team effort. Our team is part of the [*Artificial Intelligence and Machine Learning* chair](https://hsg-aiml.github.io/), headed by [Prof. Dr. Damian Borth](https://ics.unisg.ch/chair-aiml-borth/), who is also involved in many of our projects. Our success relies heavily on the work of our students; the following students are or were (co-)supervised by me:	

### Current Students

* Joelle Hanna*, PhD in Computer Science, since 2021, official supervisor: [Damian Borth](https://www.alexandria.unisg.ch/persons/7781). 
* Linus Scheibenreif*, PhD in Computer Science, since 2021, official supervisor: [Damian Borth](https://www.alexandria.unisg.ch/persons/7781).


* Yosef Asefaw, Bachelor in Business Administration, *Deep clustering of traffic camera imagery*.
* Aron Baeriswyl, Master in Quantitative Economics/Finance, *Improving Road Noise Estimation with Contrastive Self-Supervised Learning*.
* Yannick Cadonau, Bachelor in Business Adminiistration, *Setting realistic expectations for solar power production forecasts utilizing weather predictions*.
* Lorenz Dreyer, Master in General Management, *Characterization of Open-pit Mining Areas from Satellite Imagery*.
* Flurin Jacomet, Bachelor in Economics, *Identifying Active Mining Operations*.


### Former Students

* Robin Sutter, *Time Series Forecasting of Photovoltaic
Energy with Physics-guided Deep Learning Ensembles*, Master in Business Innovation, 2022.
* Leonardo Eicher, *Traffic Noise Estimation from Remote
Imaging Data with Deep Learning*, Bachelor in Business Administration, 2022; results were published at [IGARSS 2022](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9883463) (open access: [unisg](http://www.alexandria.unisg.ch/267269/1/IGARSS_traffic_noise.pdf)).  
* Moritz Blattner, *Detection and Monitoring of Commercial Vehicles from Satellite Images using Deep Learning*, Master in Business Innovation, 2021; results were published at the [*Tackling Climate Change with Machine Learning* workshop at ICML 2021](https://www.climatechange.ai/papers/icml2021/19).
* Samuel Navarro-Meza, *Rapid response
characterization of Near-Earth Asteroids using RATIR*, Universidad Nacional Autónoma de México/Northern Arizona University, PhD, 2021; co-mentored with Mauricio Reyes-Ruiz and David Trilling; results were published in *[The Astronomical Journal](https://arxiv.org/abs/1903.08320)*.
* Nathan Smith, *Thermophysical Modeling of Phobos*, Northern Arizona University Physics Master student, 2017; co-mentored with Christopher Edwards and David Trilling; results were published at the *[Ninth International Conference on Mars 2019](https://www.hou.usra.edu/meetings/ninthmars2019/pdf/6391.pdf)*.
* Louis Dan Avner, *The Flagstaff Robotic Survey Telescope*,  Northern Arizona University Physics Master student, 2017; co-mentored with David Trilling and Ted Dunham.
* Cassandra Lejoly, *Near-Infrared and Optical Observations of Centaurs and Trans-Neptunian Objects*, Northern Arizona University Physics Master student, 2016;  [thesis](https://www.proquest.com/pagepdf/1840889133?accountid=28962).



