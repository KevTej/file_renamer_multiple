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
old_word = input('Which word would you like to replace?\n')
new_word = input("What will take its place?\n")

for i in file_list:
	old_file_name = str(i)
	if old_word in old_file_name:
		new_file_name = old_file_name.replace(old_word, new_word)
		os.rename(f"{file_path}/{old_file_name}", f"{file_path}/{new_file_name}")