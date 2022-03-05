<template>
  <v-app>
    <div
      lazy-validation
      ref="form"
      style="padding-left: 20px; padding-right: 20px"
      class="text-center"
      id="app"
    >
      <v-img
        :src="require('./assets/logo.svg')"
        class="my-3"
        contain
        height="200"
      />
      <br>
      <v-row justify="center" align="center">
        <v-col cols="12" md="4">
          <v-text-field
            label="Nome do login"
            v-model="userName"
          />
        </v-col>
      </v-row>
      <v-row justify="center" align="center">
        <v-col cols="12" md="4">
          <v-text-field
            label="Senha"
            v-model="userPasword"
          />
        </v-col>
      </v-row>
      <v-row justify="center" align="center">
        <v-col cols="12" md="2">
          <v-btn color="primary" v-on:click="submit">Entrar</v-btn>
        </v-col>
        <v-col cols="12" md="2">
          <v-btn color="primary" v-on:click="submit">Cadastrar</v-btn>
        </v-col>
      </v-row>
    </div>
    <PageFooterVue />
  </v-app>
</template>

<script>
import PageFooterVue from './components/core/PageFooter.vue';

export default {
  name: 'App',

  data: () => ({
    userName: null,
    userPasword: null,
    formModel: null,
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