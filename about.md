---
layout: default
title: About
---

<section class="section">
    <div class="container">
        <div class="section-title">
            <h2>About Our Group</h2>
        </div>
        <div class="about-content">
            <div class="about-text">
                <p>The Naresh Kumar Research Group at <a href="https://www.unsw.edu.au" target="_blank">UNSW</a> Sydney is dedicated to advancing the field of Organic/Medicinal Chemistry through innovative research and collaboration. Our work focuses on developing novel therapeutic agents for various diseases, with a particular emphasis on infectious disease and cancer.</p>

                <div class="about-image">
                    <div class="about-slideshow-container">
                        <div class="about-slideshow-wrapper">
                            <div class="about-slide fade">
                                <img src="{{ site.baseurl }}/assets/images/group/group2.jpg" alt="Kumar Research Group">
                            </div>
                            <div class="about-slide fade">
                                <img src="{{ site.baseurl }}/assets/images/dec2024part.jpg" alt="Kumar Research Group - December 2024 Party">
                            </div>
                            <div class="about-slide fade">
                                <img src="{{ site.baseurl }}/assets/images/group/group3.jpg" alt="Kumar Research Group">
                            </div>
                            <div class="about-slide fade">
                                <img src="{{ site.baseurl }}/assets/images/group/group4.jpg" alt="Kumar Research Group">
                            </div>
                        </div>
                        <button class="about-slideshow-btn prev" onclick="aboutChangeSlide(-1)">&#10094;</button>
                        <button class="about-slideshow-btn next" onclick="aboutChangeSlide(1)">&#10095;</button>
                        <div class="about-slideshow-dots">
                            <span class="about-dot active" onclick="aboutCurrentSlide(1)"></span>
                            <span class="about-dot" onclick="aboutCurrentSlide(2)"></span>
                            <span class="about-dot" onclick="aboutCurrentSlide(3)"></span>
                            <span class="about-dot" onclick="aboutCurrentSlide(4)"></span>
                        </div>
                    </div>
                </div>
                
                <h3>Our Mission</h3>
                <p>We aim to:</p>
                <ul>
                    <li>Design and synthesize novel drug candidates with improved efficacy and reduced side effects</li>
                    <li>Understand the molecular mechanisms of disease and drug action</li>
                    <li>Develop new methodologies for drug discovery and development</li>
                    <li>Machine learning, deep learning, and artificial intelligence in drug discovery</li>
                    <li>Train the next generation of Organic/Medicinal chemists and drug discovery scientists</li>
                    
                </ul>

                <h3>Research Areas</h3>
                <div class="research-areas">
                    <div class="research-area">
                        <h4>Organic/Medicinal Chemistry</h4>
                        <p>Design and synthesis of small molecule therapeutics</p>
                    </div>
                    <div class="research-area">
                        <h4>Drug Discovery</h4>
                        <p>Structure-based drug design and high-throughput screening</p>
                    </div>
                    <div class="research-area">
                        <h4>Chemical Biology</h4>
                        <p>Understanding disease mechanisms through chemical tools</p>
                    </div>
                    <div class="research-area">
                        <h4>Computational Drug Discovery</h4>
                        <p>AI, machine learning, deep learning, molecular docking, and simulation for drug discovery</p>
                    </div>
                </div>

                <h3>Facilities</h3>
                <p>Our group has access to state-of-the-art facilities at <a href="https://www.unsw.edu.au" target="_blank">UNSW</a> Sydney, including:</p>
                <ul>
                    <li>Modern synthetic chemistry laboratories</li>
                    <li>High-throughput screening facilities</li>
                    <li><a href="https://www.unsw.edu.au/research/facilities-and-infrastructure/mwac" target="_blank">Mark Wainwright Analytical Centre (MWAC)</a></li>
                    <li>Advance modelling computational resources for drug design</li>
                    <li>High-performing computers: <a href="https://nci.org.au" target="_blank">National Computational Infrastructure (Gadi)</a> and <a href="https://docs.restech.unsw.edu.au/using_katana/about_katana/" target="_blank">UNSW Katana</a></li>
                </ul>
            </div>
        </div>
    </div>
</section>

<style>
.about-content {
    max-width: 800px;
    margin: 0 auto;
}

.about-image {
    text-align: center;
    margin: 4rem 0 2rem 0;
}

.about-slideshow-container {
    position: relative;
    max-width: 100%;
    margin: 0 auto;
}

.about-slideshow-wrapper {
    position: relative;
    overflow: hidden;
}

.about-slide {
    display: none;
}

.about-slide img {
    width: 100%;
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    display: block;
    margin: 0 auto;
}

.about-slideshow-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(109, 95, 217, 0.8);
    color: white;
    border: none;
    padding: 0.75rem 1rem;
    cursor: pointer;
    font-size: 1.25rem;
    border-radius: 4px;
    transition: background 0.3s;
}

.about-slideshow-btn:hover {
    background: rgba(109, 95, 217, 1);
}

.about-slideshow-btn.prev {
    left: 0.5rem;
}

.about-slideshow-btn.next {
    right: 0.5rem;
}

.about-slideshow-dots {
    text-align: center;
    margin-top: 1rem;
}

.about-dot {
    display: inline-block;
    width: 10px;
    height: 10px;
    margin: 0 4px;
    background: #ccc;
    border-radius: 50%;
    cursor: pointer;
    transition: background 0.3s;
}

.about-dot:hover,
.about-dot.active {
    background: #6d5fd9;
}

.about-text {
    line-height: 1.8;
}

.about-text h3 {
    color: #2c3e50;
    margin: 2rem 0 1rem;
}

.about-text ul {
    list-style-type: disc;
    margin-left: 1.5rem;
    margin-bottom: 1.5rem;
}

.about-text li {
    margin-bottom: 0.5rem;
}

.research-areas {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.9rem;
    margin: 1.9rem 0;
    justify-content: start;
}

.research-area {
    background: #f8f9fa;
    padding: 1.5rem;
    border-radius: 8px;
}

.research-area h4 {
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

@media (max-width: 768px) {
    .research-areas {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 480px) {
    .research-areas {
        grid-template-columns: 1fr;
    }
}
</style>

<script>
(function() {
    let aboutSlideIndex = 1;
    const aboutSlides = document.getElementsByClassName("about-slide");
    const aboutDots = document.getElementsByClassName("about-dot");

    function aboutShowSlides(n) {
        if (aboutSlides.length === 0) return;
        if (n > aboutSlides.length) aboutSlideIndex = 1;
        if (n < 1) aboutSlideIndex = aboutSlides.length;
        for (let i = 0; i < aboutSlides.length; i++) {
            aboutSlides[i].style.display = "none";
        }
        for (let i = 0; i < aboutDots.length; i++) {
            aboutDots[i].className = aboutDots[i].className.replace(" active", "");
        }
        aboutSlides[aboutSlideIndex - 1].style.display = "block";
        if (aboutDots[aboutSlideIndex - 1]) {
            aboutDots[aboutSlideIndex - 1].className += " active";
        }
    }

    window.aboutChangeSlide = function(n) {
        aboutShowSlides(aboutSlideIndex += n);
    };

    window.aboutCurrentSlide = function(n) {
        aboutShowSlides(aboutSlideIndex = n);
    };

    aboutShowSlides(aboutSlideIndex);
    setInterval(function() {
        aboutChangeSlide(1);
    }, 5000);
})();
</script>
