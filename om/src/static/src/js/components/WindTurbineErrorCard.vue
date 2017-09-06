<template>
    <v-card class="mt-4">
        <v-card-title>
            <h3 class="headline mb-0 mr-2">Errors from turbine {{ windturbine.display_name }}</h3>
            <v-btn @click.native="toggle" flat>{{ all ? 'Show unhandled' : 'Show all' }}</v-btn>
        </v-card-title>
        <v-card-text>
            <v-expansion-panel v-if="windturbineerrors">
                <v-expansion-panel-content v-for="(item, i) in windturbineerrors" :key="i">
                    <div slot="header">Registered {{ moment(item.timestamp).fromNow() }}</div>
                    <v-card>
                        <v-card-text class="grey lighten-3">
                            Code: {{ item.error_code }}<br/>
                            Message: {{ item.error_message }}<br/>
                            Resolved: {{ item.resolved ? 'Yes' : 'No' }}<br/>
                        </v-card-text>
                    </v-card>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-card-text>
    </v-card>
</template>

<script>
    export default {
        props: {
            windturbine: {
                default: {}
            },
            windturbineerrors: {
                default: []
            },
        },
        data: () => {
            return {
                all: false
            }
        },
        methods: {
            toggle() {
                this.all = !this.all;
                this.$emit('changed');
            },
            moment(str) {
                return window.moment(str);
            },
        }

    }
</script>
