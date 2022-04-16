import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Index from './pages/Index'
import './App.css';

const pageStyle = {
  backgroundColor: '#208c71'
};


function App() {
  return (
    <Router>
        <Routes>
          <Route exact path="/" element={<Index/>}/>
        </Routes>
    </Router>
  );
}

export default App;
