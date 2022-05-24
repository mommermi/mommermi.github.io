---
title: About
layout: page
---

<p align="justify">
<img src="/images/moi.jpg" alt="C'est moi" class="img-circle"
align="right" hspace="25" height="30%" width="30%">
I am Assistant Professor for Computer Vision 
at the <a href="http://www.unisg.ch">University of St. Gallen</a>'s 
<a href="https://www.unisg.ch/en/universitaet/schools/computer-science">
School of Computer Science</a>. My research 
combines computer vision with Earth observation,
thereby leveraging scalable Deep Learning approaches to extract knowledge
from remote sensing data. By implementing new methodological approaches
and tailoring existing methods in combination with unique, targeted datasets, 
my team and I are able to address a
wide range of environmental, economic, and societal issues. </p>

<p align="justify">In my previous life, I worked as an astronomer,
exploring <a href="https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=mommert&view=OPD">asteroids and comets</a> 
in our Solar System and building
<a href="https://sbpy.org/">open</a>
<a href="https://github.com/mommermi/photometrypipeline">source</a>
<a href="https://astroquery.readthedocs.io/en/latest/">software</a>
tools to make astronomers' lifes easier.</p>

<h2>Latest Research</h2>

{% for post in site.posts limit:5 %}
   <li>{{ post.date | date: "%-d %B %Y"}} - 
   <a href="{{ post.url }}" title="{{ post.description }}">
   {{ post.title }}</a></li>
{% endfor %}

<h2>Contact</h2>

<p>University of St. Gallen
<br>School of Computer Science
<br>Rosenbergstrasse 30
<br>CH-9000 St. Gallen</p>

[email](mailto:michael.mommert (you-know-what) unisg.ch) |
[Github](https://github.com/mommermi) |
[LinkedIn](https://www.linkedin.com/in/michael-mommert/) |
[Twitter](https://twitter.com/mommermi) |
[Google Scholar](https://scholar.google.com/citations?hl=de&user=KSfMP58AAAAJ) |
[Researchgate](https://www.researchgate.net/profile/Michael_Mommert)
