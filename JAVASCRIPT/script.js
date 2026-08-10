document.addEventListener('DOMContentLoaded', function() {
  if (window.AOS) {
    AOS.init({
      duration: 1000,
      once: true
    });
  }

  if (window.Typed) {
    new Typed('#typing', {
      strings: ['Front-End Developer', 'Canva Designer', 'AI Poster Creator'],
      typeSpeed: 80,
      backSpeed: 40,
      backDelay: 2000,
      loop: true
    });
  }

  const topBtn = document.getElementById('topBtn');
  if (topBtn) {
    window.addEventListener('scroll', function() {
      topBtn.style.display = window.scrollY > 400 ? 'block' : 'none';
    });

    topBtn.addEventListener('click', function() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
});
