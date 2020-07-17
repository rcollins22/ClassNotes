const prompt = require('prompt-sync')({sigint: true});


const add = (num1,num2)=> num1+num2
const sub = (a,b)=> a-b
const mult = () => {
    let n1 = process.arg[1];
    let n2 = process.arg[2];
    const final = n1*n2;
    console.log(`${n1} times ${n2} is ${final}`)
}

//THE ABOVE FUNCTION IS THE SAME AS:
// const add = (num1,num2) =>{
//     return num1+num2
// }

module.exports = {
    add,
    sub,
    mult;

}
