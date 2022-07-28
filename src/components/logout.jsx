import axios from "axios";
import { toast } from "react-toastify";

function Logout(props) {

  function logMeOut() {
    axios({
      method: "POST",
      url:"/logout",
      headers: {
        Authorization: `Bearer ${props.token}`
      }
    })
    .then((response) => {
       props.removeToken()
       toast.info('User Logged Out Success!!')
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        toast.error(error.response.data.msg)
        }
    })}

    logMeOut()

    return(
      <h1>
        Please Login To View Data
      </h1>
    )
}

export default Logout;