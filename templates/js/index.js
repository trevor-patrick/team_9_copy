var ;

$(document).ready(function(){
    $('#logBtn').click(function(){
        $('html, body').animate({
            scrollTop: $('#LogInPart').offset().top
        }, 750);
    });
    if ('speechSynthesis' in window) {
        /* speech synthesis supported */
        console.log('yes');
    }
    else {
        /* speech synthesis not supported */
        console.log('no');
    }
});