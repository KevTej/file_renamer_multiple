import tkinter as tk
from tkinter import filedialog
import os
import time

print('Please select the folder where the files are located.\n')
time.sleep(2)

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()

file_list = os.listdir(file_path)

decision = input("Would you like all the files to share the same name and be numbered in a LIST?\nOr would you like to FIND and REPLACE a term in all files?\n")
decision = decision.upper()

num = 1

if decision == 'LIST' or decision == 'NUMBERED' or decision == 'NUMBER':
	listname = input("What will be the name of these files?\n")
	for i in file_list:
		metric_name = str(i)
		imperial_name = listname + " " + str(num) + ".txt"
		# I'm trying to replace the file name each time, using an f-string
		# imperial = open(f"C:\\Users\\KevTe\\OneDrive\\Desktop\\BUTT\\{file_name}.txt", "a+")
		os.rename(f"{file_path}/{metric_name}", f"{file_path}/{imperial_name}")
		num += 1

if decision == 'REPLACE' or decision == 'FIND' or decision == 'FIND AND REPLACE' or decision == 'TERM' or decision == 'REPLACE TERM' or decision == 'FIND TERM' or decision == 'FIND AND REPLACE TERM':
	old_word = input('Which word would you like to replace?\n')
	new_word = input("What will take its place?\n")

	for i in file_list:
		old_file_name = str(i)
		if old_word in old_file_name:
			new_file_name = old_file_name.replace(old_word, new_word)
			os.rename(f"{file_path}/{old_file_name}", f"{file_path}/{new_file_name}")