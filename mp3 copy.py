from tkinter import filedialog
from mp3 import add_pinyin, convert_to_traditional, simplify
from tqdm import tqdm


files = filedialog.askopenfilenames()

for file in tqdm(files):
    try: 
        # convert_to_traditional(file)
        # add_pinyin(file)
        simplify(file)
    except Exception as e:
        print(file)
        print(e)
        continue

