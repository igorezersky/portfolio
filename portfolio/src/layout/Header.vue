<template>
  <header class="header">
    <!-- header profile -->
    <div class="profile">
      <div class="title">{{ name }}</div>
      <TypingAnimation v-if="!noTypingAnimation" :arr="arr" />
      <div class="subtitle" v-else>{{ arr }}</div>
    </div>

    <!-- menu btn -->
    <a
      v-if="!noSidebar"
      href="#"
      class="menu-btn"
      @click="navFunction.sidebarToggle(true)"
      ><span></span
    ></a>

    <!-- menu -->
    <div class="top-menu">
      <ul>
        <li
          :class="navFunction.activeNav(menu.href)"
          v-for="menu in menus"
          :key="menu.name"
        >
          <a
            :href="`#` + menu.href"
            @click="navFunction.activeSection(menu.href)"
          >
            <span :class="menu.icon"></span>
            <span class="link">{{ menu.name }}</span>
          </a>
        </li>
      </ul>
    </div>
  </header>
</template>

<script>
import TypingAnimation from "../components/TypingAnimation.vue";
import {navFunction} from "../navFunction";

export default {
  name: `Header`,
  data() {
    return {
      navFunction,
    };
  },
  props: {
    noSidebar: { type: Boolean },
    noTypingAnimation: { type: Boolean },
    arr: { type: Array },
    name: {
      type: String,
      default: "Ryan Adlard",
    },
    menus: {
      type: [Object, Array],
      default: function () {
        return [
          { name: "About", href: "about", icon: "icon ion-person" },
          { name: "Resume", href: "resume", icon: "icon ion-android-list" },
          { name: "Projects", href: "works", icon: "icon ion-paintbrush" },
        ];
      },
    },
  },
  components: { TypingAnimation },
};
</script>
