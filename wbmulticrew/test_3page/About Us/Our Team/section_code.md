## Our Team Section
### HTML

```html
<section class="cta-section bg-white text-center py-5">
    <div class="container">
        <div class="row mb-4">
            <div class="col">
                <h2 class="cta-headline font-weight-bold text-dark-blue">Join Us in the Fight Against Cancer</h2>
                <p class="cta-subheader text-gray">Discover how BKF Pharma is pioneering innovative cancer treatments and making a difference.</p>
            </div>
        </div>
        <div class="row mb-4">
            <div class="col">
                <a href="#" class="btn cta-button text-white font-weight-semi-bold">Learn More <span class="cta-icon">&#9654;</span></a>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <img src="images/generated_image_A_high-quality,_professional_image_of.jpg" class="cta-image img-fluid" alt="Scientist in lab">
            </div>
        </div>
    </div>
</section>
```

### CSS
```css
.bg-white {
    background-color: #FFFFFF;
}

.text-center {
    text-align: center;
}

.py-5 {
    padding-top: 3rem;
    padding-bottom: 3rem;
}

.mb-4 {
    margin-bottom: 1.5rem;
}

.font-weight-bold {
    font-weight: bold;
}

.font-weight-semi-bold {
    font-weight: 600;
}

.text-dark-blue {
    color: #1E3A8A;
}

.text-gray {
    color: #6B7280;
}

.cta-button {
    background-color: #3B82F6;
    border-radius: 4px;
    padding: 10px 20px;
    text-transform: uppercase;
    display: inline-flex;
    align-items: center;
}

.cta-button:hover {
    background-color: #1E3A8A;
}

.cta-button .cta-icon {
    margin-left: 0.5rem;
    color: #FFFFFF;
    font-size: 1rem;
}

.cta-subheader {
    font-size: 1.25rem;
}

.cta-headline {
    font-size: 2rem;
}

.cta-image {
    border: 1px solid #D1D5DB;
    padding: 5px;
}

.img-fluid {
    max-width: 100%;
    height: auto;
}
```

### JS (if needed)
```javascript
$(document).ready(function(){
    $(window).scroll(function() {
        var hT = $('.cta-section').offset().top,
            hH = $('.cta-section').outerHeight(),
            wH = $(window).height(),
            wS = $(this).scrollTop();
        if (wS > (hT+hH-wH)){
            $('.cta-section .container').css('opacity', '1').fadeIn(1000);
        }
    });
});

$('.cta-section .container').css('opacity', '0.3').animate({ opacity: 1 }, 2000);
```
