

import Vue from 'vue';
import axios from 'axios';
import Vuetify from 'vuetify';
import VueRouter from 'vue-router';
import * as moment from 'moment';

import AppNavigation from './components/AppNavigation.vue';


window.Vue = Vue;
Vue.use(Vuetify);
Vue.use(VueRouter);

let Cookies = require('js-cookie');

/**
 * Import Vue components to use for Vue-Router
 */
import Home from './pages/Home.vue';
import WindFarm from './pages/WindFarm.vue';
import WindTurbine from './pages/WindTurbine.vue';
import AuditLogList from './pages/AuditLogList.vue';
import NotFound from './pages/NotFound.vue';

/**
 * Define routes used with Vue-Router
 */
const routes = [
    { path: '/', component: Home, name: 'home' },
    { path: '/windfarms/:id', component: WindFarm, name: 'windfarm.detail', props:true },
    { path: '/windturbines/:id', component: WindTurbine, name: 'windturbine.detail', props:true },
    { path: '/log', component: AuditLogList, name: 'log.list'},

    /** Catchall route to display 404 page */
    { path: '*', component: NotFound, name: 'not_found' }
];

const router = new VueRouter({
    routes
});

/**
 * We'll load the axios HTTP library which allows us to easily issue requests
 * to our Laravel back-end. This library automatically handles sending the
 * CSRF token as a header based on the value of the "XSRF" token cookie.
 */

 window.axios = axios;

 window.axios.defaults.headers.common['X-CSRFToken'] = Cookies.get('csrftoken');
 window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

 /**
  * Debug code for logging AJAX calls to the console
  */
window.axios.interceptors.request.use(request => {
    console.log('Starting Request', request);
    return request;
});

function redirect(url) {
    window.location.href = url;
}

window.moment = moment;

/**
 * Next, we will create a fresh Vue application instance and attach it to
 * the page. Then, you may begin adding components to this application
 * or customize the JavaScript scaffolding to fit your unique needs.
 */

const app = new Vue({
    el: '#app',
    router,
    components: {
        'v-oma-navigation': AppNavigation
    }
});
