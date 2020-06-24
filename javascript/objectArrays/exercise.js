// Write a madlib function, which is given a name and a subject. It will return(not print) a new string: (name)'s
//  favorite subject in school is (subject).

const madLib = (name,verb) => {
    console.log(`Im ${name} and i like to ${verb}`)
  }

//   Write a function tipAmount that is given the bill amount and the level of service (one of good, fair and poor) and returns 
//   the dollar amount for the tip. Based on:

// good -> 20% fair -> 15% bad -> 10%

const tipCalc = (amount,srvcLvl) =>{
    switch(true){
      case srvcLvl === 'good':
      console.log(amount*.20)
      return
      case srvcLvl === 'fair':
      console.log(amount*.15)
      return
      case srvcLvl === 'bad':
      console.log(amount*.10)
      return
    }
  }
  tipCalc(120,'good')

//   Write a function totalAmount that takes the same arguments as tipAmount except it returns the total as the tip amount plus the 
//   bill amount. This function may make use of tipAmount as a sub-task.


const totalCalc = (amount,srvcLvl) => {
    tipCalc(amount,srvcLvl)
    console.log(tipAmt+amount)
  }
  
totalCalc(120,'fair')

// Write a function printNumbers which is given a start number and an end number. It will print the numbers from one to the other, one per line:
//   printNumbers(1, 10)
//   1
//   2
//   3
//   4
//   5
//   6
//   7
//   8
//   9
//   10
// Write two versions of the above function. One using a while loop and the other using a for loop.

const prntNum = (start,end) =>{
    for (i=start;i<=end;i++){
      console.log(i)
    }
}
prntNum(6,12)



//   Write a function printSquare which is given a size and prints a square of that size using asterisks.

const prSqr = (num) =>{
    for (x=0;x<=num;x++);{
      console.log('---')
    }
  }  
prSqr(5)

// Write function printBox which is given a width and height and prints a hollow box of those given dimensions.
// printBox(6, 4)
//  ---
// |   |
//  ---



// Write a function printBanner which is given some text and prints a banner with a border surrounding the text. The 
// border has to stretch to the length of the text.

// > printBanner('Welcome to DigitalCrafts')
// ----------------------------
// - Welcome to DigitalCrafts -
// ----------------------------


const prntBan = (string) =>{
    let tab = '-'
    console.log(tab.repeat(string.length+4))
    console.log(`- ${string} -`)
    console.log(tab.repeat(string.length+4))
}
prntBan('Hello there')

// Write a function leetspeak which is given a string, and returns the leetspeak equivalent of the string. To convert text to its 
// leetspeak version, make the following substitutions:

// A => 4 E => 3 G => 6 I => 1 O => 0 S => 5 T => 7


