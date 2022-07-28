import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Login from './components/login'
import Profile from './components/profile'
import Logout from './components/logout'
import useToken from './components/useToken'
import './App.css'
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {
  const { token, removeToken, setToken } = useToken();

  return (
    <BrowserRouter>
      <div className="App">
        <ToastContainer />
        {!token && token!=="" &&token!== undefined?  
        <Login setToken={setToken} />
        :(
          <>
            <Routes>
              <Route  exact path="/logout" element={<Logout token={removeToken}/>}></Route>
              <Route exact path="/profile" element={<Profile token={token} setToken={setToken}/>}></Route>
            </Routes>
          </>
        )}
      </div>
    </BrowserRouter>
  );
}

export default App;
