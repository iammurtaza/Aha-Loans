
 function validate_loan_details(){
    var txtLoanAmount = document.forms["myform"]["txtLoanAmount"];              
    var txtLoanTenure = document.forms["myform"]["txtLoanTenure"];   
    var loanPurpose = document.forms["myform"]["loanPurpose"]; 
    var MonthlyObligation =  document.forms["myform"]["MonthlyObligation"]; 
    
    if (txtLoanAmount.value == ""|| parseFLoat(txtLoanAmount)<0 )                                 
    {
        window.alert("Please enter correct values");
        name.focus();
        return false;
    }
  
    if (txtLoanTenure.value == ""|| parseFLoat(txtLoanTenure)<0)                              
    {
        window.alert("Please enter correct values");
        name.focus();
        return false;
    }
      
    
    if (loanPurpose.selectedIndex < 1)                 
    {
        alert("Please enter the purpose of your loan");
        loanPurpose.focus();
        return false;
    }

    
    if (MonthlyObligation.value == ""|| parseFLoat(MonthlyObligation)<0 )                                 
    {
        window.alert("Please enter correct values");
        name.focus();
        return false;
    }
  
  
  
    return true;
}

function validate_personal_details(){                             
    var fname = document.forms["myform"]["FName"];
    var mname = document.forms["myform"]["MName"];              
    var lname = document.forms["myform"]["LName"];

    var email = document.forms["myform"]["PersonalEmailID"];

    var phone1 = document.forms["myform"]["MobileNo"];
    var phone2 = document.forms["myform"]["AlternateMobileNo"];

    var PAN =document.forms["myform"]["PAN"];
    var adhar=document.forms["myform"]["AadhaarNumber"];

    var gender =  document.forms["myform"]["Gender"]; 
     
    var edu = document.forms["myform"]["Education"]; 
  
    if (fname.value == ""||)                                 
    {
        window.alert("Please enter your first name.");
        fname.focus();
        return false;
    }
  
    if (address.value == "")                              
    {
        window.alert("Please enter your address.");
        name.focus();
        return false;
    }
      
    if (email.value == "")                                  
    {
        window.alert("Please enter a valid e-mail address.");
        email.focus();
        return false;
    }
  
    if (email.value.indexOf("@", 0) < 0)                
    {
        window.alert("Please enter a valid e-mail address.");
        email.focus();
        return false;
    }
  
    if (email.value.indexOf(".", 0) < 0)                
    {
        window.alert("Please enter a valid e-mail address.");
        email.focus();
        return false;
    }
  
    if (phone.value == "")                          
    {
        window.alert("Please enter your telephone number.");
        phone.focus();
        return false;
    }
  
    if (password.value == "")                       
    {
        window.alert("Please enter your password");
        password.focus();
        return flase;
    }
  
    if (what.selectedIndex < 1)                 
    {
        alert("Please enter your course.");
        what.focus();
        return false;
    }
  
    return true;
}
}