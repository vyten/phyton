#!/usr/bin/env python3
# **************************************************************
# File      : urban.py
# Purpose   : learning python
# Linked to : urbanClasses.py
#
# Created by: Urban Björkén
# Date      : 2018-10-02
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************
from os import system
import sys
import logging
import urbanClasses

# ** Variables *************************************************
correctAnswer = 0
totalNumbers = 0

# ** Functions *************************************************


# ** Main ******************************************************
# clear linux screen
system('clear')

# logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='PhytonLogExeption.log',level=logging.ERROR)

# welcome
print ("\nHej och Välkommen!")
print ("Här kan du öva på multiplikationstabellen. Du kommer att få göra följande val:")
print ("  * Vilken tabell (ex: 3)\n  * startposition (ex: 3)\n  * slutposition  (ex: 9)\n")

# enduser input
selectedTable = urbanClasses.Calculate.checkInteger(input('Skriv in tabell: '),'firstChoice')
selectedLowerPosition = urbanClasses.Calculate.checkInteger(input('Skriv in start: '),'firstChoice')
selectedHigherPosition = urbanClasses.Calculate.checkInteger(input('Skriv in stop: '),'firstChoice')

# stop must not be lower than start
if selectedHigherPosition < selectedLowerPosition:
	logging.error('urban.py: stop (' + str(selectedHigherPosition) + ') lower than start (' + str(selectedLowerPosition) + ')')
	print ("Stop får inte vara mindre än start")
	print("Script avslutat")
	sys.exit(1)

# looping out questions
for counter in range (selectedLowerPosition,(selectedHigherPosition+1),1):
	# calling Count class
	totalNumbers = urbanClasses.Calculate.counter(totalNumbers)
	answer = urbanClasses.Calculate.result(counter,selectedTable)

	# if correct answer
	if answer == True:
		correctAnswer = urbanClasses.Calculate.counter(correctAnswer)

# feedback to enduser
print (correctAnswer ,"rätt av totalt" , totalNumbers , "tal")

# ** History ***************************************************
# 1.0 2018-10-02 Initial version
# 1.1 2019-10-03 Added logging
# 1.2 2026-10-12 New header template, converted to UTF-8
# 1.3 2026-10-12 Fixed typos, check that stop is not lower than start

# ** END SCRIPT ************************************************
