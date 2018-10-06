var lang;
var flag = false;
var utterance;
var synth;

$(document).ready(function(){
    $('#logBtn').click(function(){
        $('html, body').animate({
            scrollTop: $('#LogInPart').offset().top
        }, 750);
    });
    synth = speechSynthesis;
    if ('speechSynthesis' in window) {
        /* speech synthesis supported */
        console.log('yes');
    }
    else {
        /* speech synthesis not supported */
        console.log('no');
    }

    if(window.innerWidth < 992)
        reSizeSumBoxes();

	$('#click').click(function(){
		console.log('click has been clicked');
		if(!flag){
	       		flag = true;
	       		utterance = new SpeechSynthesisUtterance(
		     	document.getElementById('welcome').textContent);
	       		utterance.voice = synth.getVoices()[-70];
	       		utterance.onend = function(){
		   		flag = false;
       			};
       			synth.speak(utterance);
   		}	
	});

	
	$('#click2').click(function(){
		console.log('click has been clicked');
		if(!flag){
	       		flag = true;
	       		utterance = new SpeechSynthesisUtterance(
		     	document.getElementById('mission').textContent+"..."+document.getElementById('statement').textContent);
	       		utterance.voice = synth.getVoices()[-70];
	       		utterance.onend = function(){
		   		flag = false;
       			};
       			synth.speak(utterance);
   		}	
	});

});

$(window).resize(function(){
    if(window.innerWidth < 992)
        reSizeSumBoxes();
    else
        $('#navRow2').css('width', '100%');
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
