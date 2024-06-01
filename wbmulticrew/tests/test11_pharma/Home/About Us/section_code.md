## About Us
### HTML

```html
<section class="about-us" id="about-us">
    <div class="hero-bg" style="background-image: url('images/generated_image_A_futuristic,_abstract_visual_that.jpg');">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 text-center">
                    <h2>Mission Statement</h2>
                    <p At BKF Pharma, we are driven by a shared passion to revolutionize cancer treatment. Our mission is to harness the power of innovation to develop cutting-edge solutions that transform lives. We believe that every individual deserves access to effective, personalized care, and we're committed to making that a reality.</p>
                    <a class="btn btn-learn-more" href="#">Learn More</a>
                </div>
            </div>
        </div>
    </div>
    <div class="history-section">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <h2>Company History</h2>
                    <p>BKF Pharma was founded on the principles of innovation, collaboration, and a relentless pursuit of excellence. Since our inception, we've been dedicated to pushing the boundaries of cancer treatment, driven by a passion to improve patient outcomes.</p>
                    <ul>
                        <li>2015: BKF Pharma is founded by a team of visionary scientists and entrepreneurs</li>
                        <li>2018: We establish our state-of-the-art research facility, marking a significant milestone in our journey</li>
                        <li>2020: Our team expands to include renowned experts in oncology, bioinformatics, and data science</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    <div class="team-profiles-section">
        <div class="container">
            <div class="row">
                <div class="col-lg-6">
                    <div class="team-profile">
                        <img src="images/team_profile_image_1.jpg" alt="Dr. Maria Rodriguez">
                        <h3>Dr. Maria Rodriguez, CEO</h3>
                        <p>Dr. Rodriguez is a renowned oncologist with a passion for innovation. With over a decade of experience in cancer research, she brings a unique perspective to our mission.</p>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="team-profile">
                        <img src="images/team_profile_image_2.jpg" alt="Dr. John Lee">
                        <h3>Dr. John Lee, Chief Scientific Officer</h3>
                        <p>Dr. Lee is a pioneer in the field of bioinformatics. His groundbreaking research has led to significant breakthroughs in cancer treatment, and we're honored to have him on our team.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
```

### CSS
```css
.about-us {
    font-family: 'Open Sans', sans-serif;
}

.hero-bg {
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    align-items: center;
    padding: 20px;
}

.hero-bg h2 {
    font-size: 36px;
    font-weight: bold;
    color: #4567b7;
}

.hero-bg p {
    font-size: 18px;
    line-height: 1.5;
    color: #666;
}

.hero-bg .btn-learn-more {
    background-color: #34c759;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

.hero-bg .btn-learn-more:hover {
    background-color: #2f9445;
}

.history-section {
    padding: 40px 0;
}

.history-section h2 {
    font-size: 24px;
    font-weight: bold;
    color: #4567b7;
}

.history-section p {
    font-size: 18px;
    line-height: 1.5;
    color: #666;
}

.history-section ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.history-section li {
    margin-bottom: 20px;
}

.team-profiles-section {
    padding: 40px 0;
}

.team-profile {
    margin-bottom: 40px;
}

.team-profile img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 10px;
    margin-bottom: 10px;
}

.team-profile h3 {
    font-size: 24px;
    font-weight: bold;
    color: #4567b7;
    margin-bottom: 10px;
}

.team-profile p {
    font-size: 18px;
    line-height: 1.5;
    color: #666;
}
```

### JS
```javascript
$('a.btn-learn-more').hover(function() {
    $(this).css('background-color', '#2f9445');
}, function() {
    $(this).css('background-color', '#34c759');
});

$('a.btn-learn-more').on('click', function(e) {
    e.preventDefault();
    // Add smooth scroll effect here
});
```