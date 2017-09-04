<template>
    <div>
        <v-navigation-drawer persistent enable-resize-watcher clipped overflow light v-model="drawer" :mini-variant.sync="mini" height="100%">
            <v-list class="pt-0" dense>
                <v-list-tile to="/">
                    <v-list-tile-action>
                        <v-icon>home</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>
                            Dashboard
                        </v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
                <v-list-tile to="/log">
                    <v-list-tile-action>
                        <v-icon>archive</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>
                            Audit Log
                        </v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
                <template v-for="(item, i) in data">
                    <v-list-tile :to="'/windfarms/'+item.id" router exact ripple>
                        <v-list-tile-action>
                            <v-icon>settings_input_antenna</v-icon>
                        </v-list-tile-action>
                        <v-list-tile-content>
                            <v-list-tile-title>
                                Windfarm {{ (item.name) ? item.id + ' (' + item.name + ')' : item.id }}
                                <template v-if="item.info">
                                    <v-chip v-if="item.info.error" class="red white--text chip--x--small">Error</v-chip>
                                    <v-chip v-if="item.info.messages" class="orange white--text chip--x--small">{{ item.info.messages }}</v-chip>
                                </template>
                            </v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                </template>

                <v-dialog v-model="dialog" fullscreen transition="dialog-bottom-transition" :overlay="false">
                    <v-list-tile slot="activator">
                        <v-list-tile-action>
                            <v-icon>add</v-icon>
                        </v-list-tile-action>
                        <v-list-tile-content>
                            <v-list-tile-title>
                                Create WindFarm
                            </v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                    <v-card>
                        <v-toolbar dark class="red">
                            <v-btn icon @click.native="dialog = false" dark>
                                <v-icon>close</v-icon>
                            </v-btn>
                            <v-toolbar-title>Create new Windfarm</v-toolbar-title>
                            <v-spacer></v-spacer>
                            <v-toolbar-items>
                                <v-btn dark flat @click.native="createWindFarm" :loading="form_processing"><v-icon v-if="form_processing">loading</v-icon> <span v-else>Save</span></v-btn>
                            </v-toolbar-items>
                        </v-toolbar>
                        <v-card-text>
                            <v-text-field label="Name" v-model="new_windfarm_name"></v-text-field>
                        </v-card-text>
                    </v-card>
                </v-dialog>
                <v-dialog v-model="dialog_windturbine" fullscreen transition="dialog-bottom-transition" :overlay="false">
                    <v-list-tile slot="activator">
                        <v-list-tile-action>
                            <v-icon>add</v-icon>
                        </v-list-tile-action>
                        <v-list-tile-content>
                            <v-list-tile-title>
                                Add WindTurbine
                            </v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                    <v-card>
                        <v-toolbar dark class="red">
                            <v-btn icon @click.native="dialog_windturbine = false" dark>
                                <v-icon>close</v-icon>
                            </v-btn>
                            <v-toolbar-title>Add WindTurbine to Windfarm</v-toolbar-title>
                            <v-spacer></v-spacer>
                        </v-toolbar>
                        <v-create-windturbine-form @saved="dialog_windturbine = false"></v-create-windturbine-form>
                    </v-card>
                </v-dialog>
            </v-list>
        </v-navigation-drawer>
        <v-toolbar class="red" dark>
            <v-toolbar-side-icon light @click.stop="drawer = !drawer"></v-toolbar-side-icon>
            <v-toolbar-title>Offshore Monitoring Advanced</v-toolbar-title>
        </v-toolbar>
    </div>
</template>
<script>
    import CreateWindTurbineForm from '../components/CreateWindTurbineForm.vue';
    export default {
        data: function() {
            return {
                data: [],
                drawer: true,
                mini: false,
                interval: null,
                dialog: false,
                dialog_windturbine: false,
                new_windfarm_name: "",
                form_processing: false,
            }
        },
        methods: {
            loadData() {
                console.log('Polling server from navigation');
                axios.get('/webapi/windfarms/simple/').then(response => {
                    this.data = response.data.results;
                });
            },
            createWindFarm() {
                this.form_processing = true;
                console.log('Posting new windfarm to server');
                axios.post('/webapi/windfarms/', { name: this.new_windfarm_name }).then(response => {
                    this.dialog = false;
                    this.new_windfarm_name = "";
                    this.form_processing = false;
                });
            }
        },
        components: {
            'v-create-windturbine-form': CreateWindTurbineForm
        },
        created() {
            this.loadData();

            this.interval = setInterval(function () {
                this.loadData();
            }.bind(this), 3000);
        },
        beforeDestroy() {
            clearInterval(this.interval);
        }
    }
</script>
