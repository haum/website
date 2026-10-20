# Mêmes cibles que l'ancien Makefile Pelican : les bots (IRC et Matrix)
# lancent « make publish » puis copient output/ vers le serveur web.
# La variable PELICAN qu'ils passent encore est simplement ignorée.

PYTHON ?= python3
# Hugo installé sur la machine, sinon binaire officiel téléchargé dans .bin/
# (cas des conteneurs des bots, voir tools/get_hugo.py)
HUGO ?= $(shell command -v hugo 2>/dev/null || echo .bin/hugo)
OUTPUTDIR ?= output
AGENDA_DB ?= agenda.sqlite

.PHONY: help agenda html publish serve clean

help:
	@echo 'make serve     serveur local avec rechargement (http://localhost:1313)'
	@echo 'make html      génère le site dans $(OUTPUTDIR)/'
	@echo 'make publish   idem, pour la mise en ligne (utilisé par les bots)'
	@echo 'make clean     supprime $(OUTPUTDIR)/'

# agenda.sqlite (écrit par les bots) -> data/agenda.json (lu par Hugo)
agenda:
	@if [ -f $(AGENDA_DB) ]; then $(PYTHON) tools/agenda_export.py $(AGENDA_DB) data/agenda.json; fi

html: agenda $(filter .bin/hugo,$(HUGO))
	$(HUGO) --minify --cleanDestinationDir --destination $(OUTPUTDIR)
	@# Page d'erreur attendue par le serveur web de haum.org
	cp $(OUTPUTDIR)/404.html $(OUTPUTDIR)/e404.html

.bin/hugo:
	$(PYTHON) tools/get_hugo.py $@

publish: html

serve: agenda $(filter .bin/hugo,$(HUGO))
	$(HUGO) server --buildDrafts --disableFastRender

clean:
	rm -rf $(OUTPUTDIR) public resources/_gen .bin
