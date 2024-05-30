## Team Introduction Section
### HTML

```html
<section id="team" class="pt-5">
    <div class="container">
        <div class="row">
            <div class="col-12 text-center mb-4">
                <h2 class="mb-1">Meet Our Team</h2>
                <p class="lead">Dedicated Professionals Pioneering Innovation in Cancer Treatment</p>
            </div>
        </div>
        <div class="row">
          <!-- John Doe -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="card team-member-card text-center h-100">
                    <img class="card-img-top" src="images/generated_image_Professional_headshot_of_a_male.jpg" alt="John Doe">
                    <div class="card-body">
                        <h5 class="card-title team-member-name">John Doe</h5>
                        <p class="card-subtitle mb-2 text-muted">Chief Executive Officer</p>
                        <p class="card-text">John Doe brings over 20 years of experience in the pharmaceutical industry. His visionary leadership and relentless pursuit of excellence are the cornerstones of our success.</p>
                    </div>
                </div>
            </div>
            <!-- Jane Smith -->
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="card team-member-card text-center h-100">
                    <img class="card-img-top" src="images/generated_image_Professional_headshot_of_a_female.jpg" alt="Jane Smith">
                    <div class="card-body">
                        <h5 class="card-title team-member-name">Jane Smith</h5>
                        <p class="card-subtitle mb-2 text-muted">Chief Scientific Officer</p>
                        <p class="card-text">Dr. Jane Smith leads our scientific team with unparalleled expertise and passion. Her innovative approach to cancer treatment has been pivotal in advancing our proprietary therapies.</p>
                    </div>
                </div>
            </div>
             <!-- Michael Brown -->
            <!-- Add other team members here with similar blocks... -->
        </div>
    </div>
</section>
```

### CSS

```css
#team {
    background-color: #f8f9fa;
}
.team-member-card {
    border: none;
    border-radius: 10px;
    transition: transform 0.3s, box-shadow 0.3s;
}
.team-member-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}
.team-member-card .card-img-top {
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
}
.team-member-name {
    color: #1E90FF;
    font-size: 1.25rem;
    font-weight: bold;
    transition: color 0.3s;
}
.team-member-card:hover .team-member-name {
    color: #20B2AA;
}
.card-subtitle {
    color: #696969;
    font-weight: medium;
}
.card-text {
    font-size: 0.9rem;
}
```

