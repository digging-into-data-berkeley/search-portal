var KUHN = KUHN || {};


KUHN = (function(){

	var init = function(){
		console.log("page loaded");

		evtHandler();
		
	};



	function evtHandler(){
		jQuery('#card-input').submit(function(evt){

			evt.preventDefault();
			validateCard();
		});
	}


	function validateCard(){
		var cardval = jQuery('#field-num').val();

		var cardnum = [];

		var cardodd = [];
		var cardeven = [];

		checksum = 0;

		for (i=0; i< cardval.length; i++){
			// console.log(cardval[i]);
			cardnum[i] = parseInt(cardval[i], 10);

			console.log("i - i%2:", i+i%2);

			if (i%2 === 0){
				//odd digits because they start from 0
				cardodd.push(cardnum[i]);
				checksum = checksum + cardnum[i];
			}else{
				cardeven.push(cardnum[i]);
				checksum = checksum + (cardnum[i] * 2);
			}

		}

		if (checksum % 10 === 0){
			alert("valid card", checksum);
		}else{
			alert("invalid card", checksum);
		}

		
		
	}

	return {
		'init' : init
	};

})();


jQuery(document).ready(function(){
	KUHN.init();
});