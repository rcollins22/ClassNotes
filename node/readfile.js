const fs = require('fs');

fs.readFile('hello.js', 'utf8' , (err,data)=>{
    if (err) throw err;

    console.log(data)
})
//READS ENTIRE FILE IN PLAIN TEXT