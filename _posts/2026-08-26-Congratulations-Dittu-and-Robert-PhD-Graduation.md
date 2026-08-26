---
layout: news-post
title: "Congratulations to Dittu and Robert on Their PhD Graduation"
date: 2026-08-26 12:00:00 +1000
categories: news achievements
permalink: /news/congratulations-dittu-and-robert-phd-graduation/
excerpt: "The Kumar Research Group congratulates Dr Dittu Suresh and Dr Robert Rourke on their PhD graduation. We celebrate their dedication, thank Professor Naresh Kumar for his support, and share moments from the day."
---

<div class="post-content phd826-post">
    <p>Caps on, gowns flowing, and two new doctors in the house. The Kumar Research Group is delighted to congratulate <strong>Dr Dittu Suresh</strong> and <strong>Dr Robert Rourke</strong> on their PhD graduation, a proud milestone years in the making.</p>

    <p>Your dedication never wavered: the long days at the bench, the careful thinking behind every experiment, and the quiet persistence that turns hard problems into finished theses. We have watched you grow as scientists, colleagues, and friends, and today we get to cheer you on in full academic colour.</p>

    <div class="graduation-slideshow-section">
        <h3 class="slideshow-heading">Moments from graduation day</h3>
        <figure class="slideshow-figure">
            <div class="phd-slideshow-frame">
                <img id="phd826-slideshow-img" src="{{ site.baseurl }}/assets/images/PHD826/DITTU/dittu-with-naresh.jpg" alt="Graduation celebration photo">
            </div>
            <figcaption class="slideshow-legend">Slideshow of photos from Dittu and Robert's PhD graduation.</figcaption>
        </figure>
    </div>

    <p>A special thank you to <strong>Professor Naresh Kumar</strong> for the guidance, patience, and unwavering support that carried both of you through the doctoral journey. Mentorship like that does not show up in a thesis appendix, but it is written all over days like this.</p>

    <p>And Rob, about that thesis. We are still checking whether UNSW issued you a second degree for page count alone.</p>

    <p>The entire group is proud of you both. Congratulations, Dr Suresh and Dr Rourke. You have earned every smile in these photos.</p>
    
    <p>We wish you both continued success in your current jobs.</p>

    <h3 class="profiles-heading">Read more</h3>
    <div class="grad-profile-grid">
        <a class="grad-profile-card" href="{{ site.baseurl }}/news/congratulations-dittu-and-robert-phd-graduation/dittu-suresh/">
            <img src="{{ site.baseurl }}/assets/images/PHD826/DITTU/dittu-with-naresh.jpg" alt="Dr Dittu Suresh with Professor Naresh Kumar">
            <div class="grad-profile-info">
                <h4>Dr Dittu Suresh</h4>
                <p>Graduation moments with Professor Naresh and the group</p>
                <span class="grad-profile-link">View page →</span>
            </div>
        </a>
        <a class="grad-profile-card" href="{{ site.baseurl }}/news/congratulations-dittu-and-robert-phd-graduation/robert-rourke/">
            <img src="{{ site.baseurl }}/assets/images/PHD826/ROB/rob-with-naresh.jpg" alt="Dr Robert Rourke with Professor Naresh Kumar">
            <div class="grad-profile-info">
                <h4>Dr Robert Rourke</h4>
                <p>Graduation moments with Professor Naresh and on stage</p>
                <span class="grad-profile-link">View page →</span>
            </div>
        </a>
    </div>
</div>

<script>
(function () {
  var el = document.getElementById('phd826-slideshow-img');
  if (!el) return;
  var base = "{{ site.baseurl }}";
  var slides = [
    base + "/assets/images/PHD826/DITTU/dittu-with-naresh.jpg",
    base + "/assets/images/PHD826/ROB/rob-with-naresh.jpg",
    base + "/assets/images/PHD826/DITTU/dittu-with-group.jpg",
    base + "/assets/images/PHD826/ROB/rob-spotlight.jpg"
  ];
  var alts = [
    "Dr Dittu Suresh with Professor Naresh Kumar",
    "Dr Robert Rourke with Professor Naresh Kumar",
    "Dr Dittu Suresh with the Kumar Research Group",
    "Dr Robert Rourke on stage at graduation"
  ];
  var i = 0;
  setInterval(function () {
    i = (i + 1) % slides.length;
    el.style.opacity = "0.35";
    setTimeout(function () {
      el.src = slides[i];
      el.alt = alts[i];
      el.style.opacity = "1";
    }, 280);
  }, 4500);
})();
</script>

<style>
.phd826-post {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 0.5rem;
    box-sizing: border-box;
    overflow-x: hidden;
    width: 100%;
}

.phd826-post p {
    margin-bottom: 1.5rem;
    line-height: 1.65;
    text-align: justify;
    overflow-wrap: anywhere;
    word-wrap: break-word;
}

.phd826-post .graduation-slideshow-section {
    margin: 2.5rem 0;
    width: 100%;
}

.phd826-post .slideshow-heading,
.phd826-post .profiles-heading {
    color: #2c3e50;
    font-size: 1.25rem;
    margin: 0 0 1rem;
    text-align: center;
}

.phd826-post .phd-slideshow-frame {
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
    background: #f3f4f6;
    width: 100%;
}

.phd826-post .phd-slideshow-frame img {
    display: block;
    width: 100%;
    max-width: 100%;
    height: auto;
    max-height: 560px;
    object-fit: contain;
    margin: 0 auto;
    transition: opacity 0.3s ease;
}

.phd826-post .slideshow-figure {
    margin: 0;
    width: 100%;
}

.phd826-post .slideshow-legend {
    margin-top: 0.75rem;
    font-size: 0.9rem;
    line-height: 1.45;
    color: #4b5563;
    text-align: center;
}

.phd826-post .grad-profile-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.5rem;
    margin: 1.5rem 0 0.5rem;
    width: 100%;
}

.phd826-post .grad-profile-card {
    display: block;
    text-decoration: none;
    color: inherit;
    border-radius: 10px;
    overflow: hidden;
    background: #fff;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    min-width: 0;
}

.phd826-post .grad-profile-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.12);
}

.phd826-post .grad-profile-card img {
    display: block;
    width: 100%;
    max-width: 100%;
    height: 260px;
    object-fit: cover;
    object-position: center top;
}

.phd826-post .grad-profile-info {
    padding: 1.1rem 1.2rem 1.25rem;
}

.phd826-post .grad-profile-info h4 {
    margin: 0 0 0.35rem;
    color: #2c3e50;
    font-size: 1.1rem;
}

.phd826-post .grad-profile-info p {
    margin: 0 0 0.65rem;
    color: #6b7280;
    font-size: 0.95rem;
    line-height: 1.45;
    text-align: left;
}

.phd826-post .grad-profile-link {
    color: #4f46e5;
    font-size: 0.92rem;
    font-weight: 600;
}

@media (max-width: 768px) {
    .phd826-post {
        max-width: 100%;
        padding: 0 0.25rem;
    }

    .phd826-post p {
        text-align: left;
        font-size: 1rem;
        line-height: 1.65;
        margin-bottom: 1.25rem;
    }

    .phd826-post .slideshow-heading,
    .phd826-post .profiles-heading {
        font-size: 1.15rem;
    }

    .phd826-post .grad-profile-grid {
        grid-template-columns: 1fr;
        gap: 1.15rem;
    }

    .phd826-post .grad-profile-card img {
        height: auto;
        aspect-ratio: 3 / 4;
        max-height: 420px;
    }

    .phd826-post .grad-profile-info {
        padding: 1rem 1.05rem 1.15rem;
    }

    .phd826-post .phd-slideshow-frame {
        border-radius: 8px;
    }

    .phd826-post .phd-slideshow-frame img {
        max-height: none;
    }

    .phd826-post .grad-profile-link {
        display: inline-block;
        min-height: 44px;
        line-height: 44px;
    }
}

@media (max-width: 480px) {
    .phd826-post p {
        font-size: 0.98rem;
    }

    .phd826-post .slideshow-legend {
        font-size: 0.85rem;
    }
}

h1.post-title,
.post-title,
h1 {
    text-align: center !important;
}
</style>
