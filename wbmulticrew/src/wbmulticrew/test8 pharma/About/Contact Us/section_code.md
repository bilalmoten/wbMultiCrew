## Contact Us Section
### HTML
```html
<!-- Header -->
<nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #87CEEB">
    <a class="navbar-brand" href="#">
        <img src="images/bkf-pharma-logo.png" alt="BKF Pharma Logo">
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Dropdown
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="#">Action</a>
                    <a class="dropdown-item" href="#">Another action</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">Something else here</a>
                </div>
            </li>
        </ul>
    </div>
</nav>

<!-- Form -->
<section class="contact-form">
    <div class="container">
        <h2>Get in Touch with BKF Pharma</h2>
        <p>Please fill out the form below to get in touch with us.</p>
        <form>
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" class="form-control" placeholder="Name">
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" class="form-control" placeholder="Email">
            </div>
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" class="form-control" placeholder="Phone Number">
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" class="form-control" placeholder="Message"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit Your Inquiry</button>
        </form>
    </div>
</section>

<!-- Footer -->
<footer class="footer">
    <p>&copy; 2023 BKF Pharma. All rights reserved.</p>
</footer>
```
### CSS
```css
body {
    font-family: Open Sans;
    background-color: #87CEEB;
}

.navbar {
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.contact-form {
    background-image: url("images/generated_image_A_high-quality_image_of_a.jpg");
    background-size: cover;
    background-position: center;
    padding: 50px 0;
}

.container {
    max-width: 700px;
    margin: 40px auto;
    padding: 20px;
    background-color: #FFF;
    border: 1px solid #DDD;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    font-size: 24px;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 20px;
}

form {
    width: 100%;
}

label {
    display: block;
    margin-bottom: 10px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #CCC;
}

button[type="submit"] {
    background-color: #2F4F7F;
    color: #FFF;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #1A1D23;
}

_footer {
    background-color: #2F4F7F;
    padding: 10px;
    text-align: center;
    color: #FFF;
}
```
### JS
```javascript
// No JavaScript needed for this section
```