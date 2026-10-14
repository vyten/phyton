#!/usr/bin/env python3
# **************************************************************
# File      : lang_en.py
# Version   : 1.0
# Purpose   : English texts for dft.py
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
	'language': 'English',
	'title': 'D S T - Distance Speed Time',
	'menu_question': 'What do you want to calculate?',
	'distance': 'Distance',
	'speed': 'Speed',
	'time': 'Time',
	'quit': 'Quit',
	'choice': 'Choice: ',
	'goodbye': 'Goodbye!',

	# questions
	'ask_distance': 'Distance, nm: ',
	'ask_speed': 'Speed, knots: ',
	'ask_hours': 'Time, hours: ',
	'ask_minutes': 'Time, minutes: ',

	# answers
	'result_distance': 'The distance is: {distance:.1f} nm',
	'result_speed': 'The speed is: {speed:.1f} knots',
	'result_time': 'The time is: {hours} h {minutes} min',

	# errors
	'error_not_number': 'It must be a number, try again',
	'error_negative': 'The number must not be negative, try again',
	'error_time_zero': 'The time must not be 0',
	'error_speed_zero': 'The speed must not be 0',
	'error_menu': 'Choose 1, 2, 3 or 0',
}

# ** Functions *************************************************


# ** Main ******************************************************
# show all texts, runs only when this file is started directly
if __name__ == "__main__":
	for key, text in TEXTS.items():
		print(f"{key:<18} {text}")

# ** History ***************************************************
# 1.0 2026-10-14 Initial version

# ** END SCRIPT ************************************************
