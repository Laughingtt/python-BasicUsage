import requests
import json 
url="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2567198874.webp"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
}
r=requests.get(url=url,headers=headers)
#text (字符串)  content 返回得是二进制图片数据   
with open("./数据解析/xiaochou.jpg","wb") as f: #存储图片的方法，jpg格式，二进制写入，content二进制数据
    f.write(r.content)