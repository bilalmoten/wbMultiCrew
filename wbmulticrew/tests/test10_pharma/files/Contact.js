// Get in Touch
// Form validation and submission handling using jQuery
$("form").submit(function(event) {
  event.preventDefault();
  var name = $("#name").val();
  var email = $("#email").val();
  var phone = $("#phone").val();
  var message = $("#message").val();
  if (name == "" || email == "" || phone == "" || message == "") {
    alert("Please fill in all fields.");
  } else {
    // Use AJAX to submit the form data to the server
    $.ajax({
      type: "POST",
      url: "/contact',
      data: { name: name, email: email, phone: phone, message: message },
      success: function() {
        alert("Thank you for getting in touch!");
      }
    });
  }
});

// Contact Form
// No custom JS code is required for this section.

