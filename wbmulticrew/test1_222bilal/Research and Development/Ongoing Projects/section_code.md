## Ongoing Projects
### HTML

```html
<section id="ongoing-projects" class="py-5">
    <div class="container">
        <div class="row mb-4">
            <div class="col text-center">
                <h2 class="text-uppercase text-primary">Ongoing Projects</h2>
                <p class="lead">Explore our innovative research projects aimed at revolutionizing cancer treatment.</p>
            </div>
        </div>
        <div class="row">
            <div class="col-md-4 mb-4">
                <div class="card">
                    <img src="images/generated_image_A_high-quality,_abstract,_and_futuristic.jpg" class="card-img-top" alt="Immunotherapy Advancement">
                    <div class="card-body">
                        <h5 class="card-title">Immunotherapy Advancement</h5>
                        <p class="card-text">This project focuses on enhancing the efficacy of immunotherapy in treating various types of cancer. By leveraging the body's own immune system, we aim to develop more targeted and less invasive treatment options.</p>
                        <a href="#" class="btn btn-primary btn-lg">Learn More</a>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card">
                    <img src="images/generated_image_A_high-quality,_abstract,_and_futuristic.jpg" class="card-img-top" alt="Personalized Medicine">
                    <div class="card-body">
                        <h5 class="card-title">Personalized Medicine</h5>
                        <p class="card-text">Our personalized medicine project is dedicated to tailoring cancer treatments to individual genetic profiles. This approach aims to increase treatment success rates and minimize side effects.</p>
                        <a href="#" class="btn btn-primary btn-lg">Learn More</a>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card">
                    <img src="images/generated_image_A_high-quality,_abstract,_and_futuristic.jpg" class="card-img-top" alt="Early Detection Technologies">
                    <div class="card-body">
                        <h5 class="card-title">Early Detection Technologies</h5>
                        <p class="card-text">Early detection is crucial in the fight against cancer. This project is developing cutting-edge technologies to detect cancer at its earliest stages, significantly improving patient outcomes.</p>
                        <a href="#" class="btn btn-primary btn-lg">Learn More</a>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card">
                    <img src="images/generated_image_A_high-quality,_abstract,_and_futuristic.jpg" class="card-img-top" alt="Drug Resistance Solutions">
                    <div class="card-body">
                        <h5 class="card-title">Drug Resistance Solutions</h5>
                        <p class="card-text">Cancer cells often develop resistance to chemotherapy. This project aims to understand and overcome drug resistance, ensuring that treatments remain effective over time.</p>
                        <a href="#" class="btn btn-primary btn-lg">Learn More</a>
                    </div>
                </div>
            </div>
            <div class="col-md-4 mb-4">
                <div class="card">
                    <img src="images/generated_image_A_high-quality,_abstract,_and_futuristic.jpg" class="card-img-top" alt="Nanotechnology in Oncology">
                    <div class="card-body">
                        <h5 class="card-title">Nanotechnology in Oncology</h5>
                        <p class="card-text">Exploring the potential of nanotechnology to deliver drugs directly to cancer cells, minimizing damage to healthy tissues and enhancing the effectiveness of treatments.</p>
                        <a href="#" class="btn btn-primary btn-lg">Learn More</a>
                    </div>
                </div>
            </div>
        </div>
        <div class="row mt-5">
            <div class="col text-center">
                <p class="lead">Interested in learning more or partnering with us? Get in touch today!</p>
                <a href="#contact" class="btn btn-lg btn-outline-secondary">Contact Us</a>
            </div>
        </div>
    </div>
</section>
```

### CSS

```css
#ongoing-projects {
    background-color: #F2F2F2;
}

#ongoing-projects .text-primary {
    color: #003366 !important;
}

#ongoing-projects .card {
    background-color: #FFFFFF;
    border: 1px solid #F2F2F2;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}

#ongoing-projects .card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

#ongoing-projects .card-title {
    font-size: 1.5rem;
    font-weight: bold;
    text-transform: uppercase;
}

#ongoing-projects .btn-primary {
    background-color: #00FF00;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    transition: background-color 0.3s;
}

#ongoing-projects .btn-primary:hover {
    background-color: darken(#00FF00, 10%);
}

#ongoing-projects .btn-outline-secondary {
    color: #FFFFFF;
    background-color: #008080;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    transition: background-color 0.3s;
}

#ongoing-projects .btn-outline-secondary:hover {
    background-color: darken(#008080, 10%);
}

#ongoing-projects .lead {
    font-size: 1.25rem;
    font-weight: 300;
}

@media (max-width: 768px) {
    #ongoing-projects .card-title {
        font-size: 1.25rem;
    }

    #ongoing-projects .lead {
        font-size: 1rem;
    }
}
```


### JS (if needed)
```javascript
// Smooth scrolling effect for "Contact Us" button
$(document).ready(function(){
    $("a[href='#contact']").on('click', function(event) {
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