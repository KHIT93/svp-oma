<template>
    <v-snackbar
      :timeout="timeout"
      :top="y === 'top'"
      :bottom="y === 'bottom'"
      :right="x === 'right'"
      :left="x === 'left'"
      :multi-line="mode === 'multi-line'"
      :vertical="mode === 'vertical'"
      v-model="show"
    >
        {{ body }}
        <v-btn flat class="white--text" @click.native="show = false">Close</v-btn>
    </v-snackbar>
</template>

<script>
    export default {
        props: ['message'],

        data() {
            return {
                body: this.message,
                show: false,
                x: 'right',
                y: 'bottom',
                mode: 'vertical',
                timeout: 5000
            }
        },

        created() {
            if (this.message) {
                this.flash();
            }
            /**
             * Listen for a global event in order to trigger the flash notification
             */
            window.events.$on(
                'flash', data => this.flash(data)
            );
        },

        methods: {
            flash(data) {
                if (data) {
                    this.body = data.message;
                }

                this.show = true;

            },
        }
    };
</script>
