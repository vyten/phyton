#!/usr/bin/env python3
# **************************************************************
# File      : terminal_colors.py
# Version   : 1.2
# Purpose   : colors in the terminal, standalone, can be copied to other projects
# Linked to :
#
# Created by: Urban Björkén
# Date      : 2026-10-14
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************


# ** Variables *************************************************
# same codes as in bash, Python writes \e as \033
COL_WHITE_BLUE = "\033[37;44m"     # white on blue
COL_YELLOW_BLUE = "\033[93;44m"    # yellow on blue
COL_YELLOW_RED = "\033[93;41m"     # yellow on red
COL_YELLOW = "\033[0;93m"          # yellow on standard background
COL_STANDARD = "\033[0m"           # back to standard

# ** Functions *************************************************


# ** Main ******************************************************
# show all colors, runs only when this file is started directly
if __name__ == "__main__":
	print(f"{COL_WHITE_BLUE} COL_WHITE_BLUE  white on blue {COL_STANDARD}")
	print(f"{COL_YELLOW_BLUE} COL_YELLOW_BLUE yellow on blue {COL_STANDARD}")
	print(f"{COL_YELLOW_RED} COL_YELLOW_RED  yellow on red {COL_STANDARD}")
	print(f"{COL_YELLOW} COL_YELLOW      yellow {COL_STANDARD}")
	print(f"{COL_STANDARD} COL_STANDARD    standard {COL_STANDARD}")

# ** History ***************************************************
# 1.0 2026-10-14 Initial version
# 1.1 2026-10-14 descriptive color names
# 1.2 2026-10-14 constants in upper case

# ** END SCRIPT ************************************************
