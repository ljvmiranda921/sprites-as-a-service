<template>
  <div>
    <!-- Tab links -->  
    <div class="tab">
      <button class="tablinks" @click="openLang(event, 'Python')" id="defaultOpen">Python</button>
      <button class="tablinks" @click="openLang(event, 'Go')">Go</button>
      <button class="tablinks" @click="openLang(event, 'Javascript')">Javascript (Node)</button>
    </div>

    <!-- Tab content-->
    <div id="Python" class="tabcontent">
      Python {{ url }}
    </div>
    <div id="Go" class="tabcontent">
      Go  {{ url }}
    </div>
    <div id="Javascript" class="tabcontent">
      Javascript {{ url }}
    </div>
  </div>
</template>


<script>
export default {
  name: "SnippetDisplayLang", 
  props: ["url"],
  methods: {
    openLang(evt, langName) {
      // Declare all variables
      var i, tabcontent, tablinks

      // Get all elements with class="tabcontent" and hide them
      tabcontent = document.getElementsByClassName("tabcontent")
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none"
      }

      // Get all elements with class="tablinks" and remove the class "active"
      tablinks = document.getElementsByClassName("tablinks")
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "")
      }

      // Show the current tab, and add an "active" class to the button that opened the tab
      document.getElementById(langName).style.display = "block"
      evt.currentTarget.className += " active"
    },    
  },
  mounted() {
    document.getElementById("defaultOpen").click()
  }
}
</script>

<style scoped>
 /* Style the tab */
.tab {
  overflow: hidden;
  border: 1px solid #ccc;
  background-color: #f1f1f1;
}

/* Style the buttons that are used to open the tab content */
.tab button {
  background-color: inherit;
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 14px 16px;
  transition: 0.3s;
}

/* Change background color of buttons on hover */
.tab button:hover {
  background-color: #ddd;
}

/* Create an active/current tablink class */
.tab button.active {
  background-color: #ccc;
}

/* Style the tab content */
.tabcontent {
  display: none;
  padding: 6px 12px;
  border: 1px solid #ccc;
  border-top: none;
} 

.tabcontent {
  animation: fadeEffect 1s; /* Fading effect takes 1 second */
}

/* Go from zero to full opacity */
@keyframes fadeEffect {
  from {opacity: 0;}
  to {opacity: 1;}
}
</style>
