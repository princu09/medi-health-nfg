$('.day--btn').click(function () {
    $('.day--btn').addClass("data--active--btn");
    $('.week--btn').removeClass("data--active--btn");
    $('.month--btn').removeClass("data--active--btn");
    $('.year--btn').removeClass("data--active--btn");
});

$('.week--btn').click(function () {
    $('.week--btn').addClass("data--active--btn");
    $('.day--btn').removeClass("data--active--btn");
    $('.month--btn').removeClass("data--active--btn");
    $('.year--btn').removeClass("data--active--btn");
});

$('.month--btn').click(function () {
    $('.month--btn').addClass("data--active--btn");
    $('.day--btn').removeClass("data--active--btn");
    $('.week--btn').removeClass("data--active--btn");
    $('.year--btn').removeClass("data--active--btn");
});

$('.year--btn').click(function () {
    $('.year--btn').addClass("data--active--btn");
    $('.day--btn').removeClass("data--active--btn");
    $('.week--btn').removeClass("data--active--btn");
    $('.month--btn').removeClass("data--active--btn");
});