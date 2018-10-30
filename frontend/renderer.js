/*
This file is required by the index.html file
All of the Node.js APIs are available in this process.
*/
const {BrowserWindow} = require('electron').remote
const ipcRenderer = require('electron').ipcRenderer
const {shell} = require('electron')

//Adding event listeners for all form submissions
document.getElementById("indexForm").addEventListener('submit',sendForm);
document.getElementById("arbForm").addEventListener('submit',sendForm);
document.getElementById("tradeForm").addEventListener('submit',sendForm);
document.getElementById("triForm").addEventListener('submit',sendForm);

//Adding event listeners for all changes in drop down menus to create adaptiblity
//in the html forms
document.getElementById("exchangeI").addEventListener('change',changeLabel);
document.getElementById("exchangeArb1").addEventListener('change',changeLabel);
document.getElementById("exchangeArb2").addEventListener('change',changeLabel);
document.getElementById("exchangeTra").addEventListener('change',changeLabel);
document.getElementById("exchangeTri").addEventListener('change',changeLabel);

//adding event listeners to click through menu options
document.getElementsByName("landing")[0].addEventListener('click',changeDisplay);
document.getElementsByName("overview")[0].addEventListener('click',changeDisplay);
document.getElementsByName("indexing")[0].addEventListener('click',changeDisplay);
document.getElementsByName("arbitrage")[0].addEventListener('click',changeDisplay);
document.getElementsByName("trading")[0].addEventListener('click',changeDisplay);
document.getElementsByName("triarb")[0].addEventListener('click',changeDisplay);

//used to send form data to main.js so that main.js can turn it into a POST request to the server
function sendForm(event) {
  var type = event.target.id;
  // stop the default form from submitting so you can process it
  event.preventDefault()
  let formElements=document.getElementById(type).elements;
  let postData={};
  //create key-value pairs the form's name and value pairs
  for (var i=0; i<formElements.length; i++) {
    //we dont want to include the submit-buttom
    if (formElements[i].type!="submit") {
      //and store these key-value pairs in postData
      postData[formElements[i].name]=formElements[i].value;
    }
  }
}

// Event listener for clicked menu buttons
// Changing the which form is displayed
function changeDisplay(event) {
  //clearing current display
  var currentPage = document.getElementById("active");
  var currentPageContents = document.getElementById(currentPage.name);
  currentPageContents.style.display = "none";
  currentPage.removeAttribute("id");

  //showing new display
  var nextPageName = event.target.name;
  var nextPage = document.getElementById(nextPageName);
  document.getElementsByName(nextPageName)[0].setAttribute('id','active');
  nextPage.style.display = "block";
}

//Checks if Gdax is selected option because Gdax exchange
//requires an additional passphrase
function passphraseCheck(ex, passLabel, passInput) {
 var passphraseLabel = document.getElementById(passLabel);
 var passphraseInput = document.getElementById(passInput);

 if(ex === "Gdax"){
   passphraseLabel.innerHTML = ex + " Passphrase";
   passphraseLabel.style.display = "block";
   passphraseInput.style.display = "block";
   passphraseInput.required = true;
 }else{
   passphraseLabel.style.display = "none";
   passphraseInput.style.display = "none";
   passphraseInput.required = false;
 }
}

//Auto fills in the selected exchange's fee as the placeholder
function setFeePlaceHolder(exchange, exfee){
 var placeholder = "Default fee for ";
 switch(exchange){
   case "Binance":
     document.getElementById(exfee).placeholder = placeholder + exchange + " is 0.0010";
     break;
   case "Bittrex":
     document.getElementById(exfee).placeholder = placeholder + exchange + " is 0.0025";
     break;
   case "Gdax":
     document.getElementById(exfee).placeholder = placeholder + exchange + " is 0.0030";
     break;
   case "Gemini":
     document.getElementById(exfee).placeholder = placeholder + exchange + " is 0.0010";
     break;
   case "Kraken":
     document.getElementById(exfee).placeholder = placeholder + exchange + " is 0.0026";
     break;
   case "Kucoin":
     document.getElementById(exfee).placeholder = placeholder + exchange + " is 0.0010";
     break;
   case "Poloniex":
     document.getElementById(exfee).placeholder = placeholder + exchange + " is 0.0020";
     break;
 }
}

//Changes label for for the public and private key labels to match seleteced
//eschange
function changeLabel(event) {
  var selectedValue = event.target[event.target.selectedIndex].text;
  var formType = event.target.id;
  var pubKeyLabelId = formType + "pubkeylabel";
  var privKeyLabelId = formType + "privkeylabel";
  var passLabelId = formType + "passlabel";
  var passInputId = formType + "passinput";
  var exchangePubKeyLabel = document.getElementById(pubKeyLabelId);
  var exchangePrivKeyLabel = document.getElementById(privKeyLabelId);
  exchangePubKeyLabel.innerHTML = selectedValue + " Public Key";
  exchangePrivKeyLabel.innerHTML = selectedValue + " Private Key";
  passphraseCheck(selectedValue, passLabelId, passInputId);
  if(formType != "exchangeTra" || formType != "exchangeI"){
    var exFeeId = formType + "fee";
    setFeePlaceHolder(selectedValue, exFeeId);
  }
}
