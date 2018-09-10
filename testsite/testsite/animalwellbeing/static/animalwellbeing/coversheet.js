function ifother()
{
   if(document.getElementById("typeofsheet").value=='Other')
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
	var b = document.getElementsByClassName("del2");
	var c = document.getElementsByClassName("del3");
	var i;
	for(i =0; i<a.length;i++)
	{
		//console.log("es");
		a[i].onclick = delete1;
	}
	for(i =0; i<b.length;i++)
	{
		//console.log("es");
		b[i].onclick = delete2;
	}
	for(i =0; i<c.length;i++)
	{
		//console.log("es");
		c[i].onclick = delete3;
	}
}
function delete1()
{
	var i = this.parentNode.parentNode.rowIndex;
	document.getElementById("sarcrit").deleteRow(i);
	delbutinit();
}

function delete2()
{
	var i = this.parentNode.parentNode.rowIndex;
	document.getElementById("pscrit").deleteRow(i);
	delbutinit();
}

function delete3()
{
	var i = this.parentNode.parentNode.rowIndex;
	document.getElementById("asint").deleteRow(i);
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

	cell0.innerHTML += '<textarea cols="30" rows="4" placeholder="Criteria Description" style="width:100%;"></textarea>';
	cell1.innerHTML += '<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
	cell2.innerHTML += '<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
	cell3.innerHTML+='<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
	cell4.innerHTML+='<input type="button" value="X" class="del1" style="margin: 0 auto;">';

	delbutinit()
	//console.log(srtable.rows.length);
}

function add2()
{
	var srtable = document.getElementById("pscrit");
	var srcrow = srtable.insertRow(-1);
	var cell0 = srcrow.insertCell(0);
	var cell1 = srcrow.insertCell(1);
	var cell2 = srcrow.insertCell(2);
	var cell3 = srcrow.insertCell(3);
	var cell4 = srcrow.insertCell(4);

	cell0.innerHTML += '<textarea cols="30" rows="4" placeholder="Criteria Description" style="width:100%;"></textarea>';
	cell1.innerHTML += '<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
	cell2.innerHTML += '<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
	cell3.innerHTML+='<textarea cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
	cell4.innerHTML+='<input type="button" value="X" class="del2" style="margin: 0 auto;">';

	delbutinit()
}

function add3()
{
	var srtable = document.getElementById("asint");
	var srcrow = srtable.insertRow(-1);
	var cell0 = srcrow.insertCell(0);
	var cell1 = srcrow.insertCell(1);
	var cell2 = srcrow.insertCell(2);

	cell0.innerHTML += '<textarea placeholder="Intervention description (e.g. Flystrike)" style="width:100%;"></textarea>';
	cell1.innerHTML += '<textarea style="width:100%;"></textarea>';
	cell2.innerHTML += '<input type="button" value="X" class="del3">';

	delbutinit()
}
document.getElementById("tempbutt").onclick = tempsel;
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