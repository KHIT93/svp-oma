<template>
    <div>
        <v-container fluid v-if="isNumber(id)">
            <v-layout row wrap>
                <v-flex md4 sm6 xs12 v-for="item in data" :key="item.id">
                    <v-card hover class="mb-2">
                        <v-card-text>WindTurbine {{ (item.name) ? item.id + ' (' + item.name + ')' : item.id }}</v-card-text>
                        <v-card-actions>
                            <v-btn flat>Show details</v-btn>
                            <v-btn flat>Start</v-btn>
                            <v-btn flat>Stop</v-btn>
                            <small :title="item.last_connection">
                                {{ (item.last_connection == "Never") ? "No information has been recieved" : "Last connection was " + moment(item.last_connection).fromNow() }}
                            </small>
                        </v-card-actions>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
        <v-not-found v-else></v-not-found>
    </div>
</template>

<script>
    import NotFound from './NotFound.vue';
    export default {
        props: ['id'],
        data: function() {
            return {
                interval: null,
                data: [],
            }
        },
        components: {
            'v-not-found': NotFound
        },
        methods: {
            loadData() {
                if(!isNaN(+this.id) && isFinite(this.id)) {
                    console.log('Polling server from windfarm component with id ' + this.id);
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
