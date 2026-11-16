// Day / Night switch. With no stored choice, the system setting applies (tokens.css).
(function () {
  var KEY = 'dc-briefing-theme', root = document.documentElement;
  var buttons = document.querySelectorAll('[data-theme-set]');
  function current() {
    var t = root.getAttribute('data-theme');
    if (t === 'day' || t === 'night') return t;
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'night' : 'day';
  }
  function paint() {
    var c = current();
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-theme-set') === c)); });
  }
  buttons.forEach(function (b) {
    b.addEventListener('click', function () {
      var t = b.getAttribute('data-theme-set');
      root.setAttribute('data-theme', t);
      try { localStorage.setItem(KEY, t); } catch (e) {}
      paint();
    });
  });
  paint();
  // close the phone menu when a page link is chosen
  document.querySelectorAll('.nav-menu a').forEach(function (a) {
    a.addEventListener('click', function () { a.closest('details').removeAttribute('open'); });
  });
})();
