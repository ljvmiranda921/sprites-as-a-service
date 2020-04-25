<template>
  <div id="wrapper">
    <div id="left"><TechnicalNotesLicensing /></div>
    <div id="right"><TechnicalNotesChangelog /></div>
  </div>
</template>

<script>
import TechnicalNotesLicensing from "./TechnicalNotesLicensing";
import TechnicalNotesChangelog from "./TechnicalNotesChangelog";

export default {
  name: "TechnicalNotes",
  components: {
    TechnicalNotesLicensing,
    TechnicalNotesChangelog,
  },
};
</script>

<style scoped></style>
