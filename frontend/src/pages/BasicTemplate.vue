<template>
  <v-app>

      <PageFooterVue />
  </v-app>
</template>

<script>
import PageFooterVue from '../components/core/PageFooter.vue';

export default {
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