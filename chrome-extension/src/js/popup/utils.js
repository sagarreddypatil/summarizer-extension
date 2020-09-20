import "chrome-extension-async";

export async function getCurrentUrl() {
  const tabs = await chrome.tabs.query({ active: true, currentWindow: true });
  console.log(`Got ${tabs[0].url}`);
  return tabs[0].url;
}
