:slug: howto_siteweb_haum_v2

=======================================
Comment modifier le contenu du site web
=======================================

howto_siteweb_haum version 2 by jblb (jerome@jblb.net)

pour l'instant c'est des notes de travail rien n'est a publier

Le site web du **HAUM** est un espace collaboratif qui peut être enrichi par chacun des membres de l'association. Cette page se veut un aide mémoire pour que chacun dispose des informations nécéssaires à la réaliation de cette tâche.

Préparation de l'environnement de travail
-----------------------------------------


	- si se n'est pas fait installer virtualenv : ``$sudo apt-get install python-virtualenv``
	- cloner [1]_ le dépôt git du site web du HAUM : ``$ git clone git@github.com:haum/website.git``
	- se déplacer vers le repertoire de travail : ``$cd website``
	- préparer l'environement virtuel : ``$virtualenv pelican -ppython2`` (cette commande n'est a faire que la premiere)
	- activer l'environement virtuel : ``$source pelican/bin/activate``
	- installer les requirements : ``$pip install -r requirements.txt``
	- ecrire vos pages
	- générer les pages : ``$make html``
	- deactiver l'environement virtuel : ``$deactivate``




.. [1] demadez un accès si vous n'en avez pas.
