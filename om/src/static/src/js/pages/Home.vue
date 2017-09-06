<template>
        <v-container fluid>
            <v-layout row wrap>
                <v-flex md4 sm6 xs12 v-for="item in data" :key="item.id">
                    <v-windfarm-card :windfarm="item"></v-windfarm-card>
                </v-flex>
            </v-layout>
        </v-container>
</template>

<script>
    import WindFarmCard from '../components/WindFarmCard.vue';
    export default {
        data: function() {
            return {
                interval: null,
                data: [],
                has_error: false
            }
        },
        methods: {
            loadData() {
                console.log('Polling server from dashboard component');
                axios.get('/webapi/windfarms/simple/').then(response => {
                    this.data = response.data.results;
                }).catch(error => {
                    console.log(error);
                    if(!this.has_error) {
                        flash(error.toString());
                    }
                })
            }
        },
        components: {
            'v-windfarm-card': WindFarmCard
        },
        created() {
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
