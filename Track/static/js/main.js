function closeForm() {
  document.getElementById("myForm").style.display = "none";
  document.getElementById("a").style.filter = "blur(0)";
}
function openForm() {
  document.getElementById("myForm").style.display = "flex";
  document.getElementById("a").style.filter = "blur(10px)";
}

function closeAddF() {
  document.getElementById("AddFinance").style.display = "none";
  document.getElementById("a").style.filter = "blur(0)";
}
function openAddF() {
  document.getElementById("AddFinance").style.display = "flex";
  document.getElementById("a").style.filter = "blur(10px)";
}

function closeAddCat() {
  document.getElementById("AddCat").style.display = "none";
  document.getElementById("a").style.filter = "blur(0)";
}
function openAddCat() {
  document.getElementById("AddCat").style.display = "flex";
  document.getElementById("a").style.filter = "blur(10px)";
}

async function openEdit(id) {
  const r = await fetch(`http://127.0.0.1:8000/getQ/${id}/`);
  const json = await r.json();
  document.getElementById("form-edit").action = `edit/${json.q[0]["id"]}/`;

  document.getElementById("nameQu").value = `${json.q[0]["nameQu"]}`;
  document.getElementById("comments").value = `${json.q[0]["comments"]}`;
  document.getElementById("exp").value = `${json.q[0]["exp"]}`;
  document.getElementById("a").style.filter = "blur(10px)";
  document.getElementById("penis").style.display = "block";
}
function closeEdit() {
  document.getElementById("a").style.filter = "blur(0)";
  document.getElementById("penis").style.display = "none";
}


function showBlock(val){
  document.getElementById('id1').style.display='none';
  document.getElementById('id2').style.display='none';
  document.getElementById('id3').style.display='none';
  document.getElementById('id'+val).style.display='block';
}
