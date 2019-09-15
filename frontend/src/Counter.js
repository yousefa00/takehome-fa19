import React, { Component } from 'react'

class Counter extends Component {
  state = {
    count: 0,
  }

  handleIncrementer = () => {
    this.setState({count: this.state.count + 1});
  }

  handleDecrementer = () => {
    this.setState({count: this.state.count - 1});
  }

  render() {


    return (
      <div>
        <p>Count:  {this.state.count}</p>
        <button onClick={this.handleIncrementer}>Increment</button>
        <button onClick={this.handleDecrementer}>Decrement</button>
      </div>
    )
  }
}

export default Counter
