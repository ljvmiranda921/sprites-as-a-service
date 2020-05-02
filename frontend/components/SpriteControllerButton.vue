<template>
  <div>
    <input
      class="retro-btn"
      type="button"
      @click="randomSprite"
      value="Randomize!"
    />
  </div>
</template>

<script>
export default {
  name: "SpriteControllerRandom",
  methods: {
    randomSprite() {
      this.$emit("random-sprite");
    },
  },
};
</script>

<style scoped>
/*
.button-wrapper {
  padding: 10px;
  margin-bottom: 40px;
}
*/

.retro-btn {
  text-align: center;
  font-size: 16pt;
  font-family: "Press Start 2P", cursive;
  display: inline-block;
  margin: 5px;
  margin-bottom: 50px;
  font-weight: bold;
  padding: 10px 10px 10px 10px;
  background-color: #ff77a8;
  text-shadow: -1px -1px #ff004d, 1px 1px #ff004d;
  color: #fff1e8;
  -webkit-border-radius: 7px;
  -moz-border-radius: 7px;
  -o-border-radius: 7px;
  border-radius: 7px;
  box-shadow: 0 0.2em #ff004d;
  cursor: pointer;
}

.retro-btn:active {
  box-shadow: none;
  position: relative;
  top: 0.2em;
}
</style>
