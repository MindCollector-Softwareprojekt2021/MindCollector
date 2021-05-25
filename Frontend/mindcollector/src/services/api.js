import axios from "axios";

export default () => {
  return axios.create({
    baseURL: "https://mccurly.pythonanywhere.com/api",
    withCredentials: false,
  });
};

/*
export default () => {
  return axios.create({
    baseURL: "https://mezzox.pythonanywhere.com",
    withCredentials: false,
  });
};*/
