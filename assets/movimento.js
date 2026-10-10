// Movimento do site: barra de leitura, revelação ao rolar, contadores e botão de topo.
(function () {
  var reduz = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var doc = document.documentElement;

  // Barra de progresso de leitura e botão "voltar ao topo"
  var barra = document.querySelector(".progresso span");
  var topoBtn = document.querySelector(".topo-btn");
  function rolagem() {
    var max = doc.scrollHeight - doc.clientHeight;
    var p = max > 0 ? doc.scrollTop / max : 0;
    if (barra) barra.style.transform = "scaleX(" + p + ")";
    if (topoBtn) topoBtn.classList.toggle("visivel", doc.scrollTop > 600);
  }
  window.addEventListener("scroll", rolagem, { passive: true });
  rolagem();
  if (topoBtn) topoBtn.addEventListener("click", function (e) {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: reduz ? "auto" : "smooth" });
  });

  // Elementos que entram suavemente ao aparecer na tela
  var alvos = document.querySelectorAll(
    ".conteudo > h2, .conteudo > h3, .conteudo > p, .conteudo > ul, .conteudo > ol, .caixa, .tabela, .bloco, " +
    "details.instr, .numeros > div, .passo, .lista-anexos li, .ident"
  );
  // Escalona itens irmãos (cartões, números) para entrarem em sequência
  [".numeros > div", ".passo", ".lista-anexos li", "details.instr"].forEach(function (sel) {
    var grupos = new Map();
    document.querySelectorAll(sel).forEach(function (el) {
      var pai = el.parentElement;
      var i = grupos.get(pai) || 0;
      el.style.setProperty("--atraso", Math.min(i, 6) * 90 + "ms");
      grupos.set(pai, i + 1);
    });
  });

  function animaNumero(el) {
    var txt = el.textContent.trim();
    var m = txt.match(/^(\d+)(.*)$/);
    if (!m || reduz) return;
    var fim = parseInt(m[1], 10), resto = m[2], t0 = null, dur = 1100;
    function passo(t) {
      if (!t0) t0 = t;
      var k = Math.min((t - t0) / dur, 1);
      var e = 1 - Math.pow(1 - k, 3);
      el.textContent = Math.round(fim * e) + resto;
      if (k < 1) requestAnimationFrame(passo);
    }
    el.textContent = "0" + resto;
    requestAnimationFrame(passo);
  }

  if (!("IntersectionObserver" in window) || reduz) {
    alvos.forEach(function (el) { el.classList.add("visivel"); });
    return;
  }
  alvos.forEach(function (el) { el.classList.add("revela"); });
  var obs = new IntersectionObserver(function (entradas) {
    entradas.forEach(function (en) {
      if (!en.isIntersecting) return;
      var el = en.target;
      el.classList.add("visivel");
      if (el.matches(".numeros > div")) {
        var n = el.querySelector("p");
        if (n) animaNumero(n);
      }
      obs.unobserve(el);
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0 });
  alvos.forEach(function (el) { obs.observe(el); });
})();
