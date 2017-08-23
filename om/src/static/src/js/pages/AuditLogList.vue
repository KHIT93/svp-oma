<template>
    <v-container fluid>
        <v-layout row wrap>
            <v-flex xs12>
                <v-card>
                    <v-card-title>
                        Audit log
                        <v-spacer></v-spacer>
                        <v-text-field
                            append-icon="search"
                            label="Search"
                            single-line
                            hide-details
                            v-model="search"
                            ></v-text-field>
                    </v-card-title>
                    <v-data-table
                        :headers="headers"
                        :items="items"
                        :search="search"
                        :loading="loading"
                        no-results-text="The audit log seems to be empty"
                    >
                        <template slot="items" scope="props">
                            <td class="text-xs-left" :title="props.item.timestamp">{{ moment(props.item.timestamp).fromNow() }}</td>
                            <td class="text-xs-left">{{ props.item.name }}</td>
                            <td class="text-xs-left">{{ props.item.message }}</td>
                        </template>
                    </v-data-table>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    export default {
        data: () => {
            return {
                headers: [
                    {
                        text: 'Timestamp',
                        align: 'left',
                        sortable: false,
                        value: 'name'
                    },
                    {
                        text: 'Name',
                        align: 'left',
                        sortable: false,
                        value: 'name'
                    },
                    {
                        text: 'Message',
                        align: 'left',
                        sortable: false,
                        value: 'name'
                    }
                ],
                items: [],
                loading: true,
                search: null,

            }
        },
        mounted() {
            this.getLogItems()
        },
        methods: {
            getLogItems() {
                this.loading = true;
                axios.get('/webapi/auditlog/').then(response => {
                    console.log(response);
                    this.items = response.data;
                    this.loading = false;
                }).catch(error => {
                    console.log(error);
                });
            },
            moment(str) {
                return window.moment(str);
            }
        }
    }
</script>
