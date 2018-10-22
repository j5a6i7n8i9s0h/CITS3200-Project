function validateForm(usernames) 
//check fields must be filled in
//email must conform to regex format
//enforce password strength
{
	var validchars = /[^!#$%&'*+-/=?^_`{|}~]+/;
    var uname = document.forms["signup"]["Username"].value;
    if (validchars.test(uname)==false) {
	  alert("Userame must not contain special characters");
	  return false;
    }
    let username; 
    for(username in usernames)
    {
        if(uname === usernames[username])
        {
            document.getElementById('username_error').style.display =  "block";
            return false;
        }
    }
    document.getElementById('username_error').style.display =  "none";
    let email = document.forms['signup']['Email'].value;
    let re = /\S+@\S+\.\S+/;
    if(!re.test(email))
    {
        document.getElementById('email_err').style.display =  "block";
        return false;
    }
    document.getElementById('email_err').style.display =  "none";
    var passlower = /[a-z]/g;
    var passupper = /[A-Z]/g;
    var passnumer = /[0-9]/g;
    var password = document.forms["signup"]["Password"].value;
    if(password.match(passlower)===null||password.match(passupper)===null||password.match(passnumer)===null||password.length<8)
    {
        document.getElementById('password_error').style.display =  "block";
        return false;
    }
    return true;
}