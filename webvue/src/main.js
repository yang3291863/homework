import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/lib/theme-chalk/index.css'
import App from './App.vue'
import router from './router'
import Axios from 'axios'

const app = createApp(App)
app.config.globalProperties.$axios = Axios
app.use(router)
app.use(ElementPlus)
app.mount('#app')
