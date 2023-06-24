import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

from urllib.parse import urljoin



def download_image(keyword, save_path):
    # 编码关键字
    encoded_keyword = quote(keyword, safe='')
    
    # 构建Google图片搜索的URL
    search_url = f"https://www.google.com/search?q={encoded_keyword}&tbm=isch"
    
    # 发送请求获取网页内容
    response = requests.get(search_url)
    response.raise_for_status()
    
    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    

    # 找到第一个图片结果的URL
    image_relative_url = soup.find('img')['src']
    image_url = urljoin(search_url, image_relative_url)
    
    # 发送请求下载图片
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    
    # 保存图片到本地文件
    with open(save_path, 'wb') as f:
        f.write(image_response.content)
    
    print("图片下载完成！")

# 调用示例
keyword = "cat"  # 搜索关键字
save_path = "cat.jpg"  # 图片保存路径
download_image(keyword, save_path)