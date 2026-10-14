#!/usr/bin/env python3
# **************************************************************
# File      : urban_functions.py
# Version   : 1.13
# Purpose   : functions in external file
# Linked to : urban.py
#
# Created by: Urban Björkén
# Date      : 2018-10-02
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************
import logging
import sys
from os import path
# the root directory of the repo, so that common/ can be found
sys.path.insert(0, path.join(path.dirname(path.abspath(__file__)), '..'))
from common.terminal_colors import COL_YELLOW_RED, COL_GREEN, COL_STANDARD

# ** Variables *************************************************


# ** Functions *************************************************
# check_integer() - returns the integer, or None if it is not an integer (exits the script instead if exit_on_error is True)
def check_integer(user_input_value, exit_on_error):
	try:
		number = int(user_input_value)

	except (ValueError) as error:
		logging.error('urban_functions.check_integer ' + str(error))
		if exit_on_error:
			print(f"{COL_YELLOW_RED} Det måste vara heltal {COL_STANDARD}\nFel: [ {error} ]\n")
			print(f"{COL_YELLOW_RED} Script avslutat {COL_STANDARD}")
			sys.exit(1)
		else:
			print(f"{COL_YELLOW_RED} Det måste vara heltal {COL_STANDARD}")
			return None
	else:
		return number


# result() - calculates and corrects answers from users, printing answers correct | error
def result(factor, table):
	correct_answer = factor * table
	print("Vad är:", factor, '*', table,"?")

	# check that the answer is an integer
	answer = check_integer(input('svar: '), exit_on_error=False)
	if answer == correct_answer:
		print(f"{COL_GREEN}rätt{COL_STANDARD}\n")
		return True
	else:
		print(f"{COL_YELLOW_RED} fel, rätt svar är: {correct_answer} {COL_STANDARD}\n")
		return False

# ** Main ******************************************************


# ** History ***************************************************
# 1.0 2018-10-02 Initial version
# 1.1 2019-10-03 checkInteger() on error write to logfile
# 1.2 2026-10-12 New header template, converted to UTF-8
# 1.3 2026-10-12 Fixed typo, sys.exit(1) on error
# 1.4 2026-10-13 Fixed print (, added version in header
# 1.5 2026-10-13 snake_case for variable, function and file names
# 1.6 2026-10-13 removed counter(), fixed outdated comment
# 1.7 2026-10-13 readable parameter names, exit_on_error True/False instead of strings
# 1.8 2026-10-13 check_integer() returns None on error, correct_result renamed to correct_answer
# 1.9 2026-10-13 class Calculate replaced by functions in the module
# 1.10 2026-10-13 renamed from urban_classes.py
# 1.11 2026-10-14 wrong answer and wrong input in yellow on red
# 1.12 2026-10-14 right answer in green
# 1.13 2026-10-14 terminal_colors from common/

# ** END SCRIPT ************************************************
