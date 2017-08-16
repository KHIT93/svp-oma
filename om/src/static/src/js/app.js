
window._ = require('lodash');

import Vue from 'vue';
import axios from 'axios';
import Vuetify from 'vuetify';
import VueRouter from 'vue-router';


window.Vue = Vue;
Vue.use(Vuetify);
Vue.use(VueRouter);

const routes = [
    //{ path: '/', component: Home, name: 'home' },


    /** Catchall route to display 404 page */
    //{ path: '*', component: NotFound }
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

/**
 * Next, we will create a fresh Vue application instance and attach it to
 * the page. Then, you may begin adding components to this application
 * or customize the JavaScript scaffolding to fit your unique needs.
 */

const app = new Vue({
    el: '#app',
    router,
    data:
    {
        menu: [
            { icon: 'home', title: 'Home', link: '/'},
            { icon: 'shopping_cart', title: 'Orders', link: '/orders'},
            { icon: 'contacts', title: 'Customers', link: '/customers'},
            { icon: 'book', title: 'Products', link: '/products'},
            { icon: 'loyalty', title: 'Categories', link: '/categories'},
            { icon: 'description', title: 'Pages', model: false, children: [
                { icon: 'description', title: 'Web pages', link: '/pages'},
                { icon: 'description', title: 'Menu', link: '/menu'},
            ]},
            { icon: 'settings', title: 'Configuration', model: false, children: [
                { icon: 'settings', title: 'Taxes', link: '/configuration/taxes'}
            ]},
        ],
        drawer: true,
        mini: false,
    }
});
