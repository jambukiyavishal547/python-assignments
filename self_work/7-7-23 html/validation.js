function checkfname() {
			var f=document.frm.fname.value;
			var reg=/^[A-Za-z]+$/;
			if(f=="")
			{
				document.getElementById("fname").innerHTML="Please Enter First Name";
			}
			else if(!reg.test(f))
			{
				document.getElementById("fname").innerHTML="Please Enter Alpha Only";
			}
			else
			{
				document.getElementById("fname").innerHTML="";	
			}
		}
		function checklname() {
			var f=document.frm.lname.value;
			var reg=/^[A-Za-z]+$/;
			if(f=="")
			{
				document.getElementById("lname").innerHTML="Please Enter Last Name";
			}
			else if(!reg.test(f))
			{
				document.getElementById("lname").innerHTML="Please Enter Last Only";
			}
			else
			{
				document.getElementById("lname").innerHTML="";	
			}
		}
		function checkemail() {
			var f=document.frm.email.value;
			var reg=/^[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]{2,4}$/;
			if(f=="")
			{
				document.getElementById("email").innerHTML="Please Enter Email";
			}
			else if(!reg.test(f))
			{
				document.getElementById("email").innerHTML="Please Enter Valid Email";
			}
			else
			{
				document.getElementById("email").innerHTML="";	
			}
		}
		function checkmobile() {
			var f=document.frm.Mobile.value;
			var reg=/^\d{10}$/;
			if(f=="")
			{
				document.getElementById("Mobile").innerHTML="Please Enter Mobile Number";
			}
			else if(!reg.test(f))
			{
				document.getElementById("Mobile").innerHTML="Please Enter Valid Number";
			}
			else
			{
				document.getElementById("Mobile").innerHTML="";
			}
		}
		function checkpassword() {
			var f=document.frm.password.value;
			var reg=/ ^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
			if(f=="")
			{
				document.getElementById("password").innerHTML="Plaese Enter password";
			}
			else if(!reg.test(f))
			{
				document.getElementById("password").innerHTML="Entered password Is Not Valid ";
			}
			else
			{
				document.getElementById("password").innerHTML="";
			}
		}
		function matchPassword() 
		{  
  			/*var pw1 = document.getElementById("password");  
  			var pw2 = document.getElementById("c_password");  
  			if(pw1 != pw2)  
  			{   
    			alert("Passwords did not match");  
  			} else{  
    			alert("Password created successfully");  
  				 } */
  			var f=document.frm.password.value;
  			var g=document.frm.c_password.value;
  			if (g=="")
  			{
  				document.getElementById("c_password").innerHTML="Please Enter Confirm Password";
  			}
  			else if(f!=g)
  			{
  				document.getElementById("c_password").innerHTML="Password Is Not Match";
  			}
  			else
  			{
  				document.getElementById("c_password").innerHTML="";
  			}
		} 