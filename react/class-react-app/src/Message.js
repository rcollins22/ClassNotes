import React from 'react';

class Message extends React.Component {
    constructor(props){
        super(props)
        console.log(props.message)

    }
    render(){
        return(
            <div>
                <div>{this.props.message}</div>
                <p>{this.props.mess2}</p>
            </div>
        )
    }
}

export default Message 