## Contact Information Section

### HTML

```html
<section id="contact-info" class="py-5">
    <div class="container">
        <div class="row mb-4">
            <div class="col-12 text-center">
                <h2 class="display-4 font-weight-bold">Get in Touch</h2>
                <p class="lead">We’d love to hear from you. Reach out to us through the following methods.</p>
            </div>
        </div>

        <div class="row">
            <div class="col-md-4">
                <div class="contact-detail">
                    <h3 class="font-weight-semibold"><i class="fas fa-envelope"></i> Email</h3>
                    <p>📧 contact@bkfpharma.com</p>
                </div>
                <div class="contact-detail">
                    <h3 class="font-weight-semibold"><i class="fas fa-phone"></i> Phone</h3>
                    <p>📞 +1 (800) 123-4567</p>
                </div>
                <div class="contact-detail">
                    <h3 class="font-weight-semibold"><i class="fas fa-map-marker-alt"></i> Address</h3>
                    <p>📍 123 Innovation Drive, BioTech Park, City, State, ZIP</p>
                </div>
            </div>

            <div class="col-md-8">
                <h3 class="font-weight-semibold">Contact Form</h3>
                <form id="contact-form">
                    <div class="form-row">
                        <div class="form-group col-md-6">
                            <label for="name">Name</label>
                            <input type="text" class="form-control" id="name" placeholder="Your Name">
                        </div>
                        <div class="form-group col-md-6">
                            <label for="email">Email</label>
                            <input type="email" class="form-control" id="email" placeholder="Your Email">
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="subject">Subject</label>
                        <input type="text" class="form-control" id="subject" placeholder="Subject">
                    </div>
                    <div class="form-group">
                        <label for="message">Message</label>
                        <textarea class="form-control" id="message" rows="5" placeholder="Your Message"></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Send Message</button>
                </form>

                <div id="thank-you-message" class="alert alert-success mt-4 d-none">Thank you for your message. We will get back to you soon.</div>
            </div>
        </div>

        <div class="row mt-4">
            <div class="col-12">
                <h3 class="font-weight-semibold">Find us at our physical location:</h3>
                <p>123 Innovation Drive, BioTech Park, City, State, ZIP</p>
                <div id="map" class="border" style="height: 400px;"></div>
            </div>
        </div>
    </div>
</section>
```

### CSS

```css
#contact-info {
    background: url('images/generated_image_A_futuristic,_abstract_image_representing.jpg') no-repeat center center;
    background-size: cover;
    color: #FFFFFF;
}

#contact-info h2, #contact-info h3 {
    color: #003366;
}

.contact-detail p {
    color: #66CDAA;
}

#contact-form input:focus, #contact-form textarea:focus {
    border-color: #00BFFF;
    box-shadow: 0 0 5px rgba(0, 191, 255, 0.5);
}

#contact-form .form-control {
    background-color: #F0F0F0;
    color: #000;
}

#contact-form .btn-primary {
    background-color: #003366;
    border-color: #003366;
}

#contact-form .btn-primary:hover {
    background-color: #00BFFF;
    border-color: #00BFFF;
}

#map {
    background-color: #F0F0F0;
}
```

### JS (if needed)

```javascript
$(document).ready(function() {
    $('#contact-form').on('submit', function(event) {
        event.preventDefault();
        $('#thank-you-message').removeClass('d-none').fadeIn();
        $(this).trigger('reset');
    });

    function initMap() {
        var location = {lat: 40.712776, lng: -74.005974}; // Sample coordinates
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 14,
            center: location
        });
        var marker = new google.maps.Marker({
            position: location,
            map: map,
            icon: {
                url: "path/to/custom-map-marker.png",
                scaledSize: new google.maps.Size(40, 40) // Customize marker size
            }
        });
    }

    google.maps.event.addDomListener(window, 'load', initMap);
});
```