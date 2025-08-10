---
layout: default
title: Home
---

<div class="hero">
    <div class="container">
        <h1>Welcome to the Naresh Kumar Research Group</h1>
        <p class="subtitle">Medicinal Chemistry Research at <a href="https://www.unsw.edu.au" target="_blank">UNSW</a> Sydney</p>
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
            {% if post.title == "Congratulations to Maryam on the Completion of Her PhD!" %}
            <div class="card maryam-news-card" style="display: flex; align-items: center; gap: 2rem;">
                <img src="{{ site.baseurl }}/assets/images/Maryham.jpg" alt="Maryam PhD Graduation" style="width: 152px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); flex-shrink: 0;">
                <div>
                    <h3 class="card-title">{{ post.title }}</h3>
                    <p class="date">July 14, 2025</p>
                    <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
                    <a href="{{ post.url | relative_url }}" class="btn">Read More</a>
                </div>
            </div>
            {% else %}
            <div class="card">
                <h3 class="card-title">{{ post.title }}</h3>
                <p class="date">{{ post.date | date: "%B %d, %Y" }}</p>
                <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
                <a href="{{ post.url | relative_url }}" class="btn">Read More</a>
            </div>
            {% endif %}
            {% endfor %}
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="section-title">
            <h2>Gallery</h2>
        </div>
        <div class="slideshow-container">
            <div class="slideshow-wrapper">

                 <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/slideshows/dec2024part.jpg" alt="December 2024 Research">
                </div>
                
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/slideshows/1-s2.0-S0960894X25002598-ga1-2.jpg" alt="Research Image 1">
                </div>
                 <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/slideshows/5A2D7F64-EA1D-41F9-94E2-A9547A8C7BEE.jpeg" alt="Research Image 4">
                </div>
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/slideshows/id5c00148_0012-2.webp" alt="Research Image 2">
                </div>
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/slideshows/1-s2.0-S0968089625000781-ga1.jpg" alt="Research Image 3">
                </div>
               
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/slideshows/3AA8A75A-7356-4CC6-8745-A153EC92D57D.jpeg" alt="Research Image 5">
                </div>
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/slideshows/25B80DED-9513-4D01-8463-FDC2B0549E46.jpeg" alt="Research Image 6">
                </div>
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/slideshows/yaoproj2.jpg" alt="Research Image 7">
                </div>
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/slideshows/yaoproj1.jpg" alt="Research Image 8">
                </div>
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/slideshows/quorum-sensing.jpg" alt="Quorum Sensing Research">
                </div>
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/slideshows/flpt3.jpg" alt="FLT3 Research">
                </div>
                <div class="slide fade">
                    <video controls autoplay muted loop>
                        <source src="{{ site.baseurl }}/assets/images/slideshows/myncresearch.mp4" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                </div>
                <div class="slide fade">
                    <video controls autoplay muted loop>
                        <source src="{{ site.baseurl }}/assets/images/slideshows/simulation.mp4" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                </div>
               
            </div>
            
            <button class="slideshow-btn prev" onclick="changeSlide(-1)">&#10094;</button>
            <button class="slideshow-btn next" onclick="changeSlide(1)">&#10095;</button>
            
            <div class="slideshow-dots">
                <span class="dot active" onclick="currentSlide(1)"></span>
                <span class="dot" onclick="currentSlide(2)"></span>
                <span class="dot" onclick="currentSlide(3)"></span>
                <span class="dot" onclick="currentSlide(4)"></span>
                <span class="dot" onclick="currentSlide(5)"></span>
                <span class="dot" onclick="currentSlide(6)"></span>
                <span class="dot" onclick="currentSlide(7)"></span>
                <span class="dot" onclick="currentSlide(8)"></span>
                <span class="dot" onclick="currentSlide(9)"></span>
                <span class="dot" onclick="currentSlide(10)"></span>
                <span class="dot" onclick="currentSlide(11)"></span>
                <span class="dot" onclick="currentSlide(12)"></span>
                <span class="dot" onclick="currentSlide(13)"></span>
            </div>
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

<script>
let slideIndex = 1;
showSlides(slideIndex);

function changeSlide(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("slide");
    let dots = document.getElementsByClassName("dot");
    
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
        // Pause any videos when hiding slides
        let videos = slides[i].getElementsByTagName("video");
        for (let j = 0; j < videos.length; j++) {
            videos[j].pause();
            videos[j].currentTime = 0; // Reset video to beginning
        }
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
    
    // Autoplay video if the current slide contains one
    let currentVideos = slides[slideIndex-1].getElementsByTagName("video");
    for (let j = 0; j < currentVideos.length; j++) {
        currentVideos[j].play();
    }
}

// Auto-advance slides every 5 seconds
setInterval(function() {
    changeSlide(1);
}, 5000);
</script> 