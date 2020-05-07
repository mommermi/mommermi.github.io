---
layout: page
title: Blog Posts by Topic
---


{% for category in site.categories %}
 <h2 id="{{ category | first }}-ref">{{ category | first }}</h2>
  <ul>     
  {% for post in category.last %}
   <li><a href="{{ post.url }}" title="{{ post.description }}">
   {{ post.title }}</a></li>
  {% endfor %}
  </ul>
{% endfor %}

Hint: there is also a [list of posts by publication year](./blog) and a
[list of posts by type](./blog_tag).