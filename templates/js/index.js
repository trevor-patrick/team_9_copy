var lang;

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

    reSizeSumBoxes();
});

$(window).resize(function(){
    reSizeSumBoxes();
});

/* UI Experience */
//Makes every sumBox in the same row the same height
function reSizeSumBoxes() {
    $('#navRow1').css('width', ''); 
    $('#navRow2').css('width', ''); 

    if($('#navRow1').css('width') > $('#navRow2').css('width'))
    {
        $('#navRow2').css('width', $('#navRow1').css('width'));
    }

    //$('#content').css('min-height','calc(100% - 96px);');
}