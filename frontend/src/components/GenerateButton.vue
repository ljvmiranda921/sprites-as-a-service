<template>
  <div>
    <input type="button" @click="generateSprite" value="Generate!">
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: "GenerateButton",
  methods: {
    generateSprite() {
      axios
        .get("http://localhost:8000/sprite")
        .then(response => {
          console.log("response", response.statusText);
          this.$emit("create-sprite", response.data);
        })
        .catch(error => console.log("error.response", error));
    }
  }
};
</script>


<style scoped>
</style>
