#!/usr/bin/env python3
# **************************************************************
# File      : terminal_colors.py
# Version   : 1.1
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
col_white_blue = "\033[37;44m"     # white on blue
col_yellow_blue = "\033[93;44m"    # yellow on blue
col_yellow_red = "\033[93;41m"     # yellow on red
col_yellow = "\033[0;93m"          # yellow on standard background
col_standard = "\033[0m"           # back to standard

# ** Functions *************************************************


# ** Main ******************************************************
# show all colors, runs only when this file is started directly
if __name__ == "__main__":
	print(f"{col_white_blue} col_white_blue  white on blue {col_standard}")
	print(f"{col_yellow_blue} col_yellow_blue yellow on blue {col_standard}")
	print(f"{col_yellow_red} col_yellow_red  yellow on red {col_standard}")
	print(f"{col_yellow} col_yellow      yellow {col_standard}")
	print(f"{col_standard} col_standard    standard {col_standard}")

# ** History ***************************************************
# 1.0 2026-10-14 Initial version
# 1.1 2026-10-14 descriptive color names

# ** END SCRIPT ************************************************
