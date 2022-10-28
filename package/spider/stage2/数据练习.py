import requests
from lxml import etree
from bs4 import BeautifulSoup
import json
import re

url = 'http://book.zongheng.com/store/c1/c0/b0/u1/p1/v0/s9/t1/u0/i1/ALL.html'
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }
r=requests.get(url=url,headers=headers).text
tree=etree.HTML(r)
name=tree.xpath('/html/body/div[2]/em/div[1]/div[1]/div[2]/div[2]/div[2]/a[1]')
print(name)
# soup=BeautifulSoup(r,"html.parser")
# result=soup.select("div.bookname>a")
# for i in result:
#     print(i.string,end=" ")

#re_text=re.findall(r'<div class="bookname">.*?target="_blank">(.*?)</a>',r,re.S)
#print(re_text)

#book_name的段落
"""
<div class="bookname">
                            <a href="http://book.zongheng.com/book/893716.html" target="_blank">逆仙狂刀</a>
                        </div>
"""