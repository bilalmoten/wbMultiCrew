## Contact Form Section
### HTML

```html
<section id="contact-form" class="contact-form-section py-5">
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        <img src="images/generated_image_Generate_an_image_of_a.jpg" alt="Scientist working in a modern lab" class="img-fluid">
      </div>
      <div class="col-md-6">
        <h2 class="contact-form-heading">Get in Touch with BKF Pharma</h2>
        <p class="contact-form-intro">Whether you are a potential partner, investor, or simply interested in our work, we would love to hear from you. Please fill out the form below and a member of our team will get back to you shortly.</p>
        <form id="contactForm" action="#" method="post">
          <div class="form-group">
            <label for="name">Name</label>
            <div class="input-group">
              <div class="input-group-prepend">
                  <span class="input-group-text"><span class="icon-user"></span></span>
              </div>
              <input type="text" class="form-control" id="name" name="name" placeholder="Enter your full name" required>
            </div>
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <div class="input-group">
              <div class="input-group-prepend">
                <span class="input-group-text"><span class="icon-envelope"></span></span>
              </div>
              <input type="email" class="form-control" id="email" name="email" placeholder="Enter your email address" required>
            </div>
          </div>
          <div class="form-group">
            <label for="subject">Subject</label>
            <input type="text" class="form-control" id="subject" name="subject" placeholder="Enter the subject of your message" required>
          </div>
          <div class="form-group">
            <label for="message">Message</label>
            <textarea class="form-control" id="message" name="message" rows="6" placeholder="Enter your message" required></textarea>
          </div>
          <button type="submit" class="btn btn-primary btn-block">Submit</button>
          <div class="feedback-message mt-3"></div>
        </form>
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
#contact-form {
  background-color: #F0F0F0;
}

.contact-form-heading {
  color: #003366;
  font-size: 24px;
  font-family: 'Open Sans', sans-serif;
  font-weight: bold;
}

.contact-form-intro {
  color: #66CDAA;
  font-size: 16px;
  font-family: 'Open Sans', sans-serif;
  font-weight: normal;
}

.form-group label {
  color: #66CDAA;
  font-size: 14px;
  font-family: 'Open Sans', sans-serif;
  font-weight: 500;
}

.form-control {
  background-color: #ffffff;
  border-color: #003366;
  color: #003366;
  font-size: 14px;
}

.input-group-text {
  background-color: #ffffff;
  border-color: #003366;
  color: #003366;
}

.btn-primary {
  background-color: #003366;
  color: #ffffff;
  font-family: 'Open Sans', sans-serif;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #00BFFF;
}

.form-control:focus {
  border-color: #00BFFF;
  box-shadow: 0 0 5px rgba(0, 191, 255, 0.5);
}

.feedback-message {
  font-size: 14px;
  font-family: 'Open Sans', sans-serif;
  display: none;
}

.feedback-message.success {
  color: #66CDAA;
}

.feedback-message.error {
  color: #FFA500;
}
```

### JS

```javascript
$(document).ready(function(){
  $('#contactForm').on('submit', function(event){
    event.preventDefault();
    // Mock-ajax to simulate form submission
    $.ajax({
        url: '#',
        type: 'POST',
        data: $(this).serialize(),
        success: function(){
            $('.feedback-message').removeClass('error').addClass('success').text("Thank you for reaching out! We will get back to you soon.").fadeIn();
        },
        error: function(){
            $('.feedback-message').removeClass('success').addClass('error').text("There was an error submitting your form. Please try again.").fadeIn();
        }
    });
  });
});
```