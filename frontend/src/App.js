import React, { Component } from 'react'
import Instructions from './Instructions'
import Counter from './Counter'
import Contact from './Contact'

class App extends Component {
  constructor(props) {
    super(props)

    this.handleNameChange = this.handleNameChange.bind(this);
    this.handleNicknameChange = this.handleNicknameChange.bind(this);
    this.handleHobbyChange = this.handleHobbyChange.bind(this);
    this.handleFavFoodChange = this.handleFavFoodChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);

    this.state = {
      contacts: [
        {id: 1, name: "Angad", nickname: "greg", hobby: "dirty-ing"},
        {id: 2, name: "Roy", nickname: "uwu", hobby: "weeb"},
        {id: 3, name: "Daniel", nickname: "oppa", hobby: "losing money with options trading"},
      ],
      nameValue: '',
      nicknameValue: '',
      hobbyValue: '',
      favFoodValue: ''
    };
  }

  handleNameChange(event) {
    this.setState({nameValue: event.target.value});
  }

  handleNicknameChange(event) {
    this.setState({nicknameValue: event.target.value});
  }

  handleHobbyChange(event) {
    this.setState({hobbyValue: event.target.value});
  }

  handleFavFoodChange(event) {
    this.setState({favFoodValue: event.target.value});
  }

  handleSubmit(event) {
    if (this.state.nameValue != "") {
      let id = this.state.contacts[this.state.contacts.length - 1].id + 1

      this.state.contacts.push({id: id, name: this.state.nameValue,
        nickname: this.state.nicknameValue, hobby: this.state.hobbyValue,
        favFood: this.state.favFoodValue})
    }
    this.forceUpdate();
    this.refs.counter.incrementCounter();
    event.preventDefault();
  }

  render() {
    return (
      <div className="App">
        <Instructions complete={true}/>
        <Counter ref="counter"/>

        {this.state.contacts.map(x => (
          <Contact id={x.id} name={x.name} nickcname={x.nickname} hobby={x.hobby} />
        ))}

        <form onSubmit={this.handleSubmit}>
          <label>
            Preferred Name:
            <input type="text" value={this.state.nameValue} onChange={this.handleNameChange} />
            <br/>
          </label>
          <label>
            Nickname:
            <input type="text" value={this.state.nicknameValue} onChange={this.handleNicknameChange} />
            <br/>
          </label>
          <label>
            Hobby:
            <input type="text" value={this.state.hobbyValue} onChange={this.handleHobbyChange} />
            <br/>
          </label>
          <label>
            Favorite Food:
            <input type="text" value={this.state.favFoodValue} onChange={this.handleFavFoodChange} />
            <br/>
          </label>
          <input type="submit" value="Submit" />
        </form>
      </div>
    )
  }
}

export default App
