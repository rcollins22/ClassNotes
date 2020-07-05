// 'console.log' PRINTS ITEMS TO CONSOLE
console.log("Hello World")     


// SYNTAX ADDS BRACKETS TO FUNCTIONS. camelCase IS STANDARD FOR JS
funtction helloWorld(){
    console.log('Hello World')
}
// PRINTS 'Hello World'
helloWorld

// 'var' PLUS THE NAME OF THE VARIABLE SETS ONE.
var recipeient="CLint"


// CAN SET VARIABLES TO FUNCTION RECALLS
var hello=helloWorld


// 'let' ALLOWS YOU TO DECLARE A VARIABLE WITHOUT SETTING IT EQUAL TO ANYTHING, AN UNDEFINED VARIABLE 
let jusAVar 
// PRINTS 'undefined'
console.log(jusAVar)

var myItem=2
function returnMyItem(){
    // 'let' INSIDE OF A FUNCTION LOCALLY RESETS THE VARIABLE. NOT GLOBALLY!!
    let myItem =3
    // PRINTS 3
    return myItem
}
// WILL STILL PRINT 2
console.log(myItem)

// CAN SET A VARIABLE TO AN UNNAMED Function, OR ANONYMOUS Function.
let myFunc = function(){
    console.log('Crazy')
}

// PRINTS 'Crazy'
myFunc()

// CONSTANTS CANNOT BE CHANGED ONCE THEY ARE DECLARED.
const myCon=150


// ARROW FUNCTIONS
const myFunc = (param1,param2)=>{
    console.log(param1,param2)
}
// PRINTS (2,3)
myFunc(2,3)

// ${} CONCACTS ITEMS
let mySal = "dog"
let examp = '${mySal} is the man'
// PRINTS  'dog is the man'


let user = "Rashad"

if (user=="Rashad"){
  console.log("Balance:1.23")
}
// TAKE NOTE OF SYNTAX 
if (user=="Rashad"){
  console.log("Balance:1.23")
} else {
  console.log('Balance: Hidden')
}

if (user=="Rashad"){
  console.log("Balance:1.23")
  // 'else if' FOLLOWS
} else if(user=="Clint") {
  console.log('Balance: NICE TRY')
}


if (user=="Rashad"){
  console.log("Balance:1.23")
} else if(user=="Clint") {
  console.log('Balance: NICE TRY')
} else {
  console.log('Self Destruction Initiaizing')
}




let name = "Devin"
// '?' IS USED FOR 'if' COMPARISONS, ':' IS THE 'else' OF THE SECTION
name == "Devin" ? console.log('Welcome Devin'):console.log('User Unknown')