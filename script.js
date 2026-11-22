const root = document.getElementById("groups");
const toast = document.getElementById("toast");
document.getElementById("ytTop").href = SITE.yt;
document.getElementById("ytBottom").href = SITE.yt;
document.getElementById("ytAbout").href = SITE.yt;
const byId = {};

function tagsHTML(item) {
  const t = item.tags.map(x => `<span class="tag${x === "Python" ? " py" : ""}">${x}</span>`).join("");
  return `<div class="tags">${item.premium ? '<span class="tag prem">Premium</span>' : ""}${t}</div>`;
}
function vBtn(url, label) {
  return url ? `<a class="btn" href="${url}" target="_blank" rel="noopener">${label}</a>` : "";
}
function buildCard(item, key) {
  const el = document.createElement("article");
  el.className = "card";
  el.dataset.tags = item.tags.join(" ");
  const preview = item.img
    ? `<img src="${item.img}" alt="${item.title}">`
    : `<iframe src="demos/${item.id}.html" title="${item.title}"></iframe>`;
  let btns;
  if (item.premium) btns = `<a class="btn main" href="${item.buy}" target="_blank" rel="noopener">Buy</a>`;
  else if (item.code) { byId[key] = item.code; btns = `<button class="btn main" data-copy="${key}">Copy code</button><a class="btn" href="${item.dl}" download>Download</a>`; }
  else btns = `<a class="btn main" href="${item.zip}" download>Download zip</a>`;
  btns += vBtn(item.video, "Watch video");
  el.innerHTML = `${item.emoji ? `<span class="sticker">${item.emoji}</span>` : ""}<div class="frame">${preview}</div><div class="body"><h3>${item.title}</h3><p>${item.desc}</p>${tagsHTML(item)}<div class="btns">${btns}</div></div>`;
  return el;
}
SITE.groups.forEach((g, gi) => {
  const sec = document.createElement("section");
  sec.className = "group";
  const gb = (g.zip ? `<a class="btn main" href="${g.zip}" download>Download all (zip)</a>` : "") + vBtn(g.video, "Watch the video") + vBtn(g.short, "Watch the Short");
  sec.innerHTML = `<div class="ghead"><div><h2>${g.title} ${g.emoji}</h2><p>${g.desc}</p></div><div class="gbtns">${gb}</div></div><div class="grid"></div>`;
  const grid = sec.querySelector(".grid");
  g.items.forEach((it, i) => grid.appendChild(buildCard(it, gi + "_" + i)));
  root.appendChild(sec);
});

function fit() {
  document.querySelectorAll(".frame iframe").forEach(f => {
    const w = f.parentElement.clientWidth;
    if (w) f.style.transform = "scale(" + w / 960 + ")";
  });
}
addEventListener("resize", fit); fit();

function copyText(text) {
  const fallback = () => {
    const ta = document.createElement("textarea");
    ta.value = text; document.body.appendChild(ta); ta.select();
    try { document.execCommand("copy"); } catch (e) {}
    ta.remove();
  };
  if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text).catch(fallback);
  fallback();
  return Promise.resolve();
}
document.addEventListener("click", e => {
  const b = e.target.closest("[data-copy]");
  if (!b) return;
  copyText(byId[b.dataset.copy]).then(() => {
    b.textContent = "Copied ✓"; b.classList.add("done"); burst(b);
    toast.classList.add("show");
    setTimeout(() => { b.textContent = "Copy code"; b.classList.remove("done"); toast.classList.remove("show"); }, 1800);
  });
});

const chips = document.getElementById("chips");
["All", "HTML", "CSS", "JS", "Python"].forEach((name, i) => {
  const c = document.createElement("button");
  c.className = "chip" + (i === 0 ? " on" : ""); c.textContent = name;
  c.onclick = () => {
    chips.querySelectorAll(".chip").forEach(x => x.classList.remove("on")); c.classList.add("on");
    document.querySelectorAll(".group").forEach(sec => {
      let any = false;
      sec.querySelectorAll(".card").forEach(card => {
        const show = name === "All" || card.dataset.tags.split(" ").includes(name);
        card.style.display = show ? "" : "none"; if (show) any = true;
      });
      sec.style.display = any ? "" : "none";
    });
    fit();
  };
  chips.appendChild(c);
});

// cozy touches: floating hearts + click hearts
const calm = !matchMedia("(prefers-reduced-motion: reduce)").matches;
if (calm) {
  const box = document.getElementById("floaters"), sy = ["♥", "♥", "✦", "♡", "✧"];
  for (let i = 0; i < 16; i++) {
    const s = document.createElement("span");
    s.className = "fl"; s.textContent = sy[i % sy.length];
    s.style.left = Math.random() * 100 + "%";
    s.style.fontSize = 10 + Math.random() * 16 + "px";
    s.style.animationDuration = 16 + Math.random() * 18 + "s";
    s.style.animationDelay = -Math.random() * 30 + "s";
    s.style.color = ["#ffb3d9", "#c9b6ff", "#a8e6ff"][i % 3];
    box.appendChild(s);
  }
}
function heart(x, y) {
  if (!calm) return;
  const h = document.createElement("span");
  h.className = "pop"; h.textContent = ["♥", "✦", "♡"][Math.floor(Math.random() * 3)];
  h.style.left = x + "px"; h.style.top = y + "px"; document.body.appendChild(h);
  setTimeout(() => h.remove(), 1000);
}
function burst(el) {
  const r = el.getBoundingClientRect();
  for (let i = 0; i < 7; i++) setTimeout(() => heart(r.left + Math.random() * r.width, r.top + Math.random() * 10), i * 60);
}
document.addEventListener("click", e => heart(e.clientX, e.clientY));
