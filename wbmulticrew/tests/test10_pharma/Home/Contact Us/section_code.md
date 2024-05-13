## Contact Us
### HTML
```html
<section class="contact-us-section">
  <header class="header">
    <div class="bg-image" style="background-image: url('images/generated_image_A_high-quality,_high-resolution_image_of.jpg');">
      <h1>Contact Us</h1>
      <p>Get in touch with BKF Pharma</p>
    </div>
  </header>
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        <h2>Get in Touch with BKF Pharma</h2>
        <p>At BKF Pharma, we're always excited to hear from potential partners, investors, and other interested parties. Whether you're looking to collaborate, invest, or simply learn more about our mission and values, we'd love to hear from you.</p>
      </div>
      <div class="col-md-6">
        <form id="contact-form">
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
      <div class="col-md-4">
        <h3>Contact Information</h3>
        <p>**Address:** 123 Main St, Anytown, USA 12345</p>
        <p>**Phone:** +1 (555) 123-4567</p>
        <p>**Email:** <a href="mailto:info@bkfpharma.com">info@bkfpharma.com</a></p>
      </div>
      <div class="col-md-4">
        <h3>Follow Us</h3>
        <ul>
          <li><a href="https://www.facebook.com/bkfpharma">Facebook</a></li>
          <li><a href="https://www.linkedin.com/company/bkfpharma">LinkedIn</a></li>
          <li><a href="https://twitter.com/bkfpharma">Twitter</a></li>
        </ul>
      </div>
    </div>
  </div>
</section>
```

### CSS
```css
.contact-us-section {
  background-color: #f7dc6f;
  padding: 50px 0;
}

.header {
  background-size: cover;
  background-position: center;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.header h1 {
  color: #3498db;
  font-size: 36px;
  margin-bottom: 10px;
}

.header p {
  color: #8bc34a;
  font-size: 18px;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.row {
  display: flex;
  flex-wrap: wrap;
}

.col-md-6 {
  flex: 0 0 50%;
}

.col-md-4 {
  flex: 0 0 33.33%;
}

#contact-form label {
  display: block;
  margin-bottom: 10px;
}

#contact-form input[type="text"], #contact-form input[type="email"], #contact-form textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
}

#contact-form input[type="submit"] {
  background-color: #3498db;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

#contact-form input[type="submit"]:hover {
  background-color: #2980b9;
}

.contact-information p {
  margin-bottom: 10px;
}

.follow-us ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.follow-us li {
  margin-bottom: 10px;
}

.follow-us a {
  color: #3498db;
  text-decoration: none;
}

.follow-us a:hover {
  color: #2980b9;
}
```

### JS (not needed in this case)
```
```
Note: As the design brief and text content do not require any JavaScript interactions or animations, there is no JS code provided.