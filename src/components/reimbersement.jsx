import { useState, useEffect } from 'react'
import axios from "axios";
// import { toast } from 'react-toastify';
import { Link } from "react-router-dom";

function Reimbersement(props) {

  const [data, setReimbData] = useState([])

  useEffect(() => {
    (async () => {
      const result = await axios({
        method: "GET",
        url:"/reimburse",
        headers: {
          Authorization: 'Bearer ' + props.token
        }
      });
      console.log(result)
      setReimbData(result.data.data);
    })();
  }, []);
  
  return (
    <div className="table-container hero-body">
        <h1>Reimbersement Data</h1>
        <table className="table">
        <tbody>
            <tr>
                <th><abbr title="ReimbID">Reimb Id</abbr></th>
                <th><abbr title="Status">Status</abbr></th>
                <th><abbr title="Type">Type</abbr></th>
                <th><abbr title="Amount">Amount</abbr></th>
                <th><abbr title="Description">Description</abbr></th>
                <th><abbr title="Submitted">Submitted Date</abbr></th>
                <th><abbr title="Resolved">Resolve Date</abbr></th>
                <th><abbr title="Author">Created By</abbr></th>
                <th><abbr title="Resolver">Resolved By</abbr></th>
            </tr>
            {data.map((item, i) => (
                <tr key={i}>
                    <td>{item.reimb_id}</td>
                    <td>{item.status}</td>
                    <td>{item.type}</td>
                    <td>{item.reimb_amount}</td>
                    <td>{item.description}</td>
                    <td>{item.submitted}</td>
                    <td>{item.resolved}</td>
                    <td>{item.reimb_author}</td>
                    <td>{item.reimb_resolver}</td>
                    <td>
                      <Link
                        to={{
                          pathname: "/reimburse/update",
                          search: `?reimbID=${item.reimb_id}`,
                        }}
                      >
                        <span><i class="fa-solid fa-pen-to-square"></i></span>
                      </Link>
                    </td>
                </tr>
            ))}
        </tbody>
        </table>
    </div>
  );
}

export default Reimbersement;
