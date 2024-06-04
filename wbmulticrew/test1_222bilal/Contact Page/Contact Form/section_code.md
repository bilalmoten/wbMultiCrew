## Contact Form
### HTML
```html
<section class="contact-section" style="background-image: url('images/generated_image_A_sleek,_abstract_background_with.jpg');">
  <div class="container">
    <div class="row">
      <div class="col-12 text-center">
        <h2>Get in Touch with Us</h2>
        <p>We are here to answer any questions you may have about our research and innovations. Reach out to us, and we’ll respond as soon as we can.</p>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-6 col-md-12">
        <form class="contact-form">
          <div class="form-group">
            <label for="name">Name</label>
            <input type="text" class="form-control" id="name" placeholder="Your Name">
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" placeholder="Your Email">
          </div>
          <div class="form-group">
            <label for="subject">Subject</label>
            <input type="text" class="form-control" id="subject" placeholder="Subject">
          </div>
          <div class="form-group">
            <label for="message">Message</label>
            <textarea class="form-control" id="message" rows="5" placeholder="Your Message"></textarea>
          </div>
          <button type="submit" class="btn btn-submit">Send Message</button>
        </form>
      </div>
      <div class="col-lg-6 col-md-12">
        <div class="contact-info">
          <h3>Contact Information</h3>
          <p>Email: <a href="mailto:contact@bkfpharma.com">contact@bkfpharma.com</a></p>
          <p>Phone: <a href="tel:+15551234567">+1 (555) 123-4567</a></p>
          <p>Address: 123 Pharma Blvd, Innovation City, CA 94043</p>
        </div>
        <img src="images/generated_image_A_simple,_modern_icon_of.jpg" alt="Contact Icon" class="contact-icon">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3153.6454729090264!2d-122.07178128468529!3d37.421971579824026!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808fb24cf5b17201:0xdb4fangi066fovzo262hbjudfb997590255!2s123 Pharma Blvd, Innovation City, CA 94043!5e0!3m2!1sen!2sus!4v1635703726602!5m2!1sen!2sus" style="border:0;" allowfullscreen loading="lazy"></iframe>
      </div>
    </div>
  </div>
</section>
```

### CSS
```css
.contact-section {
  background-size: cover;
  padding: 60px 0;
}

.contact-section h2 {
  font-family: 'Helvetica Neue', sans-serif;
  font-size: 24px;
  text-transform: uppercase;
  font-weight: bold;
  color: #003366;
}

.contact-section p {
  font-family: 'Helvetica Neue', sans-serif;
  font-size: 16px;
  margin-bottom: 30px;
}

.contact-form .form-group {
  margin-bottom: 25px;
}

.contact-form .form-control {
  font-family: 'Helvetica Neue', sans-serif;
  font-size: 14px;
  border: 1px solid #f2f2f2;
  border-radius: 5px;
  padding: 10px;
  transition: border-color 0.3s;
}

.contact-form .form-control:focus {
  border-color: #008080;
  box-shadow: 0 0 8px rgba(0,128,128,0.4);
}

.contact-form .btn-submit {
  background-color: #00FF00;
  color: white;
  font-family: 'Helvetica Neue', sans-serif;
  font-size: 14px;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  transition: background-color 0.3s;
}

.contact-form .btn-submit:hover {
  background-color: #00e600;
}

.contact-info {
  background-color: #F2F2F2;
  padding: 20px;
  border-radius: 10px;
  color: #003366;
  margin-top: 30px;
}

.contact-info a {
  color: #003366;
}

.contact-icon {
  display: block;
  margin: 20px auto;
  max-width: 100px;
}

iframe {
  margin-top: 30px;
  width: 100%;
  height: 300px;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

@media (max-width: 767px) {
  .contact-form {
    margin-top: 30px;
  }
}
```