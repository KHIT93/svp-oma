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
              required
        ></v-select>
        <v-text-field label="Longtitide" v-model="form.longtitude" required></v-text-field>
        <v-text-field label="Latitude" v-model="form.latitude" required></v-text-field>
        <v-text-field label="IP Address" v-model="form.ip_address"></v-text-field>
        <v-text-field label="API token" v-model="form.api_token"></v-text-field>
        <v-btn flat primary @click.native="save" :loading="processing"><v-icon v-if="processing">loading</v-icon> <span v-else>Save</span></v-btn>
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
                    ip_address: "0.0.0.0",
                    api_token: ""
                }),
                windfarms: [],
                processing: false,
            }
        },
        created() {
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
                this.processing = true;
                this.form.post('/webapi/windturbines/').then(response => {
                    this.$emit('saved');
                    flash('The windturbine has been created');
                    this.processing = false;
                }).catch(error => {
                    console.log('Error while posting to server from create-windturbine-form');
                    flash('There was an error when trying to create the new windturbine.<br/>' + error);
                    console.log(error);
                    this.processing = false;
                });
            }
        }
    }
</script>
