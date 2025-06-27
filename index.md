---
layout: default
title: Home
---

<div class="hero">
    <div class="container">
        <h1>Welcome to the Naresh Kumar Research Group</h1>
        <p class="subtitle">Medicinal Chemistry Research at UNSW Sydney</p>
    </div>
</div>

<section class="section">
    <div class="container">
        <div class="section-title">
            <a href="{{ '/research' | relative_url }}" class="btn">Our Research</a>
        </div>
        <div class="grid">
            <div class="card">
                <h3 class="card-title">Medicinal Chemistry</h3>
                <p>Our group focuses on the design and synthesis of novel drug candidates for various therapeutic targets, with a particular emphasis on cancer and infectious diseases.</p>
            </div>
            <div class="card">
                <h3 class="card-title">Drug Discovery</h3>
                <p>We employ state-of-the-art techniques in medicinal chemistry, including structure-based drug design, fragment-based drug discovery, and high-throughput screening.</p>
            </div>
            <div class="card">
                <h3 class="card-title">Chemical Biology</h3>
                <p>Our research integrates chemical synthesis with biological studies to understand disease mechanisms and develop new therapeutic strategies.</p>
            </div>
        </div>
        <div class="grid center-single-card">
            <div class="card">
                <h3 class="card-title">Computational Drug Discovery</h3>
                <p>We use AI, machine learning, deep learning, molecular docking, and simulation to accelerate drug discovery and design.</p>
            </div>
        </div>
    </div>
</section>

<section class="section bg-light">
    <div class="container">
        <div class="section-title">
            <h2>Latest News</h2>
        </div>
        <div class="grid">
            {% for post in site.posts limit:3 %}
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

<section class="section">
    <div class="container">
        <div class="section-title">
            <h2>Join Our Team</h2>
        </div>
        <div class="grid">
            <div class="card">
                <h3 class="card-title">PhD Opportunities</h3>
                <p>We are always looking for motivated PhD students with a background in chemistry, medicinal chemistry, or related fields.</p>
                <a href="{{ '/opportunities' | relative_url }}" class="btn">Learn More</a>
            </div>
            <div class="card">
                <h3 class="card-title">Postdoctoral Positions</h3>
                <p>Interested in joining our team as a postdoctoral researcher? Check our current openings.</p>
                <a href="{{ '/opportunities' | relative_url }}" class="btn">View Positions</a>
            </div>
        </div>
    </div>
</section> 