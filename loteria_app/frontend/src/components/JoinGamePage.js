import React, { Component } from "react";
import { Link } from "react-router-dom";

import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography  from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormControl from "@material-ui/core/FormControl";

// from this page player can add their name and submit game code to join the running game.
//  players can only be in 1 active game.

export default class JoinGamePage extends Component {
    constructor(props) {
        super(props);
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
                    <TextField required={ true } 
                               type="text" 
                               variant="outlined"
                               label="Name"
                               inputProps={{
                                   min:1,
                               }}
                    />
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <Button color="primary" variant="contained">
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
