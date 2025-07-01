---
layout: default
title: Contact
---

<section class="section">
    <div class="container">
        <div class="section-title">
            <h2>Contact Us</h2>
        </div>

        <div class="contact-content">
            <div class="contact-grid">
                <!-- Contact Information -->
                <div class="contact-info">
                    <h3>Get in Touch</h3>
                    <div class="info-item">
                        <i class="fas fa-map-marker-alt"></i>
                        <div>
                            <h4>Address</h4>
                            <p>Dalton Building, F12 University Mall</p>
                            <p>Kensington NSW 2033</p>
                            <p>Australia</p>
                        </div>
                    </div>
                    <div class="info-item">
                        <i class="fas fa-envelope"></i>
                        <div>
                            <h4>Email</h4>
                            <p><a href="mailto:n.kumar@unsw.edu.au">n.kumar@unsw.edu.au</a></p>
                        </div>
                    </div>
                    <div class="info-item">
                        <i class="fas fa-phone"></i>
                        <div>
                            <h4>Phone</h4>
                            <p> 938 546 98</p>
                        </div>
                    </div>
                    <div class="social-links">
                        <h4>Follow Us</h4>
                        <div class="links">
                            <a href="https://www.researchgate.net/profile/Naresh-Kumar-100" target="_blank"><i class="fab fa-researchgate"></i></a>
                            <a href="https://www.linkedin.com/in/naresh-kumar-70054728/?originalSubdomain=au" target="_blank"><i class="fab fa-linkedin"></i></a>
                            <a href="#" target="_blank"><i class="fab fa-twitter"></i></a>
                        </div>
                    </div>
                </div>

                <!-- Contact Form -->
                <div class="contact-form">
                    <h3>Send us a Message</h3>
                    <form id="contactForm" action="https://formspree.io/f/mdkzpzln" method="POST">
                        <div class="form-group">
                            <label for="name">Name</label>
                            <input type="text" id="name" name="name" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Email</label>
                            <input type="email" id="email" name="email" required>
                        </div>
                        <div class="form-group">
                            <label for="subject">Subject</label>
                            <input type="text" id="subject" name="subject" required>
                        </div>
                        <div class="form-group">
                            <label for="message">Message</label>
                            <textarea id="message" name="message" rows="5" required></textarea>
                        </div>
                        <button type="submit" class="btn">Send Message</button>
                    </form>
                </div>
            </div>

            <!-- Map -->
            <div class="map-section">
                <h3>Location</h3>
                <div class="map-container">
                    <iframe 
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3312.8278533985427!2d151.2273!3d-33.9173!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b12b18b76f1d05d%3A0x253250491d5c4621!2sSchool+of+Chemistry!5e0!3m2!1sen!2sau!4v1718770000000!5m2!1sen!2sau" 
                        width="100%" 
                        height="450" 
                        style="border:0;" 
                        allowfullscreen="" 
                        loading="lazy">
                    </iframe>
                </div>
            </div>
        </div>
    </div>
</section>

<style>
.contact-content {
    max-width: 1200px;
    margin: 0 auto;
}

.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    margin-bottom: 4rem;
}

.contact-info {
    background: #f8f9fa;
    padding: 2rem;
    border-radius: 8px;
}

.contact-info h3 {
    color: #2c3e50;
    margin-bottom: 2rem;
    font-size: 1.8rem;
}

.info-item {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
}

.info-item i {
    color: #2c3e50;
    font-size: 1.5rem;
    margin-top: 0.3rem;
}

.info-item h4 {
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.info-item p {
    color: #666;
    margin-bottom: 0.3rem;
}

.info-item a {
    color: #3498db;
    text-decoration: none;
}

.info-item a:hover {
    text-decoration: underline;
}

.social-links {
    margin-top: 2rem;
}

.social-links h4 {
    color: #2c3e50;
    margin-bottom: 1rem;
}

.social-links .links {
    display: flex;
    gap: 1rem;
}

.social-links a {
    color: #2c3e50;
    font-size: 1.5rem;
    transition: color 0.3s;
}

.social-links a:hover {
    color: #3498db;
}

.contact-form {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.contact-form h3 {
    color: #2c3e50;
    margin-bottom: 2rem;
    font-size: 1.8rem;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 0.8rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
}

.form-group textarea {
    resize: vertical;
}

.map-section {
    margin-top: 4rem;
}

.map-section h3 {
    color: #2c3e50;
    margin-bottom: 2rem;
    font-size: 1.8rem;
}

.map-container {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

@media (max-width: 768px) {
    .contact-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    
    // Formspree will handle the form submission automatically
    // You can add custom success/error handling here if needed
    
    contactForm.addEventListener('submit', function(e) {
        // Let Formspree handle the submission
        // The form will be submitted to Formspree which will send emails to your specified addresses
    });
});
</script> 