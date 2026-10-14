#!/usr/bin/env python3
# **************************************************************
# File      : dft_gui.py
# Version   : 1.1
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
PADDING = 5                # space in pixels around each control

# ** Functions *************************************************
# main() - creates the window with its controls and waits for the user
# the controls are placed in a grid, row and column start at 0
def main():
	window = tk.Tk()
	window.title(WINDOW_TITLE)
	window.geometry(WINDOW_SIZE)

	# what to calculate, one radio button per choice, they share the variable calculate_choice
	tk.Label(window, text='Vad vill du räkna ut?').grid(row=0, column=0, columnspan=3, sticky='w', padx=PADDING, pady=PADDING)
	calculate_choice = tk.StringVar(value='1')
	tk.Radiobutton(window, text='Distans', variable=calculate_choice, value='1').grid(row=1, column=0, sticky='w', padx=PADDING)
	tk.Radiobutton(window, text='Fart', variable=calculate_choice, value='2').grid(row=1, column=1, sticky='w', padx=PADDING)
	tk.Radiobutton(window, text='Tid', variable=calculate_choice, value='3').grid(row=1, column=2, sticky='w', padx=PADDING)

	# input fields, a label to the left and the field to the right
	tk.Label(window, text='Distans, nm:').grid(row=2, column=0, sticky='w', padx=PADDING, pady=PADDING)
	distance_entry = tk.Entry(window, width=10)
	distance_entry.grid(row=2, column=1, sticky='w', padx=PADDING)

	tk.Label(window, text='Fart, knop:').grid(row=3, column=0, sticky='w', padx=PADDING, pady=PADDING)
	speed_entry = tk.Entry(window, width=10)
	speed_entry.grid(row=3, column=1, sticky='w', padx=PADDING)

	tk.Label(window, text='Tid, timmar:').grid(row=4, column=0, sticky='w', padx=PADDING, pady=PADDING)
	hours_entry = tk.Entry(window, width=10)
	hours_entry.grid(row=4, column=1, sticky='w', padx=PADDING)

	tk.Label(window, text='Tid, minuter:').grid(row=5, column=0, sticky='w', padx=PADDING, pady=PADDING)
	minutes_entry = tk.Entry(window, width=10)
	minutes_entry.grid(row=5, column=1, sticky='w', padx=PADDING)

	# the button does nothing yet, command= is added in step 3
	tk.Button(window, text='Räkna ut').grid(row=6, column=0, sticky='w', padx=PADDING, pady=PADDING)

	# the answer is shown here, empty until something is calculated
	result_label = tk.Label(window, text='')
	result_label.grid(row=7, column=0, columnspan=3, sticky='w', padx=PADDING, pady=PADDING)

	# mainloop() shows the window and runs until it is closed
	window.mainloop()


# ** Main ******************************************************
# run main() only when the script is started, not when it is imported
if __name__ == "__main__":
	main()

# ** History ***************************************************
# 1.0 2026-10-14 Initial version, empty window
# 1.1 2026-10-14 controls: radio buttons, input fields, button and result, no function yet

# ** END SCRIPT ************************************************
