<template>
    <div>
        <v-navigation-drawer persistent clipped enable-resize-watcher light v-model="drawer" :mini-variant.sync="mini" height="100%">
            <v-list class="pt-0" dense>
                <template v-for="(item, i) in menu">
                    <v-list-tile :to="item.link" router exact ripple>
                        <v-list-tile-action v-if="item.icon">
                            <v-icon>{{ item.icon }}</v-icon>
                        </v-list-tile-action>
                        <v-list-tile-content>
                            <v-list-tile-title>
                                {{ item.title }}
                                <template v-if="item.info">
                                    <v-chip v-if="item.info.error" class="red white--text chip--x--small">Error</v-chip>
                                    <v-chip v-if="item.info.messages" class="orange white--text chip--x--small">{{ item.info.messages }}</v-chip>
                                </template>
                            </v-list-tile-title>
                        </v-list-tile-content>
                    </v-list-tile>
                </template>
                <v-list-tile>
                    <v-list-tile-action>
                        <v-icon>add</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title>
                            Create WindFarm
                        </v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
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
    export default {
        data: function() {
            return {
                menu: [
                    { icon: 'home', title: 'Dashboard', link: '/'},
                    { icon: 'settings_input_antenna', title: 'Alpha', link: '/windfarms/1', info: {
                        error: true,
                        messages: null
                    }},
                    { icon: 'settings_input_antenna', title: 'Bravo', link: '/windfarms/2'},
                    { icon: 'settings_input_antenna', title: 'Charlie', link: '/windfarms/3', info: {
                        error: false,
                        messages: 3
                    }},
                    { icon: 'settings_input_antenna', title: 'Delta', link: '/windfarms/4'}
                ],
                drawer: true,
                mini: false,
                interval: null,
            }
        },
        methods: {
            loadData() {
                console.log('Polling server from navigation');
            }
        },
        mounted() {
            this.loadData();

            this.interval = setInterval(function () {
                this.loadData();
            }.bind(this), 30000);
        },
        beforeDestroy() {
            clearInterval(this.interval);
        }
    }
</script>
