//use better examples
//prevent file upload elsewhere
//make compilement faster?
//preview file?
//make it pretty
//add loading bar
//async def aqua
//add more compilement stats
//rename script.py?
//put info and link in a box?
//don't compress if already done?

const reader = new FileReader()

reader.onload = function(event) {

  dropZone.value = event.target;
  console.log(dropZone.value.result);

};

const dropZone = document.getElementById('aqua');
const display = document.getElementById('display');
const linkl = document.getElementById('linkl');
const link = document.getElementById('link');
const info = document.getElementById('info');
const button = document.getElementById('button');

dropZone.addEventListener('dragover', function(event) {
  event.preventDefault();
  dropZone.style.backgroundColor = '#1500b3';
});

dropZone.addEventListener('dragleave', function() {
  dropZone.style.backgroundColor = '#05002e';
});

dropZone.addEventListener('drop', function(event) {

  linkl.style.display = "none";

  document.styleSheets[0].insertRule(
    "#button:hover { background-color: #1500b3;}",
    document.styleSheets[0].cssRules.length);

  event.preventDefault();
  dropZone.style.backgroundColor = '#05002e';

  file = event.dataTransfer.files[0];
  console.log(file);
  dropZone.textContent = file.name;
  link.textContent = "pycompressed_" + file.name;
  link.download = link.textContent;

  reader.readAsText(file);

});