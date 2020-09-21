import "../css/popup.css";
import { getCurrentUrl, getSummary, getTitle } from "./popup/utils";

async function setup() {
  url.textContent = await getCurrentUrl();
  summary.textContent = await getSummary(url.textContent);
  title.textContent = getTitle(url.textContent);
}

setup();
