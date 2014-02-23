=======================================
Comment modifier le contenu du site web
=======================================

le site web du **HAUM** est un espace collaboratif qui peu etre enrichi par chacun des menbres de l'association. cette page se veut etre un aide mémoire pour que chacun dispose des informations nécéssaire a la réaliation de cette tache.

Préparation de l'environnement de travail
-----------------------------------------

    - installer Sphinx_ documentation generator    
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

Pour la suite il va vous faloir comprendre et aprendre le langage utilisé pour la création de ces pages: il s'agit du language *reStructuredText* et du projet `Sphinx Python Documentation  Generator`_
  
Quelques outils pour comprendre et utiliser ce language:
````````````````````````````````````````````````````````
    - Référence simplifiée du language
        http://docutils.sourceforge.net/docs/user/rst/quickref.html
    - la référence complète de celui ci
        http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
    - un editeur de texte qui permet de visualiser du *reStructuredText*  **retext** 
        http://sourceforge.net/p/retext/home/ReText/    
        http://www.webupd8.org/2012/03/retext-30-released-text-editor-for.html
        
Votre action
````````````
Dans le repertoire source, créez vos pages avec l'extention ``.rst`` et mettrez y informations que vous voullez.

Penssez a créer un lien vers votre page a partir de la page principale du site (index.rst) avec la directive:
::

    .. toctree::
    :maxdepth: 1
    
    votre_fichier


lorsque que vos page sont prètes elles peuvent etre testées en entrant la commande ``$ make html`` dans votre repertoire ``web_site_rep`` cela reconstruira l'emsemble du site et vous pourez le tester dans votre navigateur

Si tout vas bien, alors ``pusher`` [2]_ votre travail vers le repo git de façon a le mettre a jour. 

La commande magique qui vas mettre a jour le site est a executer sur le chan IRC [3]_ du Haum: `!updatesite`



.. _Sphinx: http://sphinx-doc.org/install.html
.. _`Sphinx Python Documentation  Generator`: http://sphinx-doc.org/index.html
.. [1] demadez un accès si vous n'en avez pas.
.. [2] ``$ git push``
.. [3] http://irc.lc/freenode/haum

:Auteur:  jerome @jblb_72, matael
:Version: 0.3 du 23/02/2014
