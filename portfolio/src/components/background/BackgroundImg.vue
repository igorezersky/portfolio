<template>
  <div class="background" :style="{ 'background-image': `url(${img})` }"></div>
</template>

<script>
export default {
  name: `BackgroundImg`,
  props: {
    img: {
      type: String,
      default: "images/bg3.jpg",
    },
  },
};
</script>
