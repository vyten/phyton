#!/usr/bin/env python3
# **************************************************************
# File      : urbanClasses.py
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
	# checkInteger() - checks that it is an integer
	def checkInteger(cIs,cIv):
		try:
			cIi = int(cIs)

		except (ValueError) as eDesc:
			# exit script if it's first choice
			if cIv == 'firstChoice':
				logging.error('class: Calculate.checkInteger ' + str(eDesc))
				print ("Det måste vara heltal\nFel: [", eDesc, "]\n")
				print("Script avslutat")
				sys.exit(1)
			else:
				logging.error('class: Calculate.checkInteger ' + str(eDesc))
				print ("Det måste vara heltal")
		else:
			return cIi

	# result() - calculates and corrects answers from users, printing answers correct | error
	def result(c,ui):
		result = c * ui
		print ("Vad är:", c, '*', ui,"?")

		# calling class Validate
		userCountInput=Calculate.checkInteger(input('svar: '),'xxx')
		if userCountInput == result:
			print ("rätt\n")
			return True
		else:
			print ("fel, rätt svar är:",result ,"\n")
			return False

	# counter()
	def counter(ci):
		ci = ci + 1
		return ci

# ** Main ******************************************************


# ** History ***************************************************
# 1.0 2018-10-02 Initial version
# 1.1 2019-10-03 checkInteger() on error write to logfile
# 1.2 2026-10-12 New header template, converted to UTF-8
# 1.3 2026-10-12 Fixed typo, sys.exit(1) on error

# ** END SCRIPT ************************************************
