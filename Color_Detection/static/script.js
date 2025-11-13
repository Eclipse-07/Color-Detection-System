'use strict';
const navbar = document.querySelector("[data-navbar]");
const navbarLinks = document.querySelectorAll("[data-nav-link]");
const navbarToggler = document.querySelector("[data-nav-toggler]");
navbarToggler.addEventListener("click", function () {
  navbar.classList.toggle("active");
  this.classList.toggle("active");
});

for (let i = 0; i < navbarLinks.length; i++) {
  navbarLinks[i].addEventListener("click", function () {
    navbar.classList.remove("active");
    navbarToggler.classList.remove("active");
  });
}
const searchTogglers = document.querySelectorAll("[data-search-toggler]");
const searchBox = document.querySelector("[data-search-box]");
for (let i = 0; i < searchTogglers.length; i++) {
  searchTogglers[i].addEventListener("click", function () {
    searchBox.classList.toggle("active");
  });
}
const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");
window.addEventListener("scroll", function () {
  if (window.scrollY >= 200) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
});
'use strict';

const video = document.getElementById("live-video");
const playBtn = document.querySelector(".play-btn");
const pauseBtn = document.querySelector(".pause-btn");
const rewindBtn = document.querySelector(".rewind-btn");
const fastForwardBtn = document.querySelector(".fast-forward-btn");
const progressBar = document.getElementById("progress");
playBtn.addEventListener("click", function () {
  video.play();
  playBtn.style.display = 'none';
  pauseBtn.style.display = 'inline';
});
pauseBtn.addEventListener("click", function () {
  video.pause();
  playBtn.style.display = 'inline';
  pauseBtn.style.display = 'none';
});
rewindBtn.addEventListener("click", function () {
  video.currentTime -= 10;
});

fastForwardBtn.addEventListener("click", function () {
  video.currentTime += 10;
});
video.addEventListener("timeupdate", function () {
  const progress = (video.currentTime / video.duration) * 100;
  progressBar.value = progress;
});
progressBar.addEventListener("input", function () {
  const time = (progressBar.value / 100) * video.duration;
  video.currentTime = time;
});
document.getElementById('getStartedBtn').addEventListener('click', function() {
  document.getElementById('targetSection').scrollIntoView({ behavior: 'smooth' });
});
document.getElementById('uploadButton').addEventListener('click', function() {
  document.getElementById('file').click();
});
document.getElementById('file').addEventListener('change', function() {
  const uploadButton = document.getElementById('uploadButton');
  if (this.files && this.files.length > 0) {
      uploadButton.querySelector('.span').textContent = 'Uploaded';
      uploadButton.querySelector('ion-icon').name = 'checkmark-outline';
  } else {
      uploadButton.querySelector('.span').textContent = 'Upload an Image';
      uploadButton.querySelector('ion-icon').name = 'cloud-upload-outline';
  }});
function getColor(event) {
  console.log('getColor function called');
  console.log(event);
  console.log(x, y);
  console.log(language);
}
const logoutBtn = document.querySelector('.logout-btn');
logoutBtn.addEventListener('click', () => {
  fetch('/logout', { method: 'GET' })
    .then(() => {
      window.location.href = '/login';
    })
    .catch((error) => {
      console.error('Error logging out:', error);
    });
});

