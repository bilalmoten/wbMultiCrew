// Mission and Values

// Innovative Work
// Smooth scrolling for internal links
$('a[href*="#"]').on('click', function (e) {
    e.preventDefault();

    $('html, body').animate(
        {
            scrollTop: $($(this).attr('href')).offset().top,
        },
        500,
        'linear'
    );
});

