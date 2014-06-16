/*
 * haumtab.js
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


$('document').ready( function (){
	$('#haumtab').hide(); // on cache les liens
	$('#haumtab').attr('state', 'hidden');

	$('#haumtab_button').click(function () {
		if ($('#haumtab').attr('state') == 'hidden') {
			$('#haumtab').slideDown(300);
			$('#haumtab').attr('state', 'visible');
			$('#haumtab_button').html('Moins');
		} else {
			$('#haumtab').slideUp(300);
			$('#haumtab').attr('state', 'hidden');
			$('#haumtab_button').html('Plus');
		}
	});
});
