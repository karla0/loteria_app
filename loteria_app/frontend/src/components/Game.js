import React, { Component } from "react";

export default class Game extends Component {
    constructor(props) {
        super(props);
        this.state = {
            cards_id: 1,
            marker_id: 1,
            host: '',
        };
        this.game_code = this.props.match.params.game_code;
        this.getGameDetails(); 
    }

    getGameDetails() {
        fetch('/api/get-game' + '?game_code=' + this.game_code)
        .then((response) => response.json())
        .then((data) => {
            this.setState({
                cards_id: data.cards_id,
                marker_id: data.marker_id,
                host: data.host,
                created_at: data.created_at,
            });
        });
    }

    render() {
        return (
        <div>
            <h3>Game Page: {this.game_code}</h3>
            <p>Cards Chosen: {this.state.cards_id}</p>
            <p>Marker Chosen: {this.state.marker_id}</p>
            <p>Host: {this.state.host}</p>
        </div>
        );
    }
}