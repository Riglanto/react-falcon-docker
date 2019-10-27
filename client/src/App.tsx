import React from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';
import './App.css';

const URL = 'http://localhost:5000/data'
class App extends React.Component {
  state = { data: [] }

  componentDidMount() {
    fetch(URL)
      .then(response => response.json())
      .then(data => this.setState({ data }))
  }

  render() {
    const { data } = this.state
    return (
      <LineChart width={800} height={400} data={data}>
        <Line type="monotone" dataKey="yield" stroke="#8884d8" />
        <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
      </LineChart>
    )
  }
}

export default App;
