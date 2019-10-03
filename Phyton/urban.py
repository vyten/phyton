#!/usr/bin/python3.6m
# coding: latin-1
# ***************************************************************
# File      : urban.py
# Purpose   : learning python
# Linked to :                  
#                                
# Updated by: Urban Bj�rken
# Update    : count correct answer
# Date      : 2018-10-02
#                        
# Created by: Urban Bj�rk�n
# Date      : 2018-10-02
# email     : vyten@starnet.nu
# ***************************************************************
# ******************************************
# clear linux screen
# ******************************************
from os import system
system('clear')

# ******************************************
# variables (global ?)
# ******************************************
correctAnswer = 0
totalNumbers = 0

# ******************************************
# import classes
# ******************************************
import urbanClasses
import logging

# ******************************************
# logging
# ******************************************
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='PhytonLogExeption.log',level=logging.ERROR)

# ***************************************************************
# START SCRIPT
# ***************************************************************
# ******************************************
# welcome
# ******************************************
print ("\nHej och V�lkommen!")
print ("Har kan du �va p� multiplikationstabellen. Du kommer att f� g�ra f�ljande val:")
print ("  * Vilken tabell (ex: 3)\n  * startposition (ex: 3)\n  * slutposition  (ex: 9)\n")

# ******************************************
# enduser input
# ******************************************
selectedTable = urbanClasses.Calculate.checkInteger(input('Skriv in tabell: '),'firstChoice')
selectedLowerPosition = urbanClasses.Calculate.checkInteger(input('Skriv in start: '),'firstChoice')
selectedHigherPosition = urbanClasses.Calculate.checkInteger(input('Skriv in stop: '),'firstChoice')

# ******************************************
# looping out questions
# ******************************************
for counter in range (selectedLowerPosition,(selectedHigherPosition+1),1):
			# ******************************************
			# calling Count class
			# ******************************************
			totalNumbers = urbanClasses.Calculate.counter(totalNumbers)						
			answer = urbanClasses.Calculate.result(counter,selectedTable)
			
			# ******************************************
			# if correct answer
			# ******************************************
			if answer == True:
				correctAnswer = urbanClasses.Calculate.counter(correctAnswer)	

# ******************************************
# feedback to enduser
# ******************************************
print (correctAnswer ,"r�tt av totalt" , totalNumbers , "tal")
# ***************************************************************
# END SCRIPT
# ***************************************************************
