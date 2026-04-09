/**
 * MediaViewer: A simple media viewer with zoom and pan.
 * - Mouse wheel: Scroll vertically.
 * - Shift + Mouse wheel: Scroll horizontally.
 * - Ctrl + Mouse wheel: Zoom in/out.
 * - Click and drag to pan.
 * - Click outside the media, click the close button, or press Escape to close.
 */
(function () {
  if (window.MediaViewer) return;

  var overlay;
  var box;
  var img;
  var label;
  var scale = 1;
  var isPanning = false;
  var panStartX = 0;
  var panStartY = 0;
  var panScrollLeft = 0;
  var panScrollTop = 0;
  var hasDragged = false;

  function injectStyles() {
    if (document.getElementById("mv-styles")) return;

    var css = document.createElement("style");
    css.id = "mv-styles";
    css.textContent = ""
      + "#mv-overlay {"
      + "--mv-gap:clamp(40px,5vw,80px);"
      + "display:none;position:fixed;inset:0;z-index:10000;"
      + "background:rgba(0,0,0,0.82);align-items:center;justify-content:center;"
      + "padding:var(--mv-gap);"
      + "}"
      + "#mv-overlay.open{display:flex;}"
      + "#mv-box {"
      + "position:relative;background:#fff;border-radius:8px;padding:16px;"
      + "max-width:100%;max-height:100%;overflow:auto;"
      + "box-shadow:0 8px 40px rgba(0,0,0,0.5);cursor:grab;"
      + "}"
      + "#mv-box.panning{cursor:grabbing;user-select:none;}"
      + "#mv-img{display:block;transform-origin:top left;user-select:none;}"
      + "#mv-close {"
      + "position:fixed;top:0;right:0;width:var(--mv-gap);height:var(--mv-gap);"
      + "border:none;background:transparent;font-size:calc(var(--mv-gap)*0.5);line-height:1;"
      + "cursor:pointer;display:flex;align-items:center;justify-content:center;"
      + "color:#fff;padding:0;z-index:10002;opacity:0.85;"
      + "}"
      + "#mv-close:hover{opacity:1;}"
      + "#mv-controls {"
      + "position:fixed;bottom:24px;left:50%;translate:-50% 0;display:flex;"
      + "align-items:center;gap:8px;z-index:10001;background:rgba(255,255,255,0.95);"
      + "border-radius:8px;padding:6px 10px;box-shadow:0 2px 12px rgba(0,0,0,0.3);"
      + "backdrop-filter:blur(4px);"
      + "}"
      + ".mv-btn{"
      + "width:32px;height:32px;border:1px solid #ccc;border-radius:4px;"
      + "background:transparent;font-size:20px;cursor:pointer;display:flex;"
      + "align-items:center;justify-content:center;color:#333;padding:0;"
      + "}"
      + ".mv-btn:hover{background:#e8e8e8;}"
      + "#mv-scale-label{"
      + "font-size:12px;font-weight:600;color:#444;min-width:42px;text-align:center;"
      + "cursor:pointer;font-family:sans-serif;user-select:none;"
      + "}"
      + "#mv-scale-label:hover{color:#000;}";

    document.head.appendChild(css);
  }

  function applyScale(nextScale) {
    scale = Math.min(8, Math.max(0.1, nextScale));
    img.style.transform = "scale(" + scale + ")";

    var extraW = img.naturalWidth * (scale - 1);
    var extraH = img.naturalHeight * (scale - 1);
    img.style.marginRight = extraW > 0 ? extraW + "px" : "0";
    img.style.marginBottom = extraH > 0 ? extraH + "px" : "0";
    label.textContent = Math.round(scale * 100) + "%";
  }

  function resetViewOnOpen() {
    applyScale(1);
    box.scrollTop = 0;
    box.scrollLeft = 0;
  }

  function openModal(src, altText) {
    if (!src) return;

    ensureModal();

    img.src = src;
    img.alt = altText || "Image viewer";
    img.style.transform = "";
    img.style.marginRight = "0";
    img.style.marginBottom = "0";
    label.textContent = "100%";

    overlay.classList.add("open");
    document.body.style.overflow = "hidden";

    function applyInitialView() {
      window.requestAnimationFrame(resetViewOnOpen);
    }

    if (img.complete && img.naturalWidth > 0) {
      applyInitialView();
    } else {
      img.addEventListener("load", applyInitialView, { once: true });
    }
  }

  function closeModal() {
    ensureModal();
    overlay.classList.remove("open");
    document.body.style.overflow = "";
  }

  function ensureModal() {
    if (overlay) return;

    injectStyles();

    overlay = document.createElement("div");
    overlay.id = "mv-overlay";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-label", "Image viewer");
    overlay.innerHTML = ""
      + '<button id="mv-close" aria-label="Close image viewer">&#x2715;</button>'
      + '<div id="mv-box">'
      + '<img id="mv-img" alt="Image viewer" draggable="false"/>'
      + "</div>"
      + '<div id="mv-controls">'
      + '<button class="mv-btn" id="mv-out" title="Zoom out (&#x2212;)">&#x2212;</button>'
      + '<span id="mv-scale-label" title="Reset zoom (0)">100%</span>'
      + '<button class="mv-btn" id="mv-in" title="Zoom in (+)">&#x2B;</button>'
      + "</div>";
    document.body.appendChild(overlay);

    box = document.getElementById("mv-box");
    img = document.getElementById("mv-img");
    label = document.getElementById("mv-scale-label");

    box.addEventListener("mousedown", function (e) {
      if (e.button !== 0) return;

      isPanning = true;
      hasDragged = false;
      panStartX = e.clientX;
      panStartY = e.clientY;
      panScrollLeft = box.scrollLeft;
      panScrollTop = box.scrollTop;
      box.classList.add("panning");
      e.preventDefault();
    });

    window.addEventListener("mousemove", function (e) {
      if (!isPanning) return;

      var dx = e.clientX - panStartX;
      var dy = e.clientY - panStartY;
      if (Math.abs(dx) > 3 || Math.abs(dy) > 3) hasDragged = true;

      box.scrollLeft = panScrollLeft - dx;
      box.scrollTop = panScrollTop - dy;
    });

    window.addEventListener("mouseup", function () {
      if (!isPanning) return;

      isPanning = false;
      box.classList.remove("panning");

      // Restore "click outside to close" behavior, after a drag action (panning)
      if (hasDragged) {
        window.setTimeout(function () {
          hasDragged = false;
        }, 0);
      }
    });

    overlay.addEventListener("click", function (e) {
      if (e.target === overlay && !hasDragged) closeModal();
    });

    document.getElementById("mv-close").addEventListener("click", closeModal);
    document.getElementById("mv-in").addEventListener("click", function () { applyScale(scale + 0.25); });
    document.getElementById("mv-out").addEventListener("click", function () { applyScale(scale - 0.25); });
    label.addEventListener("click", function () { applyScale(1); });

    box.addEventListener("wheel", function (e) {
      if (e.ctrlKey) {
        e.preventDefault();
        applyScale(scale + (e.deltaY < 0 ? 0.15 : -0.15));
      } else if (e.shiftKey) {
        e.preventDefault();
        box.scrollLeft += e.deltaY;
      }
      // no modifier: keep native vertical scrolling
    }, { passive: false });

    document.addEventListener("keydown", function (e) {
      if (!overlay.classList.contains("open")) return;

      if (e.key === "Escape") closeModal();
      else if (e.key === "+" || e.key === "=") applyScale(scale + 0.25);
      else if (e.key === "-") applyScale(scale - 0.25);
      else if (e.key === "0") applyScale(1);
    });
  }

  function resolveElement(elementOrSelector) {
    if (!elementOrSelector) return null;
    if (typeof elementOrSelector === "string") return document.querySelector(elementOrSelector);
    return elementOrSelector;
  }

  function register(config) {
    if (!config) return;

    ensureModal();

    var trigger = resolveElement(config.trigger || config.triggerSelector);
    if (!trigger) return;

    trigger.style.cursor = "zoom-in";

    trigger.addEventListener("click", function (e) {
      var source = resolveElement(config.source || config.sourceSelector);
      if (!source && config.sourceId) source = document.getElementById(config.sourceId);
      if (!source) return;

      var src = source.currentSrc || source.src || source.getAttribute("src");
      var alt = source.getAttribute("alt");
      if (!src) return;

      e.preventDefault();
      openModal(src, alt);
    });
  }

  window.MediaViewer = {
    register: register,
    open: openModal,
    close: closeModal
  };
})();
