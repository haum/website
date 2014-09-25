
howto_siteweb_haum version 2
by jblb (jerome@jblb.net)

petit guide pour écrire des pages sur le site web du haum

pour l'instant c'est des notes de travail rien n'est a publier


installer virtualenv 
    $sudo apt-get install python-virtualenv

activer le virtualenv 
    $ virtualenv ~/virtualenvs/pelican
    $ source ~/virtualenvs/pelican/bin/activate
installer pelican ( qui ne sera actif que dans ce virtualenv)
    $ pip install pelican
se rendre dans le repertoire du clone du site web
installer les dépendences nécéssaire a la construction du site 
    $ pip install -r requirements.txt
 



quitter l'environement virtuel
    $ deactivate
