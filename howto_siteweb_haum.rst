=======================================
Comment modifier le contenu du site web
=======================================

le site web du haum est un espace collaboratif qui peu etre enrichi par chacun des menbres de l'association
cette page se veut etre un aide mémoire pour que chacun dispose des informations nécéssaire a la réaliation de cette tache.

Préparation de l'environnement de travail
-----------------------------------------

    - installer Sphinx_ documenttion generator    
        créer votre repertoire de travail       
    - ``$ mkdir web_site_rep``
        se déplacer dans celui ci
    - ``$ cd web_site_rep``
        cloner [1]_ le repo git du site web du haum
    - ``$ git clone git@github.com:haum/website.git  source``
        se rendre dans le repertoire source et
    - ``$ cd source``
        copier le fichier Makefile dans votre repertoire de travail
    - ``$ cp Makefile ..``
        se placer dans le repertoire de travail
    - ``$ cd ..``
        et vérifier la bonne installation des outils et fichiers
    - ``$ make html`` 
        le resultat se trouve dans le repertoire build/html. On peu verifier le resultat en chargeant le fichier index.html de ce repertoiredans un navigateur web


Si tout c'est déroulé sans erreur vous voila pret et opérationnel pour modifier le contenu du site web.




------------

  la suite
  
  des outils
    - ref language http://docutils.sourceforge.net/docs/user/rst/quickref.html
    - un editeur retext http://www.webupd8.org/2012/03/retext-30-released-text-editor-for.html
  
------------
  
  
.. _Sphinx: http://sphinx-doc.org/install.html

.. [1] demadez un acces si vous n'en avez pas.

:Auteur:  jerome @jblb_72
:Version: 0.1 du 22/02/2014
