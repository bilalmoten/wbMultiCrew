// Latest News
$('document').ready(function(){
    $('a.read-more-btn').on('click', function(e){
        e.preventDefault();
        let anchor = $(this).attr('href');
        $('html, body').animate({
            scrollTop: $(anchor).offset().top
        }, 800);
    });
});

// Press Releases
// No JavaScript needed for this section functionality according to the design brief.

