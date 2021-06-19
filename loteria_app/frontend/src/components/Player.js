import React, { Component } from "react";

export default class Player extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: '',
            game_code: 1,
            player_id: 0,
            host_key: '',
        };
        this.player_id = this.props.match.params.player_id;
        this.getPlayerDetails();
    }

    getPlayerDetails() {
        fetch('/api/get-player' + '?player_id=' + this.player_id)
        .then((response) => response.json())
        .then((data) => {
            this.setState({
                name: data.name,
                game_code: data.game_code,
                player_id: data.player_id,
                host_key: data.host_key,
            });
        });
    }

    render() {
        return (
        <div>
            <h3>Player Page</h3>
            <p>Player ID: {this.player_id}</p>
            <p>Name: {this.state.name}</p>
            <p>Game Code: {this.state.game_code}</p>
            <p>Host Key: {this.state.host_key}</p>
        </div>
        );
    }
}