<template>
  <div>
    <SpriteControllerButton @random-sprite="setDefaults" />

    <div>
      <h4 id="options-header">More Options</h4>
      <div class="nes-field sprite-field">
        <input
          type="text"
          v-model.trim="spriteConfig.q"
          placeholder="Type anything!"
        />
      </div>

      <div>
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

      <div>
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

.sprite-field {
  font-size: 14pt;  
  padding: 10px;
}

#options-header {
  color: #29adff;
}


</style>
