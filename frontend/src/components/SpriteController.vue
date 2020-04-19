<template>
  <div>
    <SpriteControllerButton @random-sprite="setDefaults" />

    <div>
      <input type="text" v-model.trim="spriteConfig.q" placeholder="Type anything!" />
    </div>

    <div>
      <label for="extRateControl">Extinction Rate</label>
      <input
        type="range"
        id="extRateControl"
        value="0.125"
        v-model.number="spriteConfig.extRate"
        min="0"
        max="1"
        step="0.1"
      />
    </div>

    <div>
      <label for="stasisRateControl">Stasis Rate</label>
      <input
        type="range"
        id="stasisRateControl"
        value="0.375"
        v-model.number="spriteConfig.stasisRate"
        min="0"
        max="1"
        step="0.1"
      />
    </div>
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
        extRate: 0.125,
        stasisRate: 0.375,
      }
    };
  },
  methods: {
    setDefaults() {
      this.spriteConfig = {
        q: null,
        extRate: 0.125,
        stasisRate: 0.375,
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
