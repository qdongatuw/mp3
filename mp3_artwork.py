import music_tag
from tkinter import filedialog


img = r"C:\Users\dongq\OneDrive\桌面\Mason_music.jpeg"

files = filedialog.askopenfilenames()
for file in files:
    mp3 = music_tag.load_file(file)
    
    with open(img, 'rb') as img_in:
        mp3['artwork'] = img_in.read()
    #with open('music_tag/test/sample/imgB.jpg', 'rb') as img_in:
     #   mp3.append_tag('artwork', img_in.read())

    mp3.save()
