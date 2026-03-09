---
layout: post
title: "Congratulations to Yao Cheng on the Completion of His PhD"
date: 2025-10-10 10:00:00 +1000
categories: news achievements
---

<div class="post-content">
    <h3>Congratulations, Dr. Yao Cheng </h3>
    
    <p>We are delighted to congratulate <strong>Yao Cheng</strong> on the successful completion of his PhD! Well done, Yao</p>

    <p>Yao's dedication, hard work, and contributions to the Kumar Group have been outstanding. His research has made significant advances in medicinal chemistry and organic synthesis.</p>

    <p>On Friday, October 10th, the group gathered for a farewell dinner to celebrate Yao's achievements and congratulate him on his new job. It was a wonderful evening filled with great food, laughter, and fond memories of Yao's time with us.</p>

    <p>We wish Yao all the best in his new position and future endeavors. His contributions to the group will be remembered, and we look forward to following his continued success!</p>

    <div class="slideshow-container">
        <div class="slideshow-wrapper">
            <div class="slide fade">
                <img src="{{ site.baseurl }}/assets/images/yaogroupdinner/225a5713-4ce0-435d-815a-5cb91aa4443d.JPG" alt="Yao Farewell Dinner">
            </div>
            <div class="slide fade">
                <img src="{{ site.baseurl }}/assets/images/yaogroupdinner/3988492b-577f-4752-8ce8-5f7763975da1.JPG" alt="Yao Farewell Dinner">
            </div>
            <div class="slide fade">
                <img src="{{ site.baseurl }}/assets/images/yaogroupdinner/921f4a39-ad25-4da7-8007-037b3a7a4be8.JPG" alt="Yao Farewell Dinner">
            </div>
            <div class="slide fade">
                <img src="{{ site.baseurl }}/assets/images/yaogroupdinner/b0e4d2d0-cd87-42ca-82ec-2c7e18abaeb4.JPG" alt="Yao Farewell Dinner">
            </div>
        </div>
        
        <button class="slideshow-btn prev" onclick="changeSlide(-1)">&#10094;</button>
        <button class="slideshow-btn next" onclick="changeSlide(1)">&#10095;</button>
        
        <div class="slideshow-dots">
            <span class="dot active" onclick="currentSlide(1)"></span>
            <span class="dot" onclick="currentSlide(2)"></span>
            <span class="dot" onclick="currentSlide(3)"></span>
            <span class="dot" onclick="currentSlide(4)"></span>
        </div>
    </div>

    <p style="text-align: center; margin-top: 2rem;"><strong>Congratulations again, Yao! We are proud of your accomplishments and wish you all the best!</strong></p>
</div>

<style>
.post-content {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 1rem;
}

.post-content h3 {
    text-align: center;
    color: #2c3e50;
    margin-bottom: 1.5rem;
    font-size: 1.8rem;
}

.post-content p {
    margin-bottom: 1.5rem;
    line-height: 1.6;
    text-align: justify;
}

/* Slideshow styles */
.slideshow-container {
    position: relative;
    max-width: 800px;
    margin: 2rem auto;
    background: #f9f9f9;
    border-radius: 12px;
    padding: 1rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.slideshow-wrapper {
    position: relative;
    width: 100%;
    overflow: hidden;
    border-radius: 8px;
}

.slide {
    display: none;
    width: 100%;
}

.slide img {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 8px;
}

.slideshow-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(102, 126, 234, 0.8);
    color: white;
    border: none;
    padding: 1rem 1.2rem;
    font-size: 1.5rem;
    cursor: pointer;
    border-radius: 50%;
    transition: all 0.3s;
    z-index: 10;
}

.slideshow-btn:hover {
    background: linear-gradient(135deg, #5b4fc9 0%, #667eea 35%, #7c6ee8 65%, #764ba2 100%);
}

.slideshow-btn.prev {
    left: 1rem;
}

.slideshow-btn.next {
    right: 1rem;
}

.slideshow-dots {
    text-align: center;
    padding: 1rem 0;
}

.dot {
    cursor: pointer;
    height: 12px;
    width: 12px;
    margin: 0 5px;
    background-color: #bbb;
    border-radius: 50%;
    display: inline-block;
    transition: background-color 0.3s;
}

.dot.active,
.dot:hover {
    background-color: #667eea;
}

@media (max-width: 768px) {
    .slideshow-container {
        padding: 0.5rem;
    }
    
    .slideshow-btn {
        padding: 0.8rem 1rem;
        font-size: 1.2rem;
    }
    
    .slideshow-btn.prev {
        left: 0.5rem;
    }
    
    .slideshow-btn.next {
        right: 0.5rem;
    }
}

h1.post-title, .post-title, h1 {
    text-align: center !important;
}
</style>

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
    }
    
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
}

// Auto-advance slides every 5 seconds
setInterval(function() {
    changeSlide(1);
}, 5000);
</script>

