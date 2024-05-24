// Contact Form
$(document).ready(function(){
  $('#contactForm').on('submit', function(event){
    event.preventDefault();
    // Mock-ajax to simulate form submission
    $.ajax({
        url: '#',
        type: 'POST',
        data: $(this).serialize(),
        success: function(){
            $('.feedback-message').removeClass('error').addClass('success').text("Thank you for reaching out! We will get back to you soon.").fadeIn();
        },
        error: function(){
            $('.feedback-message').removeClass('success').addClass('error').text("There was an error submitting your form. Please try again.").fadeIn();
        }
    });
  });
});

// Contact Information
$(document).ready(function() {
    $('#contact-form').on('submit', function(event) {
        event.preventDefault();
        $('#thank-you-message').removeClass('d-none').fadeIn();
        $(this).trigger('reset');
    });

    function initMap() {
        var location = {lat: 40.712776, lng: -74.005974}; // Sample coordinates
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 14,
            center: location
        });
        var marker = new google.maps.Marker({
            position: location,
            map: map,
            icon: {
                url: "path/to/custom-map-marker.png",
                scaledSize: new google.maps.Size(40, 40) // Customize marker size
            }
        });
    }

    google.maps.event.addDomListener(window, 'load', initMap);
});

