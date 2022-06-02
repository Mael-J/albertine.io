import {Component } from 'react';
import { HashRouter as Router, Route, Routes, Link} from "react-router-dom";
import Landing from './pages/Landing';
import Funds from './pages/Funds';
import Home from './pages/Home';
import SideBar from './components/SideBar';
import Article from './pages/Article';
import Embed from './components/Embed'
class App extends Component { 
  render() {
    return (
      
        
      <Router>
      <Home />
      <SideBar />
         <Routes>
          
          <Route exact = {true} path="/" element= {<Landing />} />
          <Route path='/funds' element = {<Funds />}/>
          <Route path='/articles' element = {<Article />}/>
          <Route path='/pdf/manifeste' element = {<Embed />}/>
        </Routes>
      </Router>
      
    )
  }
}

export default App;
