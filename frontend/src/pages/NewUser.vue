<template>
  <v-app>
    <div
        lazy-validation
        style="padding-left: 20px; padding-right: 20px"
        class="text-center"
    >
        <v-form v-model="formModel">
            <v-container>
                <v-row justify="center" align="center">
                    <v-col cols="12" md="4">
                        <v-text-field
                            label="Nome do login"
                            v-model="credentials.username"
                            :rules="rules.username"
                            maxlength="30"
                            required
                            :counter="30"
                        />
                    </v-col>
                    <v-col cols="12" md="4">
                        <v-text-field
                            label="Senha"
                            type="password"
                            v-model="credentials.password"
                            :counter="20"
                            :rules="rules.password"
                            maxlength="20"
                            required
                        />
                    </v-col>
                </v-row>
            </v-container>
        </v-form>
    </div>
    <PageFooterVue />
  </v-app>
</template>

<script>
import PageFooterVue from '../components/core/PageFooter.vue';

export default {
  data: () => ({
    userName: null,
    userPasword: null,
    userEmail: null,
    formModel: null,
    credentials: {},
    rules: {
          username: [
            v => !!v || "Username is required",
            v => (v && v.length > 3) || "A username must be more than 3 characters long",
            v => /^[a-z0-9_]+$/.test(v) || "A username can only contain letters and digits"
          ],
          password: [
            v => !!v || "Password is required",
            v => (v && v.length > 7) || "The password must be longer than 7 characters"
          ]
        }
  }),

  methods: {
    submit: function(){
      
    }
  },

  components: {
    PageFooterVue: PageFooterVue
  },
};

</script>