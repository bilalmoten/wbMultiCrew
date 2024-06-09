## Contact Information Section
### HTML

```html
<section id="cta-section" class="text-center py-5">
    <div class="container d-flex align-items-center justify-content-between">
        <div class="cta-content text-lg-left">
            <h2>Join Us in Revolutionizing Cancer Treatment</h2>
            <p>At BKF Pharma, we're pioneering innovative solutions to combat cancer. Discover how you can be a part of this groundbreaking journey.</p>
            <a href="#" class="btn btn-primary">Learn More</a>
        </div>
        <div class="cta-image">
            <img src="https://via.placeholder.com/400" alt="Science Image" class="img-fluid">
        </div>
    </div>
</section>
```

### CSS

```css
#cta-section {
    background-color: #FFFFFF;
}

#cta-section .cta-content h2 {
    font-family: 'Roboto', sans-serif;
    font-weight: bold;
    font-size: 2.5em;
    color: #1E3A8A;
}

#cta-section .cta-content p {
    font-family: 'Open Sans', sans-serif;
    font-weight: regular;
    font-size: 1.25em;
    color: #6B7280;
}

#cta-section .btn-primary {
    font-family: 'Roboto', sans-serif;
    font-weight: medium;
    font-size: 1em;
    color: #FFFFFF;
    background-color: #3B82F6;
    border-radius: 4px;
    padding: 15px 30px;
    transition: background-color 0.3s ease;
}

#cta-section .btn-primary:hover {
    background-color: #1E3A8A;
}

#cta-section .cta-image img {
    max-width: 100%;
    transition: transform 0.3s ease;
}

#cta-section .cta-content,
#cta-section .cta-image {
    flex: 1;
}

@media (max-width: 768px) {
    #cta-section .container {
        flex-direction: column;
        text-align: center;
    }

    #cta-section .cta-image {
        margin-top: 20px;
    }
}
```

### JS

```javascript
$(document).ready(function(){
    $(window).on('scroll', function(){
        var scrolled = $(window).scrollTop();
        if ($('#cta-section').offset().top - $(window).height() < scrolled) {
            $('#cta-section .cta-content').fadeIn(800);
            $('#cta-section .cta-image img').css('transform', 'scale(1.1)').fadeIn(800);
        }
    });
});
```