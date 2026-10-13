---
title: "{{ replace .File.ContentBaseName "-" " " | strings.FirstUpper }}"
slug: {{ .File.ContentBaseName }}
date: {{ .Date }}
authors: [Ton pseudo]
categories: [news]
tags: []
summary: Une phrase qui donne envie de lire la suite.
---

Ton texte ici. Les photos se déposent dans le même dossier que ce fichier :

![Description de la photo](photo.jpg "Légende facultative")
