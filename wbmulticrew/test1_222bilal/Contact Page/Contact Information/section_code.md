## Contact Information Section
### HTML

```html
<section id="contact-info" class="container my-5">
    <div class="text-center mb-5">
        <h2 class="display-4 text-white">Get in Touch</h2>
        <p class="text-white">We would love to hear from you. Reach out with any inquiries or questions.</p>
    </div>
    
    <div class="row mb-5">
        <div class="col-lg-6 mb-4">
            <div class="contact-card p-4">
                <h4 class="mb-3"><i class="fas fa-envelope"></i> Email Addresses</h4>
                <p><strong>General Inquiries: </strong><a href="mailto:info@bkfpharma.com">info@bkfpharma.com</a></p>
                <p><strong>Partner Relations: </strong><a href="mailto:partners@bkfpharma.com">partners@bkfpharma.com</a></p>
            </div>
        </div>
        
        <div class="col-lg-6 mb-4">
            <div class="contact-card p-4">
                <h4 class="mb-3"><i class="fas fa-phone-alt"></i> Phone Numbers</h4>
                <p><strong>Main Office: </strong><a href="tel:+18001234567">+1 (800) 123-4567</a></p>
                <p><strong>Partner Relations: </strong><a href="tel:+18002345678">+1 (800) 234-5678</a></p>
            </div>
        </div>

        <div class="col-lg-6 mb-4 mt-lg-5 mt-md-1">
            <div class="contact-card p-4">
                <h4 class="mb-3"><i class="fas fa-map-marker-alt"></i> Physical Address</h4>
                <address>
                    BKF Pharma Inc.<br>
                    123 Innovation Drive<br>
                    Science City, CA 94000
                </address>
            </div>
        </div>

        <div class="col-lg-6">
            <h4 class="mb-4 text-white"><i class="fas fa-envelope-open"></i> Contact Form</h4>
            <form id="contact-form">
                <div class="form-group">
                    <label for="name" class="text-white">Name</label>
                    <input type="text" class="form-control" id="name">
                </div>
                <div class="form-group">
                    <label for="email" class="text-white">Email</label>
                    <input type="email" class="form-control" id="email">
                </div>
                <div class="form-group">
                    <label for="subject" class="text-white">Subject</label>
                    <input type="text" class="form-control" id="subject">
                </div>
                <div class="form-group">
                    <label for="message" class="text-white">Message</label>
                    <textarea class="form-control" id="message" rows="4"></textarea>
                </div>
                <button type="submit" class="btn btn-success">Send Message</button>
            </form>
        </div>
    </div>

    <div class="row mt-5">
        <div class="col-12">
            <h4 class="text-white text-center mb-4">Find Us Here</h4>
            <iframe src="images/generated_image_Interactive_map_with_a_pin.jpg" 
                    width="100%" height="450" style="border:0;" 
                    allowfullscreen="" loading="lazy"></iframe>
        </div>
    </div>
</section>
```

### CSS

```css
#contact-info {
    background-color: #003366;
    color: #FFFFFF;
    padding: 60px 20px;
}

.contact-card {
    background-color: #FFFFFF;
    border: 1px solid #F2F2F2;
    border-radius: 10px;
    transition: box-shadow 0.3s ease;
}

.contact-card h4 {
    font-weight: bold;
    text-transform: uppercase;
}

.contact-card:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.contact-card p, .contact-card a {
    color: #003366;
}

.form-group input, 
.form-group textarea {
    border: 1px solid #F2F2F2;
    padding: 10px;
    border-radius: 5px;
    background-color: #FFFFFF;
}

.form-group input:focus,
.form-group textarea:focus {
    border-color: #008080;
    outline: none;
}

btn-success {
    background-color: #00FF00;
    border-radius: 5px;
    padding: 10px 20px;
    font-weight: bold;
    text-transform: uppercase;
}

btn-success:hover {
    background-color: #00CC00;
}


```

### JS (if needed)

```javascript
// No additional JavaScript needed for static elements implementation.
```