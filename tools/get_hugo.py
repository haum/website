#!/usr/bin/env python3
"""
Télécharge le binaire Hugo officiel (version figée, somme SHA-256 vérifiée)
dans .bin/hugo, pour les machines où Hugo n'est pas installé : les bots IRC et
Matrix lancent « make publish » depuis leurs conteneurs, qui n'ont que Python.

Usage : python3 tools/get_hugo.py .bin/hugo
Pour changer de version : mettre à jour VERSION et les sommes, tirées de
https://github.com/gohugoio/hugo/releases/download/v<VERSION>/hugo_<VERSION>_checksums.txt
"""

import hashlib
import io
import os
import platform
import sys
import tarfile
import urllib.request

VERSION = '0.168.0'
SHA256 = {
    'amd64': 'fada83ad56bb27ed4cb7dd81590303bdac16140f944ac4e66fc248117e2d5594',
    'arm64': '91ce984e998a955a3dc1b5852eb4e65d0ed0f6d12a5c51690df97a548e1fdeeb',
}
ARCH = {'x86_64': 'amd64', 'amd64': 'amd64', 'aarch64': 'arm64', 'arm64': 'arm64'}


def main(dest):
    arch = ARCH.get(platform.machine().lower())
    if platform.system() != 'Linux' or arch not in SHA256:
        sys.exit(f'Pas de binaire Hugo prévu pour {platform.system()} {platform.machine()} : installer Hugo à la main')
    name = f'hugo_{VERSION}_linux-{arch}.tar.gz'
    url = f'https://github.com/gohugoio/hugo/releases/download/v{VERSION}/{name}'
    print(f'Téléchargement de {name}…')
    with urllib.request.urlopen(url, timeout=120) as r:
        data = r.read()
    if hashlib.sha256(data).hexdigest() != SHA256[arch]:
        sys.exit(f'Somme SHA-256 incorrecte pour {name}, abandon')
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        binary = tar.extractfile('hugo').read()
    os.makedirs(os.path.dirname(dest) or '.', exist_ok=True)
    tmp = dest + '.tmp'
    with open(tmp, 'wb') as f:
        f.write(binary)
    os.chmod(tmp, 0o755)
    os.replace(tmp, dest)
    print(f'Hugo {VERSION} installé dans {dest}')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.bin/hugo')
