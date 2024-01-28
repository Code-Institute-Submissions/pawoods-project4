$(document).ready(function () {
    $('a.sub-menu').on("click", function (e) {
        $(this).next('div').toggle();
        $('.collapse').not($(this).next('div')).hide();
        e.preventDefault();
        e.stopPropagation();
    });

    var $backToTop = $(".btt-btn");
    $backToTop.hide();
    $(window).on('scroll', function () {
        if ($(this).scrollTop() > 100) {
            $backToTop.fadeIn();
        } else {
            $backToTop.fadeOut();
        }
    });
    $backToTop.on('click', function (e) {
        $("html, body").animate({ scrollTop: 0 }, 500);
    });
});
