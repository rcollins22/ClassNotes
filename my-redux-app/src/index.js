import {createStore} from 'redux'
const { bindActionCreators } = require("redux");


console.log('testing')

// Setting the default state,
const defaultState = 0;

//Function used to change the state

const INCREMENT = 'increment';
const DECREMENT = 'decrement';
const actionInc = {
  type: INCREMENT
};

const actionDec = {
  type: DECREMENT
};

//Writing a function that is expecting the current state and an action.
//**MUST RETURN A COPY OF THE STATE**

function counter(state = defaultState,action) {
  
  switch(action.type){
    case 'increment':
      return state + 1;
    case 'decrement':
      return state - 1;
    default:
      return state;
    }
}

const store = createStore(counter);

//The store has 3 functions:
//  -.subscribe: YOU PASS IT A FUNCTION AND ITS CALLS IT EVERYTIME THE STATE CHANGES.
//  -.getState: returns a copy of the state
//  -.dispatch you pass an actions, it tells the store to run the reducer function.

store.subscribe(() => {
  console.log(store.getState())
});

window.store = store;
window.actionInc=actionInc;
window.actionDec=actionDec;