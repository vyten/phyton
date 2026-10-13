#!/usr/bin/env python3
# **************************************************************
# File      : urban_classes.py
# Version   : 1.7
# Purpose   : class in external file
# Linked to : urban.py
#
# Created by: Urban Björkén
# Date      : 2018-10-02
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************
import logging
import sys

# ** Variables *************************************************


# ** Functions *************************************************
class Calculate:
	# check_integer() - checks that it is an integer, exits the script on error if exit_on_error is True
	def check_integer(user_input_value, exit_on_error):
		try:
			number = int(user_input_value)

		except (ValueError) as error:
			logging.error('class: Calculate.check_integer ' + str(error))
			if exit_on_error:
				print("Det måste vara heltal\nFel: [", error, "]\n")
				print("Script avslutat")
				sys.exit(1)
			else:
				print("Det måste vara heltal")
		else:
			return number

	# result() - calculates and corrects answers from users, printing answers correct | error
	def result(factor, table):
		correct_result = factor * table
		print("Vad är:", factor, '*', table,"?")

		# check that the answer is an integer
		answer = Calculate.check_integer(input('svar: '), exit_on_error=False)
		if answer == correct_result:
			print("rätt\n")
			return True
		else:
			print("fel, rätt svar är:", correct_result, "\n")
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

# ** END SCRIPT ************************************************
