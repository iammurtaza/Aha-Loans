// Material Bootstrap Wizard Functions
var searchVisible = 0;
var transparent = true;
var mobile_device = false;

$(document).ready(function(){

    $.material.init();
    /*  Activate the tooltips      */
    $('[rel="tooltip"]').tooltip();

    $.validator.addMethod("checkNumeric",function(value,element){
        var num=parseInt(value,10);
        if((/^\d+$/.test(value))&&(num>0)){
            return true;
        }
        else{
           // //alert("Please enter correct value(s)");
            return false;
        }
    },"Please enter correct value(s)");

    $.validator.addMethod("checkAlphabetOnlyforName",function(value,element){
       // console.log(value,"***************",element);
        if(/^[a-zA-Z]+$/.test(value)){
            return true;
        }
        else{
            //var $label = $("label[for='"+$(element).attr('id')+"']")
            //alert("Name must contain only alphabets");
            return false;}
    });
    $.validator.addMethod("checkDecimal",function(value,element){
       // console.log(value,"***************",element);
        if(/^\d+(\.\d{1,2})?$/.test(value)){
            return true;
        }
        else{
            //var $label = $("label[for='"+$(element).attr('id')+"']")
            //alert("Name must contain only alphabets");
            return false;}
    });
    $.validator.addMethod("checkAlphabetOnly",function(value,element){
       // console.log(value,"***************",element);
        if(/^[a-zA-Z\s]+$/.test(value)){
            return true;
        }
        else{
            //var $label = $("label[for='"+$(element).attr('id')+"']")
            //alert("Must contain only alphabets");
            return false;
        }
    });
    $.validator.addMethod("checkMorLname",function(value,element){
       // console.log(value,"***************",element);
        if (/^$/.test(value)){
            console.log("**");
            return true;

        }
        else if(/^[a-zA-Z]+$/.test(value)){
            return true;
        }
        else{
            //var $label = $("label[for='"+$(element).attr('id')+"']")
            //alert("Must contain only alphabets");
            return false;
        }
    });
    $.validator.addMethod("checkPAN",function(value,element){
        var regpan = /^([a-zA-Z]){5}([0-9]){4}([a-zA-Z]){1}?$/;
        if(regpan.test(value)&&value.length==10){
            return true;
        }
        else{
            //alert("Enter correct PAN number please");
            return false;
        }

    });

    $.validator.addMethod("checkContactNo",function(value,element){
        if (/^$/.test(value)){
            return true;
        }
        else if((/^\d{10}$/.test(value))){
            return true;
        }
        else{
            //alert("Enter correct Contact Number please");
            return false;
        }

    });
    $.validator.addMethod("checkAddress",function(value,element){
        var reg=/^[a-zA-Z0-9\s,.'-/\\\\]{3,}$/ ;

        if(reg.test(value)&&value.length>10){
            return true;
        }
        else{
            //alert("Enter correct address please");
            return false;
        }

    });
    $.validator.addMethod("checkPIN",function(value,element){
        var reg=/^[1-9][0-9]{5}$/ ;

        if(reg.test(value)&&value.length==6){
            return true;
        }
        else{
            ////alert("Enter correct PIN please");
            return false;
        }

    });
    $.validator.addMethod("checkAadhar",function(value,element){
        var reg=/^\d{12}$/ ;

        if(reg.test(value)&&value.length==12){
            return true;
        }
        else{
           // //alert("Enter correct Aadhaar Number please");
            return false;
        }

    });





    // Code for the Validator
     var $validator = $('.wizard-card form').validate({
		rules: {
		    AppliedLoanamount: {
		      required: true,
              checkNumeric:true,
		    },
		  Tenure: {
		      required: true,
              checkNumeric: true,
		    },
            loanPurpose: {
              required: true,
            },
            MonthlyObligation: {
              required: true,
              checkNumeric:true,
            },
            MobileNo:{
                required:true,
                checkContactNo:true,
            },
                
            PersonalEmailID: {
                required:true,
                email:true,
            },

            FName:{
                required:true,
                checkMorLname:true,
            },
            LName:{
                checkMorLname:true,
            },
            MName:{
                checkMorLname:true,

            },
            PAN:{
                required:true,
                checkPAN:true,
            },
            AadhaarNumber:{
                required:true,
                checkAadhar:true,
            },
            Gender:{
                required:true,
            },
            
            DOB:{
                required:true,
            },
            CurrentWorkExp:{
                required:true,
                checkNumeric:true,
                checkDecimal:true,
            },
            TotalWorkExp:{
                required:true,
                checkNumeric:true,
                checkDecimal:true,
            },
            CurrentAddress1:{
                required:true,
                checkAddress:true,
            },
            CurrentPin:{
                required:true,
                checkPIN:true,
                
            },
            CurrentCity:{
                required:true,
                checkAlphabetOnly:true,
                minlength:2,
            },
            CurrentState:{
                required:true,
                checkAlphabetOnly:true,
                minlength:2,
            },
            PermanentAddress1:{
                required:true,
                checkAddress:true,
            },
            PermanentPin:{
                required:true,
                checkPIN:true,
            },
            PermanentCity:{
                required:true,
                checkAlphabetOnly:true,
            },
            PermanentState:{
                required:true,
                checkAlphabetOnly:true,
            },
            ResidenceType:{
                required:true,
            },
            ResidenceStability:{
                required:true,
                checkNumeric:true,
            },
            Education:{
                required:true,
            },
            MaritalStatus:{
                required:true,
            },
            AlternateMobileNo:{
                checkContactNo:true,
            },
            AvgBankBalance:{
                required:true,
                checkDecimal:true,
            },
            CompanyState:{
                required:true,
                checkAlphabetOnly:true,
            },
            CompanyPin:{
                required:true,
                checkPIN:true,
            },
            CompanyAddress:{
                required:true,
                checkAddress:true,
            },
            ComapanyCity:{
                required:true,
            },
            OfficeEmailID:{
                required:true,
            },
            PermanentAddress:{
                checkAddress:true,
            },
            PermanentResidenceType:{
                required:true,
            },
            CompanyCity:{
                required:true,
                checkAlphabetOnly:true,
            }
        
        },
        messages: {
            txtLoanAmount:{
                checkNumeric:"Enter valid value(s)"
            },
        },

        errorPlacement: function(error, element) {
            $(element).parent('div').addClass('has-error');

         }
	}); 

    // Wizard Initialization
  	$('.wizard-card').bootstrapWizard({
        'tabClass': 'nav nav-pills',
        'nextSelector': '.btn-next',
        'previousSelector': '.btn-previous',

        onNext: function(tab, navigation, index) {
        	var $valid = $('.wizard-card form').valid();
            //console.log('XXXXXXXXXXXX',$valid);
        	if(!$valid) {
        		$validator.focusInvalid();
        		//console.log('YYYYYYYYYYY');
                return false;
        	}
        },

        onInit : function(tab, navigation, index){
            //check number of tabs and fill the entire row
            var $total = navigation.find('li').length;
            var $wizard = navigation.closest('.wizard-card');

            $first_li = navigation.find('li:first-child a').html();
            $moving_div = $('<div class="moving-tab">' + $first_li + '</div>');
            $('.wizard-card .wizard-navigation').append($moving_div);

            refreshAnimation($wizard, index);

            $('.moving-tab').css('transition','transform 0s');
       },

        onTabClick : function(tab, navigation, index){
            var $valid = $('.wizard-card form').valid();

            if(!$valid){
                return false;
            } else{
                return true;
            }
        },

        onTabShow: function(tab, navigation, index) {
            var $total = navigation.find('li').length;
            var $current = index+1;
			////alert($current);
            var $wizard = navigation.closest('.wizard-card');

            // If it's the last tab then hide the last button and show the finish instead
            if($current >= $total) {
                $($wizard).find('.btn-next').hide();
                $($wizard).find('.btn-finish').show();
            } else {
                $($wizard).find('.btn-next').show();
                $($wizard).find('.btn-finish').hide();
            }

            button_text = navigation.find('li:nth-child(' + $current + ') a span').html();
            navigation.find('li.active a i').html('lens');

            setTimeout(function(){
                $('.moving-tab').text(button_text);
            }, 150);

            var checkbox = $('.footer-checkbox');

            if( !index == 0 ){
                $(checkbox).css({
                    'opacity':'0',
                    'visibility':'hidden',
                    'position':'absolute'
                });
            } else {
                $(checkbox).css({
                    'opacity':'1',
                    'visibility':'visible'
                });
            }

            refreshAnimation($wizard, index);
        }
  	});


    // Prepare the preview for profile picture
    $(".wizard-picture").change(function(){ 
		var id = $(this).data('id');
        readURL(this, id);
    });

    $('[data-toggle="wizard-radio"]').click(function(){
        wizard = $(this).closest('.wizard-card');
        wizard.find('[data-toggle="wizard-radio"]').removeClass('active');
        $(this).addClass('active');
        $(wizard).find('[type="radio"]').removeAttr('checked');
        $(this).find('[type="radio"]').attr('checked','true');
    });

    $('[data-toggle="wizard-checkbox"]').click(function(){
        if( $(this).hasClass('active')){
            $(this).removeClass('active');
            $(this).find('[type="checkbox"]').removeAttr('checked');
        } else {
            $(this).addClass('active');
            $(this).find('[type="checkbox"]').attr('checked','true');
        }
    });

    $('.set-full-height').css('height', 'auto');

});



 //Function to show image before upload

function readURL(input, id) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#wizardPicturePreview'+id).attr('src', e.target.result).fadeIn('slow');
        }
        reader.readAsDataURL(input.files[0]);
    }
}

$(window).resize(function(){
    $('.wizard-card').each(function(){
        $wizard = $(this);

        index = $wizard.bootstrapWizard('currentIndex');
        refreshAnimation($wizard, index);

        $('.moving-tab').css({
            'transition': 'transform 0s'
        });
    });
});

function refreshAnimation($wizard, index){
    $total = $wizard.find('.nav li').length;
    $li_width = 100/$total;

    total_steps = $wizard.find('.nav li').length;
    move_distance = $wizard.width() / total_steps;
    index_temp = index;
    vertical_level = 0;

    mobile_device = $(document).width() < 600 && $total > 3;

    if(mobile_device){
        move_distance = $wizard.width() / 5;
        index_temp = index % 5;
        $li_width = 20;
    }

    $wizard.find('.nav li').css('width',$li_width + '%');

    step_width = move_distance;
    move_distance = move_distance * index_temp;

    $current = index + 1;

    if($current == 1 || (mobile_device == true && (index % 2 == 0) )){
        move_distance -= 8;
    } else if($current == total_steps || (mobile_device == true && (index % 2 == 1))){
        move_distance += 8;
    }

    if(mobile_device){
        vertical_level = parseInt(index / 5);
        vertical_level = vertical_level * 38;
    }

    $wizard.find('.moving-tab').css('width', step_width);
    $('.moving-tab').css({
        'transform':'translate3d(' + move_distance + 'px, ' + vertical_level +  'px, 0)',
        'transition': 'all 0.5s cubic-bezier(0.29, 1.42, 0.79, 1)'

    });
}

materialDesign = {

    checkScrollForTransparentNavbar: debounce(function() {
                if($(document).scrollTop() > 260 ) {
                    if(transparent) {
                        transparent = false;
                        $('.navbar-color-on-scroll').removeClass('navbar-transparent');
                    }
                } else {
                    if( !transparent ) {
                        transparent = true;
                        $('.navbar-color-on-scroll').addClass('navbar-transparent');
                    }
                }
        }, 17)

}

function debounce(func, wait, immediate) {
	var timeout;
	return function() {
		var context = this, args = arguments;
		clearTimeout(timeout);
		timeout = setTimeout(function() {
			timeout = null;
			if (!immediate) func.apply(context, args);
		}, wait);
		if (immediate && !timeout) func.apply(context, args);
	};
};
