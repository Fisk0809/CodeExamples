function control(e){
    var felt = e.target.name;
    var string = e.target.value;			 
    if (felt == "username"){				
      string = string.toLowerCase();
      string = string.replace(string[0],string[0].toUpperCase());  
      string = string.replace(/[^A-Za-zÆæØøÅå.-0-9]/g,'');
    }
    if (felt == "email"){
        string = string.replace(/[^a-z.-@0-9]/g,'');
    }
    if (felt == "fname"){				
      string = string.toLowerCase();
      string = string.replace(string[0],string[0].toUpperCase());  
      string = string.replace(/[^A-Za-zÆæØøÅå.-]/g,'');
    }
    if (felt == "lname"){				
      string = string.toLowerCase();
      string = string.replace(string[0],string[0].toUpperCase());  
      string = string.replace(/[^A-Za-zÆæØøÅå.-]/g,'');
    }
    e.target.value = string;	
    if (username.value != "" & mail.value != "" & fname.value != "" & lname.value != "" & pasw.value != ""){
      submit.disabled = false;
      submit.style.display = "block";
    }
  }		
  //Hovedprogram
  var username = document.querySelector("#username");
  var mail = document.querySelector("#mail");
  var fname = document.querySelector("#fname");
  var lname = document.querySelector("#lname");
  var pasw = document.querySelector("#pasw");
  var submit = document.querySelector("#submit");
          
  fnavn.value = "";
  enavn.value = "";
  mail.value = "";
  pasw.value = "";
          
  submit.disabled = true;
  submit.style.display = "none";
          
  document.addEventListener("input",control);