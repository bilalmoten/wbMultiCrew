## Address and Contact Info Section

### HTML
```html
<section class="address-contact-section">
  <div class="container">
    <div class="row">
      <div class="col-md-4">
        <img src="images/generated_image_A_futuristic,_abstract_visual_representing.jpg" alt="Abstract Visual" class="img-fluid">
      </div>
      <div class="col-md-8">
        <h1>Get in Touch</h1>
        <p>Contact us to learn more about BKF Pharma's mission and values.</p>
        <div class="contact-info">
          <p><strong<Address:></strong> 123 Main St, Anytown, USA 12345</p>
          <p><strong>Phone Number:</strong> 555-555-5555</p>
          <p><strong>Email Address:</strong> <a href="mailto:info@bkfpharma.com">info@bkfpharma.com</a></p>
        </div>
        <form>
          <label for="name">Name:</label>
          <input type="text" id="name" name="name"><br><br>
          <label for="email">Email:</label>
          <input type="email" id="email" name="email"><br><br>
          <label for="message">Message:</label>
          <textarea id="message" name="message"></textarea><br><br>
          <input type="submit" value="Send">
        </form>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <p>Stay up-to-date with the latest news and developments from BKF Pharma.</p>
        <a href="#">Follow us on social media</a>
      </div>
    </div>
  </div>
</section>
```

### CSS
```css
.address-contact-section {
  background-color: #f7f7f7;
  padding: 50px 0;
}

.address-contact-section .container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.address-contact-section img {
  width: 100%;
  height: 300px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 20px;
}

.address-contact-section h1 {
  font-family: Open Sans;
  font-size: 24px;
  margin-top: 0;
}

.address-contact-section p {
  font-family: Open Sans;
  font-size: 16px;
  margin-bottom: 20px;
}

.address-contact-section .contact-info {
  margin-bottom: 20px;
}

.address-contact-section .contact-info strong {
  font-weight: bold;
}

.address-contact-section form {
  margin-top: 20px;
}

.address-contact-section label {
  font-family: Open Sans;
  font-size: 16px;
  margin-bottom: 10px;
}

.address-contact-section input[type="text"], .address-contact-section input[type="email"] {
  width: 100%;
  height: 40px;
  padding: 10px;
  font-family: Open Sans;
  font-size: 16px;
  border: 1px solid #cccccc;
  border-radius: 5px;
  margin-bottom: 20px;
}

.address-contact-section textarea {
  width: 100%;
  height: 150px;
  padding: 10px;
  font-family: Open Sans;
  font-size: 16px;
  border: 1px solid #cccccc;
  border-radius: 5px;
  margin-bottom: 20px;
}

.address-contact-section input[type="submit"] {
  background-color: #34c759;
  color: #ffffff;
  border: none;
  padding: 10px 20px;
  font-family: Open Sans;
  font-size: 16px;
  cursor: pointer;
}

.address-contact-section input[type="submit"]:hover {
  background-color: #228944;
}
```

### JS
```
// No JavaScript code is needed for this section
```