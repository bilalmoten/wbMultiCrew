## Contact Information Section

### HTML

```html
<section id="contact-info" class="text-center text-lg-left">
   <div class="container-fluid p-5" style="background-image: url('images/generated_image_An_abstract,_futuristic_visual_that.jpg'); background-size: cover; background-position: center;">
      <div class="row mb-5">
         <div class="col-md-8 mx-auto">
            <h2 class="bold text-primary">Get in Touch with Us</h2>
            <p class="text-secondary">We are here to answer any questions you may have about BKF Pharma. Reach out to us, and we'll respond as soon as we can.</p>
         </div>
      </div>
      <div class="row">
         <div class="col-md-6 order-2 order-md-1">
            <form>
               <div class="form-group">
                  <label for="name" class="font-weight-bold text-secondary">Name</label>
                  <input type="text" class="form-control border-primary" id="name" required>
               </div>
               <div class="form-group">
                  <label for="email" class="font-weight-bold text-secondary">Email</label>
                  <input type="email" class="form-control border-primary" id="email" required>
               </div>
               <div class="form-group">
                  <label for="subject" class="font-weight-bold text-secondary">Subject</label>
                  <input type="text" class="form-control border-primary" id="subject" required>
               </div>
               <div class="form-group">
                  <label for="message" class="font-weight-bold text-secondary">Message</label>
                  <textarea class="form-control border-primary" id="message" rows="4" required></textarea>
               </div>
               <button type="submit" class="btn btn-primary btn-block font-weight-bold">Send Message</button>
            </form>
         </div>
         <div class="col-md-6 order-1 order-md-2">
            <div class="d-flex flex-column h-100 justify-content-center align-items-start mb-4 mb-md-0">
               <p><img src="images/generated_image_A_friendly_customer_support_representative.jpg" alt="Customer Support" class="img-fluid rounded"></p>
               <div class="text-left">
                  <h4 class="font-weight-bold">Contact Details</h4>
                  <p>
                      <strong>Email:</strong> <a href="mailto:contact@bkfpharma.com" class="text-primary">contact@bkfpharma.com</a><br>
                      <strong>Phone:</strong> +1-800-123-4567<br>
                      <strong>Address:</strong> 123 Pharma Street, BioCity, CA 94016, USA
                  </p>
                  <div class="d-flex justify-content-start social-links">
                     <a href="https://www.linkedin.com/company/bkfpharma" class="pr-3"><img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn"></a>
                     <a href="https://twitter.com/bkfpharma" class="pr-3"><img src="https://img.icons8.com/color/48/000000/twitter.png" alt="Twitter"></a>
                     <a href="https://facebook.com/bkfpharma"><img src="https://img.icons8.com/color/48/000000/facebook.png" alt="Facebook"></a>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </div>
</section>
```

### CSS

```css
#contact-info {
  color: #6c757d;
  background: none; /* Background image is already set inline */
}

h2.bold {
  font-size: 32px;
  color: #1a73e8;
}

p.text-secondary {
  font-size: 18px;
}

.form-control.border-primary {
  border-color: #1a73e8;
}

.btn-primary {
  background-color: #1a73e8;
  border-color: #1a73e8;
}

.btn-primary:hover {
  background-color: #0c60d0;
  border-color: #0c60d0;
}

.social-links a img {
  height: 48px;
  transition: transform 0.2s;
}

.social-links a:hover img {
  transform: scale(1.1);
}
```

### JS (if needed)

```javascript
$(document).ready(function(){
    $('form').on('submit', function(event){
        event.preventDefault();
        alert('Message Sent. We will get back to you shortly!');
    });
});
```