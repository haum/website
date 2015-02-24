==========
HAUMTinsel
==========

:slug: haumtinsel


Après avoir réalisé le Pong_ et alors que les fêtes de fin d'année approchait. Le HAUM a décidé de faire une
guirlande-jeu à afficher à l'extérieur du local.

    Ce projet est typique de cette fin d'année : on discute, on discute et un jour on s'y met et c'est règlé en 2h --
    Mathieu


.. _Pong: /pages/1Dpong.html


Qu'est ce que c'est?
====================

La guirlande (*tinsel* en anglais) est un *hack* du Pong_ en question. L'idée part là encore d'un jeu minimaliste et
cette fois ci connecté.

L'objet final est finalement découpé en 3 parties :

- le matériel (qui est commun avec le Pong_ quoique le *soft* interne ait été modifié pour utiliser PolychrHAUM_)
- la partie serveur et jeu (qui tournera sur une RaspberryPi_ dans un premier temps et une `BeagleBone Black`_ ensuite)

Tout le code est disponible `sur Github`_.

La suite ne parle que de la partie serveur et jeu, les pages à propos du Pong_ et de PolychrHAUM_ parlent du reste

.. _sur github: https://github.com/haum/HaumTinsel/tree/master/Games
.. _PolychrHAUM: /pages/polychrhaum.html
.. _RaspberryPi: http://www.raspberrypi.org/
.. _BeagleBone Black: http://beagleboard.org/black

Principe du jeu
===============

En arrivant sur une page web, vous entrez un pseudo et une des quatres couleurs disponibles est assignée. Il s'agit
ensuite de cliquer (ou toucher) un logo qui se déplace sur une page. Chaque touche réussie ajoute une LED de votre
couleur à la guirlande. L'objectif ? tout remplir de votre couleur :) (oui, vous pouvez écraser les autres).


Mise en Oeuvre
==============

Les 2 choix faits au niveau de la communication serveur/joueur d'une part et serveur/arduino d'autres part sont les
suivant :

- serveur/joueur : la connexion disponible au HAUM n'autorise pas les requêtes entrantes. La carte serveur toune donc
  dans le réseau local et ouvre un `tunnel SSH`_ vers le serveur hébergeant le site du HAUM. Celui-ci est configuré
  en *proxy* (serveur Apache + mod_proxy) pour permettre aux Internetz d'accèder à la guirlande. Pour soulager le
  réseau, les images sont servies depuis le serveur proxy.
- serveur/arduino : la connexion passe par la laison série disponible et l'envoie de commandes à un seul caractère. Au
  total, 6 commandes : 4 pour l'ajout d'une couleur (la position est automatique), 2 pour la sauvegarde/restoration de
  l'état de la guirlande.

Matériel
--------

L'arduino à l'intérieur du boitier est, pour les besoins de communication avec la carte serveur, reprogrammé avec le
code disponible dans le dossier `Game/Arduino`_ du dépôt. Ce programme est basé (comme dit plus haut) sur PolychrHAUM_
une *lib* créée au HAUM et permettant un contrôle simplifié de la bande de LEDs.

Pour une vision plus détaillée du code, la fonction ``loop()`` ne sert qu'a effectuer un nouveau tour de boucle avec
l'affichage et à lire d'éventuels messages sur la liaison série.

Serveur
-------

La partie serveur tient en `un fichier`_ (environ 100 lignes, donc pas grand chose). Il s'agit d'une petite application
basée sur Bottle qui d'un côté initialise un serveur minimaliste (1 page statique avec du JS et 1 point d'API pour
ajouter des LEDs) et d'un autre ouvre un *thread* capable d'ajouter périodiquement des flocons à la guirlande.

.. _un fichier: https://github.com/haum/HaumTinsel/blob/master/Games/RunningSquare/server.py
.. _game/arduino: https://github.com/haum/HaumTinsel/tree/master/Games/Arduino
.. _tunnel SSH: https://fr.wikipedia.org/wiki/Tunnel_%28r%C3%A9seau_informatique%29

Installation
============

L'installation s'est faite à la fenêtre du HAUM, dans le grand froid de l'hiver. De l'extérieur, on voyait ce qu'il y a
sur la photo

.. container:: alignright

    .. image:: /images/haumtinsel/haumtinsel.jpg
        :width: 300px

Et après ?
==========

Ce projet a permit d'ancrer un peu plus la HAUM dans l'univers du ludique. On réfléchit à plus gros et ambitieux pour
l'an prochain.... affaire à suivre.

.. _HaumTinsel: /pages/haumtinsel.html

