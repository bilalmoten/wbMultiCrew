// Hero
$(document).ready(function() {
  $(".hero").on("mouseover", function() {
    $(this).addClass("hover");
  }).on("mouseout", function() {
    $(this).removeClass("hover");
  });
});

// About Us
// Add JS code for hover effects, scrolling animations, and fade-in effects if needed.

// Features

// Testimonials
// Add hover effect to testimonials
$('.testimonial').hover(function() {
  $(this).animate({
    'box-shadow': '0 0 20px rgba(0, 0, 0, 0.3)'
  }, 300);
}, function() {
  $(this).animate({
    'box-shadow': '0 0 10px rgba(0, 0, 0, 0.1)'
  }, 300);
});

// Contact Us
$(document).ready(function() {
    $('form').submit(function(e) {
        e.preventDefault();
        // form submission logic here
    });
});

