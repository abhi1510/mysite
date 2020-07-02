$(document).ready(() => {
    $('.nav-menu-toggle').click(() => {
        $('#sidebar').toggleClass('active');
        $('.nav-menu-toggle').toggleClass('active');
        $('.nav-menu-toggle i').toggleClass('bx-menu bx-window-close');
    });

    if ($('.typed').length) {
        var typed_strings = $(".typed").data('typed-items');
        typed_strings = typed_strings.split(',')
        new Typed('.typed', {
            strings: typed_strings,
            loop: true,
            typeSpeed: 100,
            backSpeed: 50,
            backDelay: 2000
        });
  }
});
