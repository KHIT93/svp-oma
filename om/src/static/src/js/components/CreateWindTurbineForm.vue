<template>
    <v-card-text>
        <v-text-field label="Name" v-model="form.name"></v-text-field>
        <v-select
              :items="windfarms"
              v-model="form.windfarm"
              label="Select Windfarm"
              single-line
              item-text="display_name"
              item-value="id"
              bottom
        ></v-select>
        <v-text-field label="Longtitide" v-model="form.longtitude"></v-text-field>
        <v-text-field label="Latitude" v-model="form.latitude"></v-text-field>
        <v-text-field label="IP Address" v-model="form.ip_address"></v-text-field>
        <v-btn flat primary @click.native="save">Save</v-btn>
    </v-card-text>
</template>

<script>
import Form from '../classes/Form';
    export default {
        data: () => {
            return {
                form: new Form({
                    name: "",
                    windfarm: null,
                    longtitude: 0,
                    latitude: 0,
                    ip_address: "0.0.0.0"
                }),
                windfarms: []
            }
        },
        mounted() {
            this.getWindFarms();
        },
        methods: {
            getWindFarms() {
                axios.get('/webapi/windfarms/simple/').then(response => {
                    console.log('Getting windfarms from webapi');
                    this.windfarms = response.data.results;
                });
            },
            save() {
                this.form.post('/webapi/windturbines/').then(response => {
                    this.$emit('saved');
                }).catch(error => {
                    console.log('Error while posting to server from create-windturbine-form');
                    console.log(error);
                });
            }
        }
    }
</script>
