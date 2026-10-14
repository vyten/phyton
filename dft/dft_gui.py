#!/usr/bin/env python3
# **************************************************************
# File      : dft_gui.py
# Version   : 1.3
# Purpose   : calculate distance, speed or time at sea (Distans Fart Tid) in a window
# Linked to : dft_functions.py
#
# Created by: Urban Björkén
# Date      : 2026-10-14
# email     : vyten@starnet.nu
# **************************************************************

# ** Imports ***************************************************
import tkinter as tk
from os import path
import dft_functions
import lang_se

# ** Variables *************************************************
WINDOW_TITLE = 'D F T - Distans Fart Tid'
WINDOW_SIZE = '400x450'    # width x height in pixels
IMAGE_DIR = path.join(path.dirname(path.abspath(__file__)), 'img')

# colors from the PHP version (w3.css)
COL_BACKGROUND = '#616161'    # dark gray, the page
COL_BUTTON = '#607d8b'        # blue gray, choice buttons
COL_HOVER = '#2196F3'         # blue, button under the mouse pointer
COL_CALCULATE = '#4CAF50'     # green, the calculate button
COL_BACK = '#ff5722'          # deep orange, back and quit
COL_TEXT = '#ffffff'          # white
COL_ANSWER = '#ffeb3b'        # yellow, the answer
COL_INPUT = '#bbbbbb'         # gray, input fields

FONT_HEADER = ('Helvetica', 18, 'bold')
FONT_TEXT = ('Helvetica', 12)

# the languages, the number is the same as in dft.py and dft_lang.txt
FLAGS = {
	'1': 'flag_nation_se.png',
	'2': 'flag_nation_en.png',
	'3': 'flag_nation_cz.png',
}

# the fields on each calculation page: (text, unit), in the same order as calculate() reads them
CALCULATIONS = {
	'distance': ('Distans', [('Fart', 'knop'), ('Tid', 'h'), ('', 'min')]),
	'speed': ('Fart', [('Distans', 'nm'), ('Tid', 'h'), ('', 'min')]),
	'time': ('Tid', [('Distans', 'nm'), ('Fart', 'knop')]),
}

# the images must be kept in a variable, otherwise Python throws them away and the buttons become empty
flag_images = {}
small_flag_images = {}

# ** Functions *************************************************
# load_images() - loads the flags, can only be done after tk.Tk() has been created
def load_images():
	for number, file_name in FLAGS.items():
		flag_images[number] = tk.PhotoImage(file=path.join(IMAGE_DIR, file_name))
		small_flag_images[number] = flag_images[number].subsample(2)    # every second pixel, 32 x 32


# clear_page() - removes everything in the window before a new page is shown
def clear_page(window):
	for widget in window.winfo_children():
		widget.destroy()


# make_button() - a button with the colors from the PHP version
def make_button(parent, text, color, command):
	return tk.Button(parent, text=text, command=command, font=FONT_TEXT, width=15,
		bg=color, fg=COL_TEXT, activebackground=COL_HOVER, activeforeground=COL_TEXT,
		relief='flat', cursor='hand2')


# calculate() - reads the fields, calculates and shows the answer
# step 4 adds checks for wrong input, until then a letter or 0 gives a Python error in the terminal
def calculate(calculation, entries, result_label):
	texts = lang_se.TEXTS    # Swedish until the language files are used in step 6
	values = [float(entry.get().replace(',', '.')) for entry in entries]

	if calculation == 'distance':
		speed, hours, minutes = values
		distance = dft_functions.calculate_distance(speed, hours, minutes)
		answer = texts['result_distance'].format(distance=distance)

	elif calculation == 'speed':
		distance, hours, minutes = values
		speed = dft_functions.calculate_speed(distance, hours, minutes)
		answer = texts['result_speed'].format(speed=speed)

	else:
		distance, speed = values
		hours, minutes = dft_functions.calculate_time(distance, speed)
		answer = texts['result_time'].format(hours=hours, minutes=minutes)

	result_label.config(text=answer)


# show_header() - the header at the top of each page
def show_header(window, text):
	tk.Label(window, text=text, font=FONT_HEADER, bg=COL_BACKGROUND, fg=COL_TEXT).pack(pady=15)


# show_flag_page() - page 1, choose language with the flags
def show_flag_page(window):
	clear_page(window)
	show_header(window, ' ')
	for number in FLAGS:
		tk.Button(window, image=flag_images[number], bg=COL_BUTTON, activebackground=COL_HOVER,
			relief='flat', cursor='hand2',
			command=lambda: show_start_page(window)).pack(pady=10)


# show_start_page() - page 2, choose what to calculate
def show_start_page(window):
	clear_page(window)
	show_header(window, 'Beräkna din')
	for calculation, (header, fields) in CALCULATIONS.items():
		make_button(window, header, COL_BUTTON,
			lambda calculation=calculation: show_calculate_page(window, calculation)).pack(pady=10)
	make_button(window, 'Avsluta', COL_BACK, window.destroy).pack(pady=30)


# show_calculate_page() - page 3, the fields for the chosen calculation
def show_calculate_page(window, calculation):
	clear_page(window)
	header, fields = CALCULATIONS[calculation]
	show_header(window, header)

	# the answer is shown here, empty until something is calculated
	result_label = tk.Label(window, text='', font=FONT_TEXT, bg=COL_BACKGROUND, fg=COL_ANSWER)
	result_label.pack()

	# the fields in a grid: text, field and unit on each row
	form = tk.Frame(window, bg=COL_BACKGROUND)
	form.pack(pady=10)
	entries = []    # the fields are saved here so that calculate() can read them
	for row, (text, unit) in enumerate(fields):
		tk.Label(form, text=text, font=FONT_TEXT, bg=COL_BACKGROUND, fg=COL_TEXT).grid(row=row, column=0, sticky='e', padx=5, pady=5)
		entry = tk.Entry(form, width=6, font=FONT_TEXT, bg=COL_INPUT)
		entry.grid(row=row, column=1, padx=5, pady=5)
		entries.append(entry)
		tk.Label(form, text=unit, font=FONT_TEXT, bg=COL_BACKGROUND, fg=COL_TEXT).grid(row=row, column=2, sticky='w', padx=5, pady=5)

	# the cursor starts in the first field, like setFocus() in the PHP version
	entries[0].focus_set()

	make_button(window, 'Beräkna', COL_CALCULATE,
		lambda: calculate(calculation, entries, result_label)).pack(pady=10)
	make_button(window, '« Tillbaka', COL_BACK, lambda: show_start_page(window)).pack(pady=10)

	# small flags to change language, they do nothing yet except show the start page again
	flag_row = tk.Frame(window, bg=COL_BACKGROUND)
	flag_row.pack(pady=10)
	for number in FLAGS:
		tk.Button(flag_row, image=small_flag_images[number], bg=COL_BACKGROUND, activebackground=COL_HOVER,
			relief='flat', cursor='hand2', bd=0,
			command=lambda: show_calculate_page(window, calculation)).pack(side='left', padx=5)


# main() - creates the window, shows the first page and waits for the user
def main():
	window = tk.Tk()
	window.title(WINDOW_TITLE)
	window.geometry(WINDOW_SIZE)
	window.configure(bg=COL_BACKGROUND)

	load_images()
	show_flag_page(window)

	# mainloop() shows the window and runs until it is closed
	window.mainloop()


# ** Main ******************************************************
# run main() only when the script is started, not when it is imported
if __name__ == "__main__":
	main()

# ** History ***************************************************
# 1.0 2026-10-14 Initial version, empty window
# 1.1 2026-10-14 controls: radio buttons, input fields, button and result, no function yet
# 1.2 2026-10-14 three pages like the PHP version: flags, start page and calculation page
# 1.3 2026-10-14 the calculate button calculates with dft_functions.py

# ** END SCRIPT ************************************************
