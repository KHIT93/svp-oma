<template>
    <div>
        <v-container fluid>
            <v-layout row wrap>
                <v-flex md4 sm6 xs12 v-for="item in data" :key="item.id">
                    <v-card hover class="mb-2">
                        <v-card-text>WindFarm {{ (item.name) ? item.id + ' (' + item.name + ')' : item.id }}</v-card-text>
                        <v-card-actions>
                            <v-btn flat :to="'/windfarms/' + item.id">Show Details</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
    export default {
        data: function() {
            return {
                interval: null,
                data: [],
            }
        },
        methods: {
            loadData() {
                console.log('Polling server from dashboard component');
                axios.get('/webapi/windfarms/simple/').then(response => {
                    console.log(response.data.results);
                    this.data = response.data.results;
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
