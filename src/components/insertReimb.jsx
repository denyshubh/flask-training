import { useState } from 'react';
import axios from "axios";
import { toast } from 'react-toastify';
// import { Link } from "react-router-dom";


function InsertReimb(props) {
   
	
	// status text NOT NULL CHECK( status in ('pending','approved','denied')),
	// type text NOT NULL CHECK(type in ('Lodging','Travel','Food','Other')),
	// description VARCHAR(100) NOT NULL,
	// receipt BYTEA NOT NULL,
	// reimb_author SERIAL,
    // reimb_resolver SERIAL,

    const [reimbInfo, setReimbInfo] = useState({ reimbursement_amount: "", type:"", status: "", description: ""});

    function insertReimb(event) {
      axios({
        method: "POST",
        url:"/reimburse/insert",
        data: reimbInfo
      })
      .then((response) => {
        console.log(response)
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

    const handleChange = (event) => {  
        // console.log(event.target.name)
        // console.log(event.target.value)
        setReimbInfo({ ...reimbInfo, [event.target.name]: event.target.value });
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        insertReimb(reimbInfo);
        setReimbInfo({ 
            reimbursement_amount: "",
            type: "",
            status: "",
            description: "", 
        });
    }

    return (
        <section className="hero is-success is-fullheight">
        <div className="hero-body">
            <div className="container has-text-centered">
                <div className="column is-4 is-offset-4">
                    <h3 className="title has-text-black">Add Reimbersement Data</h3>
                    <hr className="login-hr"/>
                    <div className="box">
                        <form>
                            <div className="field">
                                <div className="control">
                                    <input 
                                      className="input is-large" 
                                      type="text" 
                                      placeholder="Reimbursement Amount"
                                      value={reimbInfo.reimbursement_amount}
                                      name='reimbursement_amount'
                                      autoFocus="" 
                                      onChange={handleChange}/>
                                </div>
                            </div>
                            
                            <div className="field">
                                <div className="control select">
                                        <select name='type' value={reimbInfo.type} onChange={handleChange} className="input is-large">
                                            <option value="Type">Type of Reimbursement</option>
                                            <option value="Lodging">Lodging</option>
                                            <option value="Travel">Travel</option>
                                            <option value="Food">Food</option>
                                            <option value="Other">Other</option>
                                        </select>

                                </div>
                            </div>

                            <div className="field">
                                <div className="control select">
                                        <select name='status' value={reimbInfo.status} onChange={handleChange} className="input is-large">
                                            <option value="Type">Status of Reimbursement</option>
                                            <option value="pending">pending</option>
                                            <option value="approved">approved</option>
                                            <option value="denied">denied</option>
                                        </select>

                                </div>
                            </div>
                            
                            <div className="field">
                                <div className="control">
                                    <input 
                                      name='description'
                                      className="input is-large" 
                                      type="text" 
                                      placeholder="Description"
                                      value={reimbInfo.description}
                                      onChange={handleChange}/>
                                </div>
                            </div>
                            
                            <button 
                              className="button is-block is-info is-large is-fullwidth"
                              onClick={handleSubmit}>
                                Submit 
                              <i className="fa fa-sign-in" aria-hidden="true"></i>
                            </button>
                        </form>
                    </div>
                    {/* <p className="has-text-grey">
                        <Link to='/login'>Sign In</Link>
                        <Link to='/help'>Need Help ?</Link>
                    </p> */}
                </div>
            </div>
        </div>
        </section>
      );
}

export default InsertReimb;
