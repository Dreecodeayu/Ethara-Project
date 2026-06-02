import axios from "axios";

const api = axios.create({
  baseURL: "https://ethara-project-z0zh.onrender.com"
});

export default api;