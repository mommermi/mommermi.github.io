---
layout: page
title: Articles by Year
---

There is also a [list of articles by topic](./blog_category) and a
[list of articles by type](./blog_tag).



{% for post in site.posts  %}
 {% capture this_year %}{{ post.date | date: "%Y" }}{% endcapture %}
 {% capture next_year %}{{ post.previous.date | date: "%Y" }}{% endcapture %}

 {% if forloop.first %}
 <h2 id="{{ this_year }}-ref">{{this_year}}</h2>
 <ul>
 {% endif %}

 <li><a href="{{ post.url }}" title="{{ post.description }}">
 {{ post.title }}</a></li>

 {% if forloop.last %}
 </ul>
 {% else %}
  {% if this_year != next_year %}
  </ul>
  <h2 id="{{ next_year }}-ref">{{next_year}}</h2>
  <ul>
  {% endif %}
 {% endif %}
{% endfor %}

