<template>
  <div id="app">
    <GenerateButton msg="Hi there"/>
  </div>
</template>

<script>
import GenerateButton from './components/GenerateButton.vue'

export default {
  name: 'App',
  components: {
    GenerateButton
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
