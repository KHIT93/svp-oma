<template>
    <div>
        <v-container fluid>
            <v-layout row wrap>
                <v-flex md4 sm6 xs12 v-for="item in data" :key="item.id">
                    <v-card hover class="mb-2">
                        <v-card-text>WindTurbine {{ (item.name) ? item.id + ' (' + item.name + ')' : item.id }}</v-card-text>
                        <v-card-actions>
                            <v-btn flat>Show details</v-btn>
                            <v-btn flat>Start</v-btn>
                            <v-btn flat>Stop</v-btn>
                            <small>Last reply 5 miuntes ago</small>
                        </v-card-actions>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
    export default {
        props: ['id'],
        data: function() {
            return {
                interval: null,
                data: [],
            }
        },
        methods: {
            loadData() {
                console.log('Polling server from windfarm component with id ' + this.id);
                axios.get('/webapi/windfarms/' + this.id).then(response => {
                    this.data = response.data.windturbine_set;
                })
            }
        },
        mounted() {
            this.loadData();

            this.interval = setInterval(function () {
                this.loadData();
            }.bind(this), 5000);
        },
        beforeDestroy() {
            clearInterval(this.interval);
        }
    }
</script>
