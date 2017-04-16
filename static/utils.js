window.requestFileSystem = window.requestFileSystem || window.webkitRequestFileSystem;
var fs;
var uploadButton;
var generateTeams;

function onInitFs(f){
    fs = f;
    console.log("DEBUG - Loaded a filesystem: " + fs.name);
}

function errorHandler(e) {
    console.log('DEBUG - Error: ' + e);
}

function setupElements(){
  generateTeams = document.querySelector('#generateTeams')
  uploadButton = document.querySelector('#uploadButton')
  uploadButton.addEventListener('click',function(){
    generateTeams.style.display = 'block'
  }, false)
}

document.addEventListener("DOMContentLoaded", function(event){
    setupElements();
});
