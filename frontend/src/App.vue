<template>
  <div id="app">
    <!-- TODO: Add header -->
    <!-- TODO: Add subheader -->
    <SpriteDisplay :img="img" />
    <SpriteController @update-sprite="generateSprite($event)" />
    <SnippetDisplay :url="requesturl" />
  </div>
</template>

<script>
import SpriteDisplay from "./components/SpriteDisplay.vue";
import SpriteController from "./components/SpriteController";
import SnippetDisplay from "./components/SnippetDisplay";
import axios from "axios";

export default {
  name: "App",
  components: {
    SpriteDisplay,
    SpriteController,
    SnippetDisplay
  },
  data() {
    return {
      img: "",
      requesturl: "",
      baseurl: "http://localhost:8000/sprite",
      spriteConfig: {
        q: null,
        extRate: 0.125,
        stasisRate: 0.375,
      }
    };
  },
  methods: {
    generateSprite(spriteConfig) {
      // Whether spriteConfig.q is null or an empty string,
      // we will always return null
      var queryPrefix = "?q=";
      var extRatePrefix = "&ext_rate=";
      var queryText = spriteConfig.q;
      if (spriteConfig.q === null || spriteConfig.q == "") {
        queryPrefix = "";
        extRatePrefix = "?ext_rate=";
        queryText = null
      }
      axios
        .get(this.baseurl, {
          params: {
            q: queryText,
            ext_rate: spriteConfig.extRate,
            stasis_rate: spriteConfig.stasisRate,
            size: 300
          }
        })
        .then(response => {
          console.log("response", response.statusText);
          this.img = response.data;
          this.requesturl = (this.baseurl
                          + queryPrefix + spriteConfig.q
                          + extRatePrefix + spriteConfig.extRate
                          + "&stasis_rate=" + spriteConfig.stasisRate
                          + "&size=" + 300);
        })
        .catch(error => console.log("error.response", error));
    }
  },
  created() {
    // Random sprite image is called every reload
    axios
      .get(this.baseurl, {
          params: {
            size: 300
          }
      })
      .then(response => {
        console.log("response", response.statusText);
        this.img = response.data;
        this.requesturl = this.baseurl;
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
