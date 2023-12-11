//De to funksjonene getFileOnChange()og readFileOnLoad()
//lar bruker velge fil og laster den inn i tekstbuffer.
function getFileOnChange(){
	var filnavn = filvalg.value;
	file.readAsText(this.files[0]);
	
	var filnavn = filvalg.value; 
	//Fjerner 'C:fakepath/' fra filnavnet
	var pos = filnavn.lastIndexOf('\\')+1; 
	filnavn = filnavn.substr(pos);
//filnavnet lagres i '<h3 id="overskrift"></h3> i htmldokumentet
	overskrift.innerHTML = "Valgt fil: "+filnavn;
//Slår av valgmulighet for fil.
	filvalg.removeEventListener('change',getFileOnChange);
	filvalg.style.display ="none";
    }
function readFileOnLoad(){
		textbuffer = file.result;
		
		file.removeEventListener('load',readFileOnLoad);
		instruksTilBruker.innerHTML = "";
		knapp.style.display = 'inline';
    }

//her hentes datasettet ut av filen	
function scanFileOnClick(){
	var tekstlinje = '';
	var lesFra = 0;//start på tekstlinje (tabellrad)første tegn
	var lesTil = 0;//Slutt på tekstlinje (posisjon til '\n' (linjeslutt))
	var endPos = textbuffer.length;//Lengde på tekstfil
	var ip = "";
	var ipArray =  [];
	var endIP = 0;
	var ipCount = [];
	var lineCount = 0;
	
	//starter på første tegn i fila
	while(lesFra < endPos){	
		//Finn hvor linjen slutter
		lesTil= textbuffer.indexOf('\n',lesFra);//finner linjeslutt
		tekstlinje = textbuffer.slice(lesFra,lesTil);//kopierer linje
	
		endIP = tekstlinje.indexOf(' ');//første tegn etter IP
		ip = tekstlinje.slice(0,endIP);//klipper ut ip fra tekstlinje
		if (ipArray.includes(ip)){//test om ip finnes fra før i array
			ipCount[ipArray.indexOf(ip)]++;	//teller opp ip
		}else{
			ipArray.push(ip);//registrerer første gangs forekomst				
			ipCount.push(1);//tell opp som nummer 1
		}

	lineCount ++;//ikke nødvendig
	lesFra = lesTil+1;//sette start neste linje
	
	}
	ipEl.value = ipArray;//array over i input i skjema
	countEl.value = ipCount;//samsvarende opptelling over i skjema
	IPskjema.submit();//sender skjema fra javascript og ikke input
}//slutt funksjon 

//main. Kjøres en gang ved lasting, venter så på hendelser.
//<tag></tag> objektvariable
var filvalg = document.getElementById("valg");
var overskrift = document.getElementById("valgtFil");
var innhold = document.getElementById("txt");
var knapp = document.getElementById("knapp");
var instruksTilBruker = document.getElementById("instruks");
var ipEl = document.getElementById('ip');
var countEl = document.getElementById('count');
var IPskjema = document.getElementById('IPskjema');

//globale data
var textbuffer = "";
var file = new FileReader();

//aktiverte hendelser
filvalg.addEventListener('change',getFileOnChange);
file.addEventListener('load',readFileOnLoad);
knapp.addEventListener('click',scanFileOnClick);
//css variable satt fra program
knapp.style.display = 'none';
//reset for nytt filvalg
filvalg.value = "";//blanker forige filvalg i tilfelle reload.
//venter på  at aktiverte hendelser oppstår.