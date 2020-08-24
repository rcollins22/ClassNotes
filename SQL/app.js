const pgp = require('pg-promise')();

//THIS CONNECTS TO OUR DATABASE 
const bc = pgp('postgres://ddjnxkmj:F2tKTzY5pld-rSdhG0_Nt72tk3m2n3ZX@ruby.db.elephantsql.com:5432/ddjnxkmj')

bc.any('SELECT * FROM accounts').then(accounts=>console.log(accounts))
.then(account=>console.log(account))


let person = {
    name:'Robert',
    points: 2500,
    walletID:'33knkn4bj612nnksn0'

}

bc.none(`INSERT INTO accounts (name,points,walletID) VALUES ('${person.name}', '${person.points}','${person.walletID}')`)
.then(res=>console.log(res))