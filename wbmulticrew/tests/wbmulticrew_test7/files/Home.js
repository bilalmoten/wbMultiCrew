// Hero
$(document).ready(function() {
  $('a.nav-link').mouseenter(function() {
    $(this).addClass('hover');
  }).mouseleave(function() {
    $(this).removeClass('hover');
  });
  
  $('a.btn-primary').mouseenter(function() {
    $(this).addClass('hover');
  }).mouseleave(function() {
    $(this).removeClass('hover');
  });
  
  $('img.hero-image').fadeIn(2000);
  
  $('h1, .subheading').fadeIn(2000);
});

// What We Do
$(document).ready(function() {
    $(".cta").hover(function() {
        $(this).css("background-color", "#212121");
        $(this).css("color", "#03A9F4");
    }, function() {
        $(this).css("background-color", "#03A9F4");
        $(this).css("color", "#FFFFFF");
    });
});

// Book a Call
// Add hover effect to CTA button
$('.btn').hover(function() {
  $(this).css('background-color', '#212121');
}, function() {
  $(this).css('background-color', '#03A9F4');
});

// Add subtle animation to CTA button
$('.cta-section').css('transition', 'all 0.3s ease-in-out');

