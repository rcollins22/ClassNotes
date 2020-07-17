let user = 'Rashad'
let balance = 25.2
console.log(`Hello ${user}, Your balance is ${balance}.`)

// RUNNING 'rashadcollins@Rashads-MacBook-Pro node % node giveName.js node' WILL LOG TEMPERATE LITERAL IN TERMINAL


console.log(process.argv)
//LOGS AN ARRAY OF USED DATA IN NODE:
// [
//     '/usr/local/bin/node',
//     '/Users/rashadcollins/Documents/class_notes/node/giveName.js',
//     'node'
//   ]

let name1 = process.argv[2]
console.log(`Hello ${name1}, Your balance is ${balance}.`)
//RUNNING 'rashadcollins@Rashads-MacBook-Pro node % node giveName.js Rashad' IN TERMINAL WILL PRINT:
//'Hello Rashad, Your balance is 25.2'


let startBal = +process.argv[2] //PLUS SIGN CONVERTS STRINGS INTO NUMBERS
let amount = process.argv[3]
 console.log(`${user}, you are sending ${amount} from your balance of ${startBal}. You now have ${startBal-amount}`)

// RUNNING 'rashadcollins@Rashads-MacBook-Pro node % node giveName.js 25.2 12' IN TERMINAL WILL PRINT:
 //                                             'Rashad, you are sending 12 from your balance of 25.2. You now have 13.2'

