## Our Team
### HTML

```html
<section id="cta" class="text-center py-5">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <h1 class="cta-headline">Join Us in the Fight Against Cancer</h1>
                <p class="cta-subheader">Discover how BKF Pharma is pioneering innovative cancer treatments and making a difference.</p>
                <button class="btn btn-cta">
                    Learn More
                    <span class="cta-icon">&rarr;</span>
                </button>
            </div>
        </div>
        <div class="row justify-content-center mt-5">
            <div class="col-md-8">
                <img src="images/generated_image_A_high-quality,_professional_image_of.jpg" alt="Scientist in a laboratory" class="img-fluid cta-image">
            </div>
        </div>
    </div>
</section>
```

### CSS

```css
#cta {
    background-color: #FFFFFF;
    padding: 2rem 0;
}

.cta-headline {
    font-family: 'Roboto', 'Open Sans', sans-serif;
    font-size: 2rem;
    font-weight: bold;
    color: #1E3A8A;
    margin-bottom: 1rem;
}

.cta-subheader {
    font-family: 'Roboto', 'Open Sans', sans-serif;
    font-size: 1.25rem;
    color: #6B7280;
    margin-bottom: 2rem;
}

.btn-cta {
    background-color: #3B82F6;
    color: #FFFFFF;
    font-family: 'Roboto', 'Open Sans', sans-serif;
    font-weight: 600;
    font-size: 1rem;
    padding: 10px 20px;
    border-radius: 4px;
    transition: background-color 0.3s ease;
    text-transform: uppercase;
}

.btn-cta .cta-icon {
    font-size: 1rem;
    margin-left: 0.5rem;
    transition: margin-left 0.3s ease;
}

.btn-cta:hover {
    background-color: #1E3A8A;
}

.btn-cta:hover .cta-icon {
    margin-left: 0.75rem;
}

.cta-image {
    border: 2px solid #D1D5DB;
    border-radius: 8px;
}

@media (max-width: 768px) {
    .cta-headline {
        font-size: 1.75rem;
    }

    .cta-subheader {
        font-size: 1rem;
    }

    .btn-cta {
        font-size: 0.875rem;
        padding: 8px 16px;
    }
}
```

### JS (if needed)

```javascript
$(document).ready(function() {
    $(window).scroll(function() {
        $('#cta .container').each(function() {
            if ($(this).isInViewport()) {
                $(this).addClass('fade-in');
            }
        });
    });

    $.fn.isInViewport = function() {
        var elementTop = $(this).offset().top;
        var elementBottom = elementTop + $(this).outerHeight();

        var viewportTop = $(window).scrollTop();
        var viewportBottom = viewportTop + $(window).height();

        return elementBottom > viewportTop && elementTop < viewportBottom;
    };
});
```