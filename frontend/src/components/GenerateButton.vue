<template>
  <div>
    <input type="button" @click="defaultConfig" value="Generate!" />
  </div>
</template>


<script>
export default {
  name: "GenerateButton",
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
  methods: {
    defaultConfig() {
      this.$emit("generate-sprite", this.spriteConfig);
    }
  }
};
</script>


<style scoped>
</style>
