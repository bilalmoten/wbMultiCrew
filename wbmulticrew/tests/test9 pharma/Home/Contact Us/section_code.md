## Contact Us
### HTML
```html
<div class="container">
  <div class="row">
    <div class="col-md-6 left-column">
      <h2>Get in Touch</h2>
      <p>At BKF Pharma, we're committed to revolutionizing cancer treatment and improving the lives of those affected by the disease. We're always looking for like-minded individuals and organizations to collaborate with and learn from. If you're interested in partnering with us or would like to learn more about our mission and values, please don't hesitate to reach out.</p>
      <form id="contact-form">
        <input type="text" name="name" placeholder="Name">
        <input type="email" name="email" placeholder="Email">
        <textarea name="message" placeholder="Message"></textarea>
        <button type="submit">Send</button>
      </form>
    </div>
    <div class="col-md-6 right-column">
      <h2>Contact Information</h2>
      <ul>
        <li><i class="fas fa-envelope"></i> <a href="mailto:info@bkfpharma.com">info@bkfpharma.com</a></li>
        <li><i class="fas fa-phone"></i> +1 (555) 123-4567</li>
        <li><i class="fas fa-map-marker"></i> BKF Pharma Headquarters, 123 Main St, Anytown, USA 12345</li>
      </ul>
      <h2>Follow Us</h2>
      <ul>
        <li><i class="fab fa-twitter"></i> <a href="https://twitter.com/bkfpharma">@bkfpharma</a></li>
        <li><i class="fab fa-linkedin"></i> <a href="https://linkedin.com/company/bkfpharma">linkedin.com/company/bkfpharma</a></li>
        <li><i class="fab fa-facebook"></i> <a href="https://facebook.com/bkfpharma">facebook.com/bkfpharma</a></li>
      </ul>
    </div>
  </div>
  <img src="images/generated_image_A_high-quality_image_of_a.jpg" alt="Contact Form Image" class="contact-form-image">
</div>
```

### CSS
```css
container {
  padding: 20px;
}

.left-column {
  padding: 20px;
  background-color: #F7F7F7;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.right-column {
  padding: 20px;
}

.contact-form-image {
  width: 100%;
  height: 300px;
  object-fit: cover;
  border-radius: 10px;
  margin-bottom: 20px;
}

#contact-form {
  padding: 20px;
  background-color: #F7F7F7;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#contact-form input, #contact-form textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

#contact-form button[type="submit"] {
  background-color: #03A9F4;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

#contact-form button[type="submit"]:hover {
  background-color: #02a3e7;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

ul li {
  margin-bottom: 10px;
}

ul li i {
  margin-right: 10px;
}

ul li a {
  text-decoration: none;
  color: #333;
}

ul li a:hover {
  text-decoration: underline;
}
```

### JS
```javascript
// no js code is needed for this section
```