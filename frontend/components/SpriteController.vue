<template>
  <div>
    <SpriteControllerButton @random-sprite="setDefaults" />

    <h4 id="options-header">Or make your own unique sprite!</h4>
    <div class="text-container">
      <input
        type="text"
        v-model.trim="spriteConfig.q"
        placeholder="Type here!"
      />
    </div>

    <div>
      <div class="sprite-range">
        <div class="tooltip">
          <label for="extinctionControl">Extinction</label>
          <span class="tooltiptext"
            >Controls how many dead cells will stay dead</span
          >
        </div>
        <input
          type="range"
          id="extinctionControl"
          value="0.125"
          v-model.number="spriteConfig.extinction"
          min="0"
          max="1"
          step="0.1"
        />
      </div>

      <div class="sprite-range">
        <div class="tooltip">
          <label for="survivalControl">Survival</label>
          <span class="tooltiptext"
            >Controls how many living cells will stay alive</span
          >
        </div>
        <input
          type="range"
          id="survivalControl"
          value="0.375"
          v-model.number="spriteConfig.survival"
          min="0"
          max="1"
          step="0.1"
        />
      </div>
    </div>
  </div>
</template>

<script>
import SpriteControllerButton from "./SpriteControllerButton";

export default {
  name: "SpriteController",
  components: {
    SpriteControllerButton,
  },
  data() {
    return {
      spriteConfig: {
        q: null,
        extinction: null,
        survival: null,
      },
    };
  },
  watch: {
    spriteConfig: {
      deep: true,
      handler() {
        this.$emit("update-sprite", this.spriteConfig);
      },
    },
  },
  methods: {
    setDefaults() {
      this.spriteConfig = {
        q: "",
        extinction: null,
        survival: null,
      };
    },
  },
};
</script>

<style scoped>
#options-header {
  color: #29adff;
}

input {
  font-family: "Press Start 2P", cursive;
}

.text-container {
  width: 70%;
  display: inline-block;
  margin: 15px;
}

input[type="text"] {
  width: 100%;
  font-size: 12pt;
  text-align: center;
}

input[type="range"] {
  margin-left: 20px;
}

label {
  font-family: "Press Start 2P", cursive;
  font-size: 18px;
}

.sprite-range {
  padding: 5px;
}

/*Chrome*/
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="range"] {
    overflow: hidden;
    -webkit-appearance: none;
    background-color: transparent;
  }

  input[type="range"]::-webkit-slider-runnable-track {
    height: 10px;
    -webkit-appearance: none;
    color: #c2c3c7;
    width: 100%;
    background-color: #c2c3c7;
  }

  input[type="range"]::-webkit-slider-thumb {
    width: 10px;
    -webkit-appearance: none;
    height: 10px;
    cursor: ew-resize;
    background: #5f574f;
    box-shadow: -80px 0px 0px 80px #00e436;
  }
}

/* FF */
input[type="range"]::-moz-range-progress {
  background-color: #00e436;
}
input[type="range"]::-moz-range-track {
  background-color: #c2c3c7;
}
/* IE*/
input[type="range"]::-ms-fill-lower {
  background-color: #00e436;
}
input[type="range"]::-ms-fill-upper {
  background-color: #c2c3c7;
}

/* Tooltip container */
.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 2px dotted #fff1e8;
}

/* Tooltip text */
.tooltip .tooltiptext {
  visibility: hidden;
  background-color: black;
  color: #fff;
  text-align: center;
  padding: 5px 5px;
  border-radius: 6px;

  /* Position the tooltip text - see examples below! */
  position: absolute;
  z-index: 1;
  width: 120px;
  bottom: 100%;
  left: 50%;
  margin-left: -60px;
}

/* Show the tooltip text when you mouse over the tooltip container */
.tooltip:hover .tooltiptext {
  visibility: visible;
}
</style>
