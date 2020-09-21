import "../css/popup.css";
import { getCurrentUrl, getSummary, getTitle } from "./popup/utils";

async function setup() {}

chrome.runtime.onMessage.addListener(function (request, sender) {
  if (request.action == "getSource") {
    getCurrentUrl().then((r) => {
      url.textContent = r;
      getSummary(r, request.source);
    });
    // summary.textContent = await getSummary(url.textContent, request.source);
  }
});

const code = `
// @author Rob W <http://stackoverflow.com/users/938089/rob-w>
// Demo: var serialized_html = DOMtoString(document);
function DOMtoString(document_root) {
   var html = "",
    node = document_root.firstChild;
  while (node) {
    switch (node.nodeType) {
      case Node.ELEMENT_NODE:
        html += node.outerHTML;
        break;
      case Node.TEXT_NODE:
        html += node.nodeValue;
        break;
      case Node.CDATA_SECTION_NODE:
        html += "<![CDATA[" + node.nodeValue + "]]>";
        break;
      case Node.COMMENT_NODE:
        html += "<!--" + node.nodeValue + "-->";
        break;
      case Node.DOCUMENT_TYPE_NODE:
        // (X)HTML documents are identified by public identifiers
        html +=
          "<!DOCTYPE " +
          node.name +
          (node.publicId ? ' PUBLIC "' + node.publicId + '"' : "") +
          (!node.publicId && node.systemId ? " SYSTEM" : "") +
          (node.systemId ? ' "' + node.systemId + '"' : "") +
          ">\\n";
        break;
    }
    node = node.nextSibling;
  }
  return html;
}

chrome.runtime.sendMessage({
  action: "getSource",
  source: DOMtoString(document),
});
`;

function onWindowLoad() {
  var message = document.querySelector("#summary");

  chrome.tabs.executeScript(
    null,
    {
      code,
    },
    function () {
      // If you try and inject into an extensions page or the webstore/NTP you'll get an error
      if (chrome.runtime.lastError) {
        message.innerText =
          "There was an error injecting script : \n" +
          chrome.runtime.lastError.message;
      }
    }
  );
}

window.onload = onWindowLoad;

setup();
