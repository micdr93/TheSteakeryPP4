$(document).ready(function() {
    // Fade out any alert messages after 3 seconds
    setTimeout(function() {
      $('.alert').fadeOut('slow');
    }, 3000);
  });
  
  // Smooth scroll animation to "Menu" section
  $(document).ready(function () {
    // Smooth scroll to the Menu section when "Menu" link is clicked
    $(".menu-link").click(function (event) {
      event.preventDefault(); // Prevent default link behavior
  
      let menuSection = $("#menu-section"); // Ensure this ID matches your Menu section
      let targetUrl = $(this).data("target-url"); // Retrieve the target URL from data attribute
  
      // Check if the current page is the home page
      if (window.location.pathname === targetUrl) {
        // Scroll to the Menu section smoothly
        $('html, body').animate({
          scrollTop: menuSection.offset().top - 100  // Adjust -100 to match your header height
        }, 800);
      } else {
        // Redirect to the target URL and append the hash fragment
        window.location.href = targetUrl + "#menu-section";
      }
    });
  });
  