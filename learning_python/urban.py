#!/usr/bin/env python3
# **************************************************************
# File      : urban.py
# Version   : 1.11
# Purpose   : learning python
# Linked to : urban_classes.py
#
# Created by: Urban Björkén
# Date      : 2018-10-02
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************
from os import system, path
import sys
import logging
import urban_classes

# ** Variables *************************************************
log_file_name = 'PythonLogException.log'
log_file = path.join(path.dirname(path.abspath(__file__)), log_file_name)

# ** Functions *************************************************
# main() - the flow of the script
def main():
	correct_count = 0
	total_numbers = 0

	# clear linux screen
	system('clear')

	# logging
	logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename=log_file,level=logging.ERROR)

	# welcome
	print("\nHej och Välkommen!")
	print("Här kan du öva på multiplikationstabellen. Du kommer att få göra följande val:")
	print("  * Vilken tabell (ex: 3)\n  * startposition (ex: 3)\n  * slutposition  (ex: 9)\n")

	# enduser input
	selected_table = urban_classes.Calculate.check_integer(input('Skriv in tabell: '), exit_on_error=True)
	selected_lower_position = urban_classes.Calculate.check_integer(input('Skriv in start: '), exit_on_error=True)
	selected_higher_position = urban_classes.Calculate.check_integer(input('Skriv in stop: '), exit_on_error=True)

	# stop must not be lower than start
	if selected_higher_position < selected_lower_position:
		logging.error('urban.py: stop (' + str(selected_higher_position) + ') lower than start (' + str(selected_lower_position) + ')')
		print("Stop får inte vara mindre än start")
		print("Script avslutat")
		sys.exit(1)

	# looping out questions
	for counter in range(selected_lower_position, selected_higher_position + 1):
		total_numbers += 1
		answer = urban_classes.Calculate.result(counter,selected_table)

		# if correct answer
		if answer:
			correct_count += 1

	# feedback to enduser
	print(correct_count ,"rätt av totalt" , total_numbers , "tal")

# ** Main ******************************************************
# run main() only when the script is started, not when it is imported
if __name__ == "__main__":
	main()

# ** History ***************************************************
# 1.0 2018-10-02 Initial version
# 1.1 2019-10-03 Added logging
# 1.2 2026-10-12 New header template, converted to UTF-8
# 1.3 2026-10-12 Fixed typos, check that stop is not lower than start
# 1.4 2026-10-13 renamed logfile, Fixed print (, added version in header
# 1.5 2026-10-13 snake_case for variable, function and file names
# 1.6 2026-10-13 logfile saved next to the script, name in variable
# 1.7 2026-10-13 flow moved to main()
# 1.8 2026-10-13 if answer: instead of if answer == True:
# 1.9 2026-10-13 x += 1 instead of counter(), removed step in range()
# 1.10 2026-10-13 exit_on_error=True instead of 'firstChoice'
# 1.11 2026-10-13 correct_answer renamed to correct_count

# ** END SCRIPT ************************************************
