=======================================
Comment modifier le contenu du site web
=======================================

le site web du HAUM est un espace collaboratif qui peu etre enrichi par chacun des menbres de l'association. cette page se veut etre un aide mémoire pour que chacun dispose des informations nécéssaire a la réaliation de cette tache.

Préparation de l'environnement de travail
-----------------------------------------

    - installer Sphinx_ documenttion generator    
    - créer votre repertoire de travail : ``$ mkdir web_site_rep``
    - se déplacer dans celui ci : ``$ cd web_site_rep``
    - cloner [1]_ le repo git du site web du HAUM : ``$ git clone git@github.com:haum/website.git  source``
    - se rendre dans le repertoire source : ``$ cd source``
    - copier le fichier Makefile dans votre repertoire de travail : ``$ cp Makefile ..``
    - se placer dans le repertoire de travail : ``$ cd ..``
    - et vérifier la bonne installation des outils et fichiers : ``$ make html`` 

Le résultat se trouve dans le répertoire ``build/html``. On peut vérifier le résultat en chargeant le fichier ``index.html`` de ce répertoire dans un navigateur web.

Si tout s'est déroulé sans erreur vous voila prêt et opérationnel pour modifier le contenu du site web.


Au travail ...
``````````````

Pour la suite il va vous faloir comprendre et aprendre le langage utilisé pour la crétion de ces pages: il s'agit du language *reStructuredText*
  
Quelques outils pour comprendre et utiliser ce language:
````````````````````````````````````````````````````````
    - Référence simplifiée du language
        http://docutils.sourceforge.net/docs/user/rst/quickref.html
    - la référence complète de celui ci
        http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
    - un editeur de texte qui permet de visualiser du *reStructuredText*  **retext** 
        http://sourceforge.net/p/retext/home/ReText/    
        http://www.webupd8.org/2012/03/retext-30-released-text-editor-for.html
  
------------


.. _Sphinx: http://sphinx-doc.org/install.html

.. [1] demadez un accès si vous n'en avez pas.

:Auteur:  jerome @jblb_72, matael
:Version: 0.2 du 22/02/2014
