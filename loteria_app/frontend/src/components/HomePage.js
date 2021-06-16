import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom"; 

import GamePage from "./GamePage";
import JoinGamePage from "./JoinGamePage"
import StartGamePage from "./StartGamePage"
import WaitingRoomPage from "./WaitingRoomPage"

export default class HomePage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (<Router>
            <Switch>
                <Route exact path='/'><p>This is the Home Page with Routing</p></Route>
                <Route path='/game' component={ GamePage }/>
                <Route path='/join' component={ JoinGamePage }/>
                <Route path='/start' component={ StartGamePage }/>
                <Route path='/waiting' component={ WaitingRoomPage }/>
            </Switch>
        </Router>
        );
    }
}