// src/router/router.js
import { createRouter, createWebHistory } from 'vue-router'

const routes = []

// 1. 使用 require.context 获取所有 .vue 文件
const pages = require.context('@/views', true, /\.vue$/)

pages.keys().forEach(filePath => {
  // 2. 转换路径（示例：./Home.vue → home）
  const routeName = filePath
    .replace(/^\.\//, '')     // 移除开头的 ./
    .replace(/\.vue$/, '')    // 移除 .vue 后缀
    // .toLowerCase()            // 统一小写（可选）

  // 3. 排除特定文件（如以 _ 开头的组件）
  if (routeName.startsWith('_')) return

  // 4. 生成路由
  routes.push({
    path: `/${routeName}`,    // 路径：/home
    name: routeName,
    component: () => import(`@/views/${routeName}.vue`)
  })
})

// 5. 添加根路径重定向到 Home
routes.push({
  path: '/',
  redirect: '/home' // 访问根路径时跳转到 /home
})

const router = createRouter({
  history: createWebHistory(),
  routes
})

console.log(routes)

export default router