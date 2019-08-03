
  // Smooth scrolling using jQuery easing
  
  // Activate scrollspy to add active class to navbar items on scroll
  
  $( document ).ready(function() {

  

    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function(event) {
      event.preventDefault();

      if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
          $('html,body').animate({
            scrollTop: (target.offset().top - 56)
          }, 1000, "easeInOutExpo");
          
          
        }
      }
    });
});