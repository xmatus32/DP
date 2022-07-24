import axios from "axios";

const config = {
  baseURL: "http://192.168.0.108:7000/",
  headers: {
    "Content-type": "application/json",
  },
  crossDomain: true,
};
const http = axios.create(config);
export default http;
