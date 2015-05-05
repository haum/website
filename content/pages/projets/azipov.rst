======
AziPOV
======

:slug: azipov

Qu'est ce que c'est?
====================

AziPOV est un afficheur tridimensionnel multicolore. Il s'agit d'un appareil que le HAUM souhaite concevoir pour afficher des animations en trois dimensions.

Le projet est en cours de réflexion. Cette page contient quelques informations sur notre avancement.

Matériel
========

Leds
----

Le projet nécessite l'utilisation d'un grand nombre de LEDs.

Nous avons déjà utilisé un grand nombre de leds dans le projet Pong_. Cependant, le bandeau de LEDs utilisé dans ce projet ne convient pas à AziPOV: la commande du bandeau utilise beaucoup de temps processeur et la vitesse de rafraichissement est limitante.

Nous avons trouvé une autre technologie de LEDs similaire dans la forme, mais mieux adaptée à nos desseins: il s'agit des LEDs "APA 102".

Dans un boîtier 5050, ces leds intègrent à la fois un circuit de contrôle intelligent et trois LEDs de couleur différente. Le processeur peut communiquer avec chaque "pixel" à travers un bus SPI pour choisir une des 16 millions de couleurs possibles.

Ce type de LEDs n'est pas très onéreux (de l'ordre de 25€ la centaine fin 2014). Elle a plusieurs grands avantages pour le projet :

- Nous pouvons facilement afficher 16 millions de couleurs
- La communication utilise un bus standard, pour lequel la plupart des microcontrôleurs ont une accélération matérielle
- La communication peut se faire à fréquence élevée (des sources précisent des utilisations à 4Mhz et certaines parlent de plusieurs dizaines de mégahertz)

.. _Pong: /pages/1dpong.html

Et après ?
==========

La suite, c'est continuer la réflexion et le construire...
