## Contact Form Section
### HTML

```html
<section id="contact-form">
  <div class="container">
    <div class="row">
      <div class="col-md-8 offset-md-2">
        <h2 class="header">Get in Touch</h2>
        <p class="intro-text">We're always excited to hear from you. Whether you're a potential partner, investor, or simply someone who shares our passion for cancer treatment, we'd love to hear from you.</p>
      </div>
    </div>
    <div class="row">
      <div class="col-md-6 offset-md-3">
        <form id="contact-form">
          <div class="form-group">
            <label for="name">Your Name</label>
            <input type="text" id="name" name="name" required>
          </div>
          <div class="form-group">
            <label for="email">Your Email</label>
            <input type="email" id="email" name="email" required>
          </div>
          <div class="form-group">
            <label for="phone">Your Phone Number</label>
            <input type="tel" id="phone" name="phone" required>
          </div>
          <div class="form-group">
            <label for="message">Your Message</label>
            <textarea id="message" name="message" required></textarea>
          </div>
          <button type="submit" class="btn-send">Send Message</button>
        </form>
      </div>
    </div>
    <div class="row">
      <div class="col-md-8 offset-md-2">
        <p class="thank-you">Thank you for your interest in BKF Pharma. We'll be in touch soon!</p>
      </div>
    </div>
  </div>
  <img src="images/generated_image_A_futuristic,_abstract_image_of.jpg" alt="A futuristic, abstract image of a person in a lab coat, with a subtle background of molecules or DNA helices, to evoke a sense of innovation and cutting-edge technology.">
</section>
```

### CSS
```css
#contact-form {
  background-color: #f7f7f7;
  padding: 40px 0;
}

.header {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.intro-text {
  margin-bottom: 30px;
}

form {
  margin-top: 20px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  font-size: 16px;
  color: #333333;
  margin-bottom: 10px;
}

input, textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #f7f7f7;
  border-radius: 5px;
}

input:focus, textarea:focus {
  border-color: #34c759;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.btn-send {
  background-color: #34c759;
  color: #ffffff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.btn-send:hover {
  background-color: #4567b7;
}

.thank-you {
  margin-top: 20px;
  font-size: 16px;
  color: #333333;
}

@media (max-width: 768px) {
  #contact-form {
    padding: 20px 0;
  }
}
```

### JS
```javascript
// No JavaScript code needed for this section
```