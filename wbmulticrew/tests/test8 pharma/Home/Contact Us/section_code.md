## Contact Us Section
### HTML
```html
<section class="contact-us">
    <header>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#"><img src="logo.png" alt="BKF Pharma Logo"></a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item active">
                        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">About Us</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Resources</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Contact Us</a>
                    </li>
                </ul>
            </div>
        </nav>
    </header>
    <div class="container">
        <h2>Get in Touch with BKF Pharma</h2>
        <p>At BKF Pharma, we're committed to revolutionizing cancer treatment through innovative research and development. We're excited to connect with potential partners, investors, researchers, and healthcare professionals who share our passion for making a difference in the lives of those affected by cancer.</p>
        <form>
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" id="name" placeholder="enter your name">
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" id="email" placeholder="enter your email">
            </div>
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" class="form-control" id="phone" placeholder="enter your phone number">
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea class="form-control" id="message" placeholder="enter your message"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit Your Inquiry</button>
        </form>
    </div>
    <footer>
        <p>&copy; 2023 BKF Pharma. All Rights Reserved.</p>
    </footer>
</section>
```
### CSS
```css
.contact-us {
    background-image: linear-gradient(to bottom, #87CEEB, #2F4F7F);
    background-size: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.navbar-nav {
    flex-direction: row;
}

.nav-item {
    margin-right: 20px;
}

.form-control {
    margin-bottom: 20px;
}

label {
    margin-bottom: 10px;
}

.btn-primary {
    background-color: #2F4F7F;
    border-color: #2F4F7F;
}

footer {
    background-color: #2F4F7F;
    color: #FFFFFF;
    padding: 10px;
    text-align: center;
}
```
### JS
```javascript
$(document).ready(function() {
    $('form').submit(function(e) {
        e.preventDefault();
        // form submission logic here
    });
});
```