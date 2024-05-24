// Hero Section
// No JavaScript code required for this section

// About Us
// No JS code needed for this section

// Call to Action
$('.learn-more-btn').on('click', function() {
  $(this).addClass('clicked');
  setTimeout(function() {
    $(this).removeClass('clicked');
  }, 500);
});

