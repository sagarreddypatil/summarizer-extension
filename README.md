# Quick Summary
This is a monorepo containing all the code for a browser extension to generate summaries of any article with the click of a button.


## Build Instructions

In order to try out this extension, first clone this repository.

Making sure you have the latest Node.js version available, run the following commands:
1. `cd chrome-extension`
2. `npm install`
3. `npm run build`. This should generate a new `build` folder in the `chrome-extension` directory.
4. Next, open `chrome://extensions` in your browser and click the "Load Unpacked" button.

  <img width="533" alt="Untitled" src="https://user-images.githubusercontent.com/30810402/93785055-a6155380-fbfb-11ea-9e9e-a6bb592c3b30.png">

5. When your file browser opens, select the new `build` folder that was created. You should now see our extension in the list.

<img width="572" alt="Screen Shot 2020-09-21 at 11 15 39 AM" src="https://user-images.githubusercontent.com/30810402/93785178-c9400300-fbfb-11ea-96a1-aa55c3d5c065.png">

6. And the extension should be installed! To try it out, just press the extension icon on a news article. A summary should load within a few seconds.
