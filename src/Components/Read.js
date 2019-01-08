import React, { Component } from 'react';
import { List, Avatar, Icon, Layout, Menu } from 'antd';
import { Spin } from 'antd';
import { Link } from 'react-router-dom';
import axios from 'axios';
import '../Styles/Read.css'; 

const {
    Content, Sider,
  } = Layout;

  const IconText = ({ type, text }) => (
    <span>
      <Icon type={type} style={{ marginRight: 8 }} />
      {text}
    </span>
  );
  

class Read extends Component {
  constructor(props){
    super(props);
    this.state = {
      isLoaded : false,
      listData : [],
      url : 'https://newsapi.org/v2/everything?' +
      `q=everything&` +
      'from=2019-01-02&' +
      'sortBy=popularity&' +
      'apiKey=4d031863e1eb4cbea1744cf28423b71d'
    }
  }

  componentDidMount(){
    this.loadData(this.state.url)
}

  loadData = (url) => {
    axios.get(url)
      .then(res => {
        this.setState({
            isLoaded : true, 
            listData : res.data.articles
        })
    })
  }

  handleClick = (page) => {
    this.setState({
      isLoaded : false,
      listData : [],
      url : `https://newsapi.org/v2/?everything` +
      `q=${page}&` +
      'from=2019-01-02&' +
      'sortBy=popularity&' +
      'apiKey=4d031863e1eb4cbea1744cf28423b71d'
    })
      this.loadData(this.state.url)
  }

  render() {

    var { isLoaded, listData } = this.state
    return (
        <div className="read">
        <Sider style={{
        overflow: 'auto', height: '100vh', position: 'fixed', left: 0
    }}
    >
      <div className="logo" />
      <Menu style = {{ fontFamily: "Ubuntu" }} theme="dark" mode="inline" defaultSelectedKeys={['1']}>
        <Menu.Item key="1" onClick={()=>this.handleClick("Everything")}>
        <Icon type="form" />
          <span className="nav-text">Front Page</span>
        </Menu.Item>
        <Menu.Item key="2" onClick={()=>this.handleClick("India")}>
          <Icon type="flag" />
          <span className="nav-text">India</span>
        </Menu.Item>
        <Menu.Item key="3" onClick={()=>this.handleClick("World")}>
          <Icon type="global" />
          <span className="nav-text">World</span>
        </Menu.Item>
        <Menu.Item key="4" onClick={()=>this.handleClick("Entertainment")}>
          <Icon type="star" />
          <span className="nav-text">Entertainment</span>
        </Menu.Item>
        <Menu.Item key="5" onClick={()=>this.handleClick("Business")}>
        <Icon type="dot-chart" />
          <span className="nav-text">Business</span>
        </Menu.Item>
        <Menu.Item key="6" onClick={()=>this.handleClick("Technology")}>
          <Icon type="mobile" />
          <span className="nav-text">Technology</span>
        </Menu.Item>
        <Menu.Item key="7" onClick={()=>this.handleClick("Sports")}>
        <Icon type="skin" />
          <span className="nav-text">Sports</span>
        </Menu.Item>
      </Menu>
    </Sider>
    <Layout style={{ marginLeft: 200 }}>
      <Content>
      <Spin spinning={!isLoaded} size="large" >
      <div style={{ paddingTop: 10, paddingBottom: 10, paddingLeft: 70, paddingRight: 70 , background: '#dfe6e9', textAlign: 'center' }}>
      <Link to='/'><Icon type="home" theme="filled" style={{ marginTop : 20 , marginLeft : -1200 }} /><p  style={{ marginLeft : -1200, fontFamily: "Ubuntu" }}>Home</p></Link>
      <List
      split= "true"
      itemLayout="vertical"
      size="large"
      dataSource={listData}
      style={{ fontFamily: "Ubuntu" }}
      renderItem={item => (
      <List.Item
        key={item.title}
        actions={[<IconText type="star-o" text={String(Math.floor((Math.random() * 1000) + 1))} />, <IconText type="like-o" text={String(Math.floor((Math.random() * 1000) + 1))} />, <IconText type="message" text={String(Math.floor((Math.random() * 1000) + 1))} />]}
        extra={<img alt="logo" src={item.urlToImage} style={{ width: 200, height: 200 , borderRadius: 100, fontFamily: "Ubuntu" }}/>}
      >
        <List.Item.Meta
          avatar={<Avatar src={item.avatar} />}
          title={<a href={item.url}>{item.title}</a>}
          description={item.description}
          style={{ fontFamily: "Ubuntu" }}

        />
        {item.content}
      </List.Item>
    )}
  />
        </div>
        </Spin>
        </Content>
        </Layout>
        </div>
    );
  }
} 
 
export default Read;