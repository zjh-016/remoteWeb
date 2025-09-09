import axios from "axios";

// 创建 Axios 实例
const service = axios.create({
  // 配置基础 URL 和超时时间等
  baseURL: 'http://127.0.0.1:5000', // 后端 API 的基础 URL
  timeout: 5000, // 请求超时时间
});
// eslint-disable-next-line no-unused-vars
export function getAction(url, params) {
    return service.get(url, {
      params: params, // URL 参数
    });
}
// eslint-disable-next-line no-unused-vars
export function postAction(url, data) {
    return service.post(url, data);
}

