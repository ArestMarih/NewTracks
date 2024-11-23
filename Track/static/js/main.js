function closeForm() {
  document.getElementById("myForm").style.display = "none";
}
function openForm() {
  document.getElementById("myForm").style.display = "flex";
}

async function openEdit(id) {
  const r = await fetch(`http://127.0.0.1:8000/getQ/${id}/`);
  const json = await r.json();
  document.getElementById("form-edit").action = `edit/${json.q[0]["id"]}/`;

  document.getElementById("nameQu").value = `${json.q[0]["nameQu"]}`;
  document.getElementById("comments").value = `${json.q[0]["comments"]}`;
  document.getElementById("exp").value = `${json.q[0]["exp"]}`;

  document.getElementById("penis").style.display = "block";
}
function closeEdit() {
  document.getElementById("penis").style.display = "none";
}
