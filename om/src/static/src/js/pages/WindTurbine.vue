<template>
    <div>
        <v-card>
            <v-card-actions>
                <v-btn flat title="Start" success @click.stop="startWindTurbine"><v-icon success>power_settings_new</v-icon> Start</v-btn>
                <v-btn flat title="Stop" error @click.stop="stopWindTurbine"><v-icon error>power_settings_new</v-icon> Stop</v-btn>
                <v-btn flat title="Edit" @click.stop="readonly = !readonly"><v-icon>edit</v-icon> Edit</v-btn>
                <v-btn flat title="Delete" @click.stop="dialog = true"><v-icon>delete</v-icon> Delete</v-btn>
            </v-card-actions>
            <v-card-title primary-title>
                <h3 class="headline mb-0 mr-2">Windturbine {{ windturbine.display_name }}</h3>
                <small :title="windturbine.last_connection">
                    {{ (windturbine.last_connection == "Never") ? "No information has been recieved" : "Last connection was " + moment(windturbine.last_connection).fromNow() }}
                </small>
                <small v-if="windturbine.brakes_active">
                    Brakes are currently active
                </small>
            </v-card-title>
            <v-card-text>
                <v-container fluid>
                    <v-layout row>
                        <v-flex sm2 xs4>
                            <v-subheader>Name</v-subheader>
                        </v-flex>
                        <v-flex xs8>
                            <v-subheader v-show="readonly">{{ windturbine.name }}</v-subheader>
                            <v-text-field v-model="form.name" hint="Insert the descriptive name of this windturbine" v-show="!readonly" :readonly="readonly"></v-text-field>
                        </v-flex>
                    </v-layout>
                    <v-layout row>
                        <v-flex sm2 xs4>
                            <v-subheader>Windfarm</v-subheader>
                        </v-flex>
                        <v-flex xs8>
                            <v-subheader v-show="readonly">{{ windturbine.windfarm }}</v-subheader>
                            <v-select
                                  :items="windfarms"
                                  v-model="form.windfarm"
                                  label="Select Windfarm"
                                  single-line
                                  item-text="display_name"
                                  item-value="id"
                                  bottom
                                  required
                                  v-show="!readonly" :readonly="readonly"
                            ></v-select>
                        </v-flex>
                    </v-layout>
                    <v-layout row>
                        <v-flex sm2 xs4>
                            <v-subheader>Longtitude</v-subheader>
                        </v-flex>
                        <v-flex xs8>
                            <v-subheader v-show="readonly">{{ windturbine.longtitude }}</v-subheader>
                            <v-text-field v-model="form.longtitude" hint="Insert the geographic longtitude of this windturbine" v-show="!readonly" :readonly="readonly" required></v-text-field>
                        </v-flex>
                    </v-layout>
                    <v-layout row>
                        <v-flex sm2 xs4>
                            <v-subheader>Latitude</v-subheader>
                        </v-flex>
                        <v-flex xs8>
                            <v-subheader v-show="readonly">{{ windturbine.latitude }}</v-subheader>
                            <v-text-field v-model="form.latitude" hint="Insert the geographic lattitude of this windturbine" v-show="!readonly" :readonly="readonly" required></v-text-field>
                        </v-flex>
                    </v-layout>
                    <v-layout row>
                        <v-flex sm2 xs4>
                            <v-subheader>IP Address</v-subheader>
                        </v-flex>
                        <v-flex xs8>
                            <v-subheader v-show="readonly">{{ windturbine.ip_address }}</v-subheader>
                            <v-text-field v-model="form.ip_address" hint="Insert the IP address of this windturbine" v-show="!readonly" :readonly="readonly"></v-text-field>
                        </v-flex>
                    </v-layout>
                    <v-layout row>
                        <v-flex sm2 xs4>
                            <v-subheader>API Token</v-subheader>
                        </v-flex>
                        <v-flex xs8>
                            <v-subheader v-show="readonly">{{ windturbine.api_token }}</v-subheader>
                            <v-text-field v-model="form.api_token" hint="Insert the descriptive name of this windturbine" v-show="!readonly" :readonly="readonly"></v-text-field>
                        </v-flex>
                    </v-layout>
                    <v-fab-transition>
                      <v-btn
                        class="green"
                        fab
                        dark
                        small
                        absolute
                        bottom
                        left
                        v-show="changed"
                        @click.native="save"
                      >
                        <v-icon>save</v-icon>
                      </v-btn>
                    </v-fab-transition>
                </v-container>
            </v-card-text>
        </v-card>
        <v-dialog v-model="dialog" persistent>
            <v-card>
                <v-card-title>Delete Windturbine {{ windturbine.display_name }}</v-card-title>
                <v-card-text>Are you sure that you want to delete {{ windturbine.display_name }}</v-card-text>
                <v-card-actions>
                    <v-btn class="green--text darken-1" flat @click.native="deleteItem">Yes</v-btn>
                    <v-btn class="red--text darken-1" flat @click.native="cancelDelete">No</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <v-windturbine-data-card :windturbinedata="windturbine_data" :windturbine="windturbine"></v-windturbine-data-card>
        <v-windturbine-errors-card @changed="toggleWindturbineErrors" @resolved="refresh" :windturbineerrors="windturbine_errors" :windturbine="windturbine"></v-windturbine-errors-card>
        <v-windturbine-settings-card @saved="getWindturbineSettings" :windturbine="windturbine" :windturbinesettings="windturbine_settings" :form="windturbine_settings_form"></v-windturbine-settings-card>
    </div>
</template>

<script>
    import Form from '../classes/Form';
    import WindTurbineDataCard from '../components/WindTurbineDataCard.vue';
    import WindTurbineSettingsCard from '../components/WindTurbineSettingsCard.vue';
    import WindTurbineErrorCard from '../components/WindTurbineErrorCard.vue';
    export default {
        props: ['id'],
        data: () => {
            return {
                windturbine: {},
                form: new Form({}),
                dialog: false,
                readonly: true,
                windfarms: [],
                windturbine_data: [],
                windturbine_errors: [],
                windturbine_settings: {},
                windturbine_settings_form: new Form({}),
                processing: false,
                interval: null,
                show_all_errors: false,
            }
        },
        created() {
            this.getItem();
            this.getWindturbineSettings();
            this.getWindturbineData();
            this.getWindturbineErrors();
            this.getWindfarms();
        },
        computed: {
            changed() {
                if(this.form.changed()) {
                    return true;
                }
                else {
                    return false;
                }
            }
        },
        components: {
            'v-windturbine-data-card': WindTurbineDataCard,
            'v-windturbine-errors-card': WindTurbineErrorCard,
            'v-windturbine-settings-card': WindTurbineSettingsCard
        },
        methods: {
            refresh() {
                this.getWindturbineSettings();
                this.getWindturbineErrors();
            },
            getItem() {
                axios.get('/webapi/windturbines/' + this.id + '/').then(response => {
                    this.windturbine = response.data;
                    this.form = new Form({
                        id: this.windturbine.id,
                        name: this.windturbine.name,
                        longtitude: this.windturbine.longtitude,
                        latitude: this.windturbine.latitude,
                        windfarm: this.windturbine.windfarm,
                        ip_address: this.windturbine.ip_address,
                        api_token: this.windturbine.api_token
                    });
                }).catch(error => {
                    flash('There was an error while getting the details of the windturbine: ' + error.toString());
                    console.log(error);
                });
            },
            getWindfarms() {
                axios.get('/webapi/windfarms/simple/').then(response => {
                    this.windfarms = response.data.results;
                }).catch(error => {
                    flash('There was an error while getting the list of windfarms: ' + error.toString());
                    console.log(error);
                })
            },
            getWindturbineData() {
                axios.get('/webapi/windturbine-data/?windturbine=' + this.id).then(response => {
                    this.windturbine_data = response.data.results;
                }).catch(error => {
                    flash('There was an error while getting the data for the windturbine: ' + error.toString());
                    console.log(error);
                })
            },
            getWindturbineErrors(all = false) {
                let url = '/webapi/windturbine-errors/?windturbine=' + this.id;
                if(!all) {
                    url += '&unhandled';
                }
                axios.get(url).then(response => {
                    this.windturbine_errors = response.data.results;
                }).catch(error => {
                    flash('There was an issue while getting the errors for the windturbine: ' + error.toString());
                    console.log(error);
                })
            },
            getWindturbineSettings() {
                axios.get('/webapi/windturbine-settings/?windturbine=' + this.id).then(response => {
                    this.windturbine_settings = response.data[0];
                    if(this.windturbine_settings.id) {
                        this.windturbine_settings_form = new Form({
                            state: this.windturbine_settings.state,
                            max_rpm_generator: this.windturbine_settings.max_rpm_generator,
                            max_temp_gearbox: this.windturbine_settings.max_temp_gearbox,
                            max_temp_generator: this.windturbine_settings.max_temp_generator,
                            windturbine: this.id,
                            brake: this.windturbine_settings.brake,
                            wing_angle: this.windturbine_settings.wing_angle
                        });
                    }
                    else {
                        this.windturbine_settings_form = new Form({
                            state: "",
                            max_rpm_generator: "",
                            max_temp_gearbox: "",
                            max_temp_generator: "",
                            brake: false,
                            wing_angle: 0,
                            windturbine: this.id
                        });
                    }
                }).catch(error => {
                    flash('There was an error while getting the settings of the windturbine: ' + error.toString());
                    console.log(error);
                })
            },
            moment(str) {
                return window.moment(str);
            },
            save() {
                if(this.form.changed()) {
                    this.form.put('/webapi/windturbines/' + this.form.id + '/').then(response => {
                        this.readonly = true;
                        this.getItem();
                        flash('Changes have been saved');
                        this.processing = false;
                    }).catch(error => {
                        flash('Changes could not be saved. Please consult the logs for further details');
                        console.log(error);
                        this.processing = false;
                    })
                }
                else {
                    console.log('The form data has not changed, so nothing can be saved');
                }
            },
            cancelDelete() {
                this.dialog = false;
            },
            deleteItem() {
                this.form.delete('/webapi/windturbines/' + this.windturbine.id + '/').then(response => {
                    //router.push('home');
                    flash('The windturbine was succesfully deleted');
                    redirect('/');
                    //window.location.href = "/";
                }).catch(error => {
                    flash('The windturbine could not be deleted. Please consult the logs for further details.');
                    console.log(error);
                })
            },
            startWindTurbine() {
                axios.patch('/webapi/windturbine-settings/' + this.windturbine_settings.id + '/', { 'state': 1 }).then(response => {
                    flash('The command to start the windturbine has been succesfully sent');
                    this.getWindturbineSettings();
                }).catch( error => {
                    flash('There was an error while trying to send a start command to the turbine. Please consult the log to find out what the issue is');
                });
            },
            stopWindTurbine() {
                axios.patch('/webapi/windturbine-settings/' + this.windturbine_settings.id + '/', { 'state': 0 }).then(response => {
                    flash('The command to stop the windturbine has been succesfully sent');
                    this.getWindturbineSettings();
                }).catch( error => {
                    flash('There was an error while trying to send a stop command to the turbine. Please consult the log to find out what the issue is');
                });
            },
            toggleWindturbineErrors() {
                this.show_all_errors = !this.show_all_errors;
                this.getWindturbineErrors(this.show_all_errors);
            },
        },
        beforeDestroy() {
            clearInterval(this.interval);
        }
    }
</script>
