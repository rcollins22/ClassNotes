// const express = require('express');
// const app = express();

const app = require("express")(); //THIS LINE IS THE SAME AS THE 2 ABOVE

const es6Renderer = require("express-es6-template-engine");

app.engine("html", es6Renderer); //THE APP ENGINE IS GOING TO RUN THE SELECTED FUNCTION, (param2) THROUGH THE TEMPLATE (param1)

app.set("views", "templates"); //ALLOWS YOU TO SET ATTRIBUTES TO THE RETURNED APP OBJECT
app.set("view engine", "html");

const friends = [
  { name: "Clint", walletID: "4217344" },
  { name: "David", walletID: "4278133" },
  { name: "Adnan", walletID: "4915734" },
];

app.get("/", (req, res) => {
        // PRINTS 'We made it.' to HTML PAGE
  res.render("index", {
    locals: {
      name: "Rashad",
      walletID: "4234544",
    },
  });
    res.send('We made it.');
});

app.get("/friends", (req, res) => {
  res.render("friends", {
    locals: {
      friends: friends,
    },
  });
});

app.get("/friend/:name", (req, res) => {
  res.render("friend", {
    locals: {
      friend: friends.find((friend) => friend.name === req.params.name),
    },
  });
});

// app.get("/", (req, res) => {
//     // res.send('We made it.');      // PRINTS 'We made it.' to HTML PAGE
//     res.render("index", {
//       locals: {
//         name: "Rashad",
//         walletID: "4234544",
//       },
//     });
//   });

app.listen(3500); // DEPLOYS NODE APP TO http://localhost:3500/
