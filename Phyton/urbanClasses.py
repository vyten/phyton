#!/usr/bin/python3.6m
# coding: latin-1
# ***************************************************************
# File      : urbanClasses.py
# Purpose   : class in external file
# Linked to : urban.py                 
#                                
# Updated by: Urban Bj�rk�n
# Update    : result()
#             return True if correct answer else return False
# Date      : 2018-10-02 
#                        
# Created by: Urban Bj�rk�n
# Date      : 2018-10-02
# email     : vyten@starnet.nu
# ***************************************************************
class Calculate:
	# ******************************************
	# checkInteger()
	# checks that it is an integer
	# ******************************************
	def checkInteger(cIs,cIv):
		try:
			cIi = int(cIs)
		
		except (ValueError) as eDesc:
			# ******************************************
			# exit script if it's first choice
			# ******************************************
			if cIv == 'firstChoice':
				print ("Det m�ste vara heltal\nFel: [", eDesc, "]\n")
				print("Script avslutat")
				exit(0)
			else:
				print ("Det m�ste vara heltal")
		else:
			return cIi

	# ******************************************
	# result()
	# Calculates and corrects answers from users
	# printing answers correct | error
	# ******************************************
	def result(c,ui):
		result = c * ui
		print ("Vad �r:", c, '*', ui,"?")
	
		# ******************************************
		# calling class Validate
		# ******************************************
		userCountInput=Calculate.checkInteger(input('svar: '),'xxx')
		if userCountInput == result:
			print ("ratt\n")
			return True
		else:	
			print ("fel, r�tt svar �r:",result ,"\n")
			return False

	# ******************************************
	# counter()
	# ******************************************
	def counter(ci):
		ci = ci + 1
		return ci
