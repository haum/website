=======================================
Comment modifier le contenu du site web
=======================================
:status: hidden


howto_siteweb_haum version 2 by jblb (jerome@jblb.net)

Pour l'instant ce ne sont que des notes de travail. Vous n'avez pas forcement toutes les infos et certaines qui sont présente içi peuvent etre fausses....

Préenbule
`````````

Le site web du **HAUM** est un espace collaboratif qui peut être enrichi par chacun des membres. Cette page se veut un aide mémoire pour que chacun dispose des informations nécéssaires à la réaliation de cette tâche.

Préparation de l'environnement de travail
`````````````````````````````````````````

	- Si se n'est pas fait installer virtualenv : ``$ sudo apt-get install python-virtualenv``
	- Cloner [#]_ [#]_ le dépôt git du site web du HAUM : ``$ git clone git@github.com:haum/website.git`` 
	- Se déplacer vers le repertoire de travail : ``$ cd website``
	- Préparer l'environement virtuel : ``$ virtualenv .pelican -ppython2`` (cette commande n'est a faire que la premiere fois)
	- Activer l'environement virtuel : ``$ source .pelican/bin/activate``
	- Installer les requirements : ``$ pip install -r requirements.txt`` (cette commande n'est a faire que la premiere fois également)
	- S'assurrer que l'on est dans la branche master du dépot :``$ git checkout master``
	- Écrire vos pages_
	- Générer les pages pour vérifier qu'il n'y a pas d'erreurs : ``$ make html``
	- S'assurrer que l'on est dans la branche master du dépot :``$ git checkout master``
	- Pousser vos nouvelles pages sur le depot git :	
            - Ajouter les pages modifées: ``$ git add pages-modifiees``	   
            - Commiter votre travail: ``$ git commit -m"votre commantaire de commit"``
            - Pousser votre travail sur le depos: ``$ git push``           
	- deactiver l'environement virtuel : ``$ deactivate``

.. _pages:

Au travail ...
``````````````

Pour la suite il va vous falloir comprendre et apprendre le systeme de gestion et de publication des pages: pelican_ et un des langages utilisé pour la création de ces pages: reStructuredText_ ou Markdown_

.. _reStructuredText:

Quelques outils pour comprendre et utiliser *reStructuredText*
--------------------------------------------------------------

    - la référence simplifiée du language
        http://docutils.sourceforge.net/docs/user/rst/quickref.html
    - la référence complète de celui ci
        http://docutils.sourceforge.net/rst.html
        
.. _editeur:

    - un éditeur de texte qui permet de visualiser du *reStructuredText* :  **retext**
        http://sourceforge.net/p/retext/home/ReText/
        http://www.webupd8.org/2012/03/retext-30-released-text-editor-for.html

.. _Markdown:

Quelques liens sur *Markdown*
-----------------------------

    - la référence simplifiée du language
        http://daringfireball.net/projects/markdown/
    - l'editeur_  retext cité plus tot permet également l'édition au format Markdown
        
Pelican apliqué au site du Haum
-------------------------------
       
        
La publication
``````````````

*de master a upstream*

    - passer sur la branche upstream : ``$ git checkout upstream``
    - la faire correspondre a la branche master : ``$ git rebase master``
    - et là s'il y a conflit : ``$ git mergetool``
    
*update du site web*

``!updatesite`` dans le canal IRC du haum


.. [#] demadez un accès si vous n'en avez pas.
.. [#] ce n'est a faire que la premiere fois, les fois suivantes, se placer dans le repertoire de travail et faire : ``$ git pull``

.. _pelican: http://docs.getpelican.com/en/latest/index.html