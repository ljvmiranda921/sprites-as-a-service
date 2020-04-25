<template>
  <div>
    <TechnicalNotesLicensing />
    <TechnicalNotesChangelog />
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
