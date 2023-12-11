var filesel = document.getElementById("input");
var header = document.getElementById("header");
var content = document.getElementById("txt");
var btn = document.getElementById("btn");
var instruction = document.getElementById("instruction");

function getFileOnChange(){
	file.readAsText(this.files[0]);
    
	header.innerHTML = "Valgt fil: "+filesel.value;
	filesel.removeEventListener('change',getFileOnChange);
	filesel.style.display ="none";
    }
function readFileOnLoad(){
		textbuffer = file.result;
		
		file.removeEventListener('load',readFileOnLoad);
		instruction.innerHTML = "";
		btn.style.display = 'inline';
    }
	
function showFileContentOnKlikk(){
btn.removeEventListener('click',showFileContentOnKlikk);
content.innerHTML = textbuffer;
}
		
var textbuffer = "";
var file = new FileReader();
filesel.addEventListener('change',getFileOnChange);
file.addEventListener('load',readFileOnLoad);
btn.addEventListener('click',showFileContentOnKlikk);
btn.style.display = 'none';

var textbuffer;
document.getElementById('input')
    .addEventListener('change', function() {
      
    var fr=new FileReader();
    fr.onload=function(){
        textbuffer = fr.result;
    }      

    fr.readAsText(this.files[0]);
})
document.getElementById('btn')
    .addEventListener('click',function(){
document.getElementById('txt')
    .textContent = textbuffer})