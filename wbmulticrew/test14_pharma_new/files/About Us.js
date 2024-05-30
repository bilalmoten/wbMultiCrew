// Company Overview
$("a[href^='#']").on('click', function (e) {
    e.preventDefault();
    var target = this.hash;
    $('html, body').animate({
        scrollTop: $(target).offset().top
    }, 800, function () {
        window.location.hash = target;
    });
});

// Team Introduction

// Company Overview
$("a[href^='#']").on('click', function (e) {
    e.preventDefault();
    var target = this.hash;
    $('html, body').animate({
        scrollTop: $(target).offset().top
    }, 800, function () {
        window.location.hash = target;
    });
});

// Team Introduction

