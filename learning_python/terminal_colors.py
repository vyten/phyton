#!/usr/bin/env python3
# **************************************************************
# File      : terminal_colors.py
# Version   : 1.0
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
COL_WB = "\033[37;44m"    # white on blue
COL_YB = "\033[93;44m"    # yellow on blue
COL_YR = "\033[93;41m"    # yellow on red
COL_YZ = "\033[0;93m"     # yellow on standard background
COL_STD = "\033[0m"       # back to standard

# ** Functions *************************************************


# ** Main ******************************************************
# show all colors, runs only when this file is started directly
if __name__ == "__main__":
	print(f"{COL_WB} COL_WB  white on blue {COL_STD}")
	print(f"{COL_YB} COL_YB  yellow on blue {COL_STD}")
	print(f"{COL_YR} COL_YR  yellow on red {COL_STD}")
	print(f"{COL_YZ} COL_YZ  yellow {COL_STD}")
	print(f"{COL_STD} COL_STD standard {COL_STD}")

# ** History ***************************************************
# 1.0 2026-10-14 Initial version

# ** END SCRIPT ************************************************
