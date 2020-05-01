import Vue from "vue";
import App from "./App.vue";

require('pattern.css/dist/pattern.min.css')
require('shorthandcss/dist/shorthand.min.css')
require('nes.css/css/nes.css')

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
}).$mount("#app");
