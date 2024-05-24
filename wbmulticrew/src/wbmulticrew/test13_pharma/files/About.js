// Company Overview
$(document).ready(function(){
    new WOW().init();
});

$(window).scroll(function() {
    if ($(this).scrollTop() > 50) {
        $('.navbar').addClass('solid');
    } else {
        $('.navbar').removeClass('solid');
    }
});

// Team

