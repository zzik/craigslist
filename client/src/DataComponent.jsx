import { useState, useEffect } from 'react';

const DataComponent = () => {
  let [data, setData] = useState([]);

  useEffect(() => {
    // Function to fetch data from Flask API
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/data');
        const jsonData = await response.json();

        setData(jsonData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    // Call the fetch function
    fetchData();
  }, []);


  return (
    <div>
      <h1>Data from MySQL</h1>
      
      <input type='checkbox' />Central Time Zone
      <ul>
        {data.map((item) => (
          <li key={item.id} className={item.checked ? 'checked' : 'unchecked'}>
            <a href={item.url}>
                <p>{item.name}</p>
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DataComponent;
