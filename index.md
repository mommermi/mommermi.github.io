---
layout: page
---

<h2>What's New?</h2>

A few things have changed recently.

This website is new. I decided to move my website from wordpress to
github pages as it provides me more flexibility.

My job is new. I have decided to leave astronomy and start a new
career as computer scientist, where I will learn about and apply
machine learning techniques - and specifically deep learning - to
remote sensing data of Earth.

I hope to be able to share some early results here, soon. Stay tuned!

<h2>Latest Blog Posts</h2>

{% for post in site.posts limit:5 %}
   <li>{{ post.date | date: "%-d %B %Y"}} - 
   <a href="{{ post.url }}" title="{{ post.description }}">
   {{ post.title }}</a></li>
{% endfor %}