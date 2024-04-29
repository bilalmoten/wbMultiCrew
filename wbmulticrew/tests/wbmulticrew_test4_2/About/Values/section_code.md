## Values Section
### HTML
```html
<section id="values" class="py-5">
  <div class="container">
    <div class="row">
      <div class="col-md-12 text-center">
        <h2 class="section-title">Our Values</h2>
        <p class="section-text">At Acceleron AI, we believe that our values are the foundation of our success.</p>
      </div>
    </div>
    <div class="row">
      <div class="col-md-3 mb-4">
        <div class="value-card">
          <i class="fas fa-lightbulb"></i>
          <h5>Innovation</h5>
          <p>We're passionate about innovation and committed to staying at the forefront of AI automation.</p>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="value-card">
          <i class="fas fa-users"></i>
          <h5>Customer-Centric</h5>
          <p>We're dedicated to providing exceptional service, listening to their needs, and delivering tailored solutions.</p>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="value-card">
          <i class="fas fa-handshake"></i>
          <h5>Collaboration</h5>
          <p>We believe that collaboration is the key to achieving great things.</p>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="value-card">
          <i class="fas fa-lock"></i>
          <h5>Integrity</h5>
          <p>Integrity is the foundation of our business.</p>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-3 mb-4">
        <div class="value-card">
          <i class="fas fa-users"></i>
          <h5>Inclusion</h5>
          <p>We believe that diversity and inclusion are essential for driving innovation and creativity.</p>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="value-card">
          <i class="fas fa-book"></i>
          <h5>Continuous Learning</h5>
          <p>We're committed to continuous learning and improvement.</p>
        </div>
      </div>
      <div class="col-md-3 mb-4">
        <div class="value-card">
          <i class="fas fa-leaf"></i>
          <h5>Sustainability</h5>
          <p>We're committed to sustainability and reducing our environmental footprint.</p>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12 text-center">
        <button class="btn btn-primary">Learn More</button>
      </div>
    </div>
  </div>
</section>
```

### CSS
```css
#values {
  background-image: url('https://dalleprodsec.blob.core.windows.net/private/images/2d138acf-700a-45b2-acab-b62da47f37d8/generated_00.png?se=2024-04-27T13%3A58%3A22Z&sig=WR73TGC0RH7gcI4dom2dMJOKTyMwneNYq0%2FdW0W6JBA%3D&ske=2024-05-03T08%3A51%3A57Z&skoid=e52d5ed7-0657-4f62-bc12-7e5dbb260a96&sks=b&skt=2024-04-26T08%3A51%3A57Z&sktid=33e01921-4d64-4f8c-a055-5bdaffd5e33d&skv=2020-10-02&sp=r&spr=https&sr=b&sv=2020-10-02');
  background-size: cover;
  background-position: center;
  padding: 50px;
}

.value-card {
  background-color: #fff;
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease-in-out;
}

.value-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
}

.value-card i {
  font-size: 24px;
  color: #03A9F4;
}

h5 {
  font-weight: bold;
  margin-top: 0;
}

button {
  background-color: #03A9F4;
  border: none;
  padding: 10px 20px;
  color: #fff;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #02a3f3;
}
```

### JS
```javascript
$('button').on('click', function() {
  alert('Learn More clicked!');
})
```