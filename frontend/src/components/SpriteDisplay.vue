<template>
  <div>
    <img class="display" :src="'data:image/png;base64,' + img" />
  </div>
</template>

<script>
export default {
  name: "SpriteDisplay",
  props: {
    img: String
  },
};
</script>

<style scoped>
.display {
  margin-top: 50px;
  margin-bottom: 20px;
  border-color: #c2c3c7;
  border-style: solid;
  border-width: 5px;
}


</style>
