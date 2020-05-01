<template>
  <div id="container">
    <div class="pattern-cross-dots-md gray-darkest">
      <div id="app">
        <TheHeroHeader />
        <SpriteDisplay :img="img" />
        <SpriteController @update-sprite="generateSprite($event)" />
        <div class="pattern-dots-sm slategray h-5 my-5" />
        <SnippetDisplay :url="requesturl" />
        <div class="pattern-dots-sm slategray h-5 my-5" />
        <TechnicalNotes />
        <BaseFooter />
      </div>
    </div>
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
        extinction: null,
        survival: null,
      },
    };
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
  methods: {
    generateSprite(spriteConfig) {
      // Whether spriteConfig.q is null or an empty string,
      // we will always return null
      var queryPrefix = "?q=";
      var extinctionPrefix = "&extinction=";
      var survivalPrefix = "&survival=";

      var queryText = spriteConfig.q;
      var extinctionText = spriteConfig.extinction;
      var survivalText = spriteConfig.survival;

      if (spriteConfig.q === null || spriteConfig.q == "") {
        queryPrefix = "";
        extinctionPrefix = "?extinction=";
        queryText = null;
      }

      if (spriteConfig.extinction === null) {
        extinctionPrefix = "";
        survivalPrefix = "?survival=";
        extinctionText = "";
      }

      if (spriteConfig.survival === null) {
        survivalPrefix = ""
        survivalText = "";
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
            extinctionText +
            survivalPrefix +
            survivalText
        })
        .catch((error) => console.log("error.response", error));
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");

h1, h2, h3, h4 {
  font-family: "Press Start 2P", cursive;
}


#container {
  background: #1d2b53;
  padding: 10px;
  position: fixed;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  overflow: auto;
}

#app {
  /* Fonts and smoothing */
  font-family: Consolas, monospace;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  /* Text design */
  text-align: center;
  color: #fff1e8;

  /* Padding and margins */
  margin-top: 60px;
  width: 80%;
  max-width: 768px;
  margin: auto;
}

a:link {
  color: #ffec27;
}

@media (min-width: 768px) {
  .wrapper {
    display: flex;
  }
}

.wrapper div {
  margin: 10px;
  text-align: left;
}

.left {
  flex: 0 0 50%;
}

.right {
  flex: 1;
}
</style>
