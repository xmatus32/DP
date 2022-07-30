import axios from "axios";
import json from "../../package.json";

const config = {
  baseURL: json.urlProd,
  headers: {
    "Content-type": "application/json",
  },
  crossDomain: true,
};
const http = axios.create(config);
export default http;
