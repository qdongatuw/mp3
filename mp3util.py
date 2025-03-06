import music_tag
from xpinyin import Pinyin
from hanziconv import HanziConv
from PIL import Image
import io


def to_pinyi(s):
    p = Pinyin()
    if s and '\u4e00' <= s[0] <= '\u9fff':
        py = p.get_pinyin(s, ' ').title()
        return f'{py} {s}'
    return s


def to_traditional(s):
    return(HanziConv.toTraditional(s))


class Mp3Util:
    def __init__(self, mp3_path):
        self.mp3 = music_tag.load_file(mp3_path)
    
    def convert_to_traditional(self):
        self.mp3['artist'] = to_traditional(self.mp3['artist'].value)
        self.mp3['album'] = to_traditional(self.mp3['album'].value)
        self.mp3['title'] = to_traditional(self.mp3['title'].value)

    def add_pinyin(self):
        self.mp3['artist'] = to_pinyi(self.mp3['artist'].value)
    
    def png2jpg(self):
        # Check if there's an embedded cover image
        if 'artwork' in self.mp3 and self.mp3['artwork']:
            # Extract the image data
            image_data = self.mp3['artwork'].value

            # Convert PNG to JPEG if necessary
            image = Image.open(io.BytesIO(image_data.data))
            if image.format == "PNG":
                jpeg_buffer = io.BytesIO()
                image = image.convert("RGB")  # Convert to RGB to ensure compatibility
                image.save(jpeg_buffer, format="JPEG", quality=85)
                jpeg_data = jpeg_buffer.getvalue()

                # Replace the existing cover with the new JPEG format
                self.mp3['artwork'] = jpeg_data

    def save(self):
        self.mp3.save()


if __name__ == '__main__':
    from tkinter import filedialog
    from tqdm import tqdm

    files = filedialog.askopenfilenames()

    for file in tqdm(files):
        try: 
            mp3 = Mp3Util(file)
            mp3.convert_to_traditional()
            mp3.add_pinyin()
            mp3.png2jpg()
            mp3.save()
        except Exception as e:
            tqdm.write(e, file)
            continue