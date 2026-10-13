#!/usr/bin/env python3
# **************************************************************
# File      : dft_functions.py
# Version   : 1.1
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
# calculate_distance() - returns the distance in nautical miles (M)
# speed in knots, time in hours and minutes
def calculate_distance(speed, hours, minutes):
	total_minutes = hours * 60 + minutes
	return speed * total_minutes / 60


# ** Main ******************************************************
# test the functions, runs only when this file is started directly
if __name__ == "__main__":
	print("6 knop i 1 h 30 min:", calculate_distance(6, 1, 30), "M")
	print("10 knop i 0 h 45 min:", calculate_distance(10, 0, 45), "M")
	print("5.5 knop i 2 h 0 min:", calculate_distance(5.5, 2, 0), "M")

# ** History ***************************************************
# 1.0 2026-10-13 Initial version
# 1.1 2026-10-13 calculate_distance()

# ** END SCRIPT ************************************************
