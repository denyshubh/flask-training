import axios from "axios";

function Logout(props) {

  function logMeOut() {
    axios({
      method: "POST",
      url:"/logout",
    })
    .then((response) => {
       props.token()
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}

    return(
      <button 
        className="button is-block is-info is-large is-fullwidth"
        onClick={logMeOut}>
          Logout 
        <i className="fa fa-sign-in" aria-hidden="true"></i>
      </button>
    )
}

export default Logout;