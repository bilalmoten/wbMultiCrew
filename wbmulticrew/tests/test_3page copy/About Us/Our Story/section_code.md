## Our Story Section
### HTML

```html
<section class="our-story py-5 text-center text-md-left">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-md-6 order-2 order-md-1">
                <h1 class="display-4 font-weight-bold text-dark-blue">Join Us in the Fight Against Cancer</h1>
                <p class="lead text-dark-blue">Discover how BKF Pharma is pioneering innovative treatments to save lives.</p>
                <a href="#" class="btn btn-primary btn-lg mt-4">Learn More <i class="fas fa-arrow-right ml-2"></i></a>
            </div>
            <div class="col-md-6 order-1 order-md-2">
                <img src="images/generated_image_An_abstract,_futuristic_background_with.jpg" class="img-fluid" alt="Abstract futuristic background with technological elements">
            </div>
        </div>
    </div>
</section>
```

### CSS

```css
.our-story {
    background-color: #E0F2FE;
}

.text-dark-blue {
    color: #1E3A8A;
}

/* Headline/Title */
.our-story .display-4 {
    font-family: 'Roboto', sans-serif;
    font-size: 2em;
}

.our-story .lead {
    font-family: 'Open Sans', sans-serif;
    font-size: 1.2em;
}

/* Button Style */
.our-story .btn-primary {
    background-color: #3B82F6;
    color: #FFFFFF;
    border-radius: 4px;
    padding: 10px 20px;
    font-family: 'Roboto', sans-serif;
    font-weight: bold;
    font-size: 1em;
}

.our-story .btn-primary:hover {
    background-color: #1E3A8A;
}


/* Image Style */
.our-story img {
    max-width: 100%;
    height: auto;
    margin-top: 20px;
    transition: transform 0.3s ease;
}

.our-story img:hover {
    transform: scale(1.05);
}
```

### JS (if needed)

```javascript
// No additional JS needed for this section
```