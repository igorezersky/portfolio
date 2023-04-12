<template>
  <Fragment>
    <li v-for="skill in skills" :key="skill.name">
      <div class="name">{{ skill.name }}</div>
      <div class="progress" :class="'p' + skill.value">
        <span>{{ skill.value }}%</span>
        <div class="slice">
          <div class="bar"></div>
          <div class="fill"></div>
        </div>
      </div></li
  ></Fragment>
</template>

<script>
import {Fragment} from "vue-fragment";

export default {
  name: `SkillProgress`,
  components: {
    Fragment,
  },
  props: {
    skills: {
      type: Array,
    },
  },
};
</script>
