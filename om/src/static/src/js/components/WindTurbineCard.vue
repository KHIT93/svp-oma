<template>
    <div>
        <v-card hover class="mb-2">
            <v-card-text>WindTurbine {{ (item.name) ? item.id + ' (' + item.name + ')' : item.id }}</v-card-text>
            <v-card-actions>
                <v-btn flat title="Show details" icon primary :to="'/windturbines/' + item.id"><v-icon>storage</v-icon></v-btn>
                <v-btn flat title="Start" icon success @click.stop="startWindTurbine"><v-icon>power_settings_new</v-icon></v-btn>
                <v-btn flat title="Stop" icon error @click.stop="stopWindTurbine"><v-icon>power_settings_new</v-icon></v-btn>
                <v-btn flat title="Delete" icon @click.stop="dialog = true"><v-icon>delete</v-icon></v-btn>
                <small :title="item.last_connection">
                    {{ (item.last_connection == "Never") ? "No information has been recieved" : "Last connection was " + moment(item.last_connection).fromNow() }}
                </small>
            </v-card-actions>
        </v-card>
        <v-dialog v-model="dialog" persistent>
            <v-card>
                <v-card-title>Delete Windturbine {{ item.display_name }}</v-card-title>
                <v-card-text>Are you sure that you want to delete {{ item.display_name }}</v-card-text>
                <v-card-actions>
                    <v-btn class="green--text darken-1" flat @click.native="deleteItem">Yes</v-btn>
                    <v-btn class="red--text darken-1" flat @click.native="cancelDelete">No</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
    import Form from '../classes/Form';
    export default {
        props: {
            item: {
                default: {}
            }
        },
        data: () =>  {
            return {
                form: new Form(this.item),
                dialog: false
            }
        },
        methods: {
            moment(str) {
                return window.moment(str);
            },
            cancelDelete() {
                this.dialog = false;
            },
            deleteItem() {
                this.form.delete('/webapi/windturbines/' + this.item.id + '/').then(response => {
                    this.$emit('deleted', this.item);
                    flash('The windturbine has been deleted');
                }).catch(error => {
                    flash('There was an error while trying to delete the windturbine:' + error.toString());
                    console.log(error);
                })
            },
            startWindTurbine() {
                axios.patch('/webapi/windturbine-settings/' + this.item.settings_id + '/', { 'state': 1 }).then(response => {
                    flash('Command to start the windturbine has been sent');
                }).catch(error => {
                    flash(error.toString());
                });
            },
            stopWindTurbine() {
                axios.patch('/webapi/windturbine-settings/' + this.item.settings_id + '/', { 'state': 0 }).then(response => {
                    flash('Command to stop the windturbine has been sent');
                }).catch(error => {
                    flash(error.toString());
                });
            }
        }
    }
</script>
