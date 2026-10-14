#!/usr/bin/env python3
# **************************************************************
# File      : dft_functions.py
# Version   : 1.4
# Purpose   : functions for calculating distance, speed and time
# Linked to : dft.py
#
# Created by: Urban Björkén
# Date      : 2026-10-13
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************
import math

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


# to_hours_and_minutes() - converts minutes to whole hours and minutes, returns two values
def to_hours_and_minutes(total_minutes):
	hours, minutes = divmod(round(total_minutes), 60)
	return hours, minutes


# calculate_time() - returns the time in hours and minutes
# distance in nautical miles (M), speed in knots
def calculate_time(distance, speed):
	return to_hours_and_minutes(distance / speed * 60)


# ** Main ******************************************************
# test the functions, runs only when this file is started directly
# assert stops with AssertionError if an answer is wrong
# math.isclose() is used for decimals, since 0.1 + 0.2 is not exactly 0.3 in a computer
if __name__ == "__main__":
	# speed, hours, minutes -> distance
	for speed, hours, minutes, expected in [(6, 1, 30, 9), (10, 0, 45, 7.5), (5.5, 2, 0, 11)]:
		distance = calculate_distance(speed, hours, minutes)
		assert math.isclose(distance, expected), f"calculate_distance({speed}, {hours}, {minutes}) gave {distance}, expected {expected}"

	# distance, hours, minutes -> speed
	for distance, hours, minutes, expected in [(9, 1, 30, 6), (7.5, 0, 45, 10), (11, 2, 0, 5.5)]:
		speed = calculate_speed(distance, hours, minutes)
		assert math.isclose(speed, expected), f"calculate_speed({distance}, {hours}, {minutes}) gave {speed}, expected {expected}"

	# distance, speed -> hours and minutes, the last two are the 60 minute bug from the C# version
	for distance, speed, expected in [(9, 6, (1, 30)), (7.5, 10, (0, 45)), (10, 3, (3, 20)), (6, 6, (1, 0)), (5.97, 6, (1, 0))]:
		result = calculate_time(distance, speed)
		assert result == expected, f"calculate_time({distance}, {speed}) gave {result}, expected {expected}"

	print("All tests OK")

# ** History ***************************************************
# 1.0 2026-10-13 Initial version
# 1.1 2026-10-13 calculate_distance()
# 1.2 2026-10-13 calculate_speed(), to_minutes()
# 1.3 2026-10-13 calculate_time(), to_hours_and_minutes()
# 1.4 2026-10-14 tests with assert instead of printing

# ** END SCRIPT ************************************************
