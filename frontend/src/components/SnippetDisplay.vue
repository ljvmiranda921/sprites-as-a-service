<template>
  <div>
    <p>curl -X GET {{ url }}</p>
    <div class="wrapper">
      <div class="right"><SnippetDisplayDocs /></div>
    </div>
    <SnippetDisplayCTA />
  </div>
</template>

<script>
import SnippetDisplayDocs from "./SnippetDisplayDocs";
import SnippetDisplayCTA from "./SnippetDisplayCTA";

export default {
  name: "SnippetDisplay",
  props: ["url"],
  components: {
    SnippetDisplayDocs,
    SnippetDisplayCTA,
  },
};
</script>

<style scoped></style>
