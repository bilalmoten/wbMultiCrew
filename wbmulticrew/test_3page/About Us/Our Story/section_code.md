## Our Story Section
### HTML

```html
<section id="our-story" class="d-flex align-items-center bg-light-blue py-5">
  <div class="container">
    <div class="row">
      <div class="col-lg-6 col-md-12 text-center text-lg-left">
        <h1 class="headline">Join Us in the Fight Against Cancer</h1>
        <p class="tagline">Discover how BKF Pharma is pioneering innovative treatments to save lives.</p>
        <a href="#" class="btn btn-primary cta-button">Learn More</a>
      </div>
      <div class="col-lg-6 col-md-12 text-center">
        <img src="images/generated_image_An_abstract,_futuristic_background_with.jpg" 
             alt="Futuristic background with technological elements" class="img-fluid cta-image">
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
.bg-light-blue {
  background-color: #E0F2FE;
}

.headline {
  color: #1E3A8A;
  font-family: 'Roboto', sans-serif;
  font-size: 2em;
  font-weight: bold;
}

.tagline {
  color: #1E3A8A;
  font-family: 'Open Sans', sans-serif;
  font-size: 1.2em;
  margin-bottom: 1em;
}

.cta-button {
  background-color: #3B82F6;
  color: #FFFFFF;
  border-radius: 4px;
  padding: 10px 20px;
  font-family: 'Roboto', sans-serif;
  font-weight: bold;
  font-size: 1em;
  text-decoration: none;
}

.cta-button:hover {
  background-color: #215495;
}

.section-image:hover {
  transform: scale(1.05);
  transition: 0.3s;
}

.container, .row, .col-lg-6, .col-md-12 {
  position: relative;
  zglFilter: alpha(opacity=0);
}

@media (max-width: 565px) {
  .headline {
    font-size: 1.75em;
  }

  .background {
    text-align: center
  }
}
```
