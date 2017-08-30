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
                            <td class="text-xs-left" :title="props.item.timestamp" @click="getDetail(props.item.id)">{{ moment(props.item.timestamp).fromNow() }}</td>
                            <td class="text-xs-left" @click="getDetail(props.item)">{{ props.item.name }}</td>
                            <td class="text-xs-left" @click="getDetail(props.item)">{{ props.item.message }}</td>
                        </template>
                    </v-data-table>
                    <v-card-text>
                        <v-fab-transition>
                            <v-btn
                                class="green"
                                fab
                                dark
                                small
                                absolute
                                bottom
                                left
                                @click.native="getLogItems"
                                :loading="loading"
                                :disabled="loading"
                            >
                            <v-icon>cached</v-icon>
                          </v-btn>
                        </v-fab-transition>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
        <v-dialog v-model="dialog" persistent width="75%">
            <v-card>
                <v-card-title class="headline">Details for entry {{ selected_entry.display_name }}</v-card-title>
                <v-card-text>
                    <p>Name: {{ selected_entry.name }}</p>
                    <p>{{ selected_entry.message }}</p>
                    <p>{{ selected_entry.result }}</p>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn class="green--text darken-1" flat="flat" @click.native="dialog = false">Close</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
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
                dialog: false,
                selected_entry: {}
            }
        },
        mounted() {
            this.getLogItems()
        },
        methods: {
            getLogItems() {
                this.loading = true;
                axios.get('/webapi/auditlog/').then(response => {
                    this.items = response.data;
                    this.loading = false;
                }).catch(error => {
                    console.log(error);
                });
            },
            getDetail(item) {
                this.selected_entry = item;
                this.dialog = !this.dialog;
            },
            moment(str) {
                return window.moment(str);
            }
        }
    }
</script>
