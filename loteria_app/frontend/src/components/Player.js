import React, { Component } from "react";

export default class Player extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            game_code: 1,
            player_id: 0,
        };
        this.player_id = this.props.match.params.player_id;
    }

    render() {
        return (
        <div>
            <h3>Player Page</h3>
            <p>Player ID: {this.player_id}</p>
            <p>Name: {this.state.name}</p>
            <p>Game Code: {this.state.game_code}</p>
        </div>
        );
    }
}