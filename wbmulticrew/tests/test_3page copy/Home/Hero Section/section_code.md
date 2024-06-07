## Hero Section
### HTML

```html
<section class="hero-section">
  <div class="container">
    <div class="row align-items-center text-center text-md-left">
      <div class="col-md-6">
        <h1>Join Us in the Fight Against Cancer</h1>
        <p>Discover how BKF Pharma is pioneering groundbreaking cancer treatments.</p>
        <a href="/learn-more" class="btn btn-primary">Learn More</a>
      </div>
      <div class="col-md-6">
        <img src="images/generated_image_Generate_an_abstract,_futuristic_visual.jpg" alt="Futuristic Visual" class="img-fluid">
      </div>
    </div>
  </div>
</section>
```

### CSS

```css
.hero-section {
  background-color: #E0F2FE;
  padding: 80px 0;
}

.hero-section h1 {
  font-size: 2em;
  font-weight: bold;
  color: #1E3A8A;
  margin-bottom: 10px;
}

.hero-section p {
  font-size: 1.5em;
  font-weight: regular;
  color: #1E3A8A;
  margin-bottom: 20px;
}

.hero-section .btn {
  background-color: #3B82F6;
  color: #FFFFFF;
  padding: 15px 30px;
  border-radius: 4px;
  font-size: 1em;
  font-weight: bold;
  transition: background-color 0.3s;
}

.hero-section .btn:hover {
  background-color: #1E3A8A;
}

.hero-section .img-fluid {
  max-width: 100%;
  height: auto;
}
```
