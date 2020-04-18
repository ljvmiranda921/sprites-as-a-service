<template>
  <div>
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

    <div>
      <input type="radio" id="60" value="60" v-model.number="spriteConfig.size" />
      <label for="60">60px</label>
      <input type="radio" id="128" value="128" v-model.number="spriteConfig.size" />
      <label for="128">128px</label>
      <input type="radio" id="180" value="180" v-model.number="spriteConfig.size" />
      <label for="180">180px</label>
      <input type="radio" id="400" value="400" v-model.number="spriteConfig.size" />
      <label for="400">400px</label>
    </div>
  </div>
</template>

<script>
export default {
  name: "SpriteController",
  data() {
    return {
      spriteConfig: {
        q: null,
        extRate: 0.125,
        stasisRate: 0.375,
        size: 180
      }
    };
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
