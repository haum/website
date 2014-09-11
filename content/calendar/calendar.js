/*
 * calendar.js
 *
 * Copyright (C) 2014 Mathieu Gaborit (matael) <mathieu@matael.org>
 *
 *
 * Distributed under WTFPL terms
 *
 *            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
 *                    Version 2, December 2004
 *
 * Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
 *
 * Everyone is permitted to copy and distribute verbatim or modified
 * copies of this license document, and changing it is allowed as long
 * as the name is changed.
 *
 *            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
 *   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
 *
 *  0. You just DO WHAT THE FUCK YOU WANT TO.
 *
 */

/***** Template :
    {'date': ['JJ', 'mois', 'AAAA', 'HH', 'MM'],
     'lieu': 'Somewhere over the rainbow',
     'texte': 'Lorem ipsum dolor sit amet sed consecuenturLorem ipsum dolor sit amet sed consecuenturLorem ipsum dolor sit amet sed consecuenturLorem ipsum dolor sit amet sed consecuentur'},
 */

/*** PLEASE USE SHORT MONTH NAMES ***/
var events = [
//    {'date': ['03', 'sept', '2014', '18', '30'],
//     'lieu': '#opendatapero au Venezzia - Pl. de la République',
//     'texte': 'Retrouvons nous en terrasse pour discuter opendata tous ensemble !'},
//    {'date': ['04', 'sept', '2014', '19', '00'],
//     'lieu': "Jeudi du Libre à l'Epicerie du Pré",
//     'texte': 'On se retrouve avec les libristes pour un rsync houblonné :)'},
    {'date': ['19', 'sept', '2014', '18', '00'],
     'lieu': 'Hackathon Opendata - Ruche Numérique',
     'texte': "Hackathon autour de l'ouverture des données en partenariat avec le Conseil Général et la Ruche Numérique <a href='/hackathon_opendata.html'>En Savoir plus >></a>"},
    {'date': ['27', 'sept', '2014', '9', '00'],
     'lieu': 'Forum Jeunes aux Quinconces',
     'texte': "Journée de présentation des activités du HAUM auprès des jeunes... #pong1D et #pianostairs au programme..."},
    {'date': ['30', 'sept', '2014', '18', '30'],
     'lieu': 'Arduino 3.1 à la Ruche Numérique',
     'texte': "Première séance de la nouvelle formation arduino (niveau 1)"},
    {'date': ['02', 'oct', '2014', '19', '00'],
     'lieu': "Jeudi du Libre à l'Epicerie du Pré",
     'texte': "Encore un coup de git pull au houblon entre libristes !"},
    {'date': ['07', 'oct', '2014', '18', '30'],
     'lieu': 'Arduino 3.2 à la Ruche Numérique',
     'texte': "Suite de  la nouvelle formation arduino (niveau 1)"},
    {'date': ['14', 'oct', '2014', '18', '30'],
     'lieu': 'Arduino 3.3 à la Ruche Numérique',
     'texte': "Fin de  la nouvelle formation arduino (niveau 1)"},
    {'date': ['21', 'oct', '2014', '18', '30'],
     'lieu': 'Arduino 3.4 à la Ruche Numérique',
     'texte': "Séance en rab' pour la nouvelle formation arduino (niveau 1)"},
    {'date': ['06', 'nov', '2014', '19', '00'],
     'lieu': "Jeudi du Libre à l'Epicerie du Pré",
     'texte': "RAID au houblon pour les libristes manceaux"},
];


