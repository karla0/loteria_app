import React, { Component } from "react";

export default class Game extends Component {
    constructor(props) {
        super(props);
        this.state = {
            cards_id: 1,
            marker_id: 1,
            isHost: false,
        };
        this.gameCode = this.props.match.params.gameCode;
    }

    render() {
        return (
        <div>
            <h3>Game Code: {this.gameCode}</h3>
            <p>Cards ID: {this.state.cards_id}</p>
            <p>Marker ID: {this.state.marker_id}</p>
            <p>isHost: {this.state.isHost}</p>
        </div>);
    }
}