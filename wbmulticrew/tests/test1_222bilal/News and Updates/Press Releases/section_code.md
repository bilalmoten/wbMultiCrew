## Press Releases
### HTML

```html
<section id="press-releases" class="container my-5">
    <div class="text-center">
        <h1 class="section-title">Press Releases</h1>
        <p class="subtitle">Stay updated with our latest news and announcements.</p>
    </div>
    <div class="row mt-4">
        <div class="col-lg-4 col-md-6 mb-4">
            <div class="card press-release-card">
                <div class="card-body">
                    <h5 class="card-title">BKF Pharma Announces Breakthrough in Cancer Treatment</h5>
                    <p class="release-date">October 5, 2023</p>
                    <p class="card-text">BKF Pharma reveals a groundbreaking discovery in the fight against cancer.</p>
                    <a href="#" class="btn btn-readmore">Read More</a>
                </div>
            </div>
        </div>
        <div class="col-lg-4 col-md-6 mb-4">
            <div class="card press-release-card">
                <div class="card-body">
                    <h5 class="card-title">New Partnership with Leading Research Institute</h5>
                    <p class="release-date">September 20, 2023</p>
                    <p class="card-text">A new collaboration promises to accelerate cancer research and treatment.</p>
                    <a href="#" class="btn btn-readmore">Read More</a>
                </div>
            </div>
        </div>
        <div class="col-lg-4 col-md-6 mb-4">
            <div class="card press-release-card">
                <div class="card-body">
                    <h5 class="card-title">Upcoming Conference on Innovative Cancer Therapies</h5>
                    <p class="release-date">August 15, 2023</p>
                    <p class="card-text">Join us at the upcoming conference to explore the latest in cancer treatment.</p>
                    <a href="#" class="btn btn-readmore">Read More</a>
                </div>
            </div>
        </div>
    </div>

    <nav aria-label="Page navigation">
        <ul class="pagination justify-content-center">
            <li class="page-item"><a class="page-link active" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
        </ul>
    </nav>
</section>
```

### CSS
```css
#press-releases {
  padding: 40px 0;
}

.section-title {
  font-family: "Helvetica Neue", sans-serif;
  font-size: 36px;
  color: #003366;
  font-weight: bold;
}

.subtitle {
  font-family: "Helvetica Neue", sans-serif;
  font-size: 18px;
  color: #008080;
  margin-bottom: 40px;
}

.press-release-card {
  background-color: #ffffff;
  border: 1px solid #f2f2f2;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: all 0.3s;
  padding: 20px;
}

.press-release-card:hover {
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
}

.card-title {
  font-family: "Helvetica Neue", sans-serif;
  font-size: 24px;
  color: #003366;
  font-weight: bold;
}

.release-date {
  font-family: "Helvetica Neue", sans-serif;
  font-size: 14px;
  color: #333333;
  margin-bottom: 15px;
}

.card-text {
  font-family: "Helvetica Neue", sans-serif;
  font-size: 16px;
  color: #333333;
  margin-bottom: 20px;
}

.btn-readmore {
  background-color: #00ff00;
  color: #ffffff;
  border-radius: 5px;
  padding: 10px 20px;
  transition: background-color 0.3s;
}

.btn-readmore:hover {
  background-color: #00cc00;
}

.pagination .page-link {
  border: none;
  color: #003366;
  font-family: "Helvetica Neue", sans-serif;
}

.pagination .page-link.active {
  background-color: #003366;
  color: #ffffff;
}

.pagination .page-link:hover {
  background-color: #008080;
}
```

### JS (if needed)

```javascript
// No JavaScript needed for this section functionality according to the design brief.
```