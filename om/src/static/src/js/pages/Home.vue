<template>
    <div>
        <v-container fluid>
            <v-layout row wrap>
                <v-flex md4 sm6 xs12 v-for="n in 12" :key="n">
                    <v-card hover class="mb-2">
                        <v-card-text>WindFarm {{ n }}</v-card-text>
                        <v-card-actions>
                            <v-btn flat to="n">Show Details</v-btn>
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
            }
        },
        methods: {
            loadData() {
                console.log('Polling server from dashboard component');
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
