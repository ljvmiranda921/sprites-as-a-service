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
  padding: 50px;
}


</style>
