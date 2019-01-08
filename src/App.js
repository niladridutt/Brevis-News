import React, { Component } from 'react';
import { Switch,Route } from 'react-router-dom';
import Home from './Components/Home';
import Read from './Components/Read';
import Api from './Components/Api';

class App extends Component {
    render() {
        return (
                <div className="App">
                        <Switch>
                            <Route path="/" exact component={Home}/>
                            <Route path="/read" exact component={Read}/>
                            <Route path="/api" exact component={Api}/>
                        </Switch>
                </div>
                );
    }
}

export default App;