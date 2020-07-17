const express = require("express");
const app = express();
const port = 5053;
app.get("/", (re, rp) => rp.send("<h1>Hello There</h1><br>You gotta agree tto the following legal terms before we can let you in man.<ul><li>you gotta chill, bro.</li></ul><br><form action=http://localhost:5053/home><input type='submit' value='Okay, Im Chill.'/></form>"));
app.get("/home", (re, rp) => rp.send("<h1>Welcome to My First Express Site! Navigate Using the Buttons Below!</h1><br><h2>Our Contact and About Us Pages are below. Dont be a creep. Hit us up.</h2><br><form action=http://localhost:5053/contact><input type='submit' value='Lets Link'/></form><br><form action=http://localhost:5053/about><input type='submit' value='About You Guys'/></form>"));

// app.get("/home", (re, rp) => rp.send(""));
// app.get("/home", (re, rp) => rp.send(""));

app.get("/contact", (re, rp) => rp.send({ phone: "281-330-8004", fax: "111-867-5309", email:"DC420@gmail.com" }));
app.get("/about", (re, rp) => rp.send({description: "We are dedicated to providing our you with the essential fundamentals of blockchain applications." , founders:["Rashad", "David","Frida","Dy-Laan"],location:'Atlanta, GA'}));


app.get("*", (re, rp) => {
  rp.statusCode(404);
  rp.send("ERROR!! GO BACK!!!! HURRY!!!!!!!!");
});
app.listen(port, () => {
  console.log(`Your URL is here My Guy.. http://localhost:${port}`);
});
