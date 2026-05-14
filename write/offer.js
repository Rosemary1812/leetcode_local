// 防抖
//
function debounce(fn, delay = 200, immediate = false) {
  let timer = null;
  return function (...args) {
    const context = this;

    if (timer) clearTimeout(timer);

    if (immediate) {
      const shouldCall = !timer;

      timer = setTimeout(() => {
        timer = null;
      }, delay);

      if (shouldCall) {
        return fn.apply(context, args);
      } else {
        timer = setTimeout(() => {
          fn.apply(context, args);
        }, delay);
      }
    }
  };
}

function throttle(fn, delay = 300) {
  let lastTime = 0;

  return function (...args) {
    const now = Date.now();

    const context = this;

    if (now - lastTime >= delay) {
      lastTime = now;
      return (fn, apply(context, args));
    }
  };
}
