## Values Section
### HTML
```html
<section class="values-section">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <img src="images/generated_image_A_high-quality_image_that_represents.jpg" class="img-fluid hero-image" alt="Hero Image">
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <h1>Values</h1>
                <h2>Our Mission</h2>
                <p>At BKF Pharma, we are driven by a shared vision to revolutionize cancer treatment and improve the lives of those affected by this devastating disease. Our mission is to harness the power of innovation and collaboration to develop groundbreaking treatments that make a meaningful difference.</p>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <h2>Our Values</h2>
                <ul>
                    <li>
                        <i class="fas fa-lightbulb"></i>
                        <span>Innovation: We believe that innovation is the key to unlocking new treatments and improving patient outcomes. We are committed to staying at the forefront of scientific discovery and technological advancements.</span>
                    </li>
                    <li>
                        <i class="fas fa-handshake"></i>
                        <span>Collaboration: We recognize that cancer is a complex and multifaceted disease that requires a collaborative approach. We work closely with researchers, scientists, and healthcare professionals to accelerate the development of new treatments.</span>
                    </li>
                    <li>
                        <i class="fas fa-user"></i>
                        <span>Patient-Centricity: We are committed to putting the needs of patients and their families at the heart of everything we do. We strive to understand their experiences, challenges, and hopes, and to develop treatments that meet their unique needs.</span>
                    </li>
                    <li>
                        <i class="fas fa-shield-alt"></i>
                        <span>Integrity: We are committed to the highest standards of integrity, transparency, and accountability in all our actions. We believe that trust is earned through consistent behavior and a commitment to doing what is right.</span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <h2>Our Approach</h2>
                <p>At BKF Pharma, we take a patient-centric approach to cancer treatment. We believe that every patient deserves access to innovative, effective, and compassionate care. We are committed to:</p>
                <ul>
                    <li>
                        <i class="fas fa-flask"></i>
                        <span>Advancing Research: We are dedicated to advancing the science of cancer treatment through cutting-edge research and collaboration with leading experts in the field.</span>
                    </li>
                    <li>
                        <i class="fas fa-capsule"></i>
                        <span>Developing New Treatments: We are committed to developing new treatments that are safe, effective, and accessible to patients worldwide.</span>
                    </li>
                    <li>
                        <i class="fas fa-heartbeat"></i>
                        <span>Improving Patient Outcomes: We strive to improve patient outcomes by providing personalized care, reducing side effects, and enhancing quality of life.</span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <h2>Join Us</h2>
                <p>We believe that together, we can make a difference in the fight against cancer. If you share our passion for innovation, collaboration, and patient-centricity, we invite you to join us on this journey. Together, let's revolutionize cancer treatment and improve the lives of those affected by this devastating disease.</p>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <h2>Get in Touch</h2>
                <p>If you would like to learn more about our mission, values, and approach to cancer treatment, or if you would like to collaborate with us, please don't hesitate to get in touch. We would be delighted to hear from you.</p>
            </div>
        </div>
    </div>
</section>
```
### CSS
```css
.values-section {
    background: #87CEEB; /* soft blue */
    padding: 40px 0;
}

.hero-image {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.values-section h1 {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 20px;
}

.values-section h2 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}

 ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

li {
    margin-bottom: 20px;
    padding: 10px;
    border-bottom: 1px solid #ccc;
}

li:last-child {
    border-bottom: none;
}

i {
    font-size: 24px;
    margin-right: 10px;
    color: #2F4F7F; /* deep blue */
}

 FA icons from fontawesome
```
### JS
```javascript
// Add animation effect on hover
$('li').hover(function() {
    $(this).css('background-color', '#f2f2f2');
    $(this).css('cursor', 'pointer');
}, function() {
    $(this).css('background-color', 'transparent');
    $(this).css('cursor', 'default');
});

// Add animation effect on icons
$('i').hover(function() {
    $(this).css('color', '#87CEEB'); /* soft blue */
}, function() {
    $(this).css('color', '#2F4F7F'); /* deep blue */
});
```