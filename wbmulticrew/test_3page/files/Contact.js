// Contact Information
$(document).ready(function(){
    $(window).on('scroll', function(){
        var scrolled = $(window).scrollTop();
        if ($('#cta-section').offset().top - $(window).height() < scrolled) {
            $('#cta-section .cta-content').fadeIn(800);
            $('#cta-section .cta-image img').css('transform', 'scale(1.1)').fadeIn(800);
        }
    });
});

// Contact Form
$(document).ready(function() {
  $('#cta-section').css('opacity', 0);
  $(window).on('scroll', function() {
    var scrollTop = $(this).scrollTop();
    var elementOffset = $('#cta-section').offset().top;
    var distance = elementOffset - scrollTop;
    var windowHeight = $(this).height();
    if (distance < windowHeight - 100) {
      $('#cta-section').animate({ 'opacity': 1 }, 1000);
    }
  });
});

// Call to Action
$(document).ready(function(){
    $('#call-to-action').fadeIn(1000);
});

