window.requestFileSystem = window.requestFileSystem || window.webkitRequestFileSystem;
var fs;
var uploadButton;
var generateTeams;
var sliders;
var generateGroupsButton;


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

  outputArea = document.querySelector('#outputArea')
  generateGroupsButton = document.querySelector('#generateGroupsButton')
  regenerateGroupsButton = document.querySelector('#regenerateGroupsButton')
  generateGroupsButton.addEventListener('click',function(){
    outputArea.style.display = 'block'
    generateGroupsButton.style.display = 'none'
    regenerateGroupsButton.style.display = 'block'
  }, false)
  /*sliders = document.querySelector('#sliders')
  uploadButton = document.querySelector('#uploadButton')
  uploadButton.addEventListener('click',function(){
    sliders.style.display = 'block'
  }, false)
  generateTeams = document.querySelector('#generateTeams')
  generateGroupsButton = document.querySelector('#generateGroupsButton')
  generateGroupsButton.addEventListener('click',function(){
    generateTeams.style.display = 'block'
  }, false)*/
}



document.addEventListener("DOMContentLoaded", function(event){
    setupElements();
});
