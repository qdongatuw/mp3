import os
from tkinter import filedialog
import music_tag


files = filedialog.askopenfilenames()
for file in files:
    print(file)
    mp3file = os.path.splitext(file)[0] + '.mp3'

    f = music_tag.load_file(file)
    art = f['artwork']

    f2 = music_tag.load_file(mp3file)
    f2['artwork'] = art
    f2.save()
