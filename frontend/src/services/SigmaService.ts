import http from "./AxiosService";

class SigmaService {
  logout() {
    return http.post("/api/logout");
  }

  getList() {
    return http.get<string>("/lists");
  }

  getBackends() {
    return http.get<[]>("/backends");
  }

  getConfigs() {
    return http.get<[]>("/configs");
  }

  // getLoggedInUser() {
  //   return http.get<User>("/user");
  // }
}
export default new SigmaService();
