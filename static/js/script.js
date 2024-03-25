$(document).ready(function () {
    // Open and close sublist menu accordions
    $('a.sub-menu').on("click", function (e) {
        $(this).next('div').toggle();
        $('.collapse').not($(this).next('div')).hide();
        e.preventDefault();
        e.stopPropagation();
    });

    // Back to Top Button
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

    // Product sort selector function
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
    });

    // Functions to handle enabling/disabling plus and minus basket item qty buttons
    function handleEnableDisable(itemId) {
        var currentVal = parseInt($(`#qty-${itemId}`).val());
        var minusDisabled = currentVal < 2;
        var plusDisabled = currentVal > 98;
        if (minusDisabled) {
            $(`#minus-${itemId}`).addClass('disabled');
        } else {
            $(`#minus-${itemId}`).removeClass('disabled');
        }
        if (plusDisabled) {
            $(`#plus-${itemId}`).addClass('disabled');
        } else {
            $(`#plus-${itemId}`).removeClass('disabled');
        }
    }

    var qtyInputs = $('.qty');
    for(var i = 0; i < qtyInputs.length; i++){
        var itemId = $(qtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }

    $('.qty').change(function() {
        var itemId = $(this).data('item_id');
        var closestInput = $(this).closest('.qty-group').find('.qty')[0];
        var currentVal = parseInt($(closestInput).val());
        if (currentVal < 1) {
            $(closestInput).val(1);
        } else if (currentVal > 99) {
            $(closestInput).val(99);
        }

        handleEnableDisable(itemId);
    });

    $('.minus').click(function(e) {
        e.preventDefault();
        var closestInput = $(this).closest('.qty-group').find('.qty')[0];
        var currentVal = parseInt($(closestInput).val());
        if (currentVal > 1) {
            $(closestInput).val(currentVal - 1);
        }
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    $('.plus').click(function (e) {
        e.preventDefault();
        var closestInput = $(this).closest('.qty-group').find('.qty')[0];
        var currentVal = parseInt($(closestInput).val());
        if (currentVal < 99) {
            $(closestInput).val(currentVal + 1);
        }
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Update basket item qty
    $('.update').click(function (e) {
        var form = $(this).closest('.update-form');
        form.submit();
    });

    // Toggle order history details
    $('.detail-toggle').click(function(e) {
        e.preventDefault();
        var details = $(this).closest('.order-line').find('.order-details')[0];
        $(details).toggleClass('hidden');
    });

    // Validate price field on product forms
    $('#id_price').change(function() {
        var price = $(this)
        var currentVal = parseInt($(price).val());
        if(currentVal < 0.5) {
            price.val(0.5)
        } else if(currentVal > 9999.99) {
            price.val(9999.99)
        }
    });

    // Handle link field required if button field populated
    // On edit post page load
    var button = $('#id_button')
    var buttonVal = button.val();

    if(buttonVal != '') {
        $('#id_link').attr('required', true);
        $('#div_id_link').find('label').text('Link*');
    } else {
        $('#id_link').attr('required', false);
        $('#div_id_link').find('label').text('Link');
    }
    // On update
    $('#id_button').change(function() {
        var button = $(this)
        var buttonVal = button.val();
        if(buttonVal != '') {
            $('#id_link').attr('required', true);
            $('#div_id_link').find('label').text('Link*');
        } else {
            $('#id_link').attr('required', false);
            $('#div_id_link').find('label').text('Link');
        }
    });
});