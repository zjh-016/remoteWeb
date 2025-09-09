import { createApp } from 'vue';
import App from './App.vue';
import router from '../src/router/router'; // 引入路由配置
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/reset.css';


const app = createApp(App);
app.use(router);
app.use(Antd);
app.mount('#app');