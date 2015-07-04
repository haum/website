=========================
Hack de la PCBlastifieuse
=========================

:date: 2015-07-04 17:00
:tags: hack
:category: hack
:slug: hack_pcblastifieuse
:authors: Microjoe
:summary: Détails sur le hack effectué sur la plastifieuse

Cet article a pour objectif de retracer, étape par étape, le hack effectué sur
une plastifieuse A3 pour la transformer en PCBlastifieuse.

Pour plus d’informations sur le projet, vous pouvez `consulter sa page`_.

.. _consulter sa page: /pages/pcblastifieuse.html

Étude de la machine
-------------------

Avant de modifier quoi que ce soit sur la machine, il faut tout d’abord
comprendre comment elle fonctionne.

Après l’ouverture du capot retenu par quelques vis, on observe différents
éléments à l’intérieur :

 - Deux résistances chauffantes (une en haut et l’autre en bas), permettant de
   générer la chaleur nécessaire à la fonte des feuilles de plastique.

 - Deux thermocouples positionnés sur une résistance pour l’allumer ou
   l’éteindre en fonction de la température qu’elle dégage, afin de pouvoir
   rester dans une certaine plage de température.

 - Un moteur relié à une boite de vitesse mécanique puis à un rouleau,
   permettant de faire avancer les feuilles de l’entrée vers la sortie de la
   machine en passant par dessus les résistances.

 - Des fils électriques un peu partout (mais globalement bien rangés).

En suivant les fils, on peut donc étudier les connexions entre les différents
éléments électriques de la machine ; celle-ci fonctionnant sur une tension
secteur, on prendra bien soin de la débrancher avant de vérifier les câblages.

Voici le schéma électrique que l’on peut donc dresser après avoir regardé les
connexions :

.. image:: /images/pcblastifieuse/schema.png

Principe de la modification
---------------------------

L’objectif principal de ce hack est de permettre de transférer le toner d’une
imprimante laser d’une feuille de papier vers un autre support. Pour ce faire,
il faut atteindre une température relativement haute (dans les 200°C) que la
plastifieuse n’est pour l’instant pas capable de délivrer.

Nous allons donc devoir faire en sorte :

 - D’allumer la résistance jusqu’à ce que sa température approche des 200°C.

 - Garder la plastifieuse à cette température en jouant avec l’allumage de
   l’extinction des résistances chauffantes.

Actionneur
""""""""""

Pour ce faire, il va donc falloir être capable d’allumer ou d’éteindre par nos
propres moyens les résistances chauffantes. Des composants permettant de
commuter une tension de 230 V, nous avons retenu le relai électromécanique pour
sa simplicité de mise en œuvre.

Capteur
"""""""

Un capteur de température basé sur une sonde de platine sera utilisé pour
détecter la température des résistances chauffantes afin de pouvoir commuter
leur alimentation.

Controlleur
"""""""""""

Afin de lire la température du capteur et activer ou non le relai, une Arduino
sur laquelle sont reliés le capteur et l’actionneur est positionnée à
l’extérieur du boitier.

Y’a plus qu’à
-------------

Maintenant que l’idée est trouvée et semble fonctionnelle, il ne nous reste
plus qu’à hacker la machine pour pouvoir mettre tout cela en place.

Fixation de la sonde de température
"""""""""""""""""""""""""""""""""""

La sonde de température est fixée dans un rail d’une des deux résistances
chauffantes.

Fixation du relai
"""""""""""""""""

Deuxième étape : fixer le relai à l’intérieur de la plastifieuse à côté du
circuit électrique du secteur.

En positionnant le module à cet endroit, toute la partie haute tension qui peut
être dangereuse est positionnée dans un côté du boitier et la partie basse
tension sera située à l’opposé pour avoir plus de sécurité.

On commence par réaliser une plaque de support pour pouvoir fixer le module
dans le boitier :

.. container:: aligncenter

    [flickr:id=19346409002] [flickr:id=19164902368]

Le module est fixé avec deux fils électriques en bleus sur la photo qui ne sont
là que pour fixer le module sur le support.

Une couche de scotch isolant a été ajoutée sous le module afin de bien isoler
la plaque en carton car les contacts du côté non visible du module sont reliés
au secteur et pourraient passer à travers la plaque de carton et être une
source d’électrisation.

On peut ensuite faire rentrer le support dans le boitier en plastique après
avoir découper certains éléments du boitier qui nous empêchaient de bien
positionner la plaque :

.. container:: aligncenter

    [flickr:id=18731859153]

Création d’une dérivation électrique vers le relai
""""""""""""""""""""""""""""""""""""""""""""""""""

En parallèle des thermocouples fixés sur la résistance du haut, on va venir
brancher notre relai qui permettra de gérer l’alimentation des résistances en
totale autonomie.

Pour celai, on coupe les gaines de protection autour des branchements des thermocouples, on y soude des fils résistants à la chaleur qui vont venir se brancher sur notre relai puis on remet de la gaine thermique pour protéger les branchements.

.. container:: aligncenter

    [flickr:id=19164865600]

Le résultat est très propre ; sauriez vous dire si ces branchements sont les
originaux ou ceux modifiés par nos petits mains ? Il s’agit ici du montage
modifié.

Passage des câbles de commande
""""""""""""""""""""""""""""""

Toute la partie haute tension est maintenant réalisée ! Après avoir branché les
nouveaux fils sur la partie haute tension du relai, on va commencer par relier
des paires torsadées au relai pour la partie commande qui vont longer tout le
haut du boitier pour ressortir de l’autre côté de la machine.

.. container:: aligncenter

    [flickr:id=19166337829]

Puis on fixe ces fils sur le haut du boitier pour les faire ressortir de
l’autre côté. Afin de les protéger de la chaleur dégagée par les éléments
chauffants, on va d’abord les coller au fond avec un scotch qui accroche bien
puis on va rajouter une couche de scotch de protection thermique pour éviter de
faire fondre la colle du premier scotch ainsi que les câbles.

.. container:: aligncenter

    [flickr:id=19346405562]

Et voilà ! Plus qu’à utiliser ces fils de commande pour activer le relai depuis
l’Arduino.

Mesures et code
---------------

Maintenant que tout est bien câblé, on passe à la partie un peu plus logicielle
du hack.

Calibrage de la sonde de température
""""""""""""""""""""""""""""""""""""

N’ayant aucune idée de la formule mathématique reliant la tension de sortie du
capteur de température à la température mesurée, nous allons devoir nous même
déterminer ce rapport.

Pour se faire, on va écrire un petit programme Arduino qui nous affiche via son
port série la tension mesurée par le capteur de température. Voici ce que l’on
obtient en allumant la plastifieuse et en mesurant la tension du capteur :

.. image:: /images/pcblastifieuse/temperatures.png

On observe un préchauffage suivi d’un maintient au chaud. Mais revenons à notre
calibrage.

Juste à côté de la sonde de température fixée sur la résistance chauffante on
place une sonde JK qui va nous permettre de mesurer la température réelle à
cette endroit. On note quelques points dans un tableur et on effectue ensuite
une régression linéaire.

.. image:: /images/pcblastifieuse/reglin.png

En trouvant le lien entre la tension mesurée par la sonde de température et la
température de la sonde JK, on peut en déduire une formule qui nous donnera la
température réelle en utilisant notre propre capteur !

Code Arduino de régulation
""""""""""""""""""""""""""

Maintenant que l’on possède une formule permettant de connaitre la température
dans notre « four », on peut écrire un petit programme Arduino qui s’assure de
maintenir la température en se basant sur l’algorithme suivant :

 - Si la température est trop froide alors
    - Allumer la résistance
 - Sinon si la température est trop chaude alors
    - Éteindre la résistance

Qui va tourner en boucle et qui va donc se faire maintenir la plastifieuse à
une température plus élevée que celle pour laquelle elle est conçue.

D’ailleurs, ça se voit (fumée qui sort du boitier) et ça se sent (odeur de
« chaud ») mais une fois que le boitier a un peu souffert à l’allumage il ne
fume plus.

Premiers résultats encourageants
--------------------------------

Une fois tout cela réalisé, reste l’étape du test.

Nous avons tenté une sorte de sérigraphie en imprimant un motif tribal (afin de
tester la précision grâce aux formes pointues) sur des feuilles de papier glacé
provenant de flyers et en la collant sur une plaque époxy.

Après quelques passages (sans doute pas assez) dans un four à 200°C (sans doute
pas assez non plus) sur une plaque d’époxy pas assez propre, on obtient un résultat plutôt encourageant !

    [flickr:id=19346399242]

Il reste du papier sur le motif noir et le toner ne colle pas bien sur la
plaque, mais on distingue bien la forme tribal de départ !

Et ensuite ?
------------

La prochaine étape est donc de refaire un test avec une température plus haute
de 5/10 °C en prenant soin de nettoyer la surface de la plaque avec de
l’acétone pour enlever la graisse qui peut provoquer la mauvaise adhérence du
motif et d’effectuer plus de passages de la plaque dans la plastifieuse pour
que le toner puisse fondre correctement.
