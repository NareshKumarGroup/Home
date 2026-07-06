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
    
    <!-- Featured News Section -->
    <div class="featured-news">
      {% assign latest_post = site.posts.first %}
      {% if latest_post %}
      <div class="featured-card">
        <div class="featured-content">
          <div class="featured-image">
            {% if latest_post.title contains "Happy Birthday" and latest_post.title contains "Vidi" %}
              <img src="{{ site.baseurl }}/assets/images/vidia/IMG_8287.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Vidi Nuraini" %}
              <img src="{{ site.baseurl }}/assets/images/vidia/presnetation1.JPG" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Md Musfizur Hassan" %}
              <img src="{{ site.baseurl }}/assets/images/new/md-hassan.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Welcome" and latest_post.title contains "Lab Members" %}
              <img src="{{ site.baseurl }}/assets/images/newlabmates/welcome-scaled.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Daniel Guo" %}
              <img src="{{ site.baseurl }}/assets/images/newlabmates/danielimahge.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Dittu and Robert" %}
              <img src="{{ site.baseurl }}/assets/june2026news/51lzzdD1IML.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Lilla, Matthew, and Tope" %}
              <img src="{{ site.baseurl }}/assets/june2026news/milestone.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Poster Award" or latest_post.title contains "PhD Review" %}
              <img src="{{ site.baseurl }}/assets/images/new/1771942652593.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Rasel" %}
              <img src="{{ site.baseurl }}/assets/images/raseloralpresenetation/oralrasel.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Happy Birthday" and latest_post.title contains "Matthew Erlik" %}
              <img src="{{ site.baseurl }}/assets/images/mattbday/pngtree-colorful-happy-birthday-hat-and-balloons-png-image_19692697.png" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "New Year" %}
              <img src="{{ site.baseurl }}/assets/images/newyear/62bb425b-3eb2-43c1-9c7d-6a5a32080e2f.JPG" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Sam" %}
              <img src="{{ site.baseurl }}/assets/images/new/Samlatestpappernov.jpeg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "ACS Infectious Diseases" %}
              <img src="{{ site.baseurl }}/assets/images/nathanpaper/images_medium_id6c00072_0005.gif" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Nathan Carey" or latest_post.title contains "JoVE Protocol for Antimicrobial" %}
              <img src="{{ site.baseurl }}/assets/images/Nathan.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Tope A. Ibisanmi" or latest_post.title contains "Peptidomimetic Research at Asia-Pacific Biofilms 2026" %}
              <img src="{{ site.baseurl }}/assets/images/topetalk/PHOTO-2026-03-29-12-08-08.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Asia-Pacific Biofilms" or latest_post.title contains "Naresh Delivers Engaging Talk" or latest_post.title contains "Professor Naresh Delivers" %}
              <img src="{{ site.baseurl }}/assets/images/nareshtalk/PHOTO-2026-03-27-13-21-29%202.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Valerio and Josh" %}
              <img src="{{ site.baseurl }}/assets/valerioandjosh/4ba466b0-4b99-44bf-9d73-875a83d52bfb.JPG" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Valerio" %}
              <img src="{{ site.baseurl }}/assets/images/Get.jpeg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Yao" %}
              <img src="{{ site.baseurl }}/assets/images/yaogroupdinner/225a5713-4ce0-435d-815a-5cb91aa4443d.JPG" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Ghayah" %}
              <img src="{{ site.baseurl }}/assets/images/ghayahpaperoct2025.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "MvfR" or latest_post.title contains "Scientific Reports: MvfR" %}
              <img src="{{ site.baseurl }}/assets/images/images-9.png" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Josh Fleming" or latest_post.title contains "Antibiotics Publication" %}
              <img src="{{ site.baseurl }}/assets/images/antibiotics-15-00484-g002.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% elsif latest_post.title contains "Tope" %}
              <img src="{{ site.baseurl }}/assets/fbinf-06-1749404-g002.webp" alt="{{ latest_post.title }}" class="featured-img">
            {% else %}
              <img src="{{ site.baseurl }}/assets/images/ghayahpaperoct2025.jpg" alt="{{ latest_post.title }}" class="featured-img">
            {% endif %}
          </div>
          <div class="featured-text">
            <h3 class="featured-title">{{ latest_post.title }}</h3>
            <p class="featured-date">{{ latest_post.date | date: "%B %d, %Y" }}</p>
            <p class="featured-excerpt">{{ latest_post.excerpt | strip_html | truncatewords: 30 }}</p>
            <a href="{{ latest_post.url | relative_url }}" class="btn btn-featured">Read More</a>
          </div>
        </div>
      </div>
      {% endif %}
    </div>
    
    <!-- All News Grid -->
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

<style>
.featured-news {
  margin-bottom: 3rem;
}

.featured-card {
  background: linear-gradient(135deg, #6d5fd9 0%, #818cf9 25%, #a78bfa 50%, #8b5cf6 75%, #7c3aed 100%);
  border-radius: 12px;
  padding: 2rem;
  color: white;
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

.featured-content {
  display: flex;
  align-items: center;
  gap: 2rem;
}

.featured-image {
  flex-shrink: 0;
}

.featured-img {
  width: 200px;
  height: 150px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.featured-text {
  flex: 1;
}

.featured-title {
  color: white;
  margin-bottom: 0.5rem;
  font-size: 1.5rem;
}

.featured-date {
  color: rgba(255,255,255,0.8);
  margin-bottom: 1rem;
  font-size: 0.9rem;
}

.featured-excerpt {
  color: rgba(255,255,255,0.9);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.btn-featured {
  background: rgba(255,255,255,0.2);
  color: white;
  border: 2px solid rgba(255,255,255,0.3);
  transition: all 0.3s ease;
}

.btn-featured:hover {
  background: rgba(255,255,255,0.3);
  border-color: rgba(255,255,255,0.5);
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .featured-card {
    padding: 1.25rem;
  }

  .featured-content {
    flex-direction: column;
    text-align: center;
    gap: 1.25rem;
  }

  .featured-image {
    width: 100%;
  }
  
  .featured-img {
    width: 100%;
    max-width: 280px;
    height: auto;
    max-height: 220px;
    object-fit: cover;
  }

  .featured-title {
    font-size: 1.2rem;
    line-height: 1.35;
    overflow-wrap: anywhere;
  }

  .featured-excerpt {
    text-align: left;
    font-size: 0.95rem;
  }

  .grid {
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }

  .card p {
    text-align: left;
  }
}

@media (max-width: 480px) {
  .featured-card {
    padding: 1rem;
  }

  .featured-title {
    font-size: 1.05rem;
  }

  .featured-img {
    max-width: 100%;
    max-height: 260px;
  }

  .card-title {
    font-size: 1.05rem;
    overflow-wrap: anywhere;
  }
}
</style> 