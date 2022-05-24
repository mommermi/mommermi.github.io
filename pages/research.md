---
layout: page
title: Research
---

My research focus lies at the intersection of computer vision and Earth observation: I am interested in advancing Deep Learning methods for computer vision problems and applying them to remote sensing data in response to a wide range of environmental, economic and societal issues. 

## Projects

The following list provides an overview of some of my previous research projects:

<ul>
{% for tag in site.tags %}
  {% if tag.first == 'research' %}
     {% for post in tag.last %}
        {%- if post.categories contains "remote sensing" -%}
        <li><a href="{{ post.url }}">{{ post.title }}</a>: {{ post.description }} 
        [{{ post.date | date: '%Y/%m'}}]</li>
        {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
</ul>

For a more complete list of research items please consult the [archive](./archive).


## Students

The success of my research heavily relies on the help of students who work on a range of different projects:

### Current Students

* Joelle Hanna<span style="color:gray">\*</span>, PhD program in Computer Science, since 2021. 
* Linus Scheibenreif<span style="color:gray">\*</span>, PhD program in Computer Science, since 2021.

### Former Students

* Robin Sutter, *Time Series Forecasting of Photovoltaic
Energy with Physics-guided Deep Learning Ensembles*, Master in Business Innovation, submitted.
* Leonardo Eicher<span style="color:gray">\*</span>, *Traffic Noise Estimation from Remote
Imaging Data with Deep Learning*, Bachelor in Business Administration, 2022; results are to be published at IGARSS 2022.  
* Moritz Blattner<span style="color:gray">\*</span>, *Detection and Monitoring of Commercial Vehicles from Satellite Images using Deep Learning*, Master in Business Innovation, 2021; results were published at the [*Tackling Climate Change with Machine Learning* workshop at ICML 2021](https://www.climatechange.ai/papers/icml2021/19).
* Samuel Navarro-Meza<span style="color:gray">\*</span>, *Rapid response
characterization of Near-Earth Asteroids using RATIR*, Universidad Nacional Autónoma de México/Northern Arizona University, PhD, 2021; co-mentored with Mauricio Reyes-Ruiz and David Trilling; results were published in *[The Astronomical Journal](https://arxiv.org/abs/1903.08320)*.
* Nathan Smith<span style="color:gray">\*</span>, *Thermophysical Modeling of Phobos*, Northern Arizona University Physics Master student, 2017; co-mentored with Christopher Edwards and David Trilling; results were published at the *[Ninth International Conference on Mars 2019](https://www.hou.usra.edu/meetings/ninthmars2019/pdf/6391.pdf)*.
* Louis Dan Avner<span style="color:gray">\*</span>, *The Flagstaff Robotic Survey Telescope*,  Northern Arizona University Physics Master student, 2017; co-mentored with David Trilling and Ted Dunham.
* Cassandra Lejoly, *Near-Infrared and Optical Observations of Centaurs and Trans-Neptunian Objects*, Northern Arizona University Physics Master student, 2016;  [thesis](https://www.proquest.com/pagepdf/1840889133?accountid=28962).


<span style="color:gray">*: supervision as acting topical advisor/co-advisor</span>


