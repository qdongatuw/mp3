from tkinter import filedialog
from mp3 import add_pinyin, convert_to_traditional
from tqdm import tqdm


files = filedialog.askopenfilenames()

cnt = len(files)
for file in tqdm(files):
    convert_to_traditional(file)
    add_pinyin(file)

