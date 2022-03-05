import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from "./router";
import VueRouter from "vue-router"
import VueSweetalert2 from 'vue-sweetalert2';
// import Routes from "./router.js"
import VueSession from 'vue-session'


Vue.use(VueRouter)
Vue.use(VueSession)
Vue.use(VueSweetalert2)

Vue.config.productionTip = false

// const router = new VueRouter({
//   routes: Routes
// })

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
import { setupComponents } from "./config/setup-components";

setupComponents(Vue);
