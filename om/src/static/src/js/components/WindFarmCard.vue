<template>
    <v-card hover class="mb-2">
        <v-card-text>WindFarm {{ (windfarm.name) ? windfarm.id + ' (' + windfarm.name + ')' : windfarm.id }}</v-card-text>
        <v-card-actions>
            <v-btn flat :to="'/windfarms/' + windfarm.id" icon primary><v-icon>storage</v-icon></v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        props: ['windfarm'],
        data: () => {
            return {

            }
        }
    }
</script>
