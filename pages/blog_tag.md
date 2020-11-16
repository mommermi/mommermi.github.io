---
layout: page
title: Articles by Type
---

{% for tag in site.tags %}
 <h2 id="{{ tag | first }}-ref">{{ tag | first }}</h2>
  <ul>     
  {% for post in tag.last %}
   <li><a href="{{ post.url }}" title="{{ post.description }}">
   {{ post.title }}</a></li>
  {% endfor %}
  </ul>
{% endfor %}

Hint: there is also a [list of articles by topic](./blog_category) and a
[list of articles by publication year](./blog).
