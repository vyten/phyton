#!/usr/bin/env python3
# **************************************************************
# File      : dft.py
# Version   : 1.2
# Purpose   : calculate distance, speed or time at sea (Distans Fart Tid)
# Linked to : dft_functions.py
#
# Created by: Urban Björkén
# Date      : 2026-10-13
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************
from os import system
import dft_functions

# ** Variables *************************************************


# ** Functions *************************************************
# ask_number() - asks until the user writes a number that is 0 or more, accepts both 2.5 and 2,5
def ask_number(question):
	while True:
		user_input_value = input(question).replace(',', '.')
		try:
			number = float(user_input_value)
		except ValueError:
			print("Det måste vara en siffra, försök igen")
			continue

		if number < 0:
			print("Talet får inte vara negativt, försök igen")
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
	system('clear')

	print("\nD F T - Distans Fart Tid")

	while True:
		print("\nVad vill du räkna ut?")
		print("  1 = Distans\n  2 = Fart\n  3 = Tid\n  0 = Avsluta")
		choice = input("Val: ")

		if choice == "1":
			speed = ask_number("Fart, knop: ")
			hours, minutes = ask_time()
			distance = dft_functions.calculate_distance(speed, hours, minutes)
			print(f"Distansen är: {distance:.1f} M")

		elif choice == "2":
			distance = ask_number("Distans, M: ")
			hours, minutes = ask_time()
			if dft_functions.to_minutes(hours, minutes) == 0:
				print("Tiden får inte vara 0")
				continue
			speed = dft_functions.calculate_speed(distance, hours, minutes)
			print(f"Farten är: {speed:.1f} knop")

		elif choice == "3":
			distance = ask_number("Distans, M: ")
			speed = ask_number("Fart, knop: ")
			if speed == 0:
				print("Farten får inte vara 0")
				continue
			hours, minutes = dft_functions.calculate_time(distance, speed)
			print(f"Tiden är: {hours} h {minutes} min")

		elif choice == "0":
			print("Hej då!")
			break

		else:
			print("Välj 1, 2, 3 eller 0")


# ** Main ******************************************************
# run main() only when the script is started, not when it is imported
if __name__ == "__main__":
	main()

# ** History ***************************************************
# 1.0 2026-10-13 Initial version
# 1.1 2026-10-13 menu, input and output
# 1.2 2026-10-13 clear screen at start

# ** END SCRIPT ************************************************
