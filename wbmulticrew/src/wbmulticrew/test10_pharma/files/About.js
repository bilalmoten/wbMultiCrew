// Company History
// No JS code is needed for this section.

// Mission
// Add hover effects and fade-in animations using jQuery
$(document).ready(function() {
  $(".value").hover(function() {
    $(this).css("background-color", "#f2f2f2");
  }, function() {
    $(this).css("background-color", "#fff");
  });
  
  $(".value").fadeTo(1000, 1);
});

// Values
$(document).ready(function() {
  $(".value-box").hover(function() {
    $(this).css("background-color", "#8bc34a");
  }, function() {
    $(this).css("background-color", "#fff");
  });
});

// Team

