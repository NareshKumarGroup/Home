---
layout: default
title: Home
---

<div class="hero">
    <div class="container">
        <h1>Welcome to the Naresh Kumar Research Group</h1>
        <p class="subtitle">Organic/Medicinal Chemistry Research at <a href="https://www.unsw.edu.au" target="_blank">UNSW</a> Sydney</p>
    </div>
</div>

<section class="section welcome-note-section">
    <div class="container">
        <div class="welcome-note">
            <h2 class="welcome-note-title">Welcome to Our Group</h2>
            <p class="welcome-note-intro">We are delighted to have you explore our research. Our group is dedicated to advancing the frontiers of organic chemistry, medicinal chemistry, and drug discovery.</p>
            <div class="welcome-note-summary">
                <p>Our research centres on the discovery and development of novel bioactive molecules for industrial and medical applications. Naturally produced chemicals play fundamental roles in biological systems, yet many are available only in trace amounts. Through innovative organic synthesis, we access these molecules and their analogues, enabling full assessment of biological activity, mode of action, and the development of new therapeutic leads. Our work is multi-disciplinary, combining synthetic organic chemistry, molecular modelling, and biological screening.</p>
            </div>
        </div>
    </div>
</section>

<section class="section research-showcase-section">
    <div class="container">
        <div class="research-showcase-header">
            <div class="research-showcase-title-wrap">
                <img src="{{ site.baseurl }}/assets/images/MPgi.gif" alt="" class="research-showcase-gif">
                <h2 class="research-showcase-title">Our Research</h2>
            </div>
            <p class="research-showcase-subtitle">Discover our research areas in Organic chemistry and drug discovery</p>
            <a href="{{ '/research' | relative_url }}" class="btn research-showcase-btn">Explore All Research</a>
        </div>
        <div class="research-cards-grid">
            <a href="{{ '/research' | relative_url }}" class="research-card">
                <div class="research-card-image">
                    <img src="{{ site.baseurl }}/assets/images/758.jpeg" alt="Organic/Medicinal Chemistry">
                    <div class="research-card-overlay"></div>
                </div>
                <div class="research-card-content">
                    <h3>Organic/Medicinal Chemistry</h3>
                    <p>Our group focuses on the design and synthesis of novel drug candidates for various therapeutic targets, with a particular emphasis on cancer and infectious diseases.</p>
                </div>
            </a>
            <a href="{{ '/research' | relative_url }}" class="research-card">
                <div class="research-card-image">
                    <img src="{{ site.baseurl }}/assets/images/flpt3.jpg" alt="Drug Discovery">
                    <div class="research-card-overlay"></div>
                </div>
                <div class="research-card-content">
                    <h3>Drug Discovery</h3>
                    <p>We employ state-of-the-art techniques in Organic/Medicinal Chemistry, including structure-based drug design, fragment-based drug discovery, and high-throughput screening.</p>
                </div>
            </a>
            <a href="{{ '/research' | relative_url }}" class="research-card">
                <div class="research-card-image">
                    <img src="{{ site.baseurl }}/assets/images/quorum-sensing.jpg" alt="Chemical Biology">
                    <div class="research-card-overlay"></div>
                </div>
                <div class="research-card-content">
                    <h3>Chemical Biology</h3>
                    <p>Our research integrates chemical synthesis with biological studies to understand disease mechanisms and develop new therapeutic strategies.</p>
                </div>
            </a>
            <a href="{{ '/research' | relative_url }}" class="research-card research-card-center">
                <div class="research-card-image">
                    <video class="research-card-video" autoplay loop muted playsinline preload="auto">
                        <source src="{{ site.baseurl }}/assets/images/simulation.mp4" type="video/mp4">
                    </video>
                    <div class="research-card-overlay"></div>
                </div>
                <div class="research-card-content">
                    <h3>Computational Drug Discovery</h3>
                    <p>We use AI, machine learning, deep learning, molecular docking, and simulation to accelerate drug discovery and design.</p>
                </div>
            </a>
        </div>
    </div>
</section>

<section class="section bg-light">
    <div class="container">
        <div class="section-title">
            <h2>Latest News</h2>
        </div>
        
        <!-- Featured News - latest post by date -->
        {% assign featured_home_post = site.posts.first %}
        {% if featured_home_post %}
        <div class="featured-news-home">
            <div class="featured-card-home">
                <div class="featured-content-home">
                    <div class="featured-image-home">
                        {% if featured_home_post.title contains "Welcome" and featured_home_post.title contains "Lab Members" %}
                          <img src="{{ site.baseurl }}/assets/images/newlabmates/welcome-scaled.jpg" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "Poster Award" or featured_home_post.title contains "PhD Review" %}
                          <img src="{{ site.baseurl }}/assets/images/new/1771942652593.jpg" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "Rasel" %}
                          <img src="{{ site.baseurl }}/assets/images/raseloralpresenetation/oralrasel.jpg" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "Happy Birthday" and featured_home_post.title contains "Matthew Erlik" %}
                          <img src="{{ site.baseurl }}/assets/images/mattbday/pngtree-colorful-happy-birthday-hat-and-balloons-png-image_19692697.png" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "New Year" %}
                          <img src="{{ site.baseurl }}/assets/images/newyear/62bb425b-3eb2-43c1-9c7d-6a5a32080e2f.JPG" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "Sam" %}
                          <img src="{{ site.baseurl }}/assets/images/new/Samlatestpappernov.jpeg" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "Nathan Carey" or featured_home_post.title contains "JoVE Protocol for Antimicrobial" %}
                          <img src="{{ site.baseurl }}/assets/images/Nathan.jpg" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "Tope A. Ibisanmi" or featured_home_post.title contains "Peptidomimetic Research at Asia-Pacific Biofilms 2026" %}
                          <img src="{{ site.baseurl }}/assets/images/topetalk/PHOTO-2026-03-29-12-08-08.jpg" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "Asia-Pacific Biofilms" or featured_home_post.title contains "Naresh Delivers Engaging Talk" %}
                          <img src="{{ site.baseurl }}/assets/images/nareshtalk/PHOTO-2026-03-27-13-21-29%202.jpg" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "Valerio and Josh" %}
                          <img src="{{ site.baseurl }}/assets/valerioandjosh/4ba466b0-4b99-44bf-9d73-875a83d52bfb.JPG" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "Valerio" %}
                          <img src="{{ site.baseurl }}/assets/images/Get.jpeg" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "Yao" %}
                          <img src="{{ site.baseurl }}/assets/images/yaogroupdinner/225a5713-4ce0-435d-815a-5cb91aa4443d.JPG" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "Ghayah" %}
                          <img src="{{ site.baseurl }}/assets/images/ghayahpaperoct2025.jpg" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "MvfR" or featured_home_post.title contains "Scientific Reports: MvfR" %}
                          <img src="{{ site.baseurl }}/assets/images/images-9.png" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "Josh Fleming" or featured_home_post.title contains "Antibiotics Publication" %}
                          <img src="{{ site.baseurl }}/assets/images/antibiotics-15-00484-g002.jpg" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% elsif featured_home_post.title contains "Tope" %}
                          <img src="{{ site.baseurl }}/assets/fbinf-06-1749404-g002.webp" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% else %}
                          <img src="{{ site.baseurl }}/assets/images/ghayahpaperoct2025.jpg" alt="{{ featured_home_post.title }}" class="featured-img-home">
                        {% endif %}
                    </div>
                    <div class="featured-text-home">
                        <h3 class="featured-title-home">{{ featured_home_post.title }}</h3>
                        <p class="featured-date-home">{{ featured_home_post.date | date: "%B %d, %Y" }}</p>
                        <p class="featured-excerpt-home">{{ featured_home_post.excerpt | strip_html | truncatewords: 30 }}</p>
                        <a href="{{ featured_home_post.url | relative_url }}" class="btn btn-featured-home">Read More</a>
                    </div>
                </div>
            </div>
        </div>
        {% endif %}
        
        <!-- Recent News Grid -->
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
        
        <!-- View All News Button -->
        <div class="text-center" style="margin-top: 2rem;">
            <a href="{{ '/news' | relative_url }}" class="btn btn-outline">View All News</a>
        </div>
    </div>
</section>

<style>
/* Welcome Note - stylish intro */
.welcome-note-section {
  padding: 3rem 0;
  background: linear-gradient(180deg, #fafbff 0%, #ffffff 100%);
}

.welcome-note {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
  padding: 2.5rem 2rem;
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(109, 95, 217, 0.08);
  border-left: 4px solid #818cf9;
  position: relative;
}

.welcome-note::before {
  content: '"';
  position: absolute;
  top: 1rem;
  left: 1.5rem;
  font-size: 4rem;
  font-family: Georgia, serif;
  color: #818cf9;
  opacity: 0.2;
  line-height: 1;
}

.welcome-note-title {
  font-size: 1.75rem;
  color: #2c3e50;
  margin-bottom: 1rem;
  font-weight: 600;
  letter-spacing: -0.02em;
}

.welcome-note-intro {
  font-size: 1.05rem;
  color: #555;
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.welcome-note-summary {
  text-align: left;
  padding: 1.25rem 0;
  border-top: 1px solid #eef2ff;
}

.welcome-note-summary p {
  font-size: 0.98rem;
  line-height: 1.75;
  color: #444;
  margin: 0;
  text-align: justify;
}

.welcome-note-summary strong {
  color: #2c3e50;
}

.welcome-note-summary em {
  color: #818cf9;
  font-style: normal;
  font-weight: 500;
}

/* Research Showcase - stylish cards with images */
.research-showcase-section {
  padding: 4rem 0;
  background: #ffffff;
}

.research-showcase-header {
  text-align: center;
  margin-bottom: 3rem;
}

.research-showcase-title-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 0.5rem;
}

.research-showcase-gif {
  width: 120px;
  height: 120px;
  object-fit: contain;
  background: white;
  padding: 8px;
  border-radius: 8px;
}

.research-showcase-title {
  font-size: 2rem;
  color: #2c3e50;
  margin: 0;
  font-weight: 700;
}

.research-showcase-subtitle {
  color: #666;
  font-size: 1.05rem;
  margin-bottom: 1.5rem;
}

.research-showcase-btn {
  display: inline-block;
}

.research-cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.research-card {
  display: block;
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0,0,0,0.08);
  transition: all 0.35s ease;
  text-decoration: none;
  color: inherit;
}

.research-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 30px rgba(109, 95, 217, 0.2);
}

.research-card-image {
  position: relative;
  height: 220px;
  overflow: hidden;
  background: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
}

.research-card-image img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: center;
  transition: transform 0.4s ease;
}

.research-card-image .research-card-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  transition: transform 0.4s ease;
  display: block;
  background: #ffffff;
}

.research-card:hover .research-card-image img,
.research-card:hover .research-card-image .research-card-video {
  transform: scale(1.05);
}

.research-card-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.4) 100%);
  opacity: 0.6;
}

.research-card-content {
  padding: 1.25rem 1.25rem 1.5rem;
}

.research-card-content h3 {
  font-size: 1.1rem;
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-weight: 600;
  transition: color 0.3s;
}

.research-card:hover .research-card-content h3 {
  color: #818cf9;
}

.research-card-content p {
  font-size: 0.9rem;
  color: #555;
  line-height: 1.5;
  margin: 0;
}

.research-card-center {
  grid-column: 2;
}

@media (max-width: 992px) {
  .research-cards-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .research-card-center {
    grid-column: 1 / -1;
    justify-self: center;
    max-width: calc((100% - 1.5rem) / 2);
  }
}

@media (max-width: 768px) {
  .research-cards-grid {
    grid-template-columns: 1fr;
  }
  
  .research-card-center {
    grid-column: 1;
    justify-self: stretch;
    max-width: none;
  }
  
  .research-card-image {
    height: 200px;
  }
}

.featured-news-home {
  margin-bottom: 2rem;
}

.featured-card-home {
  background: linear-gradient(135deg, #6d5fd9 0%, #818cf9 25%, #a78bfa 50%, #8b5cf6 75%, #7c3aed 100%);
  border-radius: 12px;
  padding: 1.5rem;
  color: white;
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
  margin-bottom: 2rem;
}

.featured-content-home {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.featured-image-home {
  flex-shrink: 0;
}

.featured-img-home {
  width: 150px;
  height: 120px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.featured-text-home {
  flex: 1;
}

.featured-title-home {
  color: white;
  margin-bottom: 0.5rem;
  font-size: 1.3rem;
}

.featured-date-home {
  color: rgba(255,255,255,0.8);
  margin-bottom: 0.8rem;
  font-size: 0.9rem;
}

.featured-excerpt-home {
  color: rgba(255,255,255,0.9);
  line-height: 1.5;
  margin-bottom: 1rem;
  font-size: 0.95rem;
}

.btn-featured-home {
  background: rgba(255,255,255,0.2);
  color: white;
  border: 2px solid rgba(255,255,255,0.3);
  transition: all 0.3s ease;
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
}

.btn-featured-home:hover {
  background: rgba(255,255,255,0.3);
  border-color: rgba(255,255,255,0.5);
  transform: translateY(-2px);
}

.btn-outline {
  background: white;
  color: #2c3e50;
  border: 2px solid white;
  transition: all 0.3s ease;
}

.btn-outline:hover {
  background: #f8faff;
  color: #2c3e50;
  border-color: #818cf9;
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .research-showcase-title-wrap {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .research-showcase-gif {
    width: 90px;
    height: 90px;
    padding: 6px;
  }
  
  .welcome-note {
    padding: 1.5rem 1.25rem;
  }
  
  .welcome-note-title {
    font-size: 1.4rem;
  }
  
  .featured-content-home {
    flex-direction: column;
    text-align: center;
  }
  
  .featured-img-home {
    width: 100%;
    max-width: 250px;
    height: 150px;
  }
  
  .featured-title-home {
    font-size: 1.1rem;
  }
}
</style>

<section class="section">
    <div class="container">
        <div class="section-title">
            <h2>Gallery</h2>
        </div>
        <div class="slideshow-container">
            <div class="slideshow-wrapper">

                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/yaogroupdinner/921f4a39-ad25-4da7-8007-037b3a7a4be8.JPG" alt="Yao Farewell Dinner">
                </div>
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/kiama/Kiamagrouppicture.JPG" alt="Kumar Group at Kiama Conference">
                </div>
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/kiama/Raselposter.JPG" alt="Rasel Khan Poster Prize Winner">
                </div>

                 <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/kiama/dcba3174-4f39-4117-801c-a005f12d709e.JPG" alt="Rasel Prize Winner">
                </div>
                 
                
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/iupac/Lilla.jpg" alt="lilla">
                </div>
                     
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/Alyssa.jpg" alt="alyssa">
                </div>

                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/iupac/PHOTO-2025-08-28-17-03-45.jpg" alt="Kumar Group at IUPAC Conference">
                </div>
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/iupac/1756963452749.jpeg" alt="IUPAC Conference 2025">
                </div>                
               
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/new/isoflavene.jpg" alt="Valerio Isoflavene Publication">
                </div>
                <div class="slide fade">
                    <img src="{{ site.baseurl }}/assets/images/ghayah-publication.jpg" alt="Ghayah Publication">
                </div>                 <div class="slide fade">
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
                    <img src="{{ site.baseurl }}/assets/images/slideshows/maydinner.jpg" alt="Research Image 2">
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
                <span class="dot" onclick="currentSlide(14)"></span>
                <span class="dot" onclick="currentSlide(15)"></span>
                <span class="dot" onclick="currentSlide(16)"></span>
                <span class="dot" onclick="currentSlide(17)"></span>
                <span class="dot" onclick="currentSlide(18)"></span>
                <span class="dot" onclick="currentSlide(19)"></span>
                <span class="dot" onclick="currentSlide(20)"></span>
                <span class="dot" onclick="currentSlide(21)"></span>
                <span class="dot" onclick="currentSlide(22)"></span>
                <span class="dot" onclick="currentSlide(23)"></span>
                <span class="dot" onclick="currentSlide(24)"></span>
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
                <p>We are always looking for motivated PhD students with a background in chemistry, Organic/Medicinal Chemistry, or related fields.</p>
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