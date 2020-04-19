<template>
  <div> 
    <p>curl -X GET {{ url }}</p>
    <!-- TODO: Add parameter description table -->
    <SnippetDisplayLang :url="url"/>
    <!-- TODO: Add call to action: "See more in the documentation" -->
  </div>
</template>

<script>
import SnippetDisplayLang from "./SnippetDisplayLang"

export default {
  name: "SnippetDisplay",
  props: ["url"],
  components: {
    SnippetDisplayLang
  }
}
</script>


<style scoped>

</style>
