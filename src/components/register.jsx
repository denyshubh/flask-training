import { useState } from 'react';
import axios from "axios";
import { toast } from 'react-toastify';
import { Link } from "react-router-dom";


function Register(props) {

    const [userInfo, setUserInfo] = useState({ username: "", password: "", role: "", first_name: "", last_name: "", gender: "", phone_number: "", email_address: ""});

    function registerUser(event) {
      axios({
        method: "POST",
        url:"/register",
        data: userInfo
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

      event.preventDefault()
    }
    
    // const { username, password, role, first_name, last_name, gender, phone_number, email_address} = userInfo

    const handleChange = (event) => {
        console.log(event)
        setUserInfo({ ...userInfo, [event.target.name]: event.target.value });
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        registerUser(userInfo);
        setUserInfo({ 
            username: "",
            password: "",
            role: "",
            first_name: "",
            last_name: "",
            gender: "",
            phone_number: "",
            email_address: ""
        });
    }

    return (
        <section className="hero is-success is-fullheight">
        <div className="hero-body">
            <div className="container has-text-centered">
                <div className="column is-4 is-offset-4">
                    <h3 className="title has-text-black">Register User</h3>
                    <hr className="login-hr"/>
                    <p className="subtitle has-text-black">Please Register New User Here</p>
                    <div className="box">
                        <form>
                            <div className="field">
                                <div className="control">
                                    <input 
                                      className="input is-large" 
                                      type="text" 
                                      placeholder="Your Username"
                                      value={userInfo.username}
                                      autoFocus="" 
                                      onChange={handleChange}/>
                                </div>
                            </div>
  
                            <div className="field">
                                <div className="control">
                                    <input 
                                      className="input is-large" 
                                      type="password" 
                                      placeholder="Your Password"
                                      value={userInfo.password}
                                      onChange={handleChange}/>
                                </div>
                            </div>

                            <div className="field">
                                <div className="control">
                                    <input 
                                      className="input is-large" 
                                      type="email" 
                                      placeholder="Your Email"
                                      value={userInfo.email_address}
                                      onChange={handleChange}/>
                                </div>
                            </div>

                            <div className="field">
                                <div className="control">
                                    <label>
                                        Select Your Role:
                                        <select value={userInfo.role} onChange={handleChange}>
                                            <option value="employee">Employee</option>
                                            <option value="finance_manager">Finance Manager</option>
                                        </select>
                                    </label>
                                </div>
                            </div>

                            
                            <div className="field">
                                <div className="control">
                                    <label>
                                        Gender:
                                        <select value={userInfo.gender} onChange={handleChange}>
                                            <option value="male">Male</option>
                                            <option value="female">Female</option>
                                            <option value="other">Other</option>
                                        </select>
                                    </label>
                                </div>
                            </div>
                            
                            <div className="field">
                                <div className="control">
                                    <input 
                                      className="input is-large" 
                                      type="text" 
                                      placeholder="First Name"
                                      value={userInfo.first_name}
                                      onChange={handleChange}/>
                                </div>
                            </div>

                            
                            <div className="field">
                                <div className="control">
                                    <input 
                                      className="input is-large" 
                                      type="text" 
                                      placeholder="Last Name"
                                      value={userInfo.last_name}
                                      onChange={handleChange}/>
                                </div>
                            </div>

                            
                            <div className="field">
                                <div className="control">
                                    <input 
                                      className="input is-large" 
                                      type="password" 
                                      placeholder="US Phone Number"
                                      value={userInfo.phone_number}
                                      onChange={handleChange}/>
                                </div>
                            </div>
                            
                            <button 
                              className="button is-block is-info is-large is-fullwidth"
                              onClick={handleSubmit}>
                                Register 
                              <i className="fa fa-sign-in" aria-hidden="true"></i>
                            </button>
                        </form>
                    </div>
                    <p className="has-text-grey">
                        <Link to='/login'>Sign In</Link>
                        <Link to='/help'>Need Help ?</Link>
                    </p>
                </div>
            </div>
        </div>
        </section>
      );
}

export default Register;
