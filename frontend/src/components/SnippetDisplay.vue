<template>
  <div> 
    <p>curl -X GET {{ url }}</p>
    <SnippetDisplayDocs />
    <SnippetDisplayLang :url="url"/>
    <SnippetDisplayCTA />
  </div>
</template>

<script>
import SnippetDisplayDocs from "./SnippetDisplayDocs"
import SnippetDisplayLang from "./SnippetDisplayLang"
import SnippetDisplayCTA from "./SnippetDisplayCTA"

export default {
  name: "SnippetDisplay",
  props: ["url"],
  components: {
    SnippetDisplayDocs,
    SnippetDisplayLang,
    SnippetDisplayCTA
  }
}
</script>


<style scoped>

</style>
