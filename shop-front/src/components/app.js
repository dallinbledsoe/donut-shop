import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

export default class App extends Component {
  render() {
    return (
      <div className="app">
        <h1>Donut Shop</h1>
        <div className="navbar">
          <Router>
            <Switch>
              <Route exact path="/" component={Home} />
            </Switch>
          </Router>
        </div>
      </div>
    );
  }
}
