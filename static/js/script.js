$(document).ready(function() {
    // alert auto show/hide
    $(".alert").first().hide().slideDown(500).delay(1500).slideUp(500, function() {
        $(this).remove();
    });
    // card flip
    $('.card').click(function() {
        $(this).toggleClass('flipped');
    });
    // tooltip
    $(document).ready(function() {
        $('[data-bs-toggle="tooltip"]').tooltip();
    });
    // validate dropdown
    /*    $("#category_name").validate({
            messages: {
                category_name: {
                    required: "Please select an option from the list, if none are appropriate please select 'Other'",
                },
            }
        });*/
});