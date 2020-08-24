import React from 'react';
import logo from './logo.svg';
import './App.css';
import Message from './Message.js'
import Button from './Button.js'
import Toggle from './Toggle.js'

class App extends React.Component { 
  constructor(props){
    super(props);
    this.state = {
      timesClicked: 0,
      hidden: true
    }
  }
  whenClicked(){
    this.setState({timesClicked:this.state.timesClicked+1})
    console.log(this.state.timesClicked)
  }
  
  render(){
  return (
      <div className="App">
          <p>Sup Guys</p>
          <h6 class = "hide-me">(Make me go away)</h6>
          <Message message = {'This is just some React Practice, Chill.'} />
          <Button text ="Ive been Clicked" timesClicked = {this.state.timesClicked} whenClicked = {this.whenClicked.bind(this)}/>
          <Toggle isHidden = {this.state.hidden} div = 
          />
          
      </div>
    );
}
}

export default App;