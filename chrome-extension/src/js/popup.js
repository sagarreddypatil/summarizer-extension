import "../css/popup.css";
function setup() {
  let params = {
    active: true,
    currentWindow: true,
  };
  chrome.tabs.query(params, gotTab);
  var username = "Chair"; // FROM BACKEND WHEN LOGINING
  function gotTab(tabs) {
    console.log("Hello from Rithvik");
    console.log(tabs);
    var val = tabs[0].url;
    Url.textContent = tabs[0].url;
  }
}
setup();
