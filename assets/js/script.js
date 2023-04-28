$(document).ready(function() {
  // URL de la API
  var url = "https://digimon-api.vercel.app/api/digimon";

  // Elemento <ul> donde se mostrarán los datos
  var listaDatos = $("#lista-datos");

  // Petición a la API con jQuery
  $.getJSON(url, function(data) {
    // Iterar sobre los datos y generar el HTML correspondiente
    $.each(data, function(index, item) {
      var li = $("<li>").addClass("dato").appendTo(listaDatos);
      $("<h3>").text(item.name).appendTo(li);
      $("<p>").text(item.level).appendTo(li);
      $("<img>").attr("src", item.img).appendTo(li);
    });
  });
});

var url = "https://digimon-api.vercel.app/api/digimon"

var contenido = document.querySelector("#contenido")

fetch(url)
.then(response => response.json())
.then(datos => {
    console.log(datos)

    for (item of datos){

    contenido.innerHTML += `
    
<div class="tarjeta">
        <div class="card" style="width: 18rem;">
        <img src="${item.img}" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">${item.name}</h5>
          <p class="card-text">${item.level}</p>
          <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
        </div>
    </div>    
    `

}

})



function searchDigimon() {
    
var searchTerm = searchInput.value.toLowerCase();
    
fetch('https://digimon-api.vercel.app/api/digimon')
  .then(response => response.json())
  .then(datos => {

var filteredData = datos.filter(function (digimon) {
  return digimon.name.toLowerCase().includes(searchTerm);
            });

tabla(filteredData);
        });
}
