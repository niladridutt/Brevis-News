import React, { Component } from 'react';
import "../Styles/Navbar.css";
class Nav extends Component {
    constructor(props) {
        super(props);
        this.state = { 

         }
    }
    render() { 
        return ( 
            <div className="nav">
                <div className="navbut1">
                    <a href="/">Home</a> 
                </div>
                <div className="navbut2">
                    <a href="/read">Read Now</a> 
                </div>
            </div>

         );
    }
}
 
export default Nav;