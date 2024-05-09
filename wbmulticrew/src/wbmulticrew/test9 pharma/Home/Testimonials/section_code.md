## Testimonials
### HTML
```html
<section id="testimonials" class="py-5">
  <div class="container">
    <h2 class="section-header">Testimonials</h2>
    <p class="subheading">Hear from those who have been impacted by our work</p>
    <div class="row">
      <div class="col-md-4">
        <div class="testimonial">
          <blockquote>
            <p>"BKF Pharma's innovative approach to cancer treatment has given me hope for a brighter future. Their dedication to finding a cure is truly inspiring."</p>
            <cite>Sarah, Cancer Survivor</cite>
          </blockquote>
        </div>
      </div>
      <div class="col-md-4">
        <div class="testimonial">
          <blockquote>
            <p>"As a researcher, I'm thrilled to be part of the BKF Pharma team. Their commitment to collaboration and innovation is a game-changer in the fight against cancer."</p>
            <cite>Dr. John Smith, Researcher</cite>
          </blockquote>
        </div>
      </div>
      <div class="col-md-4">
        <div class="testimonial">
          <blockquote>
            <p>"BKF Pharma's passion for improving cancer treatment has inspired me to take action. Their work is a beacon of hope for those affected by cancer."</p>
            <cite>Emily, Cancer Patient Advocate</cite>
          </blockquote>
        </div>
      </div>
    </div>
    <div class="call-to-action">
      <button class="btn btn-primary">Join the Movement</button>
      <p>Learn More About Our Mission and Values</p>
    </div>
    <div class="social-media">
      <ul>
        <li><a href="#" class="facebook"><i class="fa fa-facebook"></i></a></li>
        <li><a href="#" class="twitter"><i class="fa fa-twitter"></i></a></li>
        <li><a href="#" class="linkedin"><i class="fa fa-linkedin"></i></a></li>
      </ul>
    </div>
  </div>
</section>
```

### CSS
```css
#testimonials {
  background-color: #f9f9f9;
  padding: 50px 0;
}

.section-header {
  font-weight: bold;
  color: #03A9F4;
  font-size: 24px;
  margin-bottom: 10px;
}

.subheading {
  color: #333333;
  font-size: 18px;
  margin-bottom: 30px;
}

.testimonial {
  border: 1px solid #ddd;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.testimonial blockquote {
  font-size: 18px;
  font-style: italic;
  margin: 0 0 20px;
}

.testimonial cite {
  font-size: 16px;
  color: #333333;
  font-weight: bold;
}

.call-to-action {
  text-align: center;
  margin-top: 30px;
}

.call-to-action button {
  background-color: #03A9F4;
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 18px;
  cursor: pointer;
}

.call-to-action button:hover {
  background-color: #0288d1;
}

.social-media {
  text-align: center;
  margin-top: 30px;
}

.social-media ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.social-media li {
  display: inline-block;
  margin: 0 10px;
}

.social-media a {
  color: #333333;
  font-size: 24px;
}

.social-media a:hover {
  color: #03A9F4;
}
```

### JS (not needed in this case)