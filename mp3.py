import music_tag
from xpinyin import Pinyin
from hanziconv import HanziConv
from PIL import Image
import io


def to_pinyi(s):
    p = Pinyin()
    py = p.get_pinyin(s, ' ').title()
    # return p.get_pinyin(s, ' ').title()
    return f'{py} {s}'

def to_traditional(s):
    return(HanziConv.toTraditional(s))


def add_pinyin(mp3_path):
    mp3 = music_tag.load_file(mp3_path)
    mp3['artist'] = to_pinyi(mp3['artist'].value)
    mp3.save()


def simplify(mp3_path):
    mp3 = music_tag.load_file(mp3_path)
    original_artist = mp3['artist'].value.strip()
    lenth = len(original_artist)
    head = original_artist[:int(lenth/2)]
    tail = original_artist[-int(lenth/2):]

    if head.lower() == tail.lower():
        mp3['artist'] = tail
        mp3.save()


def add_artwork(mp3_path):
    pass


def convert_to_traditional(mp3_path):
    mp3 = music_tag.load_file(mp3_path)
    mp3['artist'] = to_traditional(mp3['artist'].value)
    mp3['album'] = to_traditional(mp3['album'].value)
    mp3['title'] = to_traditional(mp3['title'].value)
    mp3.save()


def png2jpg(mp3_path):
    audio = music_tag.load_file(mp3_path)

    # Check if there's an embedded cover image
    if 'art' in audio and audio['art']:
        # Extract the image data
        image_data = audio['art'][0].data

        # Convert PNG to JPEG if necessary
        image = Image.open(io.BytesIO(image_data))
        if image.format == "PNG":
            jpeg_buffer = io.BytesIO()
            image = image.convert("RGB")  # Convert to RGB to ensure compatibility
            image.save(jpeg_buffer, format="JPEG", quality=85)
            jpeg_data = jpeg_buffer.getvalue()

            # Replace the existing cover with the new JPEG format
            audio['art'] = jpeg_data
            audio.save()

if __name__ == '__main__':
    print(to_traditional('测试'))
    print(to_traditional('test 测试'))
    print(to_traditional('测试·新的测试'))
    print(to_traditional('测test试'))
    print(to_pinyi('测试'))
    print(to_pinyi('test'))