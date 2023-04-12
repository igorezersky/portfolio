<template>
  <div class="swiper">
    <div class="swiper-wrapper">
      <div class="item swiper-slide">
        <div class="revs-item">
          <div class="text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum
            dolor sit amet, consectetur adipiscing elit.
          </div>
          <div class="user">
            <div class="img">
              <img src="images/man1.jpg" alt="" />
            </div>
            <div class="info">
              <div class="name">Helen Floyd</div>
              <div class="company">Art Director</div>
            </div>
            <div class="clear"></div>
          </div>
        </div>
      </div>
      <div class="item swiper-slide">
        <div class="revs-item">
          <div class="text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum
            dolor sit amet, consectetur adipiscing elit.
          </div>
          <div class="user">
            <div class="img">
              <img src="images/man1.jpg" alt="" />
            </div>
            <div class="info">
              <div class="name">Robert Chase</div>
              <div class="company">CEO</div>
            </div>
            <div class="clear"></div>
          </div>
        </div>
      </div>
      <div class="item swiper-slide">
        <div class="revs-item">
          <div class="text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum
            dolor sit amet, consectetur adipiscing elit.
          </div>
          <div class="user">
            <div class="img">
              <img src="images/man1.jpg" alt="" />
            </div>
            <div class="info">
              <div class="name">Helen Floyd</div>
              <div class="company">Art Director</div>
            </div>
            <div class="clear"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="owl-dots"></div>
  </div>
</template>

<script>
// import Swiper JS
// add or remove unused modules
import {Autoplay, Navigation, Pagination, Swiper} from "swiper";
import "swiper/swiper-bundle.min.css";

export default {
  mounted() {
    Swiper.use([Navigation, Pagination, Autoplay]);

    new Swiper(".swiper", {
      loop: true,
      modules: [Navigation, Pagination, Autoplay],
      pagination: {
        el: ".owl-dots",
        type: "bullets",
        clickable: true,
      },
      autoplay: {
        delay: 3000,
      },
    });
  },
};
</script>

<style>
.swiper-pagination-bullet {
  background: none;
  opacity: 1 !important;
}
</style>
