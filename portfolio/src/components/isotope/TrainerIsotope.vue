<template>
  <Isotope>
    <!-- filters -->
    <div class="filter-menu filter-button-group">
      <div class="f_btn active">
        <label
          ><input type="radio" name="fl_radio" value="grid-item" />All</label
        >
      </div>
      <div class="f_btn">
        <label><input type="radio" name="fl_radio" value="photo" />Image</label>
      </div>
      <div class="f_btn">
        <label
          ><input type="radio" name="fl_radio" value="gallery" />Gallery</label
        >
      </div>
      <div class="f_btn">
        <label><input type="radio" name="fl_radio" value="video" />Video</label>
      </div>
    </div>

    <!-- content -->
    <div class="row grid-items border-line-v">
      <div class="col col-d-6 col-t-6 col-m-12 grid-item photo border-line-h">
        <div class="box-item">
          <div class="image">
            <a href="images/twork1.jpg" class="has-popup-image">
              <img src="images/twork1.jpg" alt="" />
              <span class="info">
                <span class="ion ion-image"></span>
              </span>
            </a>
          </div>
          <div class="desc">
            <a href="images/works/work1.jpg" class="name has-popup-image"
              >Fitness Item 1</a
            >
            <div class="category">Image</div>
          </div>
        </div>
      </div>

      <!-- work item video -->
      <div class="col col-d-6 col-t-6 col-m-12 grid-item video border-line-h">
        <div class="box-item">
          <div class="image">
            <a href="https://vimeo.com/97102654" class="has-popup-video">
              <img src="images/twork2.jpg" alt="" />
              <span class="info">
                <span class="ion ion-videocamera"></span>
              </span>
            </a>
          </div>
          <div class="desc">
            <a href="https://vimeo.com/97102654" class="name has-popup-video"
              >Fitness Item 2</a
            >
            <div class="category">Video</div>
          </div>
        </div>
      </div>

      <!-- work item photo -->
      <div class="col col-d-6 col-t-6 col-m-12 grid-item photo border-line-h">
        <div class="box-item">
          <div class="image">
            <a href="images/twork3.jpg" class="has-popup-image">
              <img src="images/twork3.jpg" alt="" />
              <span class="info">
                <span class="ion ion-image"></span>
              </span>
            </a>
          </div>
          <div class="desc">
            <a href="images/works/work1.jpg" class="name has-popup-image"
              >Fitness Item 3</a
            >
            <div class="category">Image</div>
          </div>
        </div>
      </div>

      <!-- work item video -->
      <div class="col col-d-6 col-t-6 col-m-12 grid-item video border-line-h">
        <div class="box-item">
          <div class="image">
            <a href="https://vimeo.com/97102654" class="has-popup-video">
              <img src="images/twork4.jpg" alt="" />
              <span class="info">
                <span class="ion ion-videocamera"></span>
              </span>
            </a>
          </div>
          <div class="desc">
            <a href="https://vimeo.com/97102654" class="name has-popup-video"
              >Fitness Item 4</a
            >
            <div class="category">Video</div>
          </div>
        </div>
      </div>

      <!-- work item photo -->
      <div class="col col-d-6 col-t-6 col-m-12 grid-item gallery border-line-h">
        <div class="box-item">
          <div class="image">
            <a href="#gallery-1" class="has-popup-gallery">
              <img src="images/twork5.jpg" alt="" />
              <span class="info">
                <span class="ion ion-images"></span>
              </span>
            </a>
            <div id="gallery-1" class="mfp-hide">
              <a href="images/twork3.jpg"></a>
              <a href="images/twork4.jpg"></a>
              <a href="images/twork5.jpg"></a>
            </div>
          </div>
          <div class="desc">
            <a href="#gallery-1" class="has-popup-gallery">Fitness Item 5</a>
            <div class="category">Gallery</div>
          </div>
        </div>
      </div>

      <!-- work item photo -->
      <div class="col col-d-6 col-t-6 col-m-12 grid-item gallery border-line-h">
        <div class="box-item">
          <div class="image">
            <a href="#gallery-2" class="has-popup-gallery">
              <img src="images/twork6.jpg" alt="" />
              <span class="info">
                <span class="ion ion-images"></span>
              </span>
            </a>
            <div id="gallery-2" class="mfp-hide">
              <a href="images/twork3.jpg"></a>
              <a href="images/twork4.jpg"></a>
              <a href="images/twork6.jpg"></a>
            </div>
          </div>
          <div class="desc">
            <a href="#gallery-2" class="has-popup-gallery">Fitness Item 6</a>
            <div class="category">Gallery</div>
          </div>
        </div>
      </div>
      <div class="clear"></div>
    </div>
  </Isotope>
</template>

<script>
import Isotope from "./Isotope.vue";

export default {
  name: `WorkIsotope`,
  components: { Isotope },
};
</script>
