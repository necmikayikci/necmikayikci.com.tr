// Mobil menü: aç/kapat, Esc ile kapat, bağlantıya basınca kapat.
(() => {
  const btn = document.querySelector(".menu-btn");
  const panel = document.getElementById("mobil-menu");
  if (!btn || !panel) return;
  const set = (open) => {
    btn.setAttribute("aria-expanded", String(open));
    btn.setAttribute("aria-label", open ? "Menüyü kapat" : "Menüyü aç");
    panel.hidden = !open;
  };
  btn.addEventListener("click", () => set(btn.getAttribute("aria-expanded") !== "true"));
  panel.addEventListener("click", (e) => { if (e.target.closest("a")) set(false); });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !panel.hidden) { set(false); btn.focus(); }
  });
  document.addEventListener("click", (e) => {
    if (!panel.hidden && !panel.contains(e.target) && !btn.contains(e.target)) set(false);
  });
})();
