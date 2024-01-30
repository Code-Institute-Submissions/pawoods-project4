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

    $('#sort-selector').change(function() {
        var selector = $(this);
        var currentUrl = new URL(window.location);

        var selectedVal = selector.val();
        if(selectedVal != "reset"){
            var sort = selectedVal.split("_")[0];
            var direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort", sort);
            currentUrl.searchParams.selete("direction", direction);

            window.location.replace(currentUrl);
        }
    })
});
