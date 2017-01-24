function prix(){
	var prixTTC = 0;
	var prixHT = 0;
	var HT = parseFloat(document.getElementById("HT").value);
	var TTC = parseFloat(document.getElementById("TTC").value);
	var taxe = parseFloat((document.querySelector("input[name='taxe']:checked").value));
	prixTTC = (HT+(HT*(taxe/100)));
	prixHT = TTC/(1+(taxe/100));
	if(HT < 0 || TTC < 0){
		document.getElementById("prix").innerHTML ='Entrez un prix positif';
	}
	else if(isNaN(HT) && isNaN(TTC)){
		document.getElementById("prix").innerHTML = 'Entrez un prix positif dans une des cases' ;
	}
	else if(HT > 0 && TTC > 0){
		document.getElementById("prix").innerHTML ='Entrez un prix HT ou un prix TTC';
	}
	else if(isNaN(TTC)){
		document.getElementById("prix").innerHTML =  HT +'€ HT<br>=<br>' + prixTTC + '€ TTC';
	}
	else if(isNaN(HT)){
		document.getElementById("prix").innerHTML = TTC + '€ TTC<br>=<br>' + prixHT + '€ HT' ;
	}	
	else{
		document.getElementById("prix").innerHTML ='Entrez un prix';
	}
}

function surligne(champ, erreur){
	if(erreur){
		champ.style.backgroundColor = "#FBA";
	}
	else{
		champ.style.backgroundColor = "";
	}
}

function VerifInput(champ)
{
	if(champ.value < 0)
	{
		surligne(champ, true);
		document.getElementById('').innerHTML = "";
		return false;
	}
	else
	{
		surligne(champ, false);
		return true;
	}
}
