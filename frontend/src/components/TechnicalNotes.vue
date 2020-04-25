<template>
  <div class="wrapper">
    <div class="left"><TechnicalNotesLicensing /></div>
    <div class="right"><TechnicalNotesChangelog /></div>
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
