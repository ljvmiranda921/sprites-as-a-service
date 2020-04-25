<template>
  <div id="app">
    <TheHeroHeader />
    <SpriteDisplay :img="img" />
    <SpriteController @update-sprite="generateSprite($event)" />
    <SnippetDisplay :url="requesturl" />
    <TechnicalNotes />
    <BaseFooter />
  </div>
</template>

<script>
import TheHeroHeader from "./components/TheHeroHeader";
import SpriteDisplay from "./components/SpriteDisplay";
import SpriteController from "./components/SpriteController";
import SnippetDisplay from "./components/SnippetDisplay";
import TechnicalNotes from "./components/TechnicalNotes";
import BaseFooter from "./components/BaseFooter";
import axios from "axios";

export default {
  name: "App",
  components: {
    TheHeroHeader,
    SpriteDisplay,
    SpriteController,
    SnippetDisplay,
    TechnicalNotes,
    BaseFooter,
  },
  data() {
    return {
      img: "",
      requesturl: "",
      baseurl: "http://localhost:8000/api/v1/sprite",
      spriteConfig: {
        q: null,
        extinction: 0.125,
        survival: 0.375,
      },
    };
  },
  methods: {
    generateSprite(spriteConfig) {
      // Whether spriteConfig.q is null or an empty string,
      // we will always return null
      var queryPrefix = "?q=";
      var extinctionPrefix = "&extinction=";
      var queryText = spriteConfig.q;
      if (spriteConfig.q === null || spriteConfig.q == "") {
        queryPrefix = "";
        extinctionPrefix = "?extinction=";
        queryText = null;
      }
      axios
        .get(this.baseurl, {
          params: {
            q: queryText,
            extinction: spriteConfig.extinction,
            survival: spriteConfig.survival,
            size: 300,
          },
        })
        .then((response) => {
          console.log("response", response.statusText);
          this.img = response.data;
          this.requesturl =
            this.baseurl +
            queryPrefix +
            spriteConfig.q +
            extinctionPrefix +
            spriteConfig.extinction +
            "&survival=" +
            spriteConfig.survival +
            "&size=" +
            300;
        })
        .catch((error) => console.log("error.response", error));
    },
  },
  created() {
    // Random sprite image is called every reload
    axios
      .get(this.baseurl, {
        params: {
          size: 300,
        },
      })
      .then((response) => {
        console.log("response", response.statusText);
        this.img = response.data;
        this.requesturl = this.baseurl;
      })
      .catch((error) => console.log("error.response", error));
  },
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
