#!/usr/bin/env python3
# **************************************************************
# File      : urban.py
# Version   : 1.5
# Purpose   : learning python
# Linked to : urban_classes.py
#
# Created by: Urban Björkén
# Date      : 2018-10-02
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************
from os import system
import sys
import logging
import urban_classes

# ** Variables *************************************************
correct_answer = 0
total_numbers = 0

# ** Functions *************************************************


# ** Main ******************************************************
# clear linux screen
system('clear')

# logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='PythonLogException.log',level=logging.ERROR)

# welcome
print("\nHej och Välkommen!")
print("Här kan du öva på multiplikationstabellen. Du kommer att få göra följande val:")
print("  * Vilken tabell (ex: 3)\n  * startposition (ex: 3)\n  * slutposition  (ex: 9)\n")

# enduser input
selected_table = urban_classes.Calculate.check_integer(input('Skriv in tabell: '),'firstChoice')
selected_lower_position = urban_classes.Calculate.check_integer(input('Skriv in start: '),'firstChoice')
selected_higher_position = urban_classes.Calculate.check_integer(input('Skriv in stop: '),'firstChoice')

# stop must not be lower than start
if selected_higher_position < selected_lower_position:
	logging.error('urban.py: stop (' + str(selected_higher_position) + ') lower than start (' + str(selected_lower_position) + ')')
	print("Stop får inte vara mindre än start")
	print("Script avslutat")
	sys.exit(1)

# looping out questions
for counter in range (selected_lower_position,(selected_higher_position+1),1):
	# calling Count class
	total_numbers = urban_classes.Calculate.counter(total_numbers)
	answer = urban_classes.Calculate.result(counter,selected_table)

	# if correct answer
	if answer == True:
		correct_answer = urban_classes.Calculate.counter(correct_answer)

# feedback to enduser
print(correct_answer ,"rätt av totalt" , total_numbers , "tal")

# ** History ***************************************************
# 1.0 2018-10-02 Initial version
# 1.1 2019-10-03 Added logging
# 1.2 2026-10-12 New header template, converted to UTF-8
# 1.3 2026-10-12 Fixed typos, check that stop is not lower than start
# 1.4 2026-10-13 renamed logfile, Fixed print (, added version in header
# 1.5 2026-10-13 snake_case for variable, function and file names

# ** END SCRIPT ************************************************
