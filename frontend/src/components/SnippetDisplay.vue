<template>
  <div>
    <h3 class="section-title">Generate sprites via a REST API</h3>
    <div class="samplecode curl-container">
        <pre class="url-container">{{ url }}</pre>
    </div>
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

<style scoped>

.section-title {
  color: #ffa300;
}

.curl-container {
  background-color: #000;
  border-radius: 10px;
  text-align: center;
  padding: 10px;
}

.url-container {
  font-family: Consolas, monospace;
  font-size: 20px;
}


</style>
