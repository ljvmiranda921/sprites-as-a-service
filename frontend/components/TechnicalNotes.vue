<template>
  <div>
    <div class="wrapper">
      <div class="left"><TechnicalNotesLicensing /></div>
      <div class="right"><TechnicalNotesChangelog /></div>
    </div>
    <SpriteControllerCTA />
  </div>
</template>

<script>
import TechnicalNotesLicensing from "./TechnicalNotesLicensing";
import TechnicalNotesChangelog from "./TechnicalNotesChangelog";
import SpriteControllerCTA from "./SpriteControllerCTA";

export default {
  name: "TechnicalNotes",
  components: {
    TechnicalNotesLicensing,
    TechnicalNotesChangelog,
    SpriteControllerCTA,
  },
};
</script>

<style scoped></style>
