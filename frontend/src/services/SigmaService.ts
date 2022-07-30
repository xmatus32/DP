import http from "./AxiosService";

class SigmaService {
  convert(target: string, config: string, rule: string) {
    return http.post<string>("/", {
      target: target,
      config: config,
      rule: rule,
    });
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
