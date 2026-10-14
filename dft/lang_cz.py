#!/usr/bin/env python3
# **************************************************************
# File      : lang_cz.py
# Version   : 1.2
# Purpose   : Czech texts for dft.py, lines marked TODO are still in Swedish
# Linked to : dft.py
#
# Created by: Urban Björkén
# Date      : 2026-10-14
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************


# ** Variables *************************************************
# {name} is replaced with a value when the text is printed, :.1f means one decimal
TEXTS = {
	# title, menu and general
	'language': 'český',
	'title': 'V R C - vzdálenost rychlost čas',
	'menu_question': 'Vad vill du räkna ut?',                         # TODO översätt
	'distance': 'vzdálenost',
	'speed': 'rychlost',
	'time': 'čas',
	'quit': 'Avsluta',                                                # TODO översätt
	'change_language': 'Změnit jazyk',
	'choice': 'Val: ',                                                # TODO översätt
	'goodbye': 'Hej då!',                                             # TODO översätt

	# questions
	'ask_distance': 'vzdálenost, nm: ',
	'ask_speed': 'rychlost, uzly: ',
	'ask_hours': 'čas, hodiny: ',
	'ask_minutes': 'čas, minuty: ',

	# answers
	'result_distance': 'Odhadovaná vzdálenost: {distance:.1f} nm',
	'result_speed': 'Odhadovaná rychlost: {speed:.1f} uzly',
	'result_time': 'Odhadovaný čas: {hours} h {minutes} m',

	# errors
	'error_not_number': 'Det måste vara en siffra, försök igen',      # TODO översätt
	'error_negative': 'Talet får inte vara negativt, försök igen',    # TODO översätt
	'error_time_zero': 'Tiden får inte vara 0',                       # TODO översätt
	'error_speed_zero': 'Farten får inte vara 0',                     # TODO översätt
	'error_menu': 'Välj 1, 2, 3, 4 eller 0',                          # TODO översätt
}

# ** Functions *************************************************


# ** Main ******************************************************
# show all texts, runs only when this file is started directly
if __name__ == "__main__":
	for key, text in TEXTS.items():
		print(f"{key:<18} {text}")

# ** History ***************************************************
# 1.0 2026-10-14 Initial version
# 1.1 2026-10-14 change_language, 4 in error_menu
# 1.2 2026-10-14 change_language in Czech

# ** END SCRIPT ************************************************
