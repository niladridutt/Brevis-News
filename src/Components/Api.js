import React, { Component } from 'react';
import axios from 'axios';

const api_key = '4d031863e1eb4cbea1744cf28423b71d' 

// var url = 'https://newsapi.org/v2/everything?' +
//           `q=${}&` +
//           'from=2019-01-02&' +
//           'sortBy=popularity&' +
//           'apiKey=4d031863e1eb4cbea1744cf28423b71d';

class Api extends Component {
    constructor(props) {
        super(props);
        this.state = { 
            isLoaded : false,
            listData : [],
            page : "Politics",
            url : 'https://newsapi.org/v2/everything?' +
          `q=${this.state.url}&` +
          'from=2019-01-02&' +
          'sortBy=popularity&' +
          'apiKey=4d031863e1eb4cbea1744cf28423b71d'
         }
    }

    componentDidMount(){
        axios.get(this.state.urlurl)
        .then(res => {
            console.log(res.data)
            this.setState({
                isLoaded : true, 
                listData : res.data.articles
            })
        })
    }

    render() { 

        var { isLoaded, listData } = this.state

        console.log({listData})

        if(!isLoaded){
            return(
                <div>is loading...</div>
            )
        } else{
        return ( 
                <div className="api">
                    <ul>
                        {listData.map((item) => <li>{item.content}</li> )}
                    </ul>
                </div>
            );
        }
    }
}
 
export default Api;