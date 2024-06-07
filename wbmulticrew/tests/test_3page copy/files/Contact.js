// Contact Information
$(document).ready(function() {
    $(window).on("scroll", function() {
        $(".cta-headline, .cta-subheadline, .btn-cta, .cta-image").each(function() {
            var offsetTop = $(this).offset().top;
            var scrollTop = $(window).scrollTop();
            if (scrollTop > (offsetTop - window.innerHeight + 100)) {
                $(this).addClass("scroll-trigger");
            }
        });

        $(".cta-image").hover(function(){
            $(this).toggleClass("scroll-zoom");
        });
    });
});

// Contact Form

// Call to Action
// Add any necessary JavaScript here

