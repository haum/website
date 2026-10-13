#!/usr/bin/env python3
"""
Migration one-shot du contenu Pelican (reStructuredText) vers Hugo (Markdown).

Usage :
    python tools/rst2hugo.py ../website-content .

- lit les fichiers .rst de website-content/{articles,pages}
- extrait le titre et les métadonnées Pelican (:slug:, :date:, :tags:...)
- convertit le corps en Markdown (pandoc, via pypandoc)
- écrit content/{articles,pages}/... avec un front matter YAML
- copie website-content/images vers static/images

Dépendance : pip install pypandoc_binary pyyaml
"""

import re
import shutil
import unicodedata
import sys
from pathlib import Path

import pypandoc
import yaml

TITLE_ADORN = re.compile(r'^([=#\-~*^+"])\1{2,}\s*$')
FIELD = re.compile(r'^:([a-z_]+):\s*(.*)$')
BADGE = re.compile(r'^(.*?)\s*-\s*(brightgreen|green|yellow|orange|red|lightgrey|blue)\s*$')


def split_header(text):
    """Sépare titre + champs Pelican du corps RST."""
    lines = text.splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    title = None
    # Titre surligné + souligné, ou seulement souligné
    if i + 2 < len(lines) and TITLE_ADORN.match(lines[i]) and TITLE_ADORN.match(lines[i + 2]):
        title, i = lines[i + 1].strip(), i + 3
    elif i + 1 < len(lines) and TITLE_ADORN.match(lines[i + 1]):
        title, i = lines[i].strip(), i + 2
    meta = {}
    while i < len(lines):
        line = lines[i]
        m = FIELD.match(line)
        if m:
            meta[m.group(1)] = m.group(2).strip()
        elif line.strip():
            break
        i += 1
    return title, meta, '\n'.join(lines[i:])


def slugify(title):
    """Équivalent du slugify de Pelican (pour les pages sans :slug:)."""
    s = unicodedata.normalize('NFKD', title).encode('ascii', 'ignore').decode()
    s = re.sub(r'[^\w\s-]', '', s).strip().lower()
    return re.sub(r'[-\s]+', '-', s)


def badge(value):
    m = BADGE.match(value.strip())
    if not m:
        return {'label': value.strip(), 'color': 'lightgrey'}
    return {'label': m.group(1).strip(), 'color': m.group(2)}


def split_list(value):
    return [v.strip() for v in re.split(r'[,;]', value) if v.strip()]


def convert_body(body):
    # docutils tolère « .. image :: », pandoc non
    body = re.sub(r'^(\s*\.\. [a-z-]+) ::', r'\1::', body, flags=re.M)
    # Directive Pelican maison -> shortcode Hugo
    body = re.sub(r'^\.\. list-projects::\s*$', '.. raw:: html\n\n  HUGO_LIST_PROJECTS',
                  body, flags=re.M)
    md = pypandoc.convert_text(
        body, 'gfm+raw_html', format='rst',
        extra_args=['--wrap=none', '--shift-heading-level-by=1'])
    md = md.replace('HUGO_LIST_PROJECTS', '{{< liste-projets >}}')
    # Chemins d'images relatifs (../images/x) -> absolus
    md = re.sub(r'(\(|src=")(?:\.\./)+images/', r'\1/images/', md)
    # Liens internes Pelican absolus vers le site de prod -> relatifs
    md = re.sub(r'https?://(?:www\.)?haum\.org/', '/', md)
    return md.strip() + '\n'


def build_front_matter(title, meta, kind, rel):
    fm = {'title': title}
    fm['slug'] = meta.get('slug') or slugify(title)
    if 'date' in meta:
        d = meta['date']
        fm['date'] = d.replace(' ', 'T') + (':00' if len(d) == 16 else '')
    if 'authors' in meta:
        fm['authors'] = split_list(meta['authors'])
    if 'category' in meta:
        fm['categories'] = [meta['category'].lower()]
    if meta.get('tags'):
        fm['tags'] = split_list(meta['tags'])
    if meta.get('summary'):
        fm['summary'] = meta['summary']
    if meta.get('status') == 'draft':
        fm['draft'] = True
    if 'projet_realisation' in meta:
        fm['realisation'] = badge(meta['projet_realisation'])
    if 'projet_etat' in meta:
        fm['etat'] = badge(meta['projet_etat'])
    return fm


def extract_banner(md):
    """Sort la bannière projet du corps pour en faire une image d'en-tête."""
    m = re.search(r'^!\[([^\]]*)\]\((/images/bannieres_projets/[^)]+)\)\s*$', md, flags=re.M)
    if not m:
        return None, md
    return m.group(2), (md[:m.start()] + md[m.end():]).lstrip('\n')


def main(src, dst):
    src, dst = Path(src), Path(dst)
    count = 0
    for kind in ('articles', 'pages'):
        for f in sorted((src / kind).rglob('*.rst')):
            rel = f.relative_to(src / kind)
            text = f.read_text(encoding='utf-8')
            # Redirections JS de Pelican : remplacées par des alias Hugo
            if 'window.location' in text and text.count('\n') < 15:
                continue
            title, meta, body = split_header(text)
            fm = build_front_matter(title, meta, kind, rel)
            md = convert_body(body)
            if kind == 'pages' and rel.parts[0] == 'projets':
                banner, md = extract_banner(md)
                if banner:
                    fm['banner'] = banner
            if fm.get('slug') == 'talks':
                fm['aliases'] = ['/haumtalks.html', '/pages/haumtalks.html']
                banner, md = extract_banner(md)
                fm['banner'] = banner
            out = dst / 'content' / kind / rel.with_suffix('.md')
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text('---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
                           + '---\n\n' + md, encoding='utf-8')
            count += 1
    print(f'{count} fichiers convertis')

    images = dst / 'content' / 'images'
    if images.exists():
        shutil.rmtree(images)
    shutil.copytree(src / 'images', images,
                    ignore=shutil.ignore_patterns('projectalea.js'))
    print('images copiées')


if __name__ == '__main__':
    main(*sys.argv[1:3])
