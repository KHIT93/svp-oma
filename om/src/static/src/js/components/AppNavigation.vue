<template>
    <div>
        <v-navigation-drawer persistent clipped enable-resize-watcher light v-model="drawer" :mini-variant.sync="mini" height="100%">
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
                <template v-for="(item, i) in data">
                    <v-list-tile :to="'/windfarms/'+item.id" router exact ripple>
                        <v-list-tile-action>
                            <v-icon>settings_input_antenna</v-icon>
                        </v-list-tile-action>
                        <v-list-tile-content>
                            <v-list-tile-title>
                                {{ (item.name) ? item.id + ' (' + item.name + ')' : item.id }}
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
                                <v-btn dark flat @click.native="createWindFarm">Save</v-btn>
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
            <v-menu bottom right origin="bottom right" transition="v-slide-y-transition">
                <v-btn light icon slot="activator">
                    <v-icon>account_circle</v-icon>
                </v-btn>
                <v-list>
                    <v-list-tile>
                        <v-list-tile-title>Change Account</v-list-tile-title>
                    </v-list-tile>
                    <v-list-tile>
                        <v-list-tile-title>Log Out</v-list-tile-title>
                    </v-list-tile>
                </v-list>
            </v-menu>
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
            }
        },
        methods: {
            loadData() {
                console.log('Polling server from navigation');
                axios.get('/webapi/windfarms/simple/').then(response => {
                    console.log(response.data.results);
                    this.data = response.data.results;
                });
            },
            createWindFarm() {
                console.log('Posting new windfarm to server');
                axios.post('/webapi/windfarms/', { name: this.new_windfarm_name }).then(response => {
                    console.log(response);
                    this.dialog = false;
                    this.new_windfarm_name = "";
                });
            }
        },
        components: {
            'v-create-windturbine-form': CreateWindTurbineForm
        },
        mounted() {
            this.loadData();

            this.interval = setInterval(function () {
                this.loadData();
            }.bind(this), 10000);
        },
        beforeDestroy() {
            clearInterval(this.interval);
        }
    }
</script>
