<template>
  <Layout :background="'gradient'" :no-sidebar="true">
    <Header :no-sidebar="true" :arr="animationText" :name="'Ihar Yazerski'" />

    <div class="card-started" id="home-card">
      <!--
  Profile
-->
      <div class="profile no-photo">
        <!-- profile image -->
        <div
          class="slide"
          style="background-image: url(images/photo.png)"
        ></div>

        <!-- profile titles -->
        <div class="title">Ihar Yazerski</div>
        <TypingAnimation :arr="animationText" />

        <!-- profile socials -->
        <div class="social">
          <a target="_blank" href="https://github.com/iyazerski"
            ><span class="fa fa-github"></span
          ></a>
          <a target="_blank" href="https://linkedin.com/in/iyazerski"
            ><span class="fa fa-linkedin"></span
          ></a>
          <a href="mailto:ihar.yazerski@gmail.com"
            ><span class="fa fa-envelope"></span
          ></a>
        </div>

        <!-- profile buttons -->
        <div class="lnks">
          <a href="/static/ihar_yazerski_cv.pdf" class="lnk" download>
            <span class="text">Download CV</span>
            <span class="ion ion-android-download"></span>
          </a>
        </div>
      </div>
    </div>
    <ActiveSection :sectionName="'about'">
      <div class="content about">
        <!-- title -->
        <div class="title">About Me</div>

        <!-- content -->
        <div class="row">
          <div class="col col-d-6 col-t-6 col-m-12 border-line-v">
            <div class="text-box">
              <p>
                <strong>Hello! I’m Ihar Yazerski.</strong>
              </p>
              <p>
                I'm a Software Engineer and Data Scientist with a passion for using Python to solve complex problems and extract insights from data. Let's collaborate to build innovative solutions that drive your business forward.
              </p>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col col-d-6 col-t-6 col-m-12 border-line-v">
            <div class="info-list">
              <ul>
                <li><strong>Location . . . . .</strong> Warsaw, Poland</li>
                <li><strong>Languages . . . . .</strong>🇺🇸 🇵🇱 🇩🇪 🇷🇺</li>
                <li><strong>Company . . . . .</strong> DataArt</li>
                <li><strong>Domains . . . . . . .</strong> FinTech, EdTech</li>
              </ul>
            </div>
          </div>
          <div class="clear"></div>
        </div>
      </div>

    </ActiveSection>
    <ActiveSection :sectionName="'resume'">
      <!--
						Resume
					-->
      <div class="content resume">
        <!-- title -->
        <div class="title">Resume</div>

        <!-- content -->
        <div class="row">
          <!-- experience -->
          <div class="col col-d-6 col-t-6 col-m-12 border-line-v">
            <div class="resume-title border-line-h">
              <div class="icon"><i class="fa fa-briefcase"></i></div>
              <div class="name">Experience</div>
            </div>
            <div class="resume-items">
              <div class="resume-item border-line-h active">
                <div class="date">Feb 2022 - Present</div>
                <div class="name">Senior Software Engineer</div>
                <div class="company">DataArt</div>
                <p>
                  Backend developer on FinTech project by US-based customer
                </p>
              </div>
              <div class="resume-item border-line-h">
                <div class="date">Aug 2021 - Feb 2022</div>
                <div class="name">Senior Software Engineer, Engineering Manager</div>
                <div class="company">Globant</div>
                <p>
                  Responsible for web services backend development on leading consulting company's project
                </p>
              </div>
              <div class="resume-item border-line-h">
                <div class="date">May 2018 - Aug 2021</div>
                <div class="name">Data Scientist</div>
                <div class="company">Silk Data</div>
                <p>
                  Core backend developer, architect and researcher on 15+ ML projects, participated in some projects management
                </p>
              </div>
              <div class="resume-item">
                <div class="date">Sep 2017 - May 2018</div>
                <div class="name">Data Scientist</div>
                <div class="company">CIB software</div>
                <p>
                  Participated in multilingual OCR engine development
                </p>
              </div>
            </div>
          </div>

          <!-- education -->
          <div class="col col-d-6 col-t-6 col-m-12 border-line-v">
            <div class="resume-title border-line-h">
              <div class="icon"><i class="fa fa-university"></i></div>
              <div class="name">Education</div>
            </div>
            <div class="resume-items">
              <div class="resume-item border-line-h">
                <div class="date">2015 - 2019</div>
                <div class="name">Belarusian State University of Informatics and Radioelectronics</div>
                <div class="company">Minsk</div>
                <p>
                  Bachelor's Degree in Computer Science
                </p>
              </div>
            </div>
          </div>

          <div class="clear"></div>
        </div>
      </div>

    </ActiveSection>

    <!--
    Card - Works
  -->
    <ActiveSection :sectionName="'works'">
      <WorkIsotope />
    </ActiveSection>

  </Layout>
</template>

<script>
import ActiveSection from "../src/components/ActiveSection.vue";
import LanguagesSkills from "../src/components/LanguagesSkills.vue";
import SkillProgress from "../src/components/SkillProgress.vue";
import Testimonials from "../src/components/Testimonials.vue";
import TypingAnimation from "../src/components/TypingAnimation.vue";
import WorkIsotope from "../src/components/WorkIsotope.vue";
import Header from "../src/layout/Header.vue";
import Layout from "../src/layout/Layout.vue";

export default {
  name: `index-new-demo-3`,
  head() {
    return {
      link: [
        {
          rel: "stylesheet",
          href: "css/new-skin/new-skin.css",
        },
        {
          rel: "stylesheet",
          href: "css/demos/demo-3-colors.css",
        },
        {
          rel: "stylesheet",
          href: "css/new-skin/classic-skin.css",
        },
      ],
    };
  },
  data() {
    return {
      skills: [
        { name: "WordPress", value: 90 },
        { name: "PHP / MYSQL", value: 75 },
        { name: "Angular / JavaScript", value: 85 },
        { name: "HTML / CSS", value: 95 },
      ],
      animationText: [
        "Senior Software Engineer",
        "Data Scientist"
      ],
    };
  },
  components: {
    Layout,
    Header,
    TypingAnimation,
    ActiveSection,
    WorkIsotope,
    SkillProgress,
    Testimonials,
    LanguagesSkills,
  },
};
</script>
