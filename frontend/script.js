const BACKEND_ROUTE = `http://${location.host}:8000`;

function alteraNome(){
  let element = document.getElementById("nome");
  
  fetch(`${BACKEND_ROUTE}/name`, { 
    method: "GET" 
  })
  .then((data) => {
    return data.json(); 
  })
  .then((json) => {
    element.innerText = json.name;
  })
}

function insereNome(){
  let element = document.getElementById("nomeInput");
  
  let body = { "name": element.value };

  fetch(`${BACKEND_ROUTE}/name`, { 
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(body)
  })
  .then((data) => {
    return data.json(); 
  })
  .then((json) => {
    alert(json.message);
  })
}

