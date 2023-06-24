from tkinter import filedialog
from mp3 import add_pinyin, convert_to_traditional


files = filedialog.askopenfilenames()

cnt = len(files)
index = 0
for file in files:
    index += 1
    convert_to_traditional(file)
    print(f'{index}/{cnt}')
