<template>
    <v-card class="mt-4">
        <v-card-title>
            <h3 class="headline mb-0 mr-2">Data from turbine {{ windturbine.display_name }}</h3>
        </v-card-title>
        <v-card-text>
            <v-expansion-panel>
                <v-expansion-panel-content v-for="(item, i) in windturbinedata" :key="i">
                    <div slot="header">Recieved {{ moment(item.timestamp).fromNow() }}</div>
                    <v-card>
                        <v-card-text class="grey lighten-3">
                            State: {{ item.state }}<br/>
                            Gearbox temperature: {{ item.temp_gearbox }}<br/>
                            Generator temperature: {{ item.temp_generator }}<br/>
                            Current generator RPM: {{ item.rpm_generator }}<br/>
                            Current windspeed: {{ item.wind_speed }}<br/>
                            Current wing angle: {{ item.wing_angle }}<br/>
                            Brakes active: {{ item.brake ? 'Yes' : 'No' }}<br/>
                        </v-card-text>
                    </v-card>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-card-text>
    </v-card>
</template>

<script>
    export default {
        props: ['windturbinedata', 'windturbine'],
        methods: {

            moment(str) {
                return window.moment(str);
            },
        }

    }
</script>
