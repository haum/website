===============================
Un test d'utilisation de Flickr
===============================

:date: 2015-02-16 17:00
:tags: talks
:category: test
:slug: test_flickr
:authors: jblb
:summary: test d'integration des photos de flickr dans le blog

flickr_ est un site web de publication de photos, le haum y a une galerie_ . Nous voulions pouvoir l'utiliser pour afficher des photos sur ce site

L'outil de publication que nous utilisons possède un plugin qui permetait de faire ce que nous voulions dans les articles, comme l'intégration des photos içi.

Nous l'avons modifié pour pouvoir l'utiliser aussi dans les autres pages de notre site. Comme l'édition de ce site est colaborative nous voulions aussi mettre en place un systeme qui permette a chacun de publier sans avoir besoin de clef d'API pour utiliser ce plugin.

Vous pouvez retrouver le code sur notre github_

Un exemple de l'utilisation avec ces photos
-------------------------------------------

.. container:: aligncenter
    
    [flickr:id=16329255616] [flickr:id=16168990829]

Tout celà à été possible grace a:

  - `Chris Streeter`_ l'auteur du plug-in qui a eu la bonne idée de le diffuser sous une licence libre
  - Matael_ et JackDesBwa_ les codeurs fous du Haum qui ont toujours la solution a vos problèmes de codeur débutant :)
  - Tous ceux qui font des photos_ pour le Haum


.. _Chris Streeter : https://github.com/streeter/pelican-flickrtag
.. _JackDesBwa : https://github.com/JackDesBwa
.. _matael : http://twitter.com/matael
.. _galerie : https://www.flickr.com/photos/126718549@N08/
.. _photos : https://www.flickr.com/photos/126718549@N08/
.. _flickr : https://www.flickr.com/
.. _github : https://github.com/haum/pelican-flickrtag
