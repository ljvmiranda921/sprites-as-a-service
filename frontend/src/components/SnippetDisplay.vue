<template>
  <div>
    <p>curl -X GET {{ url }}</p>
    <div id="wrapper">
      <div id="left"><SnippetDisplayLang :url="url" /></div>
      <div id="right"><SnippetDisplayDocs /></div>
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
