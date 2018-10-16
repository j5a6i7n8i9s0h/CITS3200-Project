function checkboxchange()
{
   if(document.getElementById("other").checked)
   {
    document.getElementById("other_description").style.display = "block";
   }
   else
   {
    document.getElementById("other_description").style.display = "none";
   }
}

function delbutinit(){
	//since onclick doesn't work for passing instances of nodes, need to do this to set the event listeners whenever tables are modified
	var a = document.getElementsByClassName("del1");

	var i;
	for(i =0; i<a.length;i++)
	{
		//console.log("es");
		a[i].onclick = delete1;
	}

}
function delete1()
{
	var i = this.parentNode.parentNode.rowIndex;
	document.getElementById("sarcrit").deleteRow(i);
	delbutinit();
}


delbutinit();

function add1()
{
	var srtable = document.getElementById("sarcrit");
	var srcrow = srtable.insertRow(-1);
	var cell0 = srcrow.insertCell(0);
	var cell1 = srcrow.insertCell(1);
	var cell2 = srcrow.insertCell(2);
	var cell3 = srcrow.insertCell(3);
	var cell4 = srcrow.insertCell(4);

	cell0.innerHTML += '<textarea class="scrit0" cols="30" rows="4" placeholder="Criteria Description" style="width:100%;"></textarea>';
	cell1.innerHTML += '<textarea class="scrit1" cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
	cell2.innerHTML += '<textarea class="scrit2" cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
	cell3.innerHTML+='<textarea class="scrit3" cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
	cell4.innerHTML+='<input type="button" value="X" class="del1" style="margin: 0 auto;">';

	delbutinit()
	//console.log(srtable.rows.length);
}

//document.getElementById("tempbutt").onclick = tempsel;
function tempsel()
{
	var a = document.getElementById("template").value;
	var b;
	var i;
	//console.log(a);

	b = document.getElementById("sarcrit");
	//repopulate table with pre-defined elements
	//first: delete all heading rows
	for(i=b.rows.length-1;i>0;i--)
	{
		b.deleteRow(i);
	}
	//this deletes all rows larger than row 0

	if(a==0)//if mouse template selected
	{
		var srcrow1 = b.insertRow(-1);
		var cell0 = srcrow1.insertCell(0);
		var cell1 = srcrow1.insertCell(1);
		var cell2 = srcrow1.insertCell(2);
		var cell3 = srcrow1.insertCell(3);
		var cell4 = srcrow1.insertCell(4);
		cell0.innerHTML += '<textarea cols="30" rows="4" placeholder="Criteria Description" style="width:100%;">Activity – i.e. movement around the cageBright, Alert, Responsive (BAR)</textarea>';
		cell1.innerHTML += '<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;">Normal – mobile and active</textarea>';
		cell2.innerHTML += '<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;">Somewhat and/or intermittent stillness as compared to others</textarea>';
		cell3.innerHTML+='<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;">Will only move if approached or reluctant to move when touched.  Moderately reduced activity, dull, lethargic</textarea>';
		cell4.innerHTML+='<input type="button" value="X" class="del1" style="margin: 0 auto;">';

		var srcrow2 = b.insertRow(-1);
		cell0 = srcrow2.insertCell(0);
		cell1 = srcrow2.insertCell(1);
		cell2 = srcrow2.insertCell(2);
		cell3 = srcrow2.insertCell(3);
		cell4 = srcrow2.insertCell(4);
		cell0.innerHTML += '<textarea cols="30" rows="4" placeholder="Criteria Description" style="width:100%;">Body Posture</textarea>';
		cell1.innerHTML += '<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;">Normal</textarea>';
		cell2.innerHTML += '<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;">Somewhat and/or intermittent hunched appearance</textarea>';
		cell3.innerHTML+='<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;">Moderate/continuous hunching and still</textarea>';
		cell4.innerHTML+='<input type="button" value="X" class="del1" style="margin: 0 auto;">';

		var srcrow3 = b.insertRow(-1);
		cell0 = srcrow3.insertCell(0);
		cell1 = srcrow3.insertCell(1);
		cell2 = srcrow3.insertCell(2);
		cell3 = srcrow3.insertCell(3);
		cell4 = srcrow3.insertCell(4);
		cell0.innerHTML += '<textarea cols="30" rows="4" placeholder="Criteria Description" style="width:100%;">Social Behaviour (only relevant for group housed animals)</textarea>';
		cell1.innerHTML += '<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;">Normal</textarea>';
		cell2.innerHTML += '<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;">Somewhat or intermittently separate from others</textarea>';
		cell3.innerHTML+='<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;">Completely separate or isolated from others</textarea>';
		cell4.innerHTML+='<input type="button" value="X" class="del1" style="margin: 0 auto;">';
		delbutinit()
		//NOTE: In the final version this would be populated from templates stored in a model, obvs
	}
}

init();
function init()
{
	var a = document.getElementById("test");
	a.onclick=criteriaprocess;
}



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


function criteriaprocess()
{
	scrit2string();
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



function scheck()
{
	var s = document.getElementById("scrit-output");
	if(s.value!="")
	{
		string2scrit();
	}
}
//scheck();