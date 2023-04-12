<template>
  <div class="content works">
    <!-- title -->
    <div class="title">Pet Projects</div>
    <slot />
  </div>
</template>

<script>
export default {
  name: `Isotope`,
  head: {
    script: [
      {
        hid: "stripe",
        src: "https://unpkg.com/isotope-layout@3/dist/isotope.pkgd.js",
        defer: true,
      },
    ],
  },
  mounted() {
    setTimeout(() => {
      // init Isotope
      var iso = new Isotope(".grid-items", {
        itemSelector: ".grid-item",
      });
      // bind filter button click
      var filtersElem = document.querySelector(".filter-button-group");
      filtersElem.addEventListener("click", function (event) {
        // console.log(event.target.closest(".f_btn"));
        if (event.target.value !== undefined) {
          var filterValue = event.target.getAttribute("value");
          iso.arrange({ filter: `.${filterValue}` });
        }
      });

      // change is-checked class on buttons
      var buttonGroups = document.querySelectorAll(".filter-menu");
      for (var i = 0, len = buttonGroups.length; i < len; i++) {
        var buttonGroup = buttonGroups[i];
        radioButtonGroup(buttonGroup);
      }

      function radioButtonGroup(buttonGroup) {
        buttonGroup.addEventListener("click", function (event) {
          if (!event.target.classList.contains("filter-menu")) {
            buttonGroup.querySelector(".active").classList.remove("active");
            event.target.closest(".f_btn").classList.add("active");
          }
        });
      }
    }, 500);
  },
};
</script>
