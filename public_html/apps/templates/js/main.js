var MADLIB = MADLIB || {};

MADLIB = (function(){


	var init = function(){
		console.log("page loaded");

		parseLyrics();
		evtHandler();
	};


	



	//Event Handler
	function evtHandler(){
		jQuery('#madlib-input').submit(function(event){
			event.preventDefault();
			
			validateForm(jQuery(this));
		});
	}


	function validateForm(elem){
		//caching element selection for DOM seek efficiency
		// console.log(elem);	

		if (!jQuery('input[type=radio]').is(':checked')){
			alert("radio button not selected");
		}
		else{
			if (jQuery('#field-dropdown').val() == "-"){
				alert("please select a dropdown item");
			}
			else{
				renderOutput();
			}
		}

	}


	function renderOutput(){
		

		var formval = getFormVal();

		console.log(formval);

		jQuery('.val-teacher').each(function(){
			jQuery(this).html(formval.teachname);
		});

		jQuery('.val-favnum').each(function(){
			jQuery(this).html(formval.favnum);
		});
		jQuery('.val-favnumadd').each(function(){
			jQuery(this).html(formval.favnum*2 + 1);
		});
		jQuery('.val-petname').html(formval.petname);

		jQuery('.val-jamname').each(function(){
			jQuery(this).html(formval.jamname);
		});


		jQuery('#wrapper-story').fadeIn(200);
	}


	function getFormVal(){
		

		return {
			'teachname' : jQuery('#field-txt').val(),
			'favnum' :jQuery('#field-num').val(),
			'petname' :jQuery('input[type=radio]:checked').val(),
			'jamname' :jQuery('#field-dropdown').val()
		};

	}

	

	//to show prettier lyrics
	//I love this song. it deserves proper respect of being 
	//displayed right :)
	function parseLyrics(){
		
		jQuery('#wrapper-madlib p').each(function(){

			var lyric = jQuery(this).html();

			var re = new RegExp(",", 'g');

			newlyric = lyric.replace(re, "<br />");

			jQuery(this).html(newlyric);
		});
	}



	return {
		'init' : init
	};
})();


jQuery(document).ready(function(){
	MADLIB.init();
});