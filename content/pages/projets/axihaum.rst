=======
AxiHAUM
=======

.. container:: alignright

    .. image:: /images/axihaum/sauvetage.jpg
        :width: 300px

À l'automne 2014, le HAUM a récupéré du matériel gracieusement offert par le département info de l'`Université du Maine`_. Parmi cet ensemble de matériel il y avait une graveuse à PCB_ (LKPS ProtoMat 91s de 1994) partiellement fonctionnelle. Celle-ci est en cours d'amélioration pour devenir une fraiseuse numérique 3 axes.
Cette modification est supportée par neomilium_, d'autres membres du HAUM (jblb_, rebrec_, matael_), ainsi que d'autres personnes ayant les compétences et les outils pour réaliser ce type de modification.

Ce projet peut être scindé selon 3 aspects :

 - mécanique : il faut modifier des pièces existantes mais également en créer de nouvelles ;
 - électronique : il faut créer une nouvelle version de l'électronique, celle existante n'étant plus fonctionnelle et ne répondant plus aux besoins d'une fraiseuse ;
 - logiciel : il faut faciliter l'accès aux logiciels libres permettant l'utilisation de cette fraiseuse, notamment pour corriger les bugs présents dans ces logiciels, les traduire, les packager.

La modification mécanique est quasiment terminée, il reste tout de même des contraintes mécaniques importantes sur son nouvel axe Z, ce qui nécessitera peut-être un usinage rectificatif ou une réfection de certaines pièces.

La réalisation d'une nouvelle carte électronique est bien avancée, le pilotage des axes reste à corriger et les fins de courses ne sont pas encore fonctionnelles.
Concernant l'aspect logiciel, le packaging d'HeeksCNC pour Debian (et variantes) est en bonne voie et quelques corrections fonctionnelles ont déjà été apportées à la version en dévelopement.

Naturellement, une fois ces étapes achevées, il faudra effectuer une calibration mécanique pour réduire les points de dureté ainsi qu'assurer le parallélisme/la perpendicularité des axes.

Note importante : le HAUM ne dispose pour le moment d'aucune broche/fraiseuse (outil rotatif supportant des outils de fraisage), ni des outils de découpe (fraises, forets, chanfreins, etc.)

.. _Université du Maine: http://www.univ-lemans.fr/fr/index.html
.. _PCB: https://en.wikipedia.org/wiki/Printed_circuit_board
.. _neomilium: http://twitter.com/neomilium
.. _matael: http://twitter.com/matael
.. _jblb: http://twitter.com/jblb_72
.. _rebrec: https://twitter.com/elfrancesco

