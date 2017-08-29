<template>
    <v-card class="mt-4">
        <v-card-actions>
            <v-btn flat title="Edit" @click.stop="readonly = !readonly"><v-icon>edit</v-icon> Edit</v-btn>
        </v-card-actions>
        <v-card-title primary-title>
            <h3 class="headline mb-0 mr-2">Settings for turbine {{ windturbine.display_name }}</h3>
        </v-card-title>
        <v-card-text v-if="!windturbinesettings.id">
            Currently no settings are registered for this turbine
        </v-card-text>
        <v-card-text>
            <v-container fluid>
                <v-layout row>
                    <v-flex sm3 xs4>
                        <v-subheader>State</v-subheader>
                    </v-flex>
                    <v-flex xs8>
                        <v-subheader v-show="readonly">{{ windturbinesettings.state }}</v-subheader>
                        <v-text-field v-model="form.state" hint="Insert the state of normal operation for this turbine" v-show="!readonly" :readonly="readonly" required></v-text-field>
                    </v-flex>
                </v-layout>
                <v-layout row>
                    <v-flex sm3 xs4>
                        <v-subheader>Max Generator RPM</v-subheader>
                    </v-flex>
                    <v-flex xs8>
                        <v-subheader v-show="readonly">{{ windturbinesettings.max_rpm_generator }}</v-subheader>
                        <v-text-field v-model="form.max_rpm_generator" hint="Insert the maximum allowd RPM for the generator of this turbine" v-show="!readonly" :readonly="readonly" required></v-text-field>
                    </v-flex>
                </v-layout>
                <v-layout row>
                    <v-flex sm3 xs4>
                        <v-subheader>Max temperature of gearbox</v-subheader>
                    </v-flex>
                    <v-flex xs8>
                        <v-subheader v-show="readonly">{{ windturbinesettings.max_temp_gearbox }}</v-subheader>
                        <v-text-field v-model="form.max_temp_gearbox" hint="Insert the maxmimum allowed temperature for the gearbox of this turbine" v-show="!readonly" :readonly="readonly" required></v-text-field>
                    </v-flex>
                </v-layout>
                <v-layout row>
                    <v-flex sm3 xs4>
                        <v-subheader>Max temperature of generator</v-subheader>
                    </v-flex>
                    <v-flex xs8>
                        <v-subheader v-show="readonly">{{ windturbinesettings.max_temp_generator }}</v-subheader>
                        <v-text-field v-model="form.max_temp_generator" hint="Insert the maximum allowed temperature of the generator in this turbine" v-show="!readonly" :readonly="readonly" required></v-text-field>
                    </v-flex>
                </v-layout>
                <v-layout row>
                    <v-flex sm3 xs4>
                        <v-subheader>Wing angle</v-subheader>
                    </v-flex>
                    <v-flex xs8>
                        <v-subheader v-show="readonly">{{ windturbinesettings.wing_angle }}</v-subheader>
                        <v-slider v-model="form.wing_angle" hint="Adjust the angle of the turbine wings" v-show="!readonly" :max="max" :disabled="readonly"></v-slider>
                    </v-flex>
                </v-layout>
                <v-layout row>
                    <v-flex sm3 xs4>
                        <v-subheader>Brakes active</v-subheader>
                    </v-flex>
                    <v-flex xs8>
                        <v-subheader v-show="readonly">{{ windturbinesettings.brake ? 'Yes' : 'No' }}</v-subheader>
                        <v-checkbox v-model="form.brake" label="Activate brakes" hint="Choose if the brakes should activate on this turbine" v-show="!readonly" :readonly="readonly"></v-checkbox>
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
                    :loading="processing"
                  >
                    <v-icon v-if="processing">loading</v-icon>
                    <v-icon v-else>save</v-icon>
                  </v-btn>
                </v-fab-transition>
            </v-container>
        </v-card-text>
    </v-card>
</template>

<script>
    import Form from '../classes/Form';
    export default {
        props: {
            windturbine: {
                default: {}
            },
            windturbinesettings: {
                default: {}
            },
            form: {
                default: new Form({})
            }
        },
        data: () => {
            return {
                //form: new Form({}),
                readonly: true,
                max: 10,
                processing: false
            }
        },
        mounted() {
            /*if(this.windturbinesettings.id) {
                this.form = new Form({
                    id: this.windturbinesettings.id,
                    state: this.windturbinesettings.state,
                    max_rpm_generator: this.windturbinesettings.max_rpm_generator,
                    max_temp_gearbox: this.windturbinesettings.max_temp_gearbox,
                    max_temp_generator: this.windturbinesettings.max_temp_generator,
                    windturbine: this.windturbine.id,
                    brake: this.windturbinesettings.brake,
                    wing_angle: this.windturbinesettings.wing_angle
                });
            }
            else {
                this.form = new Form({
                    state: "",
                    max_rpm_generator: "",
                    max_temp_gearbox: "",
                    max_temp_generator: "",
                    windturbine: this.windturbine.id
                });
            }*/
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
        methods: {
            save() {
                this.processing = true;
                if(this.windturbinesettings.id) {
                    this.form.patch('/webapi/windturbine-settings/' + this.windturbinesettings.id + '/').then(response => {
                        this.readonly = true;
                        this.$emit('saved');
                        this.processing = false;
                    }).catch(error => {
                        console.log(error);
                        this.processing = false;
                    })
                }
                else {
                    this.form.post('/webapi/windturbine-settings/').then(response => {
                        this.readonly = true;
                        this.$emit('saved');
                        this.processing = false;
                    }).catch(error => {
                        console.log(error);
                        this.processing = false;
                    })
                }
            }
        }
    }
</script>
