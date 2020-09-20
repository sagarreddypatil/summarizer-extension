import "../css/popup.css";
import { getCurrentUrl } from "./popup/utils";

async function setup() {
  addUrl.textContent = await getCurrentUrl();
}

setup();
