<template>
  <v-container grid-list-md>
    <div
      lazy-validation
      style="padding-left: 20px; padding-right: 20px"
      class="text-center"
      id="app"
    >
      <v-img
        :src="require('../assets/logo.svg')"
        class="my-3"
        contain
        height="200"
      />
      <v-layout
        row
        fill-height
        justify-center
        align-center
        v-if="loading"
      >
        <v-progress-circular
          :size="50"
          color="primary"
          indeterminate
        />
      </v-layout>
      <v-form v-else ref="form" v-model="valid" lazy-validation>
        <v-container>
          <br>
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
          </v-row>
          <v-row justify="center" align="center">
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
        <v-row justify="center" align="center">
          <v-col cols="12" md="2">
            <v-btn color="primary" :disabled="!valid" @click="login">Entrar</v-btn>
          </v-col>
          <v-col cols="12" md="2">
            <v-btn color="primary" v-on:click="submit">Cadastrar</v-btn>
          </v-col>
        </v-row>
      </v-form>
    </div>
    <PageFooterVue />
  </v-container>  
</template>

<script>
import axios from 'axios';
import swal from 'sweetalert2';
import router from '../router';
import PageFooterVue from '../components/core/PageFooter.vue';

export default {
    name: 'Auth',
    data: () => ({
        credentials: {},
        valid:true,
        loading:false,
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
        login() {
          // checking if the input is valid
            if (this.$refs.form.validate()) {
              this.loading = true;
              axios.post('http://127.0.0.1:8000/auth/', this.credentials).then(res => {
                this.$session.start();
                this.$session.set('token', res.data.token);
                router.push('/');
              }).catch(e => {
                console.log(e)
                this.loading = false;
                swal({
                  type: 'warning',
                  title: 'Error',
                  text: 'Wrong username or password',
                  showConfirmButton:false,
                  showCloseButton:false,
                  timer:3000
                })
              })
            }
        }
    },
    components: {
      PageFooterVue: PageFooterVue
  },
}
</script>
<style scoped>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>