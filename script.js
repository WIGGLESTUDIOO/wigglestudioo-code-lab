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
    : `<iframe loading="lazy" src="demos/${item.id}.html" title="${item.title}"></iframe>`;
  let btns;
  if (item.premium) btns = `<a class="btn main" href="${item.buy}" target="_blank" rel="noopener">Buy</a>`;
  else if (item.code) { byId[key] = item.code; btns = `<button class="btn main" data-copy="${key}">Copy code</button><a class="btn" href="${item.dl}" download>Download</a>`; }
  else btns = `<a class="btn main" href="${item.zip}" download>Download zip</a>`;
  btns += vBtn(item.video, "Watch video");
  el.innerHTML = `${item.emoji ? `<span class="sticker">${item.emoji}</span>` : ""}<div class="frame">${preview}</div><div class="body"><h3>${item.title}</h3><p>${item.desc}</p>${tagsHTML(item)}<div class="btns">${btns}</div></div>`;
  return el;
}
const SHORT_G = ["Little components", "Python Art"];
let curFilter = "All";
const matches = (tags, name) => name === "All" || tags.includes(name);

function railBlock(id, title, sub, cls) {
  const sec = document.createElement("section");
  sec.className = "block"; sec.id = id;
  sec.innerHTML = `<div class="bhead"><div><h2>${title}</h2><p>${sub}</p></div>
    <div class="bctl"><button class="arrow" data-dir="-1" aria-label="Scroll left">‹</button><button class="arrow" data-dir="1" aria-label="Scroll right">›</button>
    <button class="btn seeall">See all <span>›</span></button></div></div><div class="rail ${cls}"></div>`;
  const rail = sec.querySelector(".rail");
  sec.querySelectorAll(".arrow").forEach(b => b.onclick = () => rail.scrollBy({ left: b.dataset.dir * rail.clientWidth * .8, behavior: "smooth" }));
  const all = sec.querySelector(".seeall");
  all.onclick = () => {
    const w = rail.classList.toggle("wrap");
    sec.classList.toggle("open", w);
    all.innerHTML = w ? "Show less <span>‹</span>" : "See all <span>›</span>";
    fit();
  };
  root.appendChild(sec);
  return { sec, rail };
}

// Long videos: one tile per video, tap to open its code below
const L = railBlock("longBlock", "🎬 Long video code", "Full step-by-step tutorials. Tap a video to see all its code.", "tiles");
const panel = document.createElement("div"); panel.className = "panel"; L.sec.appendChild(panel);
let openGi = -1;
function openGroup(gi, tile) {
  const g = SITE.groups[gi];
  L.rail.querySelectorAll(".tile").forEach(t => t.classList.remove("on"));
  if (openGi === gi) { panel.innerHTML = ""; openGi = -1; return; }
  openGi = gi; tile.classList.add("on");
  const gb = (g.zip ? `<a class="btn main" href="${g.zip}" download>Download all (zip)</a>` : "") + vBtn(g.video, "Watch the video") + vBtn(g.short, "Watch the Short");
  panel.innerHTML = `<div class="ghead"><div><h2>${g.title} ${g.emoji}</h2><p>${g.desc}</p></div><div class="gbtns">${gb}<button class="btn" id="closeP">Close ✕</button></div></div><div class="grid"></div>`;
  const grid = panel.querySelector(".grid");
  g.items.forEach((it, i) => grid.appendChild(buildCard(it, gi + "_" + i)));
  panel.querySelector("#closeP").onclick = () => { panel.innerHTML = ""; openGi = -1; tile.classList.remove("on"); };
  applyFilter(curFilter); fit();
  panel.scrollIntoView({ behavior: "smooth", block: "start" });
}
SITE.groups.forEach((g, gi) => {
  if (SHORT_G.includes(g.title)) return;
  const t = document.createElement("button");
  t.className = "tile"; t.dataset.tags = [...new Set(g.items.flatMap(i => i.tags))].join(" ");
  t.innerHTML = `<span class="te">${g.emoji}</span><b>${g.title}</b><small>${g.items.length} ${g.items.length === 1 ? "project" : "pieces of code"}</small>`;
  t.onclick = () => openGroup(gi, t);
  L.rail.appendChild(t);
});

// Shorts: a row of small cards
const S = railBlock("shortBlock", "📱 Shorts code", "Quick little pieces from my Shorts. Copy, paste, done.", "cards");
SITE.groups.forEach((g, gi) => {
  if (!SHORT_G.includes(g.title)) return;
  g.items.forEach((it, i) => S.rail.appendChild(buildCard(it, gi + "_" + i)));
});

function applyFilter(name) {
  curFilter = name;
  document.querySelectorAll(".card").forEach(c => { c.style.display = matches(c.dataset.tags.split(" "), name) ? "" : "none"; });
  document.querySelectorAll(".tile").forEach(t => { t.style.display = matches(t.dataset.tags.split(" "), name) ? "" : "none"; });
  L.sec.style.display = [...L.rail.children].some(t => t.style.display !== "none") ? "" : "none";
  S.sec.style.display = [...S.rail.children].some(t => t.style.display !== "none") ? "" : "none";
}

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
    applyFilter(name); fit();
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
