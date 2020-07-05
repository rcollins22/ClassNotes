// // Write a function 3x that has two parameters and those parameters are used in a sentence that says "hello my name is NAME I am AGE years old", except NAME and AGE would be the parameters given.
// // Use the 3 ways of declaring a function to make each function different but the results to console the same.
// // For each function use a different way of creating the output sentence. For example only one can use concatanation.

// function greet1(name,age){
//     console.log("hi my name is",name,"and i am",age,"years old")
//   }
// greet1('Rashad',26)
  
// function greet2(name,age){
//     console.log(`hi my name is ${name} im ${age} years old`)
//   }
// greet2('Rashad',26)
  
// let greet3 = (name,age)=> "hi my name is" + name + "and im" + age + "years old"
  
// greet3("Rashad",26)

// // Write a function that has another function as a parameter, and inside the main function the parameter function is called after you print to the console "Main Function Executing".
// // You can declare the function as a varaible before and place that variable as the parameter.
// // (Challange) have the main function have a second parameter that will be used as an argument for the child function.

// let doAfter = (param1) => {
//     console.log("look I was Called")
//   }
// function mainFunction(callback){
//     console.log("Executing Function")
//     callback()
//   }
  
// // PRINTS 'Executing Function'
// //         'look i was called'
// mainFunction(doAfter)
  
  
// function mainFunction(callback,secondParam){
//     console.log("Executing Function")
//     callback(secondParam)
//   }
// mainFunction(myParam => console.log("Hi there" + myParam),"something bad")
  
// // Write a function that will print to the console "Parent Function Called" and then returns a function that when is called will print to the console "Child Function Called" The child function cannot be declared outside of the main function. Follow steps bellow if you need a step by step way to do it.
// // Create a function and have that function print to the console.
// // Inside the main function declare the second function as a variable that prints to the console the given statement
// // after the second function is declared inside the main function, return the variable that the second function is assigned to.
// // Outside of the function assign the called function to a variable (that variable is now a function).
// // call that variable.

// let aFunc = function(){
//     console.log("parent function called")
//     return ()=>console.log("child function called")
//   }
// aFunc()
  
// let aVar = aFunc()
  
// aVar()





// Write a function that accepts string as an argument and if the string is less than 4 charecters return one message, if it is greater than 12 
// return another message otherwise return a final message about being accepted.

const testFunc = myString => myString.length < 4 ? "too short" : myString.length > 12 ? "too long":"just right"