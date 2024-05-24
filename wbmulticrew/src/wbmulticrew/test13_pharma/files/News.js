// News and Updates
$(document).ready(function() {
  function onElementVisibilityChange(el, callback, offset) {
    var callback_invoked = false;

    function checkVisibility() {
      const rect = el.getBoundingClientRect();
      const windowHeight = window.innerHeight || document.documentElement.clientHeight;

      if ((rect.top <= windowHeight - offset) && rect.bottom >= 0) {
        if (!callback_invoked) {
          callback_invoked = true;
          callback(el);
        }
      }
    }

    document.addEventListener('scroll', checkVisibility);
    window.addEventListener('resize', checkVisibility);
    checkVisibility();
  }

  const newsCards = document.querySelectorAll('.news-card');
  newsCards.forEach(card => {
    onElementVisibilityChange(card, (el) => {
      $(el).css({opacity: 0, transform: 'translateY(50px)'}).animate({opacity: 1, transform: 'translateY(0)'}, 1000);
    }, 150);
  });
});

