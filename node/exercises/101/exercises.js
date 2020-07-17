// Hello World Server
// Create a "hello world" server using the http module that starts a server and returns plain text.

// const http = require('http');
// const hostName = '127.0.0.1';
// const port = 3000;

// const server = http.createServer((req,res)=>{
//     res.statusCode= 200;
//     res.setHeader('Content-Type','text/plain');
//     res.end('Hello World');
// });

// server.listen(port,hostName, () => {
//     console.log(`Your  server is up at http://${hostName}:${port}/`)
// })
// ------------------------------------------------------------------------------------------------------------------------------------------


// Print out the version of npm that you have installed
let answer= "in terminal type 'npm -v' then enter";



// Create a node app that outputs a soild 5x5 square of '*' to the console.

let size = process.argv[2];
for (let i=0; i!== size; i++) {
    console.log(`${size}*G`)
}

// reate a node app that will read a text file using readFile and will write the contents of the file to the console.
const fs = require('fs');

fs.readFile('hello.js', 'utf8' , (err,data)=>{
    if (err) throw err;
    console.log(data);
});

