---
layout: page
title: Blog Posts by Topic
---

{% for category in site.categories %}
 <h2 id="{{ category | first }}-ref">{{ category | first }}</h2>
  <ul>     
  {% for post in category.last %}
   <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
  </ul>
{% endfor %}
