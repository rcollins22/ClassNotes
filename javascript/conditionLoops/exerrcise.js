// Write a function that accepts an argument named tempature. Have at least 6 ranges of tempature that represents a html valid color. Return the color based on the argument supplied when calling the function.
// Use Switch. (hint do a google search for 'switch(true)' )

function whatTemp(temp){
    switch(true){
      case temp<45:
        console.log('test');
        return
      case temp<55:
        console.log('test1');
        return
      case temp<65:
        console.log('test2');
        return
      case temp<75:
        console.log('test3');
        return
      case temp<85:
        console.log('test4');
        return
      case temp<95:
        console.log('test5');
        return
    }
  }




// Write a function that will return an array of arrays with 100 copies of each element in the array supplied in the as an argument of the function. 
// The array in the parameter needs to be strings and needs to have at least 5 elements.
// (ridiculous unessery challenge..seriously dont try this unless you are just wanting a challange) complete the above with the following requirements (it can be more than one function for this):
// Without mutating anything (strings, arrays etc). This means no variable can change and no array can be added to or removed from. (look up imutability)
// Without Using any loops
// Without using forEach, map, filter, or reduce.
// (seriously please do not spend more than 30 minutes trying to do this)





whatTemp(75)

var final = []
  
const myFunc = function(array1) { 
  
  let x=0
  let pushArray=[]
  for (i=0; i < array1.length; i++){
    // for (x=0;)
  
    while (x!=5){
    pushArray.push(array1[i])
    x++
    
    }
  
  
  final.push(pushArray)
  }
  console.log(final)
}
myFunc(['hi','hey','sup', 'yo', 'hello'])



// ---------------------SOLUTION-------------------------

const nameList = ['hi','hey','sup', 'yo', 'hello']

const makeCopies = (myArr) => {
    let outArray = []
    for(let i=0; i<myArr.length; i++){
        outArray[i]=[]
        for (let j = 0; j < 100 ; j++){
            outArray[i][j].push(myArr[i]
                )
        }
    }
    return outArray
}
console.log(makeCopies(nameList))



let instan = {
    user:'Rashad';
    wallet:{
      id:334943
      balance:34.3
    };
    twoFact: false
  }