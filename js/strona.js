(function () {
  // podgląd miejsc na grafiki z grafiki/PROMPTY.md: adres z ?sloty
  if (/[?&]sloty/.test(location.search)) document.documentElement.classList.add('sloty');

  // nagłówek: tło po przewinięciu poza zdjęcie
  var nag = document.querySelector('.naglowek');
  var tlo = function () { nag.classList.toggle('naglowek--tlo', window.scrollY > 80); };
  tlo(); window.addEventListener('scroll', tlo, { passive: true });

  // menu na telefonie: Esc zamyka, fokus wraca na przycisk
  var btn = document.querySelector('.naglowek .menu-btn'), mob = document.getElementById('menu-mob');
  var zamknij = function () { mob.hidden = true; btn.setAttribute('aria-expanded', 'false'); document.body.style.overflow = ''; btn.focus(); };
  btn.addEventListener('click', function () { mob.hidden = false; btn.setAttribute('aria-expanded', 'true'); document.body.style.overflow = 'hidden'; mob.querySelector('nav a').focus(); });
  mob.querySelector('[data-zamknij]').addEventListener('click', zamknij);
  mob.addEventListener('click', function (e) { if (e.target.closest('nav a, .btn')) { mob.hidden = true; btn.setAttribute('aria-expanded', 'false'); document.body.style.overflow = ''; } });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !mob.hidden) zamknij(); });

  // zakładki karnetów: klik i strzałki (wzorzec WAI-ARIA)
  var taby = [].slice.call(document.querySelectorAll('.wybor [role=tab]'));
  if (taby.length) {
    var wybierz = function (t) {
      taby.forEach(function (x) {
        var on = x === t;
        x.setAttribute('aria-selected', String(on));
        x.tabIndex = on ? 0 : -1;
        document.getElementById(x.getAttribute('aria-controls')).hidden = !on;
      });
    };
    taby.forEach(function (t, i) {
      t.addEventListener('click', function () { wybierz(t); });
      t.addEventListener('keydown', function (e) {
        var k = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (!k) return;
        e.preventDefault();
        var n = taby[(i + k + taby.length) % taby.length]; wybierz(n); n.focus();
      });
    });
    wybierz(taby.filter(function (t) { return t.getAttribute('aria-selected') === 'true'; })[0]);
    document.querySelectorAll('[data-tab]').forEach(function (a) {
      a.addEventListener('click', function () { wybierz(document.getElementById(a.dataset.tab)); });
    });
  }

  // formularz kontaktowy (makieta: nic nie wysyła, pokazuje podziękowanie)
  var f = document.getElementById('kontakt-form');
  if (f) f.addEventListener('submit', function (e) {
    e.preventDefault();
    var zly = f.querySelector(':invalid');
    if (zly) { zly.focus(); zly.reportValidity && zly.reportValidity(); return; }
    f.querySelector('.form-pola').hidden = true;
    var d = f.querySelector('.dzieki'); d.hidden = false; d.focus();
  });
})();
