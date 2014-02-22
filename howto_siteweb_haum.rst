=======================================
Comment modifier le contenu du site web
=======================================

Le site web du HAUM est un espace collaboratif qui peut être enrichi par chacun des menbres de l'association.
Cette page se veut un aide-mémoire pour que chacun dispose des informations nécéssaires à la réaliation de cette tâche.

Préparation de l'environnement de travail
-----------------------------------------

    - installer Sphinx_ Documentation Generator
    - créer votre repertoire de travail : ``$ mkdir web_site_rep``
    - se déplacer dans celui ci : ``$ cd web_site_rep``
    - cloner [1]_ le dépôt git du site web du HAUM  : ``$ git clone git@github.com:haum/website.git  source``
    - se rendre dans le répertoire source  : ``$ cd source``
    - puis copier le fichier Makefile dans votre repertoire de travail : ``$ cp Makefile ..``
    - se placer dans le repertoire de travail : ``$ cd ..``
    - et vérifier la bonne installation des outils et fichiers : ``$ make html``

Le résultat se trouve dans le répertoire ``build/html``. On peut vérifier le résultat en chargeant le fichier ``index.html`` de ce répertoire dans un navigateur web.


Si tout s'est déroulé sans erreur vous voila prêt et opérationnel pour modifier le contenu du site web.


------------

La suite
--------

Quelques outils :

    - Référence du langage RestructuredText : http://docutils.sourceforge.net/docs/user/rst/quickref.html
    - Un éditeur ResT : http://www.webupd8.org/2012/03/retext-30-released-text-editor-for.html

------------


.. _Sphinx: http://sphinx-doc.org/install.html

.. [1] demadez un accès si vous n'en avez pas.

:Auteur:  jerome @jblb_72, matael
:Version: 0.2 du 22/02/2014
