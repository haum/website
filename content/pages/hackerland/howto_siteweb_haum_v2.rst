=======================================
Comment modifier le contenu du site web
=======================================
:status: hidden


howto_siteweb_haum version 2 by jblb (jerome@jblb.net)

pour l'instant ce n'est que des notes de travail
Vous n'avez pas forcement toutes les infos et que certaines qui sont présente içi peuvent etre fausses....


Le site web du **HAUM** est un espace collaboratif qui peut être enrichi par chacun des membres de l'association. Cette page se veut un aide mémoire pour que chacun dispose des informations nécéssaires à la réaliation de cette tâche.

Préparation de l'environnement de travail
`````````````````````````````````````````


	- si se n'est pas fait installer virtualenv : ``$ sudo apt-get install python-virtualenv``
	- cloner [#]_ [#]_ le dépôt git du site web du HAUM : ``$ git clone git@github.com:haum/website.git`` 
	- se déplacer vers le repertoire de travail : ``$ cd website``
	- préparer l'environement virtuel : ``$ virtualenv .pelican -ppython2`` (cette commande n'est a faire que la premiere fois)
	- activer l'environement virtuel : ``$ source .pelican/bin/activate``
	- installer les requirements : ``$ pip install -r requirements.txt``
	- s'assurrez que l'on est dans la branche master du dépot :``$ git checkout master``
	- ecrire vos pages_
	- générer les pages pour verifier qu'il n'y a pas d'erreurs : ``$ make html``
	- s'assurrez que l'on est dans la branche master du dépot :``$ git checkout master``
	- pousser vos nouvelles pages sur le depot git :``$ git push``
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
.. [#] ce n'est a faire que la premiere fois, les fois suivantes, placez vous dans le repertoire de travail et faites : ``$ git pull``
.. _pelican: http://docs.getpelican.com/en/latest/index.html