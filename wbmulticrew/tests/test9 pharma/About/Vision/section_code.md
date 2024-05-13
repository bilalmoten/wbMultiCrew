## Vision Section
### HTML
```html
<section class="vision-section">
  <header>
    <div class="container">
      <nav class="navbar navbar-expand-md">
        <a class="navbar-brand" href="#">BKF Pharma</a>
      </nav>
    </div>
  </header>
  <div class="container">
    <div class="vision-content text-center">
      <h2>Empowering a Cancer-Free Future</h2>
      <p>At BKF Pharma, we envision a world where cancer is a manageable disease, and patients can live their lives to the fullest.</p>
      <p>Our mission is to accelerate the development of innovative treatments that transform the lives of those affected by cancer.</p>
      <h4>Our Purpose</h4>
      <p>We believe that cancer treatment should be personalized, effective, and accessible to all.</p>
      <h4>Our Values</h4>
      <ul>
        <li><strong>Innovation</strong>: We strive to innovate and improve cancer treatment options through cutting-edge research and technology.</li>
        <li><strong>Collaboration</strong>: We believe that together, we can achieve more. We partner with experts from around the world to accelerate progress in cancer research.</li>
        <li><strong>Patient-Centricity</strong>: We put the needs of patients and their families at the heart of everything we do.</li>
        <li><strong>Integrity</strong>: We uphold the highest standards of integrity, transparency, and ethics in our research and business practices.</li>
      </ul>
      <h4>Our Vision</h4>
      <p>We envision a future where cancer is no longer a death sentence. Where patients can receive effective, personalized treatments that improve their quality of life.</p>
      <button class="btn btn-primary">Learn More</button>
    </div>
    <div class="vision-image">
      <img src="images/generated_image_A_high-quality_image_of_a.jpg" alt="Futuristic Cityscape">
    </div>
  </div>
</section>
```

### CSS
```css
.vision-section {
  background-color: #fff;
  padding: 50px 0;
}

.vision-content {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

.vision-content h2 {
  font-size: 36px;
  margin-bottom: 20px;
}

.vision-content p {
  margin-bottom: 20px;
}

.vision-content h4 {
  margin-bottom: 10px;
}

.vision-content ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.vision-content ul li {
  margin-bottom: 10px;
}

.vision-content ul li strong {
  font-weight: bold;
}

.vision-content .btn {
  background-color: #03A9F4;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.vision-content .btn:hover {
  background-color: #333333;
  font-size: 26px;
}

.vision-image {
  text-align: center;
}

.vision-image img {
  max-width: 100%;
  height: 300px;
  object-fit: cover;
  border-radius: 5px;
}
```

### JS
```javascript
$(document).ready(function() {
  $(".btn").hover(function() {
    $(this).css("font-size", "26px");
    $(this).css("background-color", "#333333");
  }, function() {
    $(this).css("font-size", "24px");
    $(this).css("background-color", "#03A9F4");
  });
  
  $(".btn").click(function() {
    $(this).css("font-size", "28px");
    $(this).css("background-color", "#03A9F4");
  });
});
```

(Note: The above code uses Bootstrap CSS framework and jQuery library)