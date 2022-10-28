#coding=utf-8
import requests
from lxml import etree
from bs4 import BeautifulSoup
import sys
import os



filepath="C:\\Users\\TianJian\\Desktop\\python\\数据解析1107\\4k动物图片\\"
# for tu_file in os.listdir(filepath):    #删除文件夹内的文件
#     os.remove(filepath+str(tu_file))
if not os.path.exists(filepath):
    os.mkdir(filepath)


headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }
    
for i in range(2,10):
    #url="http://pic.netbian.com/4kmeinv/index_%d.html"%i #美女
    #url="http://pic.netbian.com/4kfengjing/index_%d.html"%i #风景
    url="http://pic.netbian.com/4kdongwu/index_%d.html"%i
    print(url)
#url="http://pic.netbian.com/4kmeinv/"  #http://pic.netbian.com/4kmeinv/index_3.html
    r_text=requests.get(url=url,headers=headers).text.encode("utf-8").decode("utf-")
    #实例化xpth
    r_xpath=etree.HTML(r_text)
    r_url=r_xpath.xpath('//ul[@class="clearfix"]/li/a/img/@src')
    for tu_url in r_url:  
        
        tu_name=tu_url.split('/')[-1]
        downloadpath=filepath+tu_name
        tu_path="http://pic.netbian.com"+tu_url
        #print(tu_name,downloadpath)
        tu_r=requests.get(url=tu_path,headers=headers).content
        with open(downloadpath,"wb") as f:
            f.write(tu_r)
            print(tu_name+"finish")
    


# soup=BeautifulSoup(r_text,"html.parser")
# r=soup.select("ul.clearfix>li>a")
# print(r)

"""http://pic.netbian.com/uploads/allimg/190824/212516-1566653116f355.jpg
http://pic.netbian.com/4kmeinv/ 
<img src="/uploads/allimg/190808/224411-15652754519901.jpg" alt="居家内衣美女模特晓晓4k壁纸">
http://pic.netbian.com/4kmeinv/index_1.html
http://pic.netbian.com/4kmeinv/index_3.html
<a href="/tupian/17781.html" target="_blank"><img src="/uploads/allimg/180128/112234-1517109754fad1.jpg" alt="糖果 美女模特4k壁纸"><b>糖果 美女模特4k壁纸</b></a>
"""