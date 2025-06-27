---
layout: default
title: News
permalink: /news/
---

<section class="section bg-light">
  <div class="container">
    <div class="section-title">
      <h2>Latest News</h2>
    </div>
    <div class="grid">
      {% for post in site.posts %}
      <div class="card">
        <h3 class="card-title">{{ post.title }}</h3>
        <p class="date">{{ post.date | date: "%B %d, %Y" }}</p>
        <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
        <a href="{{ post.url | relative_url }}" class="btn">Read More</a>
      </div>
      {% endfor %}
    </div>
  </div>
</section> 