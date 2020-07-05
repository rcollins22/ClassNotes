// const list = document.getElementById('users');
// const list = document.querySelector
const list = document.querySelector("ul"); //gets first "ul"
const ns= new Nonsense()


const genPerson =() => {
    return{
        firstName:ns.firstName(),
        lastName:ns.lastName(),
        id:ns.uuid(),
        occupation:ns.jobTitle(),
        quote:ns.buzzPhrase()
    }
}

const createPErsonDOM= (person) => {
    let mYInfo = document.createElement('ul')
    mYInfo.className='Guests'
    
    let quote =document.createElement("div");
    quote.innerText= person.quote;
    quote.className = "quote-hidden"
    
    let detInfo =document.createElement('div')
    detInfo.innerText = `${person.firstName} ${person.lastName} : ${person.occupation}`
    detInfo.className='detail-info'

    mYInfo.append(detInfo,quote)
    list.append(mYInfo)
}




let users =[];

for (let i=0; i<20; i++){
    let person = genPerson()
    users.push(person)
    createPErsonDOM(person)
}
console.log(users)