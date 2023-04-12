<template>
  <fragment>
    <MfpPopup />
    <ImgGallery />
    <ContentPopup />
    <div class="page" :class="newSkin ? ' new-skin' : ''">
      <PreLoader />
      <Gradient v-if="background == 'gradient'" />
      <BackgroundImg
        v-else-if="background == 'backgroundImg'"
        :img="backgroundImg"
      />
      <div
        class="container opened"
        :data-animation-in="animationFunction.animationIn"
        :data-animation-out="animationFunction.animationOut"
      >
        <slot />
      </div>
      <SideBar v-if="!noSidebar" />
    </div>
  </fragment>
</template>

<script>
import {Fragment} from "vue-fragment";
import {animationFunction} from "../animationFunction";
import BackgroundImg from "../components/background/BackgroundImg.vue";
import Gradient from "../components/background/Gradient.vue";
import ContentPopup from "../components/popup/ContentPopup.vue";
import ImgGallery from "../components/popup/ImgGallery.vue";
import MfpPopup from "../components/popup/MfpPopup.vue";
import {activeSectionWithScroll, aTag, titleActive} from "../utils";
import PreLoader from "./PreLoader.vue";
import SideBar from "./SideBar.vue";

export default {
  name: `HomeView`,
  components: {
    PreLoader,
    Gradient,
    BackgroundImg,
    SideBar,
    MfpPopup,
    Fragment,
    ImgGallery,
    ContentPopup,
  },
  data() {
    return {
      animationFunction,
    };
  },
  props: {
    background: {
      type: String,
      default: "none",
    },
    backgroundImg: { type: String },
    newSkin: {
      type: Boolean,
      default: true,
    },
    noSidebar: { type: Boolean },
  },
  head: {
    link: [
      {
        rel: "icon",
        type: "image/x-icon",
        href: "./images/favicons/favicon.ico",
      },
    ],
  },
  mounted() {
    titleActive();
    aTag();
    window.addEventListener("scroll", activeSectionWithScroll);
  },
};
</script>
