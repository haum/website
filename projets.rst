Au HAUM
=======

Voilà une petite liste de ce qu'on fait au HAUM, projets ou autres !

Par ailleurs, on s'excuse d'être un peu limités pour les idées de noms : beaucoup de nos noms de projets contiennent "HAUM"...

Si vous souhaitez vous renseigner un peu plus sur un projet ou donner un coup de main, contactez ceux qui sont cités dans la description :)

AxiHAUM
-------

À l'automne 2014, le HAUM a récupéré du matériel gracieusement offert par le département info de l'`Université du Maine`_. Parmi cet ensemble de matériel il y avait une graveuse à PCB_ (LKPS ProtoMat 91s de 1994) partiellement fonctionnelle. Celle-ci est en cours d'amélioration pour devenir une fraiseuse numérique 3 axes.
Cette modification est supportée par neomiulium_, d'autres membres du HAUM (jblb_, rebrec_, matael_), ainsi que d'autres personnes ayant les compétences et les outils pour réaliser ce type de modification.

Ce projet peut être scindé selon 3 aspects :

 - mécanique : il faut modifier des pièces existantes mais également en créer de nouvelles ;
 - électronique : il faut créer une nouvelle version de l'électronique, celle existante n'étant plus fonctionnelle et ne répondant plus aux besoins d'une fraiseuse ;
 - logiciel : il faut faciliter l'accès aux logiciels libres permettant l'utilisation de cette fraiseuse, notamment pour corriger les bugs présents dans ces logiciels, les traduire, les packager.

La modification mécanique est quasiment terminée, il reste tout de même des contraintes mécaniques importantes sur son nouvel axe Z, ce qui nécessitera peut-être un usinage rectificatif ou une réfection de certaines pièces.

La réalisation d'une nouvelle carte électronique est bien avancée, le pilotage des axes reste à corriger et les fins de courses ne sont pas encore fonctionnelles.
Concernant l'aspect logiciel, le packaging d'HeeksCNC pour Debian (et variantes) est en bonne voie et quelques corrections fonctionnelles ont déjà été apportées à la version en dévelopement.

Naturellement, une fois ces étapes achevées, il faudra effectuer une calibration mécanique pour réduire les points de dureté ainsi qu'assurer le parallélisme/la perpendicularité des axes.

Note importante : le HAUM ne dispose pour le moment d'aucune broche/fraiseuse (outil rotatif supportant des outils de fraisage), ni des outils de découpe (fraises, forêts, chanfrin, etc.)

.. _Université du Maine: http://univ-lemans.fr
.. _PCB: https://en.wikipedia.org/wiki/Printed_circuit_board
.. _neomilium: http://twitter.com/neomilium
.. _matael: http://twitter.com/matael
.. _jblb: http://twitter.com/jblb_72
.. _rebrec: https://twitter.com/elfrancesco

HAUMTalks
---------

Au cours de son assemblée générale 2013-2014, plusieurs membres ont proposé l'organisation de sessions de type mini-conférences à sujet libre. `Un site`_ dédié a vu le jour pour les recenser et quelques éditions ont déjà eu lieu.
Si vous voulez participer à l'amélioration du site et/ou ouvrir un compte permettant d'organiser des confs, venez en discuter avec nous sur IRC_ (vous pouvez aussi pinger matael_ ou feedoo_) ! 

Un retour sur la première conf libre est `disponible ici`_.

.. _Un site: http://talks.haum.org
.. _IRC : http://irc.lc/freenode/haum
.. _feedoo: http://twitter.com/fblain
.. _disponible ici: http://blog.matael.org/writing/premiere-conf-libre/

Opendata Crunching
------------------

Depuis sa création, le HAUM s'intéresse à l'Opendata et à la visualisation de jeu de données. Après avoir embêté un peu les politiques manceaux en utilisant les `données de Nantes`_ au cours d'une manifestation publique, puis fourni une API d'accès aux données de la SETRAM (réseau de transport du Mans, `article tech`_, `article explicatif`_ et `doc`_), le HAUM s'intéresse maintenant aux données citoyennes. En 2014, ce sont les résultats des élections municipales (`article 1`_, `article 2`_ et map_) sur le Mans qui ont été exploitées et d'autres idées germent autours des données d'endettement des communes ou encore, dans la répartition des équipements culturels dans la ville... Il reste beaucoup à faire.

Si vous aimez les actions un peu militantes, que vous vous proclamez *"datalover"* ou simplement que la vue d'une jolie carte pleine de sens vous intéresse, rejoignez ceux qui jouent avec et contactez jblb_, feedoo_ ou matael_.

.. _données de Nantes: http://blog.matael.org/writing/dataporn-les-parkings-de-nantes/
.. _article tech: http://blog.matael.org/writing/cyber-ouvre-boite-opendata-ou-pas/
.. _article explicatif: http://blog.matael.org/writing/cyber-ouvre-boite-le-concept/
.. _doc: http://timeoapi.readthedocs.org/fr/latest/
.. _article 1: http://blog.matael.org/writing/scrutin-et-opendata-parlons-technique/
.. _article 2 : http://blog.matael.org/writing/scrutin-et-opendata-le-concept/
.. _map: http://umap.openstreetmap.fr/fr/map/le-mans-elections_6485#12/47.9773/0.2575

Haumelitta
----------

`HAUMelitta`_ (a.k.a la cafetière qui tweete) est un peu un emblème du HAUM. C'est bêtement une cafetière reliée à twitter via un raspberry pi, mais elle fait son effet :).
Il n'est plus vraiment possible de contribuer à ce projet parce qu'il est en *standby* et qu'il a un intérêt limité, mais si vraiment vous y tenez, alors parlez-en à jblb_ ou matael_ et on vous trouvera un coin de table pour jouer avec.

.._HAUMelitta: https://twitter.com/HAUMelitta

Haniview:
-------------

Haniview a pour objectif de hacker l'afficheur à LEDs bi-colores (vert et rouge) de _jblb pour l'utiliser sous GNU/Linux, afficher des images, etc.

Ce projet est supporté par jblb_,  neomilium_ et  matael_.

Les formations/docs
===================

Le HAUM propose quelques documentations et formations (notament *via* ses contacts avec la `Ruche Numérique`_). Si vous avez des connaissances permettant de contribuer à l'un des sujets ci-dessous, rendez-vous sur le `github du HAUM`_ :
    
- `Formation Arduino`_ (par jblb_ et matael_)
- `Introduction à LaTeX` (par matael_ )

.. _Ruche Numérique: http://www.laruchenumerique.com/
.. _Formation Arduino: https://github.com/haum/forma_arduino
.. _Introduction à LaTeX: https://github.com/haum/introduction_LaTeX

Les bots
========

Actuellement, 4 bots travaillent pour nous : Twaum (Twitter<->IRC), GHB (Todolist<->IRC), HAUMweb, (update du site) et un `bot GitHub`_ qui notifie sur notre chan IRC les différents évèments git (push, pull-resquest & co) des principaux dépots git de l'association.

Vous pouvez contribuer aux deux premiers en forkant un des dépôts suivants ou bien pinger matael_ ou feedoo_ sur IRC :
    
- https://github.com/Matael/GithubBot
- https://github.com/haum/TwitterBot

Les deux autres ne sont pas publiés soient parce qu'ils sont trop simples pour nécessiter des contributeurs soit parce qu'il sont... fantôme.

.. _bot GitHub: http://blog.fredblain.org/2014/05/github-bot-pour-irc

Le github
=========

Le `github du HAUM`_ est plein de projets auxquels vous pouvez contribuer si vous le souhaitez ! Forkez les dépôts qui vous intéressent et faites nous une pluie de *pull requests* !

Si on vous croise deux trois fois au HAUM et qu'on vous aime bien, on vous donnera un bel accès à l'organisation elle-même pour directement contribuer *upstream* :)

En attendant voilà les projets software (ou de rédaction) auxquels vous pouvez contribuer pour nous aider :

- Haumtalks : https://github.com/haum/haumtalks
- axihaum : https://github.com/haum/axihaum
- Formation arduino : https://github.com/haum/forma_arduino
- Haniview : https://github.com/haum/hanivew
- TwitterBot : https://github.com/haum/TwitterBot
- timeoAPI : https://github.com/haum/timeoAPI
- heeksCNC (parce qu'on va s'en servir sous peu) : https://code.google.com/p/heekscnc/

.. _github du HAUM: https://github.com/haum/

HAUM Internal
=============

Vu qu'on est des hackers, la *todolist* de l'asso est aussi `sur github`_. Si le coeur vous en dit, commentez les tickets ou mieux, essayez de voir comment les fixer !

.. _sur github: https://github.com/haum/haum_internal/issues/