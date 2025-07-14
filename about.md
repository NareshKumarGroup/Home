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
                <p>The Naresh Kumar Research Group at <a href="https://www.unsw.edu.au" target="_blank">UNSW</a> Sydney is dedicated to advancing the field of medicinal chemistry through innovative research and collaboration. Our work focuses on developing novel therapeutic agents for various diseases, with a particular emphasis on infectious disease and cancer.</p>

                <div class="about-image">
                    <img src="{{ site.baseurl }}/assets/images/dec2024part.jpg" alt="December 2024 Party" class="about-hero-image">
                </div>
                
                <h3>Our Mission</h3>
                <p>We aim to:</p>
                <ul>
                    <li>Design and synthesize novel drug candidates with improved efficacy and reduced side effects</li>
                    <li>Understand the molecular mechanisms of disease and drug action</li>
                    <li>Develop new methodologies for drug discovery and development</li>
                    <li>Machine learning, deep learning, and artificial intelligence in drug discovery</li>
                    <li>Train the next generation of medicinal chemists and drug discovery scientists</li>
                    
                </ul>

                <h3>Research Areas</h3>
                <div class="research-areas">
                    <div class="research-area">
                        <h4>Medicinal Chemistry</h4>
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

.about-hero-image {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    display: block;
    margin: 0 auto;
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