import React, { Component } from "react";
import { Link } from "react-router-dom";

import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography  from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";

// from this page player can add their name and submit game code to join the running game.
//  players can only be in 1 active game.

export default class JoinGamePage extends Component {
    constructor(props) {
        super(props);

        this.state = {
            game_code: 0,
            name: ''
        };

        this.handleJoinButtonPressed = this.handleJoinButtonPressed.bind(this)
        this.handleGameCode = this.handleGameCode.bind(this)
        this.handlePlayerName = this.handlePlayerName.bind(this)
    }

    handleGameCode(e) {
        this.setState({
            game_code: e.target.value
        });
    }

    handlePlayerName(e) {
        this.setState({
            name: e.target.value
        })
    }

    handleJoinButtonPressed() {
        console.log(this.state)
    }
        

    render() {
        return <Grid container spacing={1}>
            <Grid item xs={12} align="center">
                <Typography component="h4" variant="h4">
                    Join Game
                </Typography>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl>
                    <FormHelperText>
                        <div align="center"> Enter Game Code to Join</div>
                    </FormHelperText>
                    <TextField required={ true } 
                               type="number" 
                               variant="outlined"
                               onChange={this.handleGameCode}
                               inputProps={{
                                   min:1,
                                   style: {textAlign: "center"}
                               }}
                    />
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl>
                    <FormHelperText>
                        <div align="center"> Enter Display Name</div>
                    </FormHelperText>
                    <TextField required={ true } 
                               type="text" 
                               variant="outlined"
                               onChange={this.handlePlayerName}
                               inputProps={{
                                   min:1,
                                   style: {textAlign: "center"}
                               }}
                    />
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <Button color="primary" variant="contained" onClick={this.handleJoinButtonPressed}>
                    Join Game
                </Button>
            </Grid>
            <Grid item xs={12} align="center">
                <Button color="secondary" variant="contained" to="/" component={ Link }>
                    Back
                </Button>
            </Grid>
        </Grid>;
    }
}
