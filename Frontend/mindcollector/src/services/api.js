import axios from 'axios';

export default ()=>{
  return axios.create({
    baseURL: 'https://my-json-server.typicode.com/mlemac/tmpjsonDB',
    withCredentials: false,
    headers:{
      Accept: "application/json",
      "Content-Type": "application/json"
    }
  })
};