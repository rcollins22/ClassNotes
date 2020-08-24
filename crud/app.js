const express = require("express"); // after run npm install express in terminal
const app = express();
const pgp = require("pg-promise")(); //after run npm install pg-promise in terminal
const connect = require("./config");

const db = pgp(connect);

const port = 4800;



app.get('/tasks', async (req,res)=>{
    const data = await db.any("SELECT * FROM to_do");
    // .then(data=>console.log(data));
    console.log(data)

})

app.listen(port, () => {
  console.log(`Server is at... http://localhost:${port}`);
});
