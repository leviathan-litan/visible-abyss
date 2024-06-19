// =========================== 样式库
import './assets/main.css'
import './assets/css/tailwind.css'
import '@arco-design/web-vue/dist/arco.css'

// =========================== 导入包
import { createApp} from 'vue'
// import { createPinia } from 'pinia'

// =========================== Arco.design
import ArcoVue from "@arco-design/web-vue";
import ArcoVueIcon from "@arco-design/web-vue/es/icon"

// SVG图标
import "virtual:svg-icons-register"

// =========================== 导入文件

// --- 实例化对象
import App from './App.vue'

// --- 路由
import router from './router'

// --- 国际化支持
import i18n from '@/i18n/index'

// --- 持久化「Pinia」
import store from './stores'

// =========================== 测试
// 显示「环境变量」
console.log(import.meta.env)

// =========================== 实例化
const app = createApp(App)

// =========================== 注册到「Vue.JS」实例
app.use(ArcoVue, {
    componentPrefix: 'arco'
})
app.use(ArcoVueIcon)
// app.use(createPinia())
app.use(router)
app.use(i18n)
app.use(store)

// =========================== 挂载「Vue.JS」实例到「DOM容器」
app.mount('#app')
