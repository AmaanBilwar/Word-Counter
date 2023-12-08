import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

print("Welcome to word counter:")

print('Choose an option:')
print('1. Type or paste your own text')
print('2. Read from another .txt file')

choice = input('Enter an option: ')

if choice == '1':
    text = input("Enter the text here: ")
    count = len(text.split())
    print(f"The number of words are: {count}")

elif choice == '2':
    filepath = filedialog.askopenfilename(title='Select file', filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
    if filepath:
        try:
            with open(filepath, 'r') as file:
                file_contents = file.read()
                count = len(file_contents.split())
                print(f"The number of words are: {count}")
        except FileNotFoundError:
            print('File not found or path is incorrect')
    else:
        print('No file selected')
