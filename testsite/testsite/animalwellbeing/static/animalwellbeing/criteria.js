function scrit2string()
//DOM the class of scrit
//scrit0 -> scrit3 are arrays of every row in the 4 columns, should be in order
//scrub them of our used characters
//add them into one string
{
	var s0 = document.getElementsByClassName("scrit0");
	var s1 = document.getElementsByClassName("scrit1");
	var s2 = document.getElementsByClassName("scrit2");
	var s3 = document.getElementsByClassName("scrit3");
	var res ="";

	//scrub them and add them using separator char 1=@
	//add the rows together using separator char 2=#
	for(var i = 0; i < s0.length; i++)
	{
		s0[i].value.replace(/@|#/g,"");
		s1[i].value.replace(/@|#/g,"");
		s2[i].value.replace(/@|#/g,"");
		s3[i].value.replace(/@|#/g,"");
		res+=s0[i].value+"@"+s1[i].value+"@"+s2[i].value+"@"+s3[i].value;
		if(i<s0.length-1)
		{
			res+="#";
		}
		//so it will look like "part1@part2@part3@part4#part1@part2@part3@part4" etc
	}
	//output this variable on a hidden textarea that will be passed to the model
	document.getElementById("scrit-output").value = res;
	//and now this field is accessible by the server backend
}
function pcrit2string()
//DOM the class of scrit
//scrit0 -> scrit3 are arrays of every row in the 4 columns, should be in order
//scrub them of our used characters
//add them into one string
{
	var p0 = document.getElementsByClassName("pcrit0");
	var p1 = document.getElementsByClassName("pcrit1");
	var p2 = document.getElementsByClassName("pcrit2");
	var p3 = document.getElementsByClassName("pcrit3");
	var res ="";

	//scrub them and add them using separator char 1=@
	//add the rows together using separator char 2=#
	for(var i = 0; i < p0.length; i++)
	{
		p0[i].value.replace(/@|#/g,"");
		p1[i].value.replace(/@|#/g,"");
		p2[i].value.replace(/@|#/g,"");
		p3[i].value.replace(/@|#/g,"");
		res+=p0[i].value+"@"+p1[i].value+"@"+p2[i].value+"@"+p3[i].value;
		if(i<p0.length-1)
		{
			res+="#";
		}
	}
	document.getElementById("pcrit-output").value = res;
}

function criteriaprocess()
{
	scrit2string();
	pcrit2string();
}

function string2scrit()
//takes the string that gets put in scrit-output and turns it back into cover sheet
//how about, wipe out the existing sarcrit table, then create new rows using existing functions
//then fill them in
{
	var s = document.getElementById("scrit-output");
	var sar = s.value;
	//s.value="";
	var sar2 = sar.split("#");

	var s0;
	var s1;
	var s2;
	var s3;
	var temp;

	var srtable = document.getElementById("sarcrit");
	//first empty out sarcrit until only the headers remain
	for(var v=srtable.rows.length-1;v>0;v--)
	{
		srtable.deleteRow(v);
	}
	for(var b=0;b<sar2.length;b++)
	{
		add1();
	}
	var s0 = document.getElementsByClassName("scrit0");
	var s1 = document.getElementsByClassName("scrit1");
	var s2 = document.getElementsByClassName("scrit2");
	var s3 = document.getElementsByClassName("scrit3");

	for(var i = 0; i < sar2.length; i++)
	{
		temp = sar2[i].split("@");
		s0[i].value = temp[0];
		s1[i].value = temp[1];
		s2[i].value = temp[2];
		s3[i].value = temp[3];
	}

}


function string2pcrit()
//takes the string that gets put in scrit-output and turns it back into cover sheet
//how about, wipe out the existing sarcrit table, then create new rows using existing functions
//then fill them in
{
	var p = document.getElementById("pcrit-output");
	var par = p.value;
	//p.value="";
	var par2 = par.split("#");

	var p0;
	var p1;
	var p2;
	var p3;
	var temp;

	var prtable = document.getElementById("pscrit");
	//first empty out sarcrit until only the headers remain
	for(var v=prtable.rows.length-1;v>0;v--)
	{
		prtable.deleteRow(v);
	}
	for(var b=0;b<par2.length;b++)
	{
		add2();
	}
	var p0 = document.getElementsByClassName("pcrit0");
	var p1 = document.getElementsByClassName("pcrit1");
	var p2 = document.getElementsByClassName("pcrit2");
	var p3 = document.getElementsByClassName("pcrit3");

	for(var i = 0; i < par2.length; i++)
	{
		temp = par2[i].split("@");
		p0[i].value = temp[0];
		p1[i].value = temp[1];
		p2[i].value = temp[2];
		p3[i].value = temp[3];
	}

}


function scheck()
{
	var s = document.getElementById("scrit-output");
	if(s.value!="")
	{
		string2scrit();
	}
	var p = document.getElementById("pcrit-output");
	if(p.value!="")
	{
		string2pcrit();
	}
}
scheck();