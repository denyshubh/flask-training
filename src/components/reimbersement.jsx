import { useMemo, useState, useEffect } from 'react'
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
  
  // function getData() {

  //   axios({
  //     method: "GET",
  //     url:"/reimburse",
  //     headers: {
  //       Authorization: 'Bearer ' + props.token
  //     }
  //   })
  //   .then((response) => {
  //     const res  = response.data
  //     console.log(res)
  //     setReimbData({ ...res})
  //     toast.info(response.statusText)
  //   }).catch((error) => {
  //     if (error.response) {
  //       console.log(error.response)
  //       console.log(error.response.status)
  //       console.log(error.response.headers)
  //       toast.error(error.response.data.msg)
  //       }
  //   })
  //   // event.preventDefault()
  // }
  // getData()
  const columns = useMemo(
    () => [
      {
        Header: "User Info",
        // First group columns
        columns: [
          {
            Header: "User Id",
            accessor: "show.user_id"
          },
          {
            Header: "Fisrt Name",
            accessor: "show.first_name"
          },
          {
            Header: "Last Name",
            accessor: "show.last_name"
          },
          {
            Header: "Gender",
            accessor: "show.gender"
          },
        ]
      },
      {
        // Second group - Details
        Header: "Details",
        // Second group columns
        columns: [
          {
            Header: "Reimbersement Amount",
            accessor: "show.amount"
          },
          {
            Header: "Status",
            accessor: "show.status"
          },
          {
            Header: "Type",
            accessor: "show.type"
          },
          {
            Header: "Author",
            accessor: "show.author"
          },
          {
            Header: "Resolver",
            accessor: "show.resolver"
          }
        ]
      }
    ],
    []
  );
    // Use the state and functions returned from useTable to build your UI
  const {
      getTableProps,
      getTableBodyProps,
      headerGroups,
      rows,
      prepareRow,
    } = useTable({
      columns,
      data,
    })
  
    // Render the UI for your table
    return (
      <table {...getTableProps()}>
        <thead>
          {headerGroups.map(headerGroup => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map(column => (
                <th {...column.getHeaderProps()}>{column.render('Header')}</th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody {...getTableBodyProps()}>
          {rows.map((row, i) => {
            prepareRow(row)
            return (
              <tr {...row.getRowProps()}>
                {row.cells.map(cell => {
                  return <td {...cell.getCellProps()}>{cell.render('Cell')}</td>
                })}
              </tr>
            )
          })}
        </tbody>
      </table>
    )
}

export default Reimbersement;
