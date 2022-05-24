---
layout: page
title: Articles by Type
---

This page contains a list of all articles published on this webpage sorted by the type of publication.

There is also a [list of articles by topic](./archive_category) and a
[list of articles by publication year](./archive).


{% for tag in site.tags %}
 <h2 id="{{ tag | first }}-ref">{{ tag | first }}</h2>
  <ul>     
  {% for post in tag.last %}
   <li><a href="{{ post.url }}" title="{{ post.description }}">
   {{ post.title }}</a></li>
  {% endfor %}
  </ul>
{% endfor %}

