$(document).ready(function(){
    $('#logBtn').click(function(){
        $('html, body').animate({
            scrollTop: $('#LogInPart').offset().top
        }, 750);
    });
});