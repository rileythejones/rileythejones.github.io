(function () {
  'use strict';
  document.querySelectorAll('iframe.cyprus-visual').forEach(function (frame) {
    let observer;
    function fit() {
      try {
        const main = frame.contentDocument && frame.contentDocument.querySelector('main');
        if (!main) return;
        const height = Math.ceil(main.getBoundingClientRect().height) + 2;
        if (height > 2) frame.style.height = height + 'px';
      } catch (error) {
        // Keep the HTML fallback height if the embedded document is unavailable.
      }
    }
    function watch() {
      if (observer) observer.disconnect();
      try {
        const main = frame.contentDocument && frame.contentDocument.querySelector('main');
        if (main && 'ResizeObserver' in window) {
          observer = new ResizeObserver(fit);
          observer.observe(main);
        }
      } catch (error) {
        // A missing visual leaves the original iframe size intact.
      }
      fit();
    }
    frame.addEventListener('load', watch);
    window.addEventListener('resize', fit);
    watch();
  });
}());
