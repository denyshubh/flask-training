import axios from "axios";

function Header(props) {

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
        <header className="App-header">
            <img src='https://cdn.pixabay.com/photo/2017/05/29/23/02/logging-out-2355227_960_720.png' className="App-logo" alt="logo" />
            <button onClick={logMeOut}> 
                Logout
            </button>
        </header>
    )
}

export default Header;