// Hero Section
$(document).ready(function(){
    $('.content').hide().fadeIn(2000);
});

// Mission and Vision

// Innovative Work

// Call-to-Action
$(document).ready(function() {
  $("a").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
        window.location.hash = hash;
      });
    }
  });
});

