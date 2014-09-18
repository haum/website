Opendata Crunching
==================

Au HAUM, on aime les trucs ouverts, les codes sources ouverts, les portes ouvertes, les gens ouverts, les bières
ouvertes et bien sûr : les **données ouvertes** !

.. container:: alignright

    .. image:: /images/opendata/parkings_nantes.jpg
        :width: 400px

Vu qu'au Mans, les données ouvertes, c'est pas encore ça, nous, on titille un peu. Ça a commencé gentillet en
utilisation des `données de Nantes`_ dans une présentation publique au Mans.

Les parkings de Nantes, c'était rigolo.... mais... on pouvait aller plus loin.

.. container:: clearer

    |clearer|

Setram
------

Depuis, on a joué avec les données de la SETRAM.

.. container:: alignright

    .. image:: /images/opendata/timeomap.png
        :width: 400px

Cette fois ci, il s'agissait de pouvoir récupérer les informations de passage des bus et tram sur Le Mans.

Sachant que la SETRAM propose un service (appelé Timeo_) d'accès aux horaires de passage en temps réel, nous avons écrit
un *wrapper* Python permettant de récupérer facilement ces données et une API pour y accèder *over HTTP*.

Ces projets sont disponibles sur le github du HAUM pour l'API et sur celui de matael_ pour le *wrapper* :

- *wrapper* (**pyTimeo**) :

  - `pytimeo@github`_
  - `documentation`_

- API (**timeoapi**) :

  - `Accès HTTP`_
  - `timeoapi@github`_
  - `documentation de l'API`_

Histoire de documenter un peu le processus, on a aussi rédigé deux articles : un `article technique`_ pour expliquer
l'analyse et un autre plus politique et `explicatif`_ pour mettre en avant l'intérêt de cette action.

Data Citoyenne
--------------

L'opendata est un moyen de transparence important et l'année 2014 a vu deux élections.

.. container:: twocolumns

    .. container:: alignleft

        .. image:: /images/opendata/municipales.png
            :width: 300px

    .. container:: textcolumn

        Les élections municipales ont été pour le HAUM un bon prétexte pour s'intéresser à ce type de données. Après un lent et
        douloureux *mapping* des secteurs de vote sur Le Mans, nous avons pu recréer une `carte des résultats`_.

        Là aussi, deux articles ont accompagné la carte : comme auparavant `le premier`_ explique les aspects techniques et `le
        second`_ les aspects politiques.

.. container:: clearer

    |clearer|


.. container:: twocolumns

    .. container:: alignright

        .. image:: /images/opendata/europeennes.png
            :width: 300px

    .. container:: textcolumn

        Comme les élections européennes étaient dans la foulée et que la manière de présenter les données n'avait pas changé,
        nous avons remis ça et créé de nouveau une `carte`_.

.. container:: clearer

    |clearer|

Et maintenant ?
---------------

L'opendata est encore à ses débuts et tout reste à faire. Si vous voulez en savoir plus sur nos actions ou même mieux y
participer, contactez nous *via* la `mailing-list`_ , le twitter_ ou parlez en avec jblb_, feedoo_ ou matael_.

Pour vous mettre l'eau à la bouche, en ce moment, ça cause des données d'endettement et de la répartition des
équipements culturels.

.. _matael: http://twitter.com/matael
.. _jblb: http://twitter.com/jblb_72
.. _feedoo: http://twitter.com/fblain
.. _mailing-list: http://lists.matael.org/mailman/listinfo/haum_hackerspace
.. _twitter: http://twitter.com/haum72

.. _données de Nantes: http://blog.matael.org/writing/dataporn-les-parkings-de-nantes/
.. _article technique: http://blog.matael.org/writing/cyber-ouvre-boite-opendata-ou-pas/
.. _explicatif: http://blog.matael.org/writing/cyber-ouvre-boite-le-concept/

.. _le premier: http://blog.matael.org/writing/scrutin-et-opendata-parlons-technique/
.. _le second: http://blog.matael.org/writing/scrutin-et-opendata-le-concept/
.. _carte des résultats: http://umap.openstreetmap.fr/fr/map/le-mans-elections_6485#12/47.9773/0.2575
.. _carte: http://umap.openstreetmap.fr/en/map/elections-europeennes-14-sur-le-mans_10621#13/47.9852/0.2379

.. _Timeo: http://www.setram.fr/698-TIMEO2C-l-info-en-temps-reel.html
.. _pytimeo@github: https://github.com/Matael/pytimeo
.. _documentation: http://pytimeo.rtfd.org
.. _Accès HTTP: http://timeoapi.haum.org
.. _timeoapi@github: https://github.com/haum/timeoAPI
.. _documentation de l'API: http://timeoapi.rtfd.org

.. |clearer| unicode:: U+0020 .. space
