import { useState } from 'react'
import axios from "axios";
import { toast } from 'react-toastify';

function Reimbersement(props) {

  const [reimbData, setReimbData] = useState(null)
  function getData() {
    axios({
      method: "GET",
      url:"/reimburse",
      headers: {
        Authorization: 'Bearer ' + props.token
      }
    })
    .then((response) => {
      const res =response.data
      toast.info(res.msg)
      console.log(res)
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        toast.error(error.response.data.msg)
        }
    })}

  return (
    <div className="Profile">

        <p>To get your profile details: </p><button onClick={getData}>Click me</button>
        {/* {setReimbData && <div>
              <p>Profile name: {profileData.profile_name}</p>
              <p>About me: {profileData.about_me}</p>
            </div>
        } */}

    </div>
  );
}

export default Reimbersement;
