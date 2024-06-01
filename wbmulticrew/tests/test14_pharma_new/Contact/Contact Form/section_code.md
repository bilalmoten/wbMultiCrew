## Contact Form Section

### HTML

```html
<section class="contact-form-section">
  <div class="container" style="background-image: url('path-to-header-background-image.jpg');">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="header">
          <h2>Get in Touch with Us</h2>
          <p>We're here to answer any questions you may have about partnering with BKF Pharma.</p>
        </div>
        <form>
          <div class="form-group">
            <label for="name">Name</label>
            <input type="text" class="form-control" id="name" placeholder="Enter your full name">
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" class="form-control" id="email" placeholder="Enter your email address">
          </div>
          <div class="form-group">
            <label for="subject">Subject</label>
            <select class="form-control" id="subject">
              <option value="" disabled selected>Select the subject of your inquiry</option>
              <option value="Partnership">Partnership</option>
              <option value="Investment">Investment</option>
            </select>
          </div>
          <div class="form-group">
            <label for="message">Message</label>
            <textarea class="form-control" id="message" rows="5" placeholder="Type your message here"></textarea>
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </div>
  <div class="container contact-info">
    <div class="row justify-content-center">
      <div class="col-md-4">
        <div class="card">
          <div class="card-body">
            <p><i class="fas fa-envelope"></i> Email: contact@bkfpharma.com</p>
            <p><i class="fas fa-phone"></i> Phone: +1-800-123-4567</p>
            <p><i class="fas fa-map-marker-alt"></i> Address: 123 Pharma Street, Medicine City, State, ZIP</p>
          </div>
        </div>
      </div>
      <div class="col-md-8">
        <iframe
          src="path-to-google-maps-embed-link"
          width="100%"
          height="300"
          frameborder="0" 
          style="border:0" 
          allowfullscreen
          aria-hidden="false" 
          tabindex="0"></iframe>
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
.contact-form-section {
  background-color: #0044cc;
  padding: 50px 0;
}

.contact-form-section .header {
  text-align: center;
  color: #ffffff;
  margin-bottom: 30px;
}

.contact-form-section .header h2 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.contact-form-section .header p {
  font-size: 16px;
}

.contact-form-section .form-group label {
  color: #ffffff;
  font-size: 14px;
  font-weight: 500;
}

.contact-form-section .form-control {
  background-color: #ffffff;
  border: 2px solid #0044cc;
  border-radius: 5px;
  color: #000000;
}

.contact-form-section .form-group .form-control:focus {
  border-color: #003399;
}

.contact-form-section .btn-primary {
  background-color: #0044cc;
  border-color: #0044cc;
  font-size: 18px;
  font-weight: bold;
  border-radius: 5px;
}

.contact-form-section .btn-primary:hover {
  background-color: #0055dd;
  border-color: #0055dd;
}

.contact-info {
  margin-top: 50px;
}

.contact-info .card {
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
  transition: transform 0.3s;
}

.contact-info .card:hover {
  transform: translateY(-10px);
}

.contact-info .card-body {
  padding: 30px;
  color: #666666;
}

.contact-info .card-body p {
  font-size: 14px;
  margin: 10px 0;
}

.contact-info .card-body i {
  color: #0044cc;
  margin-right: 10px;
}
```

### JS

```javascript
$(document).ready(function() {
  $('form').on('submit', function(e) {
    e.preventDefault();
    // Implement form validation or submit
  });

  $('.contact-info .card').on('mouseenter', function() {
    $(this).css('box-shadow', '0 6px 12px rgba(0, 0, 0, 0.2)');
  }).on('mouseleave', function() {
    $(this).css('box-shadow', '0 4px 8px rgba(0, 0, 0, 0.1)');
  });
});
```