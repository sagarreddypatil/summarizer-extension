// var { Readability } = require("@mozilla/readability");
// var fs = require("fs");
var Mercury = require("@postlight/mercury-parser");
// var JSDOM = require("jsdom").JSDOM;
// var doc = new JSDOM(fs.readFileSync(__dirname + "/output.txt"), {});
// let reader = new Readability(doc.window.document);
// let article = reader.parse();

// console.log(article.content);

Mercury.parse(
  "https://www.cnn.com/2020/09/18/business/jobs-robots-microchips-cyborg/index.html",

  {
    html: fs.readFileSync(__dirname + "/output.txt"),
    contentType: "text",
  }
).then((result) => console.log(result.content));
