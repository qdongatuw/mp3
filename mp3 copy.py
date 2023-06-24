from tkinter import filedialog
from mp3 import add_pinyin, convert_to_traditional


files = filedialog.askopenfilenames()
for file in files:
    add_pinyin(file)
