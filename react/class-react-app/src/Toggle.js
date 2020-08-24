import React from "react"
const Toggle = ({isHidden,div}) => {
    if(isHidden === true){
        div.style.display = "none"
    } else {
        div.style.display = "block"
    }
    return(<button onClick="Toggle()">Dont Press</button>)
 }

export default Toggle