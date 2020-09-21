import "chrome-extension-async";
import Mercury from "@postlight/mercury-parser";

export async function getCurrentUrl() {
  const tabs = await chrome.tabs.query({ active: true, currentWindow: true });
  return tabs[0].url;
}

export async function getSummary(url, htmlCode) {
  Mercury.parse(url, { html: htmlCode, contentType: "text" }).then((result) => {
    title.textContent = result.title;
    const parsed = result.content;
    const resultFetch = fetch("http://home.sagarpatil.me:5000/summarize", {
      method: "POST",
      body: JSON.stringify({ text: parsed }),
    })
      .then((response) => response.json())
      .then((d) => (summary.textContent = d.summary))
      .catch((err) => console.log(err));
  });
}

export function getTitle(url) {
  return "Trump vows to appoint a woman to Supreme Court as vacancy re-energizes his political prospects";
}
