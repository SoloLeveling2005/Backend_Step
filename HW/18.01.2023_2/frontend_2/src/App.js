// import logo from './logo.svg';
import './App.css';

import {
  BrowserRouter as Router,
  Route,
  Routes,
  // Layout
} from 'react-router-dom';
import Identification from './components/Identification';
import Home from './components/Home';

function App() {
  return (
    <Router>
      {/* <Layout> */}
        <Routes>
          <Route exact path="/" element={<Home/>}/>
          <Route exact path="/login" element={<Identification/>}/>
        </Routes>
      {/* </Layout> */}
    </Router>
  );
}
export default App;
