---
layout: post
title: "Congratulations to Valerio and Josh on Their Graduation"
date: 2026-03-23 20:00:00 +1000
categories: news achievements
excerpt: "Congratulations to Dr. Valerio Falasca on completing his PhD, and to Josh Fleming on completing Honours. We are proud of your achievements with the Kumar Group and wish you both the very best for what comes next."
---

<div class="post-content">
    <figure class="post-figure post-figure-half">
        <img src="{{ site.baseurl }}/assets/valerioandjosh/4ba466b0-4b99-44bf-9d73-875a83d52bfb.JPG" alt="Dr. Valerio Falasca (PhD) and Josh Fleming (Honours) at graduation" class="featured-image">
        <figcaption>Dr. Valerio Falasca and Josh Fleming at the graduation ceremony.</figcaption>
    </figure>

    <p>We are delighted to celebrate two outstanding milestones. Valerio Falasca has completed his PhD and graduates as Dr. Valerio Falasca. Josh Fleming has successfully completed his Honours degree. Both achievements reflect years of dedication, curiosity, and hard work in the lab and beyond.</p>

    <figure class="post-figure post-figure-half">
        <img src="{{ site.baseurl }}/assets/valerioandjosh/2e7c00ea-bd31-4184-be4e-130aa886eaac%202.jpg" alt="Dr. Valerio Falasca with Professor Naresh Kumar" class="featured-image">
        <figcaption>Dr. Valerio Falasca with Professor Naresh Kumar.</figcaption>
    </figure>

    <p>Valerio and Josh have each contributed to our group in their own way, through research, collaboration, and the energy they brought to the team. Seeing you both at graduation is a proud moment for everyone who has worked alongside you.</p>

    <p> we wish you  both the very best</p>

  

    <div class="graduation-slideshow-section">
        <h3 class="slideshow-heading">More moments from the day</h3>
        <figure class="slideshow-figure">
            <div class="graduation-slideshow-frame">
                <img id="valerio-josh-slideshow-img" src="{{ site.baseurl }}/assets/valerioandjosh/0c212947-9eb6-4f6a-a6bb-ddbdf72cb7db.JPG" alt="Graduation celebration photo">
            </div>
            <figcaption class="slideshow-legend">Slideshow of graduation photos.</figcaption>
        </figure>
    </div>
</div>

<script>
(function () {
  var el = document.getElementById('valerio-josh-slideshow-img');
  if (!el) return;
  var slides = [
    "{{ site.baseurl }}/assets/valerioandjosh/0c212947-9eb6-4f6a-a6bb-ddbdf72cb7db.JPG",
    "{{ site.baseurl }}/assets/valerioandjosh/1de570ad-b81c-4b43-a9fe-b92620d7471c.JPG",
    "{{ site.baseurl }}/assets/valerioandjosh/228dc4b3-78ce-4780-9c15-12bdee2d817d.JPG",
    "{{ site.baseurl }}/assets/valerioandjosh/5213631e-ce59-42f8-8f9b-bf11998afa03.JPG",
    "{{ site.baseurl }}/assets/valerioandjosh/57b7b801-d30f-4590-8a8f-9fb4740d2c95.JPG",
    "{{ site.baseurl }}/assets/valerioandjosh/f8c9d845-99b9-4c2a-a3aa-e0cff782ac61.JPG"
  ];
  var i = 0;
  setInterval(function () {
    i = (i + 1) % slides.length;
    el.src = slides[i];
  }, 5000);
})();
</script>

<style>
.post-content {
    max-width: 800px;
    margin: 0 auto;
}

.post-figure {
    margin: 2rem auto;
    text-align: center;
}

.post-figure-half {
    max-width: 50%;
}

.post-figure .featured-image {
    max-width: 100%;
    width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.post-figure figcaption {
    margin-top: 0.65rem;
    font-size: 0.95rem;
    line-height: 1.45;
    color: #4b5563;
}

@media (max-width: 640px) {
    .post-figure-half {
        max-width: 100%;
    }
}

.featured-image {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.post-content p {
    margin-bottom: 1.5rem;
    line-height: 1.6;
    text-align: justify;
}

.graduation-slideshow-section {
    margin-top: 3rem;
    padding-top: 2rem;
    border-top: 1px solid #e5e7eb;
}

.slideshow-heading {
    color: #2c3e50;
    font-size: 1.25rem;
    margin-bottom: 1rem;
    text-align: center;
}

.graduation-slideshow-frame {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
    background: #f3f4f6;
}

.graduation-slideshow-frame img {
    display: block;
    width: 100%;
    height: auto;
    max-height: 520px;
    object-fit: contain;
    margin: 0 auto;
    transition: opacity 0.35s ease;
}

.slideshow-figure {
    margin: 0;
}

.slideshow-legend {
    margin-top: 0.75rem;
    font-size: 0.9rem;
    line-height: 1.45;
    color: #4b5563;
    text-align: center;
}

h1.post-title, .post-title, h1 {
    text-align: center !important;
}
</style>
