/*
* This file is some simple javascript to run the UI and will be used in future
* versions of this project.
*
*/
window.requestFileSystem = window.requestFileSystem || window.webkitRequestFileSystem;
//This is for the filesystem
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
  /*
  * This whole block is so that we can create the button events in the
  * html UI.
  *
  */
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
}



document.addEventListener("DOMContentLoaded", function(event){
    //This executes it when the html loads.
    setupElements();
});
