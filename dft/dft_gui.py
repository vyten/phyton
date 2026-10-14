#!/usr/bin/env python3
# **************************************************************
# File      : dft_gui.py
# Version   : 1.0
# Purpose   : calculate distance, speed or time at sea (Distans Fart Tid) in a window
# Linked to : dft_functions.py
#
# Created by: Urban Björkén
# Date      : 2026-10-14
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************
import tkinter as tk

# ** Variables *************************************************
WINDOW_TITLE = 'D F T - Distans Fart Tid'
WINDOW_SIZE = '400x300'    # width x height in pixels

# ** Functions *************************************************
# main() - creates the window and waits for the user
def main():
	window = tk.Tk()
	window.title(WINDOW_TITLE)
	window.geometry(WINDOW_SIZE)

	# mainloop() shows the window and runs until it is closed
	window.mainloop()


# ** Main ******************************************************
# run main() only when the script is started, not when it is imported
if __name__ == "__main__":
	main()

# ** History ***************************************************
# 1.0 2026-10-14 Initial version, empty window

# ** END SCRIPT ************************************************
