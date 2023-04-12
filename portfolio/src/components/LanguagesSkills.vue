<template>
  <ul>
    <li class="border-line-h">
      <div class="name">English</div>
      <div class="progress">
        <div class="percentage" style="width: 90%"></div>
      </div>
    </li>
    <li class="border-line-h">
      <div class="name">German</div>
      <div class="progress">
        <div class="percentage" style="width: 60%"></div>
      </div>
    </li>
    <li class="border-line-h">
      <div class="name">Italian</div>
      <div class="progress">
        <div class="percentage" style="width: 30%"></div>
      </div>
    </li>
    <li>
      <div class="name">French</div>
      <div class="progress">
        <div class="percentage" style="width: 70%"></div>
      </div>
    </li>
  </ul>
</template>

<script>
import {createSkillsDot, dotResize} from "../utils";

export default {
  name: `LanguagesSkills`,
  mounted() {
    dotResize();
    setTimeout(createSkillsDot, 1000);
  },
};
</script>
