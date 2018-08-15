$(document).ready(function() {
 
	$("#confirm-date").click(function () {
		$(".pres-details").toggle( "highlight" );			
	});
	
	$('#date').bootstrapMaterialDatePicker({
			time: false,
			clearButton: true
	});
	$('#date1').bootstrapMaterialDatePicker({
			time: false,
			clearButton: true
	});
	
	$("input[type='radio']").change(function () {
		var selection=$(this).val();
		//alert("Radio button selection changed. Selected: "+selection);
		if(selection == 1){
			$('.selected-duration').show();
			$('.selected-meds').hide();
		} else if(selection == 2){
			$('.selected-meds').show();
			$('.selected-duration').hide();
		} else if (selection == 0){
			$('.selected-duration').hide();
			$('.selected-meds').hide();
		} else {
			$('.selected-duration').hide();
			$('.selected-meds').hide();
		}
	});
	
	$("#address input[type='radio']").change(function () {
		var selection=$(this).val();
		//alert("Radio button selection changed. Selected: "+selection);
		if(selection == 0){
			$('.pick-up-pharmacy').show();
			$('.pick-up-pilbox').hide();
			$('.home-delivery').hide();
		} else if(selection == 1){
			$('.pick-up-pilbox').show();
			$('.pick-up-pharmacy').hide();
			$('.home-delivery').hide();
		} else if(selection == 2){
			$('.home-delivery').show();
			$('.pick-up-pharmacy').hide();
			$('.pick-up-pilbox').hide();
		}
	});

});

