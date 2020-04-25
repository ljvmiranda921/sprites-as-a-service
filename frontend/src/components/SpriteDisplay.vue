<template>
  <div>
    <img :src="'data:image/png;base64,' + img" />
  </div>
</template>

<script>
export default {
  name: "SpriteDisplay",
  props: ["img"],
};
</script>

<style scoped></style>
