## Contact Information Section
### HTML

```html
<section id="cta-section" class="container text-center my-5">
    <div class="row align-items-center">
        <div class="col-lg-6">
            <h1 class="cta-headline">Join Us in Revolutionizing Cancer Treatment</h1>
            <p class="cta-subheadline">
                At BKF Pharma, we're pioneering innovative solutions to combat cancer. Discover how you can be a part of this groundbreaking journey.
            </p>
            <a href="/about-us" class="btn btn-primary btn-cta">Learn More</a>
        </div>
        <div class="col-lg-6">
            <img src="path/to/futuristic-lab-image.jpg" alt="Scientist in modern lab" class="img-fluid cta-image">
        </div>
    </div>
</section>
```

### CSS

```css
#cta-section {
    background-color: #ffffff;
    padding: 3rem;
}

.cta-headline {
    color: #1E3A8A;
    font-family: 'Roboto', sans-serif;
    font-weight: bold;
    font-size: 2.5em;
}

.cta-subheadline {
    color: #6B7280;
    font-family: 'Open Sans', sans-serif;
    font-size: 1.25em;
    margin-top: 1rem;
    margin-bottom: 2rem;
}

.btn-cta {
    background-color: #3B82F6;
    color: #ffffff;
    font-family: 'Roboto', sans-serif;
    font-weight: medium;
    font-size: 1em;
    padding: 15px 30px;
    border-radius: 4px;
    transition: background-color 0.3s;
}

.btn-cta:hover {
    background-color: #1E3A8A;
}

.cta-image {
    max-width: 100%;
    border: solid 4px #E0F2FE;
    transition: transform 0.3s;
}

/* Scroll Animation */
@keyframes fadeIn {
  0% { 
    opacity: 0; 
    transform: translateY(20px);
  }
  100% { 
    opacity: 1; 
    transform: translateY(0);
  }
}

.cta-headline, .cta-subheadline, .btn-cta {
    animation: fadeIn ease 0.5s;
    animation-fill-mode: forwards;
    opacity: 0;
}

.cta-image {
    animation: fadeIn ease 0.8s;
    animation-fill-mode: forwards;
    opacity: 0;
}

/* Scroll Trigger */
.cta-headline.scroll-trigger, .cta-subheadline.scroll-trigger, .btn-cta.scroll-trigger, .cta-image.scroll-trigger {
    opacity: 1;
}

.cta-image.scroll-zoom {
    transform: scale(1.05);
}
```

### JS

```javascript
$(document).ready(function() {
    $(window).on("scroll", function() {
        $(".cta-headline, .cta-subheadline, .btn-cta, .cta-image").each(function() {
            var offsetTop = $(this).offset().top;
            var scrollTop = $(window).scrollTop();
            if (scrollTop > (offsetTop - window.innerHeight + 100)) {
                $(this).addClass("scroll-trigger");
            }
        });

        $(".cta-image").hover(function(){
            $(this).toggleClass("scroll-zoom");
        });
    });
});
```