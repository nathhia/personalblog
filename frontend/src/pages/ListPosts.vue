<template>
    <div>
        List Posts
    </div>
</template>

<script>
import router from "../router";
export default {
  name: "ListPosts",
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
      this.$session.start();
      if (!this.$session.has("token")) {
        router.push("/auth");
      }
    }
  }
};
</script>