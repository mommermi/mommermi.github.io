---
layout: page
title: Archive
---

This archive lists my research activities over the past years. For a listing <a href="#categories-ref">by research category</a> or <a href="#topics-ref">by research topic</a>, please see below.

<ul>
{% for post in site.posts %}
    <li>{% include post_preview.html post=post %}
{% endfor %}
</ul>

<p style="margin: 40px 0 40px 0;">
<hr>
</p>

<header class="post-header" id="categories-ref">
    <h1 class="post-title">Research categories</h1>
</header>

{% for category in site.categories %}
 <h2 id="{{ category | first }}-ref">{{ category | first }}</h2>
  <ul>     
  {% for post in category.last %}
      <li>{% include post_preview.html post=post %}
  {% endfor %}
  </ul>
{% endfor %}

<p style="margin: 40px 0 40px 0;">
<hr>
</p>

<header class="post-header" id="topics-ref">
    <h1 class="post-title">Research topics</h1>
</header>

{% for tag in site.tags %}
 <h2 id="{{ tag | first }}-ref">{{ tag | first }}</h2>
  <ul>     
  {% for post in tag.last %}
      <li>{% include post_preview.html post=post %}
  {% endfor %}
  </ul>
{% endfor %}



