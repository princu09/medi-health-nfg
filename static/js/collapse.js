$('.collapse-btn').click(function () {
    $('.nav--menu').addClass("deactive");
    $('.collapse-btn-close').addClass("active");
});

$('.collapse-btn-close').click(function () {
    $('.nav--menu').removeClass("deactive");
    $('.collapse-btn-close').removeClass("active");
});