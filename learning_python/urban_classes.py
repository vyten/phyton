#!/usr/bin/env python3
# **************************************************************
# File      : urban_classes.py
# Version   : 1.6
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
	# check_integer() - checks that it is an integer
	def check_integer(cIs,cIv):
		try:
			cIi = int(cIs)

		except (ValueError) as e_desc:
			# exit script if it's first choice
			if cIv == 'firstChoice':
				logging.error('class: Calculate.check_integer ' + str(e_desc))
				print("Det måste vara heltal\nFel: [", e_desc, "]\n")
				print("Script avslutat")
				sys.exit(1)
			else:
				logging.error('class: Calculate.check_integer ' + str(e_desc))
				print("Det måste vara heltal")
		else:
			return cIi

	# result() - calculates and corrects answers from users, printing answers correct | error
	def result(c,ui):
		result = c * ui
		print("Vad är:", c, '*', ui,"?")

		# check that the answer is an integer
		user_count_input=Calculate.check_integer(input('svar: '),'xxx')
		if user_count_input == result:
			print("rätt\n")
			return True
		else:
			print("fel, rätt svar är:",result ,"\n")
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

# ** END SCRIPT ************************************************
