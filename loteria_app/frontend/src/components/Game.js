import React, { Component } from "react";

export default class Game extends Component {
    constructor(props) {
        super(props);
        this.state = {
            cards_id: 1,
            marker_id: 1
        };
        this.game_code = this.props.match.params.game_code;
    }

    render() {
        return (
        <div>
            <h3>Game Page: {this.game_code}</h3>
            <p>Cards Chosen: {this.state.cards_id}</p>
            <p>Marker Chosen: {this.state.marker_id}</p>
        </div>
        );
    }
}