# Site web du HAUM — version Hugo

Moteur du site https://haum.org, généré avec [Hugo](https://gohugo.io/) (anciennement Pelican).

```sh
git clone git@github.com:haum/website-content.git content   # le contenu, comme avec Pelican
make serve       # http://localhost:1313, rechargement à chaud (toutes les pages)
make publish     # génère output/ (≈ 100 ms pour 300 pages)
```

Un seul binaire (Hugo ≥ 0.156), plus de virtualenv Python, de plugins maison ni de jQuery.
Si Hugo n'est pas installé, `make` télécharge le binaire officiel dans `.bin/`
(version figée et somme SHA-256 vérifiée, voir `tools/get_hugo.py`).

## Organisation

| Dossier | Rôle |
|---|---|
| `content/` | Clone de **website-content** : `articles/`, `pages/`, `images/` |
| `content/articles/<nom>/index.md` | Nouvel article, photos rangées dans le même dossier |
| `content/pages/projets/` | Projets : `banner`, `realisation`, `etat` dans le front matter |
| `site/` | Pages techniques du moteur (iCal, index des tags…) |
| `agenda.sqlite` | Agenda, alimenté par le bot Matrix (`!agenda add`) |
| `layouts/`, `assets/` | Gabarits et thème (aucune dépendance externe) |
| `tools/` | Export de l'agenda, migration RST → Markdown |

## Bots (Matrix et IRC)

Rien ne change pour eux : ils écrivent toujours dans `agenda.sqlite`, puis
`!updatesite` lance `git pull` (moteur et contenu), `make publish` et le rsync de
`output/`. Le Makefile convertit l'agenda en `data/agenda.json` avant d'appeler Hugo.

Rien à installer dans leurs conteneurs : au premier `make publish`, Hugo est
téléchargé dans `.bin/` (il faut seulement Python 3 et un accès à GitHub).
`make publish` crée aussi `e404.html`, la page d'erreur servie par nginx.

Les anciennes adresses Pelican des étiquettes, auteurs et catégories
(`/tag/x.html`, `/author/x.html`, `/category/x.html`) mènent à leur page Hugo
(`layouts/_partials/pelican-redirects.html`).

Le salon Matrix affiché sur le site se règle dans `hugo.toml` (`params.matrix`).

## Écrire un article

Bouton « Proposer un article » sur /articles/ (éditeur GitHub pré-rempli), ou
`hugo new articles/mon-article/index.md` en local. Guide complet pour les membres :
`content/pages/hackerland/howto_siteweb_haum_v2.md`.

```markdown
---
title: Mon super hack
slug: mon-super-hack
date: 2026-10-13T20:00:00
authors: [Pseudo]
categories: [hack]
tags: [arduino, led]
summary: Une phrase d'accroche.
---

## Première partie

Du texte, des ![images](/images/mon-hack/photo.jpg)…
```

Chaque page a un lien « Modifier cette page » qui ouvre l'éditeur GitHub.

## Migration depuis Pelican

```sh
pip install pypandoc_binary pyyaml
python tools/rst2hugo.py ../website-content .   # RST → Markdown, à lancer une seule fois
```

- `rst2hugo.py` reprend les métadonnées Pelican, le slug implicite, les badges projet,
  la directive `list-projects` (→ shortcode `{{< liste-projets >}}`) et les redirections JS
  de HAUMTalks (→ `aliases`).
