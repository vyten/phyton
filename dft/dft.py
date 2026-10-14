#!/usr/bin/env python3
# **************************************************************
# File      : dft.py
# Version   : 1.8
# Purpose   : calculate distance, speed or time at sea (Distans Fart Tid)
# Linked to : dft_functions.py
#
# Created by: Urban Björkén
# Date      : 2026-10-13
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************
import subprocess
import logging
from os import path
import dft_functions
import lang_se
from terminal_colors import COL_YELLOW_BLUE, COL_YELLOW_RED, COL_GREEN, COL_STANDARD

# ** Variables *************************************************
LOG_FILE_NAME = 'dft.log'
LOG_FILE = path.join(path.dirname(path.abspath(__file__)), LOG_FILE_NAME)

# ** Functions *************************************************
# ask_number() - asks until the user writes a number that is 0 or more, accepts both 2.5 and 2,5
def ask_number(question, texts):
	while True:
		user_input_value = input(question).replace(',', '.')
		try:
			number = float(user_input_value)
		except ValueError:
			logging.error(f"ask_number: '{user_input_value}' is not a number")
			print(f"{COL_YELLOW_RED} {texts['error_not_number']} {COL_STANDARD}")
			continue

		if number < 0:
			logging.error(f"ask_number: {number} is negative")
			print(f"{COL_YELLOW_RED} {texts['error_negative']} {COL_STANDARD}")
			continue

		return number


# ask_time() - asks for hours and minutes, returns two values
def ask_time(texts):
	hours = ask_number(texts['ask_hours'], texts)
	minutes = ask_number(texts['ask_minutes'], texts)
	return hours, minutes


# main() - the flow of the script
def main():
	# texts in the chosen language
	texts = lang_se.TEXTS

	# clear linux screen
	subprocess.run(['clear'])

	# logging
	logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename=LOG_FILE, level=logging.ERROR)

	print()
	print(f"{COL_YELLOW_BLUE}   {texts['title']}   {COL_STANDARD}")

	while True:
		print()
		print(texts['menu_question'])
		print(f"  1 = {texts['distance']}")
		print(f"  2 = {texts['speed']}")
		print(f"  3 = {texts['time']}")
		print(f"  0 = {texts['quit']}")
		choice = input(texts['choice'])

		if choice == "1":
			speed = ask_number(texts['ask_speed'], texts)
			hours, minutes = ask_time(texts)
			distance = dft_functions.calculate_distance(speed, hours, minutes)
			print(f"{COL_GREEN}{texts['result_distance'].format(distance=distance)}{COL_STANDARD}")

		elif choice == "2":
			distance = ask_number(texts['ask_distance'], texts)
			hours, minutes = ask_time(texts)
			if dft_functions.to_minutes(hours, minutes) == 0:
				logging.error("main: speed asked with time 0")
				print(f"{COL_YELLOW_RED} {texts['error_time_zero']} {COL_STANDARD}")
				continue
			speed = dft_functions.calculate_speed(distance, hours, minutes)
			print(f"{COL_GREEN}{texts['result_speed'].format(speed=speed)}{COL_STANDARD}")

		elif choice == "3":
			distance = ask_number(texts['ask_distance'], texts)
			speed = ask_number(texts['ask_speed'], texts)
			if speed == 0:
				logging.error("main: time asked with speed 0")
				print(f"{COL_YELLOW_RED} {texts['error_speed_zero']} {COL_STANDARD}")
				continue
			hours, minutes = dft_functions.calculate_time(distance, speed)
			print(f"{COL_GREEN}{texts['result_time'].format(hours=hours, minutes=minutes)}{COL_STANDARD}")

		elif choice == "0":
			print(texts['goodbye'])
			break

		else:
			print(f"{COL_YELLOW_RED} {texts['error_menu']} {COL_STANDARD}")


# ** Main ******************************************************
# run main() only when the script is started, not when it is imported
# Ctrl+C or Ctrl+D ends the script quietly instead of showing a Python error
if __name__ == "__main__":
	try:
		main()
	except (KeyboardInterrupt, EOFError):
		print()
		print(lang_se.TEXTS['goodbye'])

# ** History ***************************************************
# 1.0 2026-10-13 Initial version
# 1.1 2026-10-13 menu, input and output
# 1.2 2026-10-13 clear screen at start
# 1.3 2026-10-13 subprocess.run() instead of os.system()
# 1.4 2026-10-13 logging to dft.log, Ctrl+C and Ctrl+D end the script quietly
# 1.5 2026-10-14 constants in upper case
# 1.6 2026-10-14 colors (terminal_colors.py)
# 1.7 2026-10-14 answers in green
# 1.8 2026-10-14 texts from lang_se.py

# ** END SCRIPT ************************************************
