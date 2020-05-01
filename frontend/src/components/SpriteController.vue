<template>
  <div>
    <SpriteControllerButton @random-sprite="setDefaults" />

    <h4 id="options-header">More Options</h4>
    <div class="sprite-field">
      <input
        type="text"
        v-model.trim="spriteConfig.q"
        placeholder="Type here!"
      />
    </div>

    <div>
      <div class="sprite-range">
        <label for="extinctionControl">Extinction</label>
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
        <label for="survivalControl">Survival</label>
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
    <SpriteControllerCTA />
  </div>
</template>

<script>
import SpriteControllerButton from "./SpriteControllerButton";
import SpriteControllerCTA from "./SpriteControllerCTA";

export default {
  name: "SpriteController",
  components: {
    SpriteControllerButton,
    SpriteControllerCTA,
  },
  data() {
    return {
      spriteConfig: {
        q: null,
        extinction: 0.125,
        survival: 0.375,
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
        extinction: 0.125,
        survival: 0.375,
      };
    },
  },
};
</script>

<style scoped>

#options-header {
  color: #29adff;
}

.sprite-field {
  font-size: 14pt;
  padding: 10px;
}

input {
  font-family: "Press Start 2P", cursive;
}

input[type='text'] {
  width: 60%;
}

input[type='range'] {
  padding-left: 10px;
}

label {
  font-family: "Press Start 2P", cursive;
  font-size: 20px
}

.sprite-range {
  padding: 5px;
}

/*Chrome*/
@media screen and (-webkit-min-device-pixel-ratio:0) {
    input[type='range'] {
      overflow: hidden;
      -webkit-appearance: none;
      background-color: transparent;
    }
    
    input[type='range']::-webkit-slider-runnable-track {
      height: 10px;
      -webkit-appearance: none;
      color: #00e436;
      margin-top: -1px;
    }
    
    input[type='range']::-webkit-slider-thumb {
      width: 10px;
      -webkit-appearance: none;
      height: 10px;
      cursor: ew-resize;
      background: #434343;
      box-shadow: -80px 0 0 80px #00e436;
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

</style>
