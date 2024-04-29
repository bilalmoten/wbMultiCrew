# **What We Do Section**

### HTML

```html
<div class="what-we-do-section">
  <div class="hero-section">
    <img
      src="https://example.com/hero-image.jpg"
      alt="AI Automation Hero Image"
    />
    <div class="hero-overlay">
      <h2>What We Do</h2>
      <p>Boost Efficiency, Cut Costs, and Stay Ahead of the Competition</p>
    </div>
  </div>
  <div class="content-section">
    <div class="container">
      <h3>The Power of AI Automation</h3>
      <ul>
        <li>
          <i class="fas fa-setChecked"></i>
          <p>
            Boost Efficiency: Automate repetitive tasks, freeing up your team to
            focus on high-value tasks that drive growth and innovation.
          </p>
        </li>
        <li>
          <i class="fas fa-setChecked"></i>
          <p>
            Cut Costs: Reduce operational costs by minimizing manual labor,
            reducing errors, and optimizing resource allocation.
          </p>
        </li>
        <li>
          <i class="fas fa-setChecked"></i>
          <p>
            Stay Ahead of the Competition: Stay ahead of the competition by
            leveraging AI-driven insights to make data-driven decisions and
            drive business growth.
          </p>
        </li>
      </ul>
      <div class="/how-we-can-help">
        <h3>How We Can Help</h3>
        <p>
          Our team of experts will work closely with you to understand your
          unique business needs and develop a customized AI automation solution
          that meets your goals. From integrating with your existing systems to
          providing ongoing support and maintenance, we're committed to helping
          you achieve your objectives.
        </p>
      </div>
      <div class="book-a-call">
        <a href="#" class="btn btn-primary">Book a Call</a>
        <p>
          Ready to learn more about how AI automation can benefit your business?
          Book a call with our experts today and take the first step towards
          unlocking your organization's full potential.
        </p>
      </div>
      <div class="get-started">
        <a href="#" class="btn btn-secondary">Get Started</a>
        <p>
          Don't miss out on the opportunity to revolutionize your business with
          AI automation. Contact us today to learn more about our services and
          how we can help you achieve your goals.
        </p>
      </div>
    </div>
  </div>
</div>
```

### CSS

```css
.what-we-do-section {
  background-image: url("https://example.com/background-image.jpg");
  background-size: cover;
  padding: 50px 0;
}

.hero-section {
  background-color: #2e4053;
  padding: 100px 0;
  position: relative;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #2e4053;
  opacity: 0.5;
  padding: 20px;
  color: #ffffff;
}

.hero-overlay h2 {
  font-weight: bold;
  margin-bottom: 10px;
}

.hero-overlay p {
  font-size: 18px;
  margin-bottom: 20px;
}

.content-section {
  padding: 50px 0;
}

.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

ul li {
  margin-bottom: 20px;
}

ul li i {
  margin-right: 10px;
  font-size: 18px;
}

p,
h3 {
  font-size: 18px;
  margin-bottom: 20px;
}

.how-we-can-help,
.get-started {
  margin-top: 50px;
}

button.btn {
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
  cursor: pointer;
}

button.btn-primary {
  background-color: #03a9f4;
  color: #ffffff;
}

button.btn-secondary {
  background-color: #ffffff;
  border: 1px solid #2e4053;
  color: #2e4053;
}

button.btn:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  background-color: #ffffff;
  color: #2e4053;
}

button.btn-primary:hover {
  background-color: #2e4053;
  color: #ffffff;
}

.book-a-call,
.get-started {
  margin-top: 50px;
}
```

```javascript
// **No JavaScript needed for this section**
```
