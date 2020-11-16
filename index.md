---
layout: page
---

<h2>Remote Sensing and Artificial Intelligence</h2>

Earth-observing satellites provide a plethora of data that are
directly related to our environment, our habitat, and our community. I
am applying artificial intelligence methods to remote sensing data to
extract information that affect us and our planet.

My research currently focuses on quantifying the forces that are
driving climate change: greenhouse gas emissions, human mobility, and
other economic factors.

I utilize state-of-the-art computer vision methods for the
classification and segmentation of Earth observation data covering a
wide range of the electromagnetic spectrum, as well as to detect
individual objects in remote sensing image data.


<h2>Latest Articles</h2>

{% for post in site.posts limit:5 %}
   <li>{{ post.date | date: "%-d %B %Y"}} - 
   <a href="{{ post.url }}" title="{{ post.description }}">
   {{ post.title }}</a></li>
{% endfor %}