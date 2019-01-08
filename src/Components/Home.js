import React, { Component } from 'react';
import { Spin } from 'antd';
import { Modal } from 'antd';
import Nav from './Navbar';
import "../Styles/Home.css";

class Home extends Component {
    constructor(props) {
        super(props);
        this.state = { 
            visible: false,
            spin: true  
        }
    }

    showModal = () => {
        this.setState({
          visible: true,
        });
      }
    
      handleOk = (e) => {
        console.log(e);
        this.setState({
          visible: false,
        });
      }
    
      handleCancel = (e) => {
        console.log(e);
        this.setState({
          visible: false,
        });
      }

      handleKeyPress = (e) => {
          if(e.key === "Enter"){
              this.showModal();
          }
      }

      handleSpin = () => {
        return (!this.state.spin)
      }

    render() { 
        return ( 
            <div className="home">
                <div className="navbar">
                    
                </div>
                <div className="head1">
                    <Nav/>
                    <h1>Brevis News</h1>
                </div>
                <div className="head2">
                    <h2>Summarize the news.</h2>
                </div>
                <div className="para">
                    <p>On the go? Use Brevis to abbreviate any<br/>news article into 100 word summaries</p>
                </div>
                <div className="head">
                    <input type="url" name="urlname" id="urlname" placeholder="Enter Article URL" onKeyPress={this.handleKeyPress}/>
                </div>
                <div className="but">
                    <button type="submit" onClick={this.showModal}>Summarize Article</button>
                </div>
                <Modal
                    title="Summary"
                    visible={this.state.visible}
                    onOk={this.handleOk}
                    onCancel={this.handleCancel}
                    >
                    <p>The Mumbai terror attacks of 26 November 2008 left 166 people dead and soured ties between India and Pakistan. During the 60-hour siege, the gunmen also ambushed a group of policemen, including three of the city's top officers travelling in a vehicle and killed six of them. The only surviving policeman, Arun Jadhav, tells the grisly story of his escape.</p>
                </Modal>
            </div>
         );
    }
}
 
export default Home;