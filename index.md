---
title: Remote Sensing and Artificial Intelligence
layout: page
---

Earth-observing satellites provide a plethora of data directly related
to environmental, economic, and societal issues. Due to their sheer
amount, the systematic interpretation of remote sensing data on a regional or
even global scale requires highly scalable analysis methods.

As a researcher at the intersection between artificial intelligence
research and remote sensing, I am utilizing artificial neural networks
to extract knowledge from satellite observations in the form of
classification, segmentation, and object detection problems.

My current research focuses on quantifying climate change drivers,
including greenhouse gas emissions from industrial plants and human
mobility, as well as other economic sectors. In general, I am
interested in the combination of artificial intelligence methods with
imaging data of Earth to investigate current issues related to
environmental science, hazard prevention and monitoring, geoscience,
and making Earth a better place for all of us.


<h2>Latest Articles</h2>

{% for post in site.posts limit:5 %}
   <li>{{ post.date | date: "%-d %B %Y"}} - 
   <a href="{{ post.url }}" title="{{ post.description }}">
   {{ post.title }}</a></li>
{% endfor %}