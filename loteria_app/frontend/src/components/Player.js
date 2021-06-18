import React, { Component } from "react";

export default class Player extends Component {
    constructor(props) {
        super(props);
        this.state = {
            game_code: 1,
        };
        this.player_id = this.props.match.params.player_id;
    }

    render() {
        return (
        <div>
            <h3>Player Page</h3>
            <p>Player ID: {this.player_id}</p>
        </div>
        );
    }
}