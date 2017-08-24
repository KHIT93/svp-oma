<template>
    <div>
        <v-container fluid v-if="isNumber(id)">
            <v-layout row wrap>
                <v-flex md4 sm6 xs12 v-for="item in data" :key="item.id">
                    <v-windturbine-card :item="item" @deleted="loadData"></v-windturbine-card>
                </v-flex>
            </v-layout>
        </v-container>
        <v-not-found v-else></v-not-found>
    </div>
</template>

<script>
    import NotFound from './NotFound.vue';
    import WindTurbine from '../components/WindTurbineCard.vue';
    export default {
        props: ['id'],
        data: function() {
            return {
                interval: null,
                data: [],
            }
        },
        components: {
            'v-not-found': NotFound,
            'v-windturbine-card': WindTurbine
        },
        methods: {
            loadData() {
                if(!isNaN(+this.id) && isFinite(this.id)) {
                    axios.get('/webapi/windfarms/' + this.id + "/").then(response => {
                        this.data = response.data.windturbine_set;
                    });
                }
            },
            isNumber(n) {
                return !isNaN(+n) && isFinite(n);
            },
            moment(str) {
                return window.moment(str);
            }
        },
        mounted() {
            if(!isNaN(+this.id) && isFinite(this.id)) {
                this.loadData();
            }
            this.interval = setInterval(function () {
                this.loadData();
            }.bind(this), 5000);
        },
        beforeDestroy() {
            clearInterval(this.interval);
        }
    }
</script>
