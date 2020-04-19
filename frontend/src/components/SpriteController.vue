<template>
  <div>
    <SpriteControllerButton @random-sprite="setDefaults" />

    <div>
      <input type="text" v-model.trim="spriteConfig.q" placeholder="Type anything!" />
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
    <!-- TODO: Add call to action: "Like it? Love it? Leave us a Star on Github"-->
  </div>
</template>

<script>
import SpriteControllerButton from "./SpriteControllerButton.vue";

export default {
  name: "SpriteController",
  components: {
    SpriteControllerButton
  },
  data() {
    return {
      spriteConfig: {
        q: null,
        extinction: 0.125,
        survival: 0.375,
      }
    };
  },
  methods: {
    setDefaults() {
      this.spriteConfig = {
        q: "",
        extinction: 0.125,
        survival: 0.375,
      };
    }
  },
  watch: {
    spriteConfig: {
      deep: true,
      handler() {
        this.$emit("update-sprite", this.spriteConfig);
      }
    }
  }
};
</script>

<style scoped>
</style>
