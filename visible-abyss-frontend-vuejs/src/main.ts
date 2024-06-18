// ============================== 导入样式
import './assets/main.css'
import './assets/css/tailwind.css'
import '@arco-design/web-vue/dist/arco.css'

// ============================== 导入组件「VUE」
import { createApp } from 'vue'

// ============================== 导入组件「Pinia」
import { createPinia } from 'pinia'

// ============================== 导入组件「Arco.design」
import ArcoVue from '@arco-design/web-vue'


// ============================== 导入文件「VUE」
import App from '@/App.vue'
// ============================== 导入文件「路由」
import router from './router'

// ============================== 实例化「Vue」
const app = createApp(App)


// ============================== 「Vue」注册组件
// ------------------ Arco.design
app.use(ArcoVue,
  {
    // 用于改变使用组件时的前缀名称
    componentPrefix: 'arco'
  }
)

// ------------------ Pinia
app.use(createPinia())

// ------------------ 路由
app.use(router)


// ============================== 「Vue」挂载容器
app.mount('#app')
