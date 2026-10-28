(function () {
  'use strict';
  document.querySelectorAll('iframe.corn-earworm-map').forEach(function (frame) {
    let sizeObserver;
    let loadObserver;
    let pendingFit;

    function watch() {
      if (sizeObserver) sizeObserver.disconnect();
      if (loadObserver) loadObserver.disconnect();
      cancelAnimationFrame(pendingFit);
      try {
        const doc = frame.contentDocument;
        if (!doc || !doc.body) return;

        function attach() {
          const map = doc.querySelector('[data-root-id] > .bk-Column');
          if (!map) return;
          loadObserver.disconnect();

          function fit() {
            cancelAnimationFrame(pendingFit);
            pendingFit = requestAnimationFrame(function () {
              // measure the map, not the iframe's full document height
              const height = Math.ceil(map.getBoundingClientRect().height) + 2;
              if (height > 2) {
                // avoid scrollbars changing the map width during a resize
                frame.scrolling = 'no';
                if (frame.style.height !== height + 'px') {
                  frame.style.height = height + 'px';
                }
              }
            });
          }

          sizeObserver = new ResizeObserver(fit);
          sizeObserver.observe(map);
          fit();
        }

        // bokeh can finish drawing after the iframe loads
        loadObserver = new MutationObserver(attach);
        loadObserver.observe(doc.body, {childList: true, subtree: true});
        attach();
      } catch (error) {
        // keep the fallback height if the map is unavailable
      }
    }

    frame.addEventListener('load', watch);
    watch();
  });
}());
