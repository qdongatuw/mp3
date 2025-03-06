from tkinter import filedialog
from mp3 import add_pinyin, convert_to_traditional, simplify, png2jpg
from tqdm import tqdm


files = filedialog.askopenfilenames()

for file in tqdm(files):
    try: 
        # convert_to_traditional(file)
        # add_pinyin(file)
        # simplify(file)
        png2jpg(file)
    except Exception as e:
        print(e)
        continue

