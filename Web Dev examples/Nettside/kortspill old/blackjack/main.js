var type = ["Spar", "Hjerter", "Ruter", "Kløver", "Spar", "Hjerter", "Ruter", "Kløver"];
var tall = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dronning", "Konge", "Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dronning", "Konge", "Ess"];  
var kortstokk = new Array();
var poengsum = 0
var dealersum = 0
var spillerbunke = []
var dealerbunke = []
var as = {}
// Create WebSocket connection.
const socket = new WebSocket('ws://localhost:8080');

// Connection opened
socket.addEventListener('open', function (event) {
    socket.send('Hello Server!');
});

// Listen for messages
socket.addEventListener('message', function (event) {
    console.log('Message from server ', event.data);
});

function lagStokk()
{
    kortstokk = new Array();
    for (var i = 0 ; i < tall.length; i++)
    {
        for (var x = 0; x < type.length; x++)
        {
            var verdi = parseInt(tall[i]);
            if (tall[i] == "Knekt" || tall[i] == "Dronning" || tall[i] == "Konge")
                verdi = 10;
            if (tall[i] == "Ess")
                verdi = 11;
            var kort = " " + type[x] + " " + tall[i];
            kortstokk.push(kort);
        }
    }
}

function stokke() {
    for (var i = 0; i < 1000; i++) {
        var l1 = Math.floor((Math.random() * kortstokk.length));
        var l2 = Math.floor((Math.random() * kortstokk.length));
        var tmp = kortstokk[l1];

        kortstokk[l1] = kortstokk[l2]
        kortstokk[l2] = tmp;
    }
}

function lagSpillere() {
    
    for (var i = 0; i < as.antallspillere; i++) {
        console.log("filip er taper")
    }
}



function startspill() {
    document.getElementById('btnStart').value = 'Restart';
    document.getElementById("game").style.display="block";
    document.getElementById("blackjack").style.display="none";
    document.getElementById("taper").style.display="none";
    document.getElementById("vant").style.display="none";
    as.antallspillere = document.getElementById("sa").value;

    dealersum = 0
    dealerbunke = [];
    console.log(as.antallspillere)
    lagStokk();
    stokke();
    lagSpillere();
    // giKort();
    // dealer();
}

// function giKort() {
//     var kort = kortstokk.pop();
//     spillerbunke.push(kort);
//     if (kort.includes("Knekt") == true || kort.includes("Dronning") == true || kort.includes("Konge") == true) {
//         poengsum += 10
//     } else if (kort.includes("Ess") == true) {
//         poengsum+= 11 
//     } else {
//         var korttall = kort.replace( /^\D+/g, '');
//         poengsum += parseInt(korttall)
//     }
//     let sb = spillerbunke.toString();
//     document.getElementById("spillerbunke").innerHTML = sb;
//     document.getElementById("poengsum").innerHTML = poengsum;
//     if (poengsum > 21) {
//         tapt()
//     } else if (poengsum == 21) {
//         blackjack()
//     }
// }

function hitMe() {
    var kort = kortstokk.pop();
    spillerbunke.push(kort);
    if (kort.includes("Knekt") == true || kort.includes("Dronning") == true || kort.includes("Konge") == true) {
        poengsum += 10
    } else if (kort.includes("Ess") == true) {
        poengsum+= 11
    } else {
        var korttall = kort.replace( /^\D+/g, '');
        poengsum += parseInt(korttall)
    }
    let sb = spillerbunke.toString();
    document.getElementById("spillerbunke").innerHTML = sb;
    document.getElementById("poengsum").innerHTML = poengsum;
    dealer();
}

function stay() {

}

function dealer() {
    var kort = kortstokk.pop();
    dealerbunke.push(kort);
    if (kort.includes("Knekt") == true || kort.includes("Dronning") == true || kort.includes("Konge") == true) {
        dealersum += 10
    } else if (kort.includes("Ess") == true) {
        dealersum += 11
    } else {
        var korttall = kort.replace( /^\D+/g, '');
        dealersum += parseInt(korttall)
    }
    let db = dealerbunke.toString();
    document.getElementById("dealerbunke").innerHTML = db;
    document.getElementById("dealersum").innerHTML = dealersum;
    sjekk();
}

function sjekk() {
    if (poengsum > 21) {
        tapt()
    } else if (poengsum == 21 && dealersum !== 21) {
        blackjack()
    } else if (dealersum > 21 && poengsum < 21) {
        vant()
    } else if (dealersum == 21 && poengsum !== 21) {
        tapt()
    } else if (dealersum == 21 && poengsum == 21) {
        draw()
    }
}

function tapt() {
    document.getElementById("game").style.display="none";
    document.getElementById("taper").style.display="block"
}

function blackjack() {
    document.getElementById("game").style.display="none";
    document.getElementById("blackjack").style.display="block"
}

function vant() {
    document.getElementById("game").style.display="none";
    document.getElementById("vant").style.display="block"
}