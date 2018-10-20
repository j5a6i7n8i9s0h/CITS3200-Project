function add2string()
{
	let a = document.getElementsByClassName("addfield1");
	let b = document.getElementsByClassName("addfield2");
	let res = "";
	for(var i = 0; i < a.length; i++)
	{
		a[i].value.replace(/@|#/g,"");
		b[i].value.replace(/@|#/g,"");
		res+=a[i].value+"@"+b[i].value;
		if(i<a.length-1)
		{
			res+="#";
		}
		document.getElementById("additional-output").value = res;
	}
}
function string2add()
//takes the string that gets put in scrit-output and turns it back into cover sheet
//how about, wipe out the existing sarcrit table, then create new rows using existing functions
//then fill them in
{
	var x = document.getElementById("additional-output");
	let aar = x.value;//test
	let aar2 = aar.split("#");

	let a;
	let b;
	let temp;

	var atable = document.getElementById("asint");
	//first empty out addutuibak until only the headers remain
	//there's only one by default
	atable.deleteRow(6);
	for(var y=0;y<aar2.length;y++)
	{
		add3();
	}
	a = document.getElementsByClassName("addfield1");
	b = document.getElementsByClassName("addfield2");

	for(var i = 0; i < aar2.length; i++)
	{
		temp = aar2[i].split("@");
		a[i].value = temp[0];
		b[i].value = temp[1];
	}

}

function scrit2string()
//DOM the class of scrit
//scrit0 -> scrit3 are arrays of every row in the 4 columns, should be in order
//scrub them of our used characters
//add them into one string
{
	let s0 = document.getElementsByClassName("scrit0");
	let s1 = document.getElementsByClassName("scrit1");
	let s2 = document.getElementsByClassName("scrit2");
	let s3 = document.getElementsByClassName("scrit3");
	let res ="";

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
	let p0 = document.getElementsByClassName("pcrit0");
	let p1 = document.getElementsByClassName("pcrit1");
	let p2 = document.getElementsByClassName("pcrit2");
	let p3 = document.getElementsByClassName("pcrit3");
	let res ="";

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
	add2string();
}

function string2scrit()
//takes the string that gets put in scrit-output and turns it back into cover sheet
//how about, wipe out the existing sarcrit table, then create new rows using existing functions
//then fill them in
{
	var s = document.getElementById("scrit-output");
	let sar = s.value;
	//s.value="";
	let sar2 = sar.split("#");

	let s0;
	let s1;
	let s2;
	let s3;
	let temp;

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
	s0 = document.getElementsByClassName("scrit0");
	s1 = document.getElementsByClassName("scrit1");
	s2 = document.getElementsByClassName("scrit2");
	s3 = document.getElementsByClassName("scrit3");

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
	let par = p.value;
	//p.value="";
	let par2 = par.split("#");

	let p0;
	let p1;
	let p2;
	let p3;
	let temp;

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
	p0 = document.getElementsByClassName("pcrit0");
	p1 = document.getElementsByClassName("pcrit1");
	p2 = document.getElementsByClassName("pcrit2");
	p3 = document.getElementsByClassName("pcrit3");

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
	var a = document.getElementById("additional-output");
	if(a.value!="")
	{
		string2add();
	}
}
scheck();