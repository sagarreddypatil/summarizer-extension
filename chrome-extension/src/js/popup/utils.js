import "chrome-extension-async";

export async function getCurrentUrl() {
  const tabs = await chrome.tabs.query({ active: true, currentWindow: true });
  return tabs[0].url;
}

export async function getSummary(url) {
  return `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras molestie
  libero vel nunc mattis hendrerit. Integer sed nulla non dui congue
  consectetur. Phasellus nec sapien at velit faucibus facilisis eu eget
  augue. Aenean id nunc ut purus hendrerit placerat sed non massa. Aenean
  velit metus, rutrum eget congue id, rhoncus et nulla. Duis quis
  tincidunt mi, sed tristique metus. Aliquam non ultrices lorem, sed
  fermentum lorem. Quisque lacinia mauris lectus, a imperdiet mauris
  suscipit sed. Cras condimentum, lacus quis ultricies tristique, nulla
  nulla mattis ipsum, quis commodo libero est eu ante. Mauris a sapien
  ultricies, sodales ligula eget, viverra urna. Curabitur ac risus a
  libero vehicula porta. Mauris purus ex, feugiat ac vulputate quis,
  accumsan in felis. Fusce ultricies tellus suscipit justo posuere
  laoreet. Suspendisse potenti. In vitae malesuada leo. Nullam et est
  ipsum.`;
}
