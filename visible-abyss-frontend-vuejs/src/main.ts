import './assets/main.css'

import { createApp } from 'vue'

// import { createPinia } from 'pinia'
import stores from '@/stores'

import ArcoVue from "@arco-design/web-vue";
import ArcoVueIcon from "@arco-design/web-vue/es/icon";
import "@arco-design/web-vue/dist/arco.css";

import App from './App.vue'
import router from './router'

import i18n from "@/locale";

const app = createApp(App)

// app.use(createPinia())
app.use(stores)

app.use(router)
app.use(i18n)

app.use(ArcoVue,{
    // 用于改变使用组件时的前缀名称
    componentPrefix: 'arco'
})
app.use(ArcoVueIcon)

app.mount('#app')
