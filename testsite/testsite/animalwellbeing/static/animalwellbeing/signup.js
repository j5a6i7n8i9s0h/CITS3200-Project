function validateForm() 
//check fields must be filled in
//email must conform to regex format
//enforce password strength
{
	var validchars = /[^!#$%&'*+-/=?^_`{|}~]+/;
    var uname = document.forms["loginForm"]["Username"].value;
    if (uname == "") {
        alert("Userame must be filled out");
        return false;
    }
    if (validchars.test(uname)==false) {
	  alert("Userame must not contain special characters");
	  return false;
    }

    var fname = document.forms["loginForm"]["First_Name"].value;
    var lname = document.forms["loginForm"]["Surname"].value;
    if (fname == "" || lname == "") {
        alert("First and last name must be filled out");
        return false;
    }

    var emailpat = /[^!#$%&'*+-/=?^_`{|}~]+@[^!#$%&'*+-/=?^_`{|}~]+/;
    var email = document.forms["loginForm"]["Email"].value;
    if(emailpat.test(email)==false)
    {
    	alert("Email must be in the format 'examplename@examplehost");
    	return false;
    }

    var passlower = /[a-z]/g;
    var passupper = /[A-Z]/g;
    var passnumer = /[0-9]/g;
    var password = document.forms["loginForm"]["Password"].value;
    if(password.match(passlower)==null||password.match(passupper)==null||password.match(passnumer)==null||password.length<8)
    {
    	alert("Password must have minimum length of 8 characters and contain at least one lowercase letter, uppercase letter and one digit");
    	return false;
    }
}