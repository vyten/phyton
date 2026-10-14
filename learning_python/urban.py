#!/usr/bin/env python3
# **************************************************************
# File      : urban.py
# Version   : 1.19
# Purpose   : learning python
# Linked to : urban_functions.py
#
# Created by: Urban Björkén
# Date      : 2018-10-02
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************
from os import path
import subprocess
import sys
import logging
# the root directory of the repo, so that common/ can be found
sys.path.insert(0, path.join(path.dirname(path.abspath(__file__)), '..'))
import urban_functions
from common.terminal_colors import COL_YELLOW_BLUE, COL_YELLOW_RED, COL_STANDARD

# ** Variables *************************************************
LOG_FILE_NAME = 'PythonLogException.log'
LOG_FILE = path.join(path.dirname(path.abspath(__file__)), LOG_FILE_NAME)

# ** Functions *************************************************
# main() - the flow of the script
def main():
	correct_count = 0
	total_numbers = 0

	# clear linux screen
	subprocess.run(['clear'])

	# logging
	logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename=LOG_FILE,level=logging.ERROR)

	# welcome, yellow on blue, all lines padded to the same width
	welcome_lines = [
		"",
		"Hej och Välkommen!",
		"",
		"Här kan du öva på multiplikationstabellen. Du kommer att få göra följande val:",
		"  * Vilken tabell (ex: 3)",
		"  * startposition (ex: 3)",
		"  * slutposition  (ex: 9)",
		"",
	]
	width = max(len(line) for line in welcome_lines)
	print()
	for line in welcome_lines:
		print(f"{COL_YELLOW_BLUE}  {line.ljust(width)}  {COL_STANDARD}")
	print()

	# enduser input
	selected_table = urban_functions.check_integer(input('Skriv in tabell: '), exit_on_error=True)
	selected_lower_position = urban_functions.check_integer(input('Skriv in start: '), exit_on_error=True)
	selected_higher_position = urban_functions.check_integer(input('Skriv in stop: '), exit_on_error=True)

	# stop must not be lower than start
	if selected_higher_position < selected_lower_position:
		logging.error('urban.py: stop (' + str(selected_higher_position) + ') lower than start (' + str(selected_lower_position) + ')')
		print(f"{COL_YELLOW_RED} Stop får inte vara mindre än start {COL_STANDARD}")
		print(f"{COL_YELLOW_RED} Script avslutat {COL_STANDARD}")
		sys.exit(1)

	# looping out questions
	for counter in range(selected_lower_position, selected_higher_position + 1):
		total_numbers += 1
		answer = urban_functions.result(counter,selected_table)

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
# 1.12 2026-10-13 calls functions directly, class Calculate removed
# 1.13 2026-10-13 urban_classes.py renamed to urban_functions.py
# 1.14 2026-10-13 subprocess.run() instead of os.system()
# 1.15 2026-10-14 welcome text yellow on blue (terminal_colors.py)
# 1.16 2026-10-14 descriptive color names
# 1.17 2026-10-14 constants in upper case
# 1.18 2026-10-14 wrong input in yellow on red
# 1.19 2026-10-14 terminal_colors from common/

# ** END SCRIPT ************************************************
