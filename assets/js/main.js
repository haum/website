// HAUM — petites interactions, sans dépendance (remplace jQuery 2.1).

// Liens vers d'autres sites : nouvel onglet (sous-domaines compris : forum,
// photos…). Les liens internes et « mailto: » ne changent pas.
function externalLinks(root = document) {
  root.querySelectorAll('a[href]').forEach((a) => {
    if (!/^https?:$/.test(a.protocol) || a.hostname === location.hostname) return;
    if (a.target) return;
    a.target = '_blank';
    a.rel = (a.rel ? `${a.rel} ` : '') + 'noopener';
    if (!a.querySelector('.sr-only')) {
      const hint = document.createElement('span');
      hint.className = 'sr-only';
      hint.textContent = ' (nouvel onglet)';
      a.append(hint);
    }
  });
}

// Statut d'ouverture du local (même API que l'ancien site : "1" = ouvert)
function spaceStatus() {
  const el = document.querySelector('.space-status');
  if (!el) return;
  const label = el.querySelector('.label');
  fetch(el.dataset.url, { cache: 'no-store' })
    .then((r) => (r.ok ? r.text() : Promise.reject()))
    .then((t) => {
      const open = t.trim() === '1';
      el.dataset.status = open ? 'open' : 'closed';
      label.textContent = open ? 'Local ouvert' : 'Local fermé';
      // Version détaillée de la page « Le local est-il ouvert ? »
      document.querySelectorAll('.local-status').forEach((box) => {
        box.dataset.status = el.dataset.status;
        box.querySelector('.local-status-text').textContent = open
          ? 'Le local est ouvert : passez nous voir !'
          : 'Le local est fermé pour le moment.';
      });
    })
    .catch(() => { label.textContent = 'Local'; });
}

// Bouton de thème : automatique (système) → clair → sombre
function themeToggle() {
  const btn = document.querySelector('.theme-toggle');
  if (!btn) return;
  const root = document.documentElement;
  const labels = { auto: 'automatique', light: 'clair', dark: 'sombre' };
  const next = { auto: 'light', light: 'dark', dark: 'auto' };
  const label = (t) => {
    const text = `Thème : ${labels[t]} (cliquer pour changer)`;
    btn.setAttribute('aria-label', text);
    btn.title = text;
  };
  label(root.dataset.theme || 'auto');
  btn.addEventListener('click', () => {
    const t = next[root.dataset.theme || 'auto'];
    if (t === 'auto') delete root.dataset.theme;
    else root.dataset.theme = t;
    try {
      if (t === 'auto') localStorage.removeItem('theme');
      else localStorage.setItem('theme', t);
    } catch (e) { /* navigation privée : le choix vaut pour la page */ }
    label(t);
  });
}

// Masque les évènements passés (le site n'est régénéré qu'à chaque commit)
function agenda() {
  const now = new Date();
  now.setHours(4, 0, 0, 0);
  document.querySelectorAll('.events').forEach((list) => {
    const limit = parseInt(list.dataset.limit, 10) || Infinity;
    let shown = 0;
    list.querySelectorAll('.event').forEach((ev) => {
      const upcoming = new Date(ev.dataset.date) > now;
      ev.hidden = !upcoming || shown >= limit;
      if (!ev.hidden) shown++;
    });
    const empty = list.nextElementSibling;
    if (empty && empty.classList.contains('events-empty')) empty.hidden = shown > 0;
  });
}

// Accroche aléatoire façon terminal
function tagline() {
  const el = document.querySelector('[data-taglines]');
  if (!el) return;
  const lines = JSON.parse(el.dataset.taglines);
  const text = el.querySelector('.tagline-text');
  let i = Math.floor(Math.random() * lines.length);
  text.textContent = lines[i];
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  setInterval(() => {
    i = (i + 1) % lines.length;
    text.textContent = lines[i];
  }, 8000);
}

// Bouton « Proposer un article » : date du jour dans le modèle
function newArticle() {
  const today = new Date().toISOString().slice(0, 10);
  document.querySelectorAll('[data-new-article]').forEach((a) => {
    a.href = a.href.replace(/date%3A\+\d{4}-\d{2}-\d{2}/, `date%3A+${today}`);
  });
}

// Projet vedette aléatoire
function spotlight() {
  document.querySelectorAll('[data-random]').forEach((box) => {
    const items = box.children;
    if (items.length) items[Math.floor(Math.random() * items.length)].hidden = false;
  });
}

// Derniers messages Mastodon (API publique, pas de bibliothèque tierce)
function toots() {
  const box = document.querySelector('.toots');
  if (!box) return;
  const { instance, account } = box.dataset;
  const api = `https://${instance}/api/v1`;
  fetch(`${api}/accounts/lookup?acct=${account}`)
    .then((r) => r.json())
    .then((acc) => fetch(`${api}/accounts/${acc.id}/statuses?limit=8&exclude_replies=true`))
    .then((r) => r.json())
    .then((statuses) => {
      box.replaceChildren(...statuses.map((s) => {
        const src = s.reblog || s;
        const a = document.createElement('a');
        a.className = 'toot';
        a.href = src.url;
        a.style.display = 'block';
        a.style.color = 'inherit';
        a.style.textDecoration = 'none';
        const body = document.createElement('div');
        // Contenu HTML assaini par l'instance Mastodon
        body.innerHTML = src.content;
        body.querySelectorAll('a').forEach((l) => l.replaceWith(...l.childNodes));
        const media = src.media_attachments.find((m) => m.type === 'image');
        if (media) {
          const img = document.createElement('img');
          img.src = media.preview_url;
          img.alt = media.description || '';
          img.loading = 'lazy';
          body.append(img);
        }
        const time = document.createElement('time');
        time.dateTime = src.created_at;
        time.textContent = (s.reblog ? '↻ partagé · ' : '')
          + new Date(src.created_at).toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' });
        a.append(body, time);
        return a;
      }));
      externalLinks(box);
    })
    .catch(() => {
      box.innerHTML = `<p class="muted">Impossible de charger le fil. <a href="https://${instance}/@${account}">Voir sur Mastodon</a>.</p>`;
    });
}

document.addEventListener('DOMContentLoaded', () => {
  externalLinks();
  spaceStatus();
  themeToggle();
  agenda();
  tagline();
  spotlight();
  newArticle();
  toots();
});
