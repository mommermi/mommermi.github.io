---
layout: page
title: Blog Posts by Type
---

{% for tag in site.tags %}
 <h2 id="{{ tag | first }}-ref">{{ tag | first }}</h2>
  <ul>     
  {% for post in tag.last %}
   <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
  </ul>
{% endfor %}
