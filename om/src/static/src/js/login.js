import Vue from 'vue';
import axios from 'axios';
import Vuetify from 'vuetify';


window.Vue = Vue;
Vue.use(Vuetify);

let Cookies = require('js-cookie');

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
if(process.env.NODE_ENV != "production") {
    window.axios.interceptors.request.use(request => {
        console.log('Starting Request', request);
        return request;
    });
}

function redirect(url) {
    window.location.href = url;
}

/**
 * Next, we will create a fresh Vue application instance and attach it to
 * the page. Then, you may begin adding components to this application
 * or customize the JavaScript scaffolding to fit your unique needs.
 */

const app = new Vue({
    el: '#app',
    data: {
        loading: false
    }
});
