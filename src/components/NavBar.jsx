import { Link } from "react-router-dom";
function NavBar(props) {
  const is_logged_in = props.token != null ? true : false
  if (is_logged_in){
    return (
      <div className="hero-head">
          <nav className="navbar">
              <div className="container">
                  <div className="navbar-brand">
                      <Link className="navbar-item" to="#">
                          
                      </Link>
                      <span className="navbar-burger burger" data-target="navbarMenu">
                          <span>ERS</span>
                      </span>
                  </div>
                  <div id="navbarMenu" className="navbar-menu">
                      <div className="navbar-end">
                          <div className="tabs is-right">
                              <ul>
                                  <li className="is-active"><Link to='#'>Home</Link></li>
                                  <li><Link to="/reimburse">View Reimbursement</Link></li>
                                  <li><Link to="/logout">Log Out</Link></li>
                                  <li><Link to="/reimburse/insert">Add Reimbursement</Link></li>
                              </ul>
                          </div>
                      </div>
                  </div>
              </div>
          </nav>
      </div>
    );
  } else {
    return (
      <div className="hero-head">
        <nav className="navbar">
            <div className="container">
                <div className="navbar-brand">
                    <Link className="navbar-item" to="#">
                        
                    </Link>
                    <span className="navbar-burger burger" data-target="navbarMenu">
                        <span>ERS</span>
                    </span>
                </div>
                <div id="navbarMenu" className="navbar-menu">
                    <div className="navbar-end">
                        <div className="tabs is-right">
                            <ul>
                                <li className="is-active"><Link to="#">Home</Link></li>
                                <li><Link to="/login">Login</Link></li>
                                <li><Link to="/register">Register</Link></li>
                                <li><Link to="/help">Help</Link></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </nav>
    </div>
    );
  }
}

export default NavBar;