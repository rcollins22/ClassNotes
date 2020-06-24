// Write a function that will recieve a sentance as a string and return another string of only the letters that MATCH the requirement of being upper case JOINed together.
// Hint you will be using a string method and an array method.


const toUp = (string) =>{
    const splArr =/[A-Z]/g;
    const final = string.match(splArr); 
    console.log(final)
}
  
toUp('I Like To play')


// Write a function that will return the KEYS of an object as an array and have the array SORTed in alphebetical order.

object1= {
    name: 'Rashad',
    dob: '2243',
    passion:"Blockchain"
  }
  
  const getKey = (object) => {
    arR= Object.keys(object)
    console.log(arR.sort())
  }
  getKey(object1)