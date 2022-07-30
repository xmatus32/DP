import axios from "axios";
import jsooon from "../../package.json";

const config = {
  baseURL: jsooon.urlProd,
  headers: {
    "Content-type": "application/json",
  },
  crossDomain: true,
};
const http = axios.create(config);
export default http;
