var fs = require("fs");
var Mercury = require("@postlight/mercury-parser");

Mercury.parse(
  "https://www.cnn.com/2020/09/18/business/jobs-robots-microchips-cyborg/index.html",

  {
    html: fs.readFileSync(__dirname + "/output.txt"),
    contentType: "text",
  }
).then((result) => console.log(result.content));
