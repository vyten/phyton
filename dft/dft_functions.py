#!/usr/bin/env python3
# **************************************************************
# File      : dft_functions.py
# Version   : 1.2
# Purpose   : functions for calculating distance, speed and time
# Linked to : dft.py
#
# Created by: Urban Björkén
# Date      : 2026-10-13
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************


# ** Variables *************************************************


# ** Functions *************************************************
# to_minutes() - converts hours and minutes to minutes
def to_minutes(hours, minutes):
	return hours * 60 + minutes


# calculate_distance() - returns the distance in nautical miles (M)
# speed in knots, time in hours and minutes
def calculate_distance(speed, hours, minutes):
	return speed * to_minutes(hours, minutes) / 60


# calculate_speed() - returns the speed in knots
# distance in nautical miles (M), time in hours and minutes
def calculate_speed(distance, hours, minutes):
	return distance / to_minutes(hours, minutes) * 60


# ** Main ******************************************************
# test the functions, runs only when this file is started directly
if __name__ == "__main__":
	print("6 knop i 1 h 30 min:", calculate_distance(6, 1, 30), "M")
	print("10 knop i 0 h 45 min:", calculate_distance(10, 0, 45), "M")
	print("5.5 knop i 2 h 0 min:", calculate_distance(5.5, 2, 0), "M")
	print()
	print("9 M på 1 h 30 min:", calculate_speed(9, 1, 30), "knop")
	print("7.5 M på 0 h 45 min:", calculate_speed(7.5, 0, 45), "knop")
	print("11 M på 2 h 0 min:", calculate_speed(11, 2, 0), "knop")

# ** History ***************************************************
# 1.0 2026-10-13 Initial version
# 1.1 2026-10-13 calculate_distance()
# 1.2 2026-10-13 calculate_speed(), to_minutes()

# ** END SCRIPT ************************************************
