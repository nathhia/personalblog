<template>
  <v-footer padless height="auto" class="footer-position" absolute>
    <v-card
      text
      item
      width="100%"
      class="text-center"
      color="#222222"
      dark>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        &copy;2022 — <strong>Digit.e</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>



<script>
export default {
  data() {
    return {
    }
  }
}
</script>

<style>
  .footer-position{
    position: fixed;
    bottom: 0px;
    padding: 0px 3px;
    
  }
</style>
