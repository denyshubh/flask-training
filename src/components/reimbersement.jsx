import { useState, useEffect } from 'react'
import axios from "axios";
// import { toast } from 'react-toastify';
import { useTable } from "react-table";
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
  // id: 'reimb_author', accessor: ƒ, …}
  // 1: {Header: 'Submitted', parent: {…}, depth: 1, id: 'submitted', accessor: ƒ, …}
  // 2: {Header: 'Resolved', parent: {…}, depth: 1, id: 'resolved', accessor: ƒ, …}
  // 3: {Header: 'Reimbersement Amount', parent: {…}, depth: 1, id: 'amount', accessor: ƒ, …}
  // 4: {Header: 'Status', parent: {…}, depth: 1, id: 'status', accessor: ƒ, …}
  // 5: {Header: 'Type', parent: {…}, depth: 1, id: 'type', accessor: ƒ, …}
  // 6: {Header: 'Author', parent: {…}, depth: 1, id: 'reimb_author', accessor: ƒ, …}
  // 7: {Header: 'Resolver', parent: {…}, depth: 1, id: 'reimb_resolver'
  return (
    <div className="table-container hero-body">
        <h1>Reimbersement Data</h1>
        <table className="table">
        <tbody>
            <tr>
                <th><abbr title="Position">Reimb Id</abbr></th>
                <th><abbr title="Position">Status</abbr></th>
                <th><abbr title="Position">Type</abbr></th>
                <th><abbr title="Position">Amount</abbr></th>
            </tr>
            {data.map((item, i) => (
                <tr key={i}>
                    <td>{item.reimb_id}</td>
                    <td>{item.status}</td>
                    <td>{item.type}</td>
                    <td>{item.reimb_amount}</td>
                </tr>
            ))}
        </tbody>
        </table>
    </div>
  );
}

export default Reimbersement;
