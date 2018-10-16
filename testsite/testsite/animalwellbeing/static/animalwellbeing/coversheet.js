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

	cell0.innerHTML += '<textarea class="scrit0" cols="30" rows="4" placeholder="Criteria Description" style="width:100%;"></textarea>';
	cell1.innerHTML += '<textarea class="scrit1" cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
	cell2.innerHTML += '<textarea class="scrit2" cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
	cell3.innerHTML+='<textarea class="scrit3" cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
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

	cell0.innerHTML += '<textarea class="pcrit0" cols="30" rows="4" placeholder="Criteria Description" style="width:100%;"></textarea>';
	cell1.innerHTML += '<textarea class="pcrit1" cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
	cell2.innerHTML += '<textarea class="pcrit2" cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
	cell3.innerHTML += '<textarea class="pcrit3" cols="30" rows="4" placeholder="Severity indicator description" style="width:100%;"></textarea>';
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