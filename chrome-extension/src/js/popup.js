import "../css/popup.css";
import { getCurrentUrl, getSummary } from "./popup/utils";

async function setup() {
  url.textContent = await getCurrentUrl();
  summary.textContent = await getSummary(url.textContent);
}

setup();
