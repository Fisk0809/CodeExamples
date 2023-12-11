function getFileOnChange(){
	file.readAsText(this.files[0]);
	
	overskrift.innerHTML = "Valgt fil: "+filvalg.value;
	filvalg.removeEventListener('change',getFileOnChange);
	filvalg.style.display ="none";
    }
function readFileOnLoad(){
		textbuffer = file.result;
		
		file.removeEventListener('load',readFileOnLoad);
		instruksTilBruker.innerHTML = "";
		knapp.style.display = 'inline';
    }
	
function showFileContentOnKlikk(){
knapp.removeEventListener('click',showFileContentOnKlikk);
innhold.innerHTML = textbuffer;
}
		
//Hovedprogram:
var textbuffer = "";
var file = new FileReader();
filvalg.addEventListener('change',getFileOnChange);
file.addEventListener('load',readFileOnLoad);
knapp.addEventListener('click',showFileContentOnKlikk);
knapp.style.display = 'none';

