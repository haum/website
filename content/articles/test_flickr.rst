===============================
Un test d'utilisation de Flickr
===============================

:date: 2015-02-16 17:00
:tags: talks
:category: test
:slug: test_flickr
:authors: jblb
:summary: Test d'intégration des photos de Flickr dans notre blog

Flickr_ est un site web de publication de photos, et le HAUM y a une galerie_. Cette galerie, nous voulions pouvoir l'utiliser afin d'afficher des photos sur notre site.

L'outil de publication que nous utilisons permettait déjà de le faire mais (i) uniquement dans nos articles ce qui était rédhibitoire pour les autres pages du site, (ii) il nécessitait de connaître une clé d'API.
Nous l'avons donc modifié (hacké ;-) pour pouvoir l'employer dans un cas, comme dans l'autre et ce, sans avoir à diffuser notre clé d'API. De cette manière, nous respectons notre souhait premier en matière de rédaction de contenu sur ce site : qu'elle soit ouverte et collaborative !

Vous pouvez retrouver le code du plug-in modifié sur notre github_.

Un exemple de l'utilisation avec ces photos
-------------------------------------------

.. container:: aligncenter
    
    [flickr:id=16329255616] [flickr:id=16168990829]

Tout cela a été possible grâce à:

  - `Chris Streeter`_ l'auteur du plug-in qui a eu la bonne idée de le diffuser sous une licence libre ;
  - Matael_ et JackDesBwa_ les codeurs fous du HAUM qui ont toujours la solution à vos problèmes de codeur débutant :) ;
  - Tous ceux qui font/feront des photos_ pour le HAUM.

Merci à eux !

.. _Chris Streeter : https://github.com/streeter/pelican-flickrtag
.. _JackDesBwa : https://github.com/JackDesBwa
.. _matael : http://twitter.com/matael
.. _galerie : https://www.flickr.com/photos/126718549@N08/
.. _photos : https://www.flickr.com/photos/126718549@N08/
.. _Flickr : https://www.flickr.com/
.. _github : https://github.com/haum/pelican-flickrtag
