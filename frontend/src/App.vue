<template>
  <div id="app">
    <SpriteDisplay :img="img" />
    <SpriteController @update-sprite="generateSprite($event)" />
  </div>
</template>

<script>
import SpriteDisplay from "./components/SpriteDisplay.vue";
import SpriteController from "./components/SpriteController";
import axios from "axios";

export default {
  name: "App",
  components: {
    SpriteDisplay,
    SpriteController
  },
  data() {
    return {
      img: "",
      spriteConfig: {
        q: null,
        extRate: 0.125,
        stasisRate: 0.375,
        size: 180
      }
    };
  },
  methods: {
    setSprite(value) {
      this.img = value;
    },
    generateSprite(spriteConfig) {
      axios
        .get("http://localhost:8000/sprite", {
          params: {
            q: spriteConfig.q,
            ext_rate: spriteConfig.extRate,
            stasis_rate: spriteConfig.stasisRate,
            size: spriteConfig.size
          }
        })
        .then(response => {
          console.log("response", response.statusText);
          this.img = response.data;
        })
        .catch(error => console.log("error.response", error));
    }
  },
  created() {
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
