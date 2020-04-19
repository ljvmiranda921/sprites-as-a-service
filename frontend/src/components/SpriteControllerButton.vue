<template>
  <div>
    <input type="button" @click="randomSprite" value="Random Sprite!" />
  </div>
</template>


<script>
export default {
  name: "SpriteControllerRandom",
  methods: {
    randomSprite() {
      this.$emit("random-sprite");
    }
  }
};
</script>


<style scoped>
</style>
