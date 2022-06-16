$(document).ready(function() {
    // alert auto show/hide
    $(".alert").first().hide().slideDown(500).delay(1500).slideUp(500, function() {
        $(this).remove();
    });
    // tooltip
    $(document).ready(function() {
        $('[data-bs-toggle="tooltip"]').tooltip();
    });
    // comment modal
    $(document).ready(function() {
        $(".comment-btn").click(function() {
            $(".pop-outer").fadeIn("slow");
        });
        $(".btn-close").click(function() {
            $(".pop-outer").fadeOut("slow");
        });
    });
});