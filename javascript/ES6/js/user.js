let name = ""
let age = ""
let balance = ""
export default addToUser = (att, value) =>{
    let userObj ={
        name:name,
        age:age,
        balance:balance
    }
    Object.freeze(userObj)

    return userObj;
}

export const editName = (n) => {
    name = n
}