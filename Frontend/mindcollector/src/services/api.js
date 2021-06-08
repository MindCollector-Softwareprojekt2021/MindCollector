import axios from "axios";

export default () => {
  return axios.create({
    baseURL: "https://mccurly.pythonanywhere.com/api",
    withCredentials: false,
  });
};
