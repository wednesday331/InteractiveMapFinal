function startTime() {
  var today = new Date();
  var h = today.getHours();
  var m = today.getMinutes();
  var s = today.getSeconds();
  var mo = today.getMonth()
  var day = today.getDate()
  var year = today.getFullYear()
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('txt').innerHTML ="Current Time in Massachusetts: "+"<b>"+ mo+"/"+ day+"/"+year +" " + h + ":" + m + ":" + s+"</b>";
  var t = setTimeout(startTime, 500);
}
function checkTime(i) {
  if (i < 10) {i = "0" + i};
  return i;
}

function countyfunction(County_Name) {
  if (County_Name === 'Berkshire') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementById('FIPScode').innerHTML= "003";
  document.getElementById('yearestablished').innerHTML= "1761";
  document.getElementById('population').innerHTML= "124,944"
  }
  else if (County_Name === 'Franklin') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementById('FIPScode').innerHTML= "011"
  document.getElementById('yearestablished').innerHTML= "1811"
  document.getElementById('population').innerHTML= "70,180"
  }
  else if (County_Name === 'Hampshire') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementById('FIPScode').innerHTML="015"
  document.getElementById('yearestablished').innerHTML="1662"
  document.getElementById('population').innerHTML="160,830"
  }
  else if (County_Name === 'Hampden') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementById('FIPScode').innerHTML="013"
  document.getElementById('yearestablished').innerHTML="1812"
  document.getElementById('population').innerHTML="466,372"
  }
  else if (County_Name === 'Worcester') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementById('FIPScode').innerHTML="027"
  document.getElementById('yearestablished').innerHTML="1731"
  document.getElementById('population').innerHTML="830,622"
  }
  else if (County_Name === 'Middlesex') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementById('FIPScode').innerHTML="017"
  document.getElementById('yearestablished').innerHTML="1643"
  document.getElementById('population').innerHTML="1,611,699"
  }
  else if (County_Name === 'Essex') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementById('FIPScode').innerHTML="009"
  document.getElementById('yearestablished').innerHTML="1643"
  document.getElementById('population').innerHTML="789,034"
  }
  else if (County_Name === 'Suffolk') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementById('FIPScode').innerHTML="025"
  document.getElementById('yearestablished').innerHTML="1643"
  document.getElementById('population').innerHTML="803,907"
  }
  else if (County_Name === 'Norfolk') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementsByClassName('FIPScode').innerHTML="021"
  document.getElementsByClassName('yearestablished').innerHTML="1793"
  document.getElementsByClassName('population').innerHTML="706,775"
  }
  else if (County_Name === 'Plymouth') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementById('FIPScode').innerHTML="023"
  document.getElementById('yearestablished').innerHTML="1685"
  document.getElementById('population').innerHTML="521,202"
  }
  else if (County_Name === 'Bristol') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementById('FIPScode').innerHTML="005"
  document.getElementById('yearestablished').innerHTML="1685"
  document.getElementById('population').innerHTML="565,217"
  }
  else if (County_Name === 'Barnstable') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementById('FIPScode').innerHTML="001"
  document.getElementById('yearestablished').innerHTML="1685"
  document.getElementById('population').innerHTML="212,990"
  }
  else if (County_Name === 'Dukes') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementById('FIPScode').innerHTML="007"
  document.getElementById('yearestablished').innerHTML="1695"
  document.getElementById('population').innerHTML="17,332"
  }
  else if (County_Name === 'Nantucket') {
  document.getElementById('exampleModalLongTitle').innerHTML= County_Name + " County"
  document.getElementById('FIPScode').innerHTML="019"
  document.getElementById('yearestablished').innerHTML="1695"
  document.getElementById('population').innerHTML="11,399"
  }

  var x = document.getElementById("linktopage");
  x.href = "countyinformation/"+County_Name+"";

}
