<template>
  <div id="app">
    <GenerateButton @create-sprite="setSprite($event)" />
    <SpriteImage :img="img" />
  </div>
</template>

<script>
import GenerateButton from "./components/GenerateButton.vue";
import SpriteImage from "./components/SpriteImage.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    GenerateButton,
    SpriteImage
  },
  data: function() {
    return {
      img: ""
    };
  },
  methods: {
    setSprite: function(value) {
      this.img = value;
    }
  },
  created: function() {
    // Random sprite image is called every reload
    axios
      .get("http://localhost:8000/sprite")
      .then(response => {
        console.log("response", response.statusText);
        this.img = response.data;
      })
      .catch(error => console.log("error.response", error));
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
