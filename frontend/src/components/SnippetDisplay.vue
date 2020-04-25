<template>
  <div>
    <p>curl -X GET {{ url }}</p>
    <div class="wrapper">
      <div class="left"><SnippetDisplayLang :url="url" /></div>
      <div class="right"><SnippetDisplayDocs /></div>
    </div>
    <SnippetDisplayCTA />
  </div>
</template>

<script>
import SnippetDisplayLang from "./SnippetDisplayLang";
import SnippetDisplayDocs from "./SnippetDisplayDocs";
import SnippetDisplayCTA from "./SnippetDisplayCTA";

export default {
  name: "SnippetDisplay",
  props: ["url"],
  components: {
    SnippetDisplayLang,
    SnippetDisplayDocs,
    SnippetDisplayCTA,
  },
};
</script>

<style scoped></style>
