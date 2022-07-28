import { useState } from 'react';
import axios from "axios";
import { toast } from 'react-toastify';


function Login(props) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    function logMeIn(event) {
      axios({
        method: "POST",
        url:"/login",
        data:{
          username: username,
          password: password
         }
      })
      .then((response) => {
        console.log(response)
        props.setToken(response.data.auth_token)
        toast.info(response.data.message)
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          toast.error(error.response.data.message);
          }
      })

      setUsername("")
      setPassword("")

      event.preventDefault()
    }

    return (
      <section className="hero is-success is-fullheight">
      <div className="hero-body">
          <div className="container has-text-centered">
              <div className="column is-4 is-offset-4">
                  <h3 className="title has-text-black">Login</h3>
                  <hr className="login-hr"/>
                  <p className="subtitle has-text-black">Please login to proceed.</p>
                  <div className="box">
                      <figure className="avatar">
                          <img 
                          src="https://raw.githubusercontent.com/mahwishubham/proj1/main/app/static/images/Login.jpg"
                          alt='Avatar'/>
                      </figure>
                      <form>
                          <div className="field">
                              <div className="control">
                                  <input 
                                    className="input is-large" 
                                    type="text" 
                                    placeholder="Your Username"
                                    value={username}
                                    autoFocus="" 
                                    onChange={({ target }) => setUsername(target.value)}/>
                              </div>
                          </div>

                          <div className="field">
                              <div className="control">
                                  <input 
                                    className="input is-large" 
                                    type="password" 
                                    placeholder="Your Password"
                                    value={password}
                                    onChange={({ target }) => setPassword(target.value)}/>
                              </div>
                          </div>
                          <div className="field">
                              <label className="checkbox">
                <input type="checkbox"/>
                Remember me
              </label>
                          </div>
                          <button 
                            className="button is-block is-info is-large is-fullwidth"
                            onClick={logMeIn}>
                              Login 
                            <i className="fa fa-sign-in" aria-hidden="true"></i>
                          </button>
                      </form>
                  </div>
                  <p className="has-text-grey">
                      <a href="../">Register</a> &nbsp;·&nbsp;
                      <a href="../">Forgot Password</a> &nbsp;·&nbsp;
                      <a href="../">Need Help?</a>
                  </p>
              </div>
          </div>
      </div>
      </section>
    );
}

export default Login;
