import "../css/popup.css";

function getUrl() {
  chrome.tabs.query(
    {
      active: true,
      currentWindow: true,
    },
    (tabs) => {
      addUrl.textContent = tabs[0].url;
    }
  );
}

getUrl();
