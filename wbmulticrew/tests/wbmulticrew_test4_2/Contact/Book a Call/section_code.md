## Book a Call
### HTML

```html
<div class="container">
  <div class="row">
    <div class="col-md-12">
      <div class="section-header">
        <h2>Book a Call</h2>
        <img src="https://via.placeholder.com/100x50" alt="Acceleron AI Logo">
      </div>
    </div>
  </div>
  <div class="row">
    <div class="col-md-6">
      <img src="https://via.placeholder.com/800x600" alt="Futuristic Image" class="img-fluid">
    </div>
    <div class="col-md-6">
      <h2>Take the First Step Towards AI Automation</h2>
      <p>Discover how Acceleron AI can help your business stay ahead of the competition with our cutting-edge AI automation solutions.</p>
      <button class="btn btn-primary">Book a Call</button>
    </div>
  </div>
  <div class="row">
    <div class="col-md-12">
      <p>Are you tired of manual processes holding you back? Do you want to stay ahead of the competition and improve efficiency? Look no further! At Acceleron AI, we specialize in AI automation solutions that can help your business thrive.</p>
      <p>Our team of experts will work closely with you to understand your unique needs and develop a customized AI automation strategy that meets your goals. From automating repetitive tasks to improving customer service, our solutions can help you:</p>
      <ul>
        <li>Boost efficiency and productivity</li>
        <li>Reduce costs and increase profitability</li>
        <li>Stay ahead of the competition and drive innovation</li>
      </ul>
      <p>Ready to take the first step towards AI automation? Book a call with our experts today and discover how Acceleron AI can help your business thrive.</p>
    </div>
  </div>
</div>
```

### CSS
```css
_section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.section-header img {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}

h2 {
  font-weight: bold;
  font-size: 24px;
}

.img-fluid {
  width: 100%;
  height: 400px;
  object-fit: cover;
}

 btn-primary {
  background-color: #03A9F4;
  color: #FFFFFF;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #2E4053;
}
```

### JS
```javascript
$(document).ready(function() {
  $('button.btn-primary').hover(function() {
    $(this).css('background-color', '#2E4053');
  }, function() {
    $(this).css('background-color', '#03A9F4');
  });
});
```