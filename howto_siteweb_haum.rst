=======================================
Comment modifier le contenu du site web
=======================================

Le site web du **HAUM** est un espace collaboratif qui peut être enrichi par chacun des membres de l'association. Cette page se veut un aide mémoire pour que chacun dispose des informations nécéssaires à la réaliation de cette tâche.

Préparation de l'environnement de travail
-----------------------------------------

    - installer Sphinx_ Documentation Generator
    - créer votre répertoire de travail : ``$ mkdir web_site_rep``
    - se déplacer vers celui-ci : ``$ cd web_site_rep``
    - cloner [1]_ le dépôt git du site web du HAUM : ``$ git clone git@github.com:haum/website.git  source``
    - se rendre dans le répertoire source : ``$ cd source``
    - copier le fichier Makefile dans votre repertoire de travail : ``$ cp Makefile ..``
    - se placer dans le repertoire de travail : ``$ cd ..``
    - et vérifier la bonne installation des outils et fichiers : ``$ make html``

Le résultat se trouve dans le répertoire ``build/html``. On peut vérifier le résultat en chargeant le fichier ``index.html`` de ce répertoire dans un navigateur web.

Si tout s'est déroulé sans erreur vous voila prêt et opérationnel pour modifier le contenu du site web.


Au travail ...
``````````````

Pour la suite il va vous falloir comprendre et apprendre le langage utilisé pour la création de ces pages: il s'agit du language *reStructuredText* et du projet `Sphinx Python Documentation Generator`_

Quelques outils pour comprendre et utiliser ce language
```````````````````````````````````````````````````````

    - la référence simplifiée du language
        http://docutils.sourceforge.net/docs/user/rst/quickref.html
    - la référence complète de celui ci
        http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
    - un éditeur de texte qui permet de visualiser du *reStructuredText* :  **retext**
        http://sourceforge.net/p/retext/home/ReText/
        http://www.webupd8.org/2012/03/retext-30-released-text-editor-for.html

Votre action
````````````
Dans le répertoire source, créez vos pages avec l'extension ``.rst`` et mettez-y les informations que vous voulez.

Pensez à créer un lien vers votre page à partir de la page principale du site (``index.rst``) avec la directive:

::

    .. toctree::
    :maxdepth: 1

    votre_fichier

Vous pouvez aussi ajouter le nom de votre fichier (sans l'extension ``.rst``) à un des ``toctree`` déjà present sur la
homepage ou ailleurs.

Lorsque que vos pages sont prêtes, elles peuvent être testées en entrant la commande ``$ make html`` dans votre repertoire ``web_site_rep``. Celle-ci reconstruira l'ensemble du site et vous pourrez le tester dans votre navigateur (en local).

Si tout va bien, alors ``pushez`` [2]_ votre travail vers le dépôt git de façon à le mettre a jour.

La commande magique qui va mettre à jour la version publique du site est à éxécuter sur le chan IRC [3]_ du Haum: `!updatesite` (si cela ne fait rien, *pingez* matael).


.. _Sphinx: http://sphinx-doc.org/install.html
.. _`Sphinx Python Documentation  Generator`: http://sphinx-doc.org/index.html
.. [1] demadez un accès si vous n'en avez pas.
.. [2] ``$ git push``
.. [3] http://irc.lc/freenode/haum

:Auteur:  jerome @jblb_72, matael
:Version: 0.3 du 23/02/2014
