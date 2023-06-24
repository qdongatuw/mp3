import music_tag
from xpinyin import Pinyin
from hanziconv import HanziConv


def to_pinyi(s):
    p = Pinyin()
    return p.get_pinyin(s, ' ').title() + s

def to_traditional(s):
    return(HanziConv.toTraditional(s))


def add_pinyin(mp3_path):
    mp3 = music_tag.load_file(mp3_path)
    mp3['artist'] = to_pinyi(mp3['artist'].value)
    mp3.save()


def convert_to_traditional(mp3_path):
    mp3 = music_tag.load_file(mp3_path)
    mp3['artist'] = to_traditional(mp3['artist'].value)
    mp3['album'] = to_traditional(mp3['album'].value)
    mp3['title'] = to_traditional(mp3['title'].value)
    mp3.save()


if __name__ == '__main__':
    print(to_traditional('测试'))
    print(to_traditional('test 测试'))
    print(to_traditional('测试·新的测试'))
    print(to_traditional('测test试'))