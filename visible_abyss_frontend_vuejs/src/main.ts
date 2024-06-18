import './assets/main.css'
import './assets/css/tailwind.css'

import { createApp} from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

// 显示「环境变量」
console.log(import.meta.env)

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
