#!/usr/bin/env python3
# **************************************************************
# File      : dft.py
# Version   : 1.6
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
from terminal_colors import COL_YELLOW_BLUE, COL_YELLOW_RED, COL_YELLOW, COL_STANDARD

# ** Variables *************************************************
LOG_FILE_NAME = 'dft.log'
LOG_FILE = path.join(path.dirname(path.abspath(__file__)), LOG_FILE_NAME)

# ** Functions *************************************************
# ask_number() - asks until the user writes a number that is 0 or more, accepts both 2.5 and 2,5
def ask_number(question):
	while True:
		user_input_value = input(question).replace(',', '.')
		try:
			number = float(user_input_value)
		except ValueError:
			logging.error(f"ask_number: '{user_input_value}' is not a number")
			print(f"{COL_YELLOW_RED} Det måste vara en siffra, försök igen {COL_STANDARD}")
			continue

		if number < 0:
			logging.error(f"ask_number: {number} is negative")
			print(f"{COL_YELLOW_RED} Talet får inte vara negativt, försök igen {COL_STANDARD}")
			continue

		return number


# ask_time() - asks for hours and minutes, returns two values
def ask_time():
	hours = ask_number("Tid, timmar: ")
	minutes = ask_number("Tid, minuter: ")
	return hours, minutes


# main() - the flow of the script
def main():
	# clear linux screen
	subprocess.run(['clear'])

	# logging
	logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename=LOG_FILE, level=logging.ERROR)

	print()
	print(f"{COL_YELLOW_BLUE}   D F T - Distans Fart Tid   {COL_STANDARD}")

	while True:
		print("\nVad vill du räkna ut?")
		print("  1 = Distans\n  2 = Fart\n  3 = Tid\n  0 = Avsluta")
		choice = input("Val: ")

		if choice == "1":
			speed = ask_number("Fart, knop: ")
			hours, minutes = ask_time()
			distance = dft_functions.calculate_distance(speed, hours, minutes)
			print(f"{COL_YELLOW}Distansen är: {distance:.1f} M{COL_STANDARD}")

		elif choice == "2":
			distance = ask_number("Distans, M: ")
			hours, minutes = ask_time()
			if dft_functions.to_minutes(hours, minutes) == 0:
				logging.error("main: speed asked with time 0")
				print(f"{COL_YELLOW_RED} Tiden får inte vara 0 {COL_STANDARD}")
				continue
			speed = dft_functions.calculate_speed(distance, hours, minutes)
			print(f"{COL_YELLOW}Farten är: {speed:.1f} knop{COL_STANDARD}")

		elif choice == "3":
			distance = ask_number("Distans, M: ")
			speed = ask_number("Fart, knop: ")
			if speed == 0:
				logging.error("main: time asked with speed 0")
				print(f"{COL_YELLOW_RED} Farten får inte vara 0 {COL_STANDARD}")
				continue
			hours, minutes = dft_functions.calculate_time(distance, speed)
			print(f"{COL_YELLOW}Tiden är: {hours} h {minutes} min{COL_STANDARD}")

		elif choice == "0":
			print("Hej då!")
			break

		else:
			print(f"{COL_YELLOW_RED} Välj 1, 2, 3 eller 0 {COL_STANDARD}")


# ** Main ******************************************************
# run main() only when the script is started, not when it is imported
# Ctrl+C or Ctrl+D ends the script quietly instead of showing a Python error
if __name__ == "__main__":
	try:
		main()
	except (KeyboardInterrupt, EOFError):
		print("\nHej då!")

# ** History ***************************************************
# 1.0 2026-10-13 Initial version
# 1.1 2026-10-13 menu, input and output
# 1.2 2026-10-13 clear screen at start
# 1.3 2026-10-13 subprocess.run() instead of os.system()
# 1.4 2026-10-13 logging to dft.log, Ctrl+C and Ctrl+D end the script quietly
# 1.5 2026-10-14 constants in upper case
# 1.6 2026-10-14 colors (terminal_colors.py)

# ** END SCRIPT ************************************************
