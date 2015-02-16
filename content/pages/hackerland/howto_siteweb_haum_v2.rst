=======================================
Comment modifier le contenu du site web
=======================================
:status: hidden


howto_siteweb_haum version 2 by jblb (jerome@jblb.net)

Pour l'instant ce ne sont que des notes de travail.
Vous n'avez pas forcément toutes les infos et certaines qui sont présente içi peuvent être devenues obsolètes...

Préambule
`````````

Le site web du **HAUM** est un espace collaboratif qui peut être enrichi par chacun de ses membres.
Cette page se veut un aide mémoire pour que chacun dispose des informations nécéssaires à la réaliation de cette tâche.

Préparation de l'environnement de travail
`````````````````````````````````````````

	- Si se n'est pas déjà fait, installer "Virtualenv" : ``$ sudo apt-get install python-virtualenv`` (Ubuntu) ou ``$ pip install virtualenv``  (MacOS) ;
	- Cloner ([#]_ [#]_) le dépôt git du site web : ``$ git clone git@github.com:haum/website.git`` ;
	- Se déplacer vers le repertoire de travail : ``$ cd website`` ;
	- Préparer l'environement virtuel : ``$ virtualenv .pelican -ppython2`` (cette commande n'est à faire que la première fois) ;
	- Activer l'environement virtuel : ``$ source .pelican/bin/activate`` ;
	- Installer les requirements : ``$ pip install -r requirements.txt`` (cette commande n'est a faire que la premiere fois également) ;
	- Si vous voulez intégrer a vos pages des photos qui sont disponibles sur flickr il faut intaller un plugin suplementaire, comme ce plugin ne correspondait pas entierrement a nos besoin nous l'avons modifié. Il ne peut donc pas (encore) etre installé avec la commande précédente. Pour l'installer ``$ pip install git+https://github.com/haum/pelican-flickrtag.git`` ;
	- S'assurer que l'on est bien dans la branche master du dépot :``$ git checkout master`` (/!\\ ne faire aucune modification ailleurs que dans cette branche !) ;
	- Écrire vos pages_ ;
	- Générer les pages pour vérifier qu'il n'y a pas d'erreurs : ``$ make html`` ;
	- S'assurrer que l'on est dans la branche master du dépot :``$ git checkout master``
	- Pousser vos nouvelles pages sur le dépôt git :
            - Ajouter les pages modifées: ``$ git add vos-pages-modifiées``
            - Commiter votre travail: ``$ git commit -m"votre commantaire de commit"``
            - Pousser votre travail sur le dépôt: ``$ git push``
	- désactiver l'environnement virtuel : ``$ deactivate``

.. _pages:

À vous de jouer !
``````````````````

Maintenant que votre environnement est prêt, il va vous falloir comprendre/apprendre le système de gestion et de publication des pages sous Pelican_. Pour ce faire, vous aurez besoin notamment de connaître un des deux langages utilisés pour la création des pages : reStructuredText_ ou Markdown_.

.. _reStructuredText:

Quelques outils pour comprendre et utiliser *reStructuredText* :

    - La `référence simplifiée <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_ du langage, ou la version `complète <http://docutils.sourceforge.net/rst.html>`_

.. _editeur:

    - Un éditeur de texte qui permet de visualiser du *reStructuredText* :  ReText_ (ou `ici <http://www.webupd8.org/2012/03/retext-30-released-text-editor-for.html>`_)

.. _Markdown:

Et pour le *Markdown* alors ?

    - La `documentation <http://daringfireball.net/projects/markdown>`_ du langage
    - L'editeur_ ReText est également compatible pour la rédaction du Markdown

Pelican apliqué au site du Haum
-------------------------------


La publication
``````````````

*de master a upstream*

    - passer sur la branche upstream : ``$ git checkout upstream``
    - la faire correspondre a la branche master : ``$ git merge --ff master``
    - et là s'il y a conflit : ``$ git mergetool``

*update du site web*

``!updatesite`` dans le canal IRC du `haum <http://irc.lc/freenode/haum>`_

Pensez ensuite a vous remetre sur la branche master du site : ``$ git checkout master``


Des liens qui peuvent servir
----------------------------

    - `Markdown Cheatsheet <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>`_
    - `Ce que j’aurais aimé savoir quand j’ai commencé GIT <http://software-craftsman.fr/2014/05/12/a-la-decouverte-de-git/>`_
    
    

.. [#] Demadez un accès si vous n'en avez pas.
.. [#] Ce n'est à faire que la première fois. Par la suite, se placer dans le répertoire de travail et faire : ``$ git pull``

.. _Pelican: http://docs.getpelican.com/en/latest/index.html
.. _ReText: http://sourceforge.net/p/retext/home/ReText
