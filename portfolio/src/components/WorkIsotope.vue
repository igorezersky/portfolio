<template>
  <div class="content works">
    <!-- title -->
    <div class="title">Pet Projects</div>

    <!-- content -->
    <div class="row grid-items border-line-v">

      <!-- work item -->
      <div class="col col-d-6 col-t-6 col-m-12 border-line-h">
        <div class="box-item">
          <div class="desc">
            <a target="_blank" href="https://weatherapi.iyazerski.me" class="name">Weather API</a>
            <div class="category">RESTful and asynchronous weather API, created as a pet project to demonstrate my skills in API development</div>
          </div>
        </div>
      </div>
      <div class="col col-d-6 col-t-6 col-m-12">
        <div class="box-item">
          <div class="desc">
            <a target="_blank" href="https://newsclassifier.iyazerski.me" class="name">News Classifier</a>
            <div class="category">RESTful and asynchronous API to a news classification model, created as a pet project to demonstrate my skills in ML</div>
          </div>
        </div>
      </div>
      <div class="col col-d-6 col-t-6 col-m-12">
        <div class="box-item">
          <div class="desc">
            <a target="_blank" href="https://pypi.org/project/pydeployhelp/" class="name">pydeployhelp</a>
            <div class="category">CLI tool that helps integrating deploy (via Docker) to Python projects</div>
          </div>
        </div>
      </div>
      <div class="col col-d-6 col-t-6 col-m-12">
        <div class="box-item">
          <div class="desc">
            <a target="_blank" href="https://github.com/iyazerski/cookiecutter-api" class="name">cookecutter-api</a>
            <div class="category">cookiecutter template project for web-service with RESTful API on Python</div>
          </div>
        </div>
      </div>
      <div class="col col-d-6 col-t-6 col-m-12">
        <div class="box-item">
          <div class="desc">
            <a target="_blank" href="https://github.com/iyazerski/portfolio" class="name">Portfolio</a>
            <div class="category">My personal website, where you are now</div>
          </div>
        </div>
      </div>

      <div class="clear"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: `WorkIsotope`,
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
