## Call-to-Action Section
### HTML

```html
<section id="cta-section" class="text-center d-flex align-items-center" style="background-color: #F2F2F2;">
  <div class="container py-5 px-4">
    <div class="row">
      <div class="col-lg-6">
        <h1 class="cta-headline" style="color: #003366;">Join Us in the Fight Against Cancer</h1>
        <p class="cta-subheadline" style="color: #333333;">Discover how our innovative research is changing lives. Be a part of our journey.</p>
        <p class="cta-supporting-text" style="color: #333333;">BKF Pharma is at the forefront of cancer research, developing groundbreaking treatments that offer hope to millions. Your support and partnership can help us make a difference.</p>
        
        <div class="cta-buttons">
          <a href="[Insert URL to relevant page]" class="btn btn-primary me-2" style="background-color: #00FF00; color: #FFFFFF;">Learn More</a>
          <a href="[Insert URL to contact page]" class="btn btn-secondary" style="background-color: #008080; color: #FFFFFF;">Contact Us</a>
        </div>
      </div>
      <div class="col-lg-6 d-flex justify-content-center">
        <img src="https://via.placeholder.com/500x400" alt="Abstract illustration" class="cta-image img-fluid ms-4">
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
#cta-section .cta-headline {
  font-family: 'Helvetica Neue', Bold;
  font-size: 36px;
}

#cta-section .cta-subheadline {
  font-family: 'Helvetica Neue', Regular;
  font-size: 24px;
  margin-top: 15px;
}

#cta-section .cta-supporting-text {
  font-family: 'Helvetica Neue', Light;
  font-size: 18px;
  margin: 20px 0;
}

.cta-buttons .btn-primary {
  background-color: #00FF00;
  color: #FFFFFF;
  border: none;
  border-radius: 5px;
  padding: 15px 30px;
  transition: background-color 0.3s;
}

.cta-buttons .btn-primary:hover {
  background-color: darken(#00FF00, 10%);
}

.cta-buttons .btn-secondary {
  background-color: #008080;
  color: #FFFFFF;
  border: none;
  border-radius: 5px;
  padding: 15px 30px;
  transition: background-color 0.3s;
}

.cta-buttons .btn-secondary:hover {
  background-color: darken(#008080, 10%);
}

.cta-image {
  max-width: 100%;
  height: auto;
}

.cta-buttons a {
  margin-right: 20px;
}
```

### JS

```javascript
$(document).ready(function() {
  $("a").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
        window.location.hash = hash;
      });
    }
  });
});
```
