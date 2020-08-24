import React from "react"
const Button = ({text, whenClicked, timesClicked}) => {
    return (<button onClick = {whenClicked}>{text}: {timesClicked}</button>)
}
export default Button