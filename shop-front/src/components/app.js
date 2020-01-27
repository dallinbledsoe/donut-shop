import React, { Component } from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  NavLink
} from "react-router-dom";

import Home from "./pages/home";
import About from "./pages/about";

export default class App extends Component {
  render() {
    return (
      <div className="app">
        <div className="page-wrapper">
          <Router>
            <div className="navbar">
              <h1>Donut Shop</h1>
              <div className="nav-links-wrapper">
                <NavLink to="/" activeClassName="nav-link-active">
                  Home
                </NavLink>
                <NavLink to="/about" activeClassName="nav-link-active">
                  About
                </NavLink>
              </div>
              <div className="login">user</div>
            </div>

            <div className="page-content">
              <Switch>
                <Route exact path="/" component={Home} />
                <Route path="/about" component={About} />
              </Switch>
            </div>
          </Router>
        </div>
      </div>
    );
  }
}
