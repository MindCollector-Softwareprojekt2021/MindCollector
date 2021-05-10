import axios from "axios";

export default () => {
  return axios.create({
    baseURL: "http://mezzox.pythonanywhere.com",
    withCredentials: false,
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*"
    },
  });
};
