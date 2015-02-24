=======================================
Comment modifier le contenu du site web
=======================================
:status: hidden


howto_siteweb_haum version 2 by jblb (jerome@jblb.net)

Préambule
`````````

Le site web du **HAUM** est un espace collaboratif qui peut être enrichi par chacun de ses membres.
Cette page se veut un aide mémoire pour que chacun dispose des informations nécéssaires à la création de contenu sur ce site.

Préparation de l'environnement de travail
`````````````````````````````````````````

Installation des pré-requis
+++++++++++++++++++++++++++

Pour isoler l'environnement Python, il est recommandé d'utiliser "Virtualenv" :
``$ sudo apt-get install python-virtualenv`` (Ubuntu) ou ``$ pip install virtualenv``  (MacOS)

Récupération des sources et configuration initiale
++++++++++++++++++++++++++++++++++++++++++++++++++

	- Cloner ([#]_) le dépôt git du site web : ``$ git clone git@github.com:haum/website.git`` ;
	- Se déplacer vers le répertoire de travail : ``$ cd website`` ;
	- Préparer l'environement virtuel : ``$ virtualenv .pelican -ppython2`` ;
	- Activer l'environement virtuel : ``$ source .pelican/bin/activate`` ;
	- Installer les requirements : ``$ pip install -r requirements.txt`` ;

Voilà, l'ensemble des pré-requis est installé, tant coté système que dans l'environnement local.

Édition et publication du contenu
`````````````````````````````````

Dans le répertoire *website* se trouve un répertoire *content* où se trouve l'ensemble des pages et autres articles présents sur le site.
C'est probablement dans ce répertoire que vous allez pouvoir éditer/ajouter vos pages_ ;

Rappel: il faut avoir activé l'environnement virtuel pour produire localement le contenu (``$ source .pelican/bin/activate``) et de préférence avoir mis à jour ses sources (``$ git pull``)
Note: pour désactiver l'environnement virtuel : ``$ deactivate``

Pour visualiser et verifier le rendu du contenu écrit, on génére localement les pages html : ``$ make html``

Propager ses modifications
``````````````````````````

S'assurrer que l'on est dans la branche master du dépot :``$ git checkout master``

Pour propager ses modifications sur le dépôt git :
  - Ajouter les pages modifées/crées: ``$ git add vos-pages-modifiées``
  - Commiter votre travail: ``$ git commit -m"votre commantaire de commit"``
  - Pousser votre travail sur le dépôt: ``$ git push``

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

La publication
``````````````

La publication s'opère en deux étapes:

Fusion de *master* dans *upstream*
++++++++++++++++++++++++++++++++++

    - passer sur la branche *upstream* : ``$ git checkout upstream``
    - fusionner la branche *master* sur la branche *upstream*: ``$ git merge --ff master``
    - en cas de conflit : ``$ git mergetool``

Note: Pensez ensuite à vous repositionnez sur la branche master du site : ``$ git checkout master``

Mise à jour du rendu sur le site
++++++++++++++++++++++++++++++++

``!updatesite`` dans le canal IRC du `haum <http://irc.lc/freenode/haum>`_


Des liens qui peuvent servir
----------------------------

    - `Markdown Cheatsheet <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>`_
    - `Ce que j’aurais aimé savoir quand j’ai commencé GIT <http://software-craftsman.fr/2014/05/12/a-la-decouverte-de-git/>`_
    

.. [#] Demadez un accès si vous n'en avez pas.

.. _Pelican: http://docs.getpelican.com/en/latest/index.html
.. _ReText: http://sourceforge.net/p/retext/home/ReText
