---
title: About
layout: page
---

Earth-observing satellites provide a plethora of data directly related
to environmental, economic, and societal issues. Due to their sheer
amount, the systematic interpretation of remote sensing data on a regional or
even global scale requires highly scalable analysis methods.


<p align="justify">
<img src="/images/moi.jpg" alt="C'est moi" class="img-circle"
align="right" hspace="25" height="30%" width="30%">
I am currently a senior researcher at the
<a href="https://hsg.ai">
Institute of Computer Science</a> of the
<a href="http://www.unisg.ch">University of St. Gallen</a> where my research 
focuses on the intersection between computer vision and remote
sensing. I am utilizing deep learning methods to extract knowledge
from satellite observations to improve these methods and to address a
wide range of issues related to environmental science, hazard
prevention and monitoring and geoscience.
</p>

<p align="justify">In my previous life, I worked as an astronomer,
exploring asteroids and comets in our Solar System and building
<a href="https://sbpy.org/">open</a>
<a href="https://github.com/mommermi/photometrypipeline">source</a>
<a href="https://astroquery.readthedocs.io/en/latest/">software</a>
tools to make astronomers' lifes easier.</p>

<p align="justify">Results from my current and previous research are
presented in a number of articles on this website.</p>

<h2>Latest Research</h2>

{% for post in site.posts limit:5 %}
   <li>{{ post.date | date: "%-d %B %Y"}} - 
   <a href="{{ post.url }}" title="{{ post.description }}">
   {{ post.title }}</a></li>
{% endfor %}

<h2>Contact</h2>

<p>University of St. Gallen
<br>Institute of Computer Science (ICS-HSG)
<br>Rosenbergstrasse 30
<br>CH-9000 St. Gallen</p>

[email](mailto:mommermiscience (you-know-what) gmail.com) |
[Github](https://github.com/mommermi) |
[LinkedIn](https://www.linkedin.com/in/michael-mommert/) |
[Twitter](https://twitter.com/mommermi) |
[Google Scholar](https://scholar.google.com/citations?hl=de&user=KSfMP58AAAAJ) |
[Researchgate](https://www.researchgate.net/profile/Michael_Mommert)
