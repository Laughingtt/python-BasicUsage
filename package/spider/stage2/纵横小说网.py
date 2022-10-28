#coding=utf-8
import requests
from bs4 import BeautifulSoup
from lxml import etree
import os
from time import time

t0=time()

headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }


if not os.path.exists("./数据解析1107/book/"):
    os.mkdir("./数据解析1107/book/")


def grap_book(url,book_path):
  if os.path.exists(book_path):
          os.remove(book_path)

  r_text=requests.get(url=url,headers=headers).text.encode("utf-8").decode("utf-8")
  soup=BeautifulSoup(r_text,"html.parser")
  chapter=soup.select("ul.chapter-list>li>a")
  for a in chapter:
      chapter_name=a.string
      chapter_url=a.attrs['href']
      chapter_text=requests.get(url=chapter_url,headers=headers).text.encode("utf-8").decode("utf-8") #爬取对应url的小说内容
      chapter_soup=BeautifulSoup(chapter_text,"html.parser")
      with open(book_path,"a",encoding="utf-8") as f: #章节title
              f.write("\n"+chapter_name+" :\n\n")
      chapter_content=chapter_soup.select("div.content>p")  #小说内容
      for p in chapter_content:
          chapters_content=p.string
          with open(book_path,"a",encoding="utf-8") as f:
              f.write(chapters_content+"\n")
      print(chapter_name+" 下载完成")

def novel(first_url):
    first_r=requests.get(url=first_url,headers=headers).text.encode("utf-8").decode("utf-8")
    first_etree=etree.HTML(first_r)
    second_url_list=first_etree.xpath('//div[@class="bookinfo"]/div[@class="bookname"]/a/@href')
    second_name_list=first_etree.xpath('//div[@class="bookinfo"]/div[@class="bookname"]/a/text()')
    for second_name,second_url in zip(second_name_list,second_url_list):
        print(second_name+" "+second_url)
        second_r=requests.get(url=second_url,headers=headers).text.encode("utf-8").decode("utf-8")
        second_etree=etree.HTML(second_r)
        three_url=second_etree.xpath('//a[@class="all-catalog"]/@href')[0]
        book_path="./数据解析1107/book/%s.txt"%second_name
        t1=time()
        grap_book(three_url,book_path)
        t2=time()
        print("\n\n\n"+second_name+"--------下载完成--------用时：%.2f秒\n\n\n"%(t2-t1))

#first_url="http://book.zongheng.com/store/c0/c0/b0/u1/p1/v0/s9/t1/u0/i1/ALL.html"  #男频
#first_url="http://book.zongheng.com/store/c0/c0/b1/u1/p1/v0/s9/t1/u0/i1/ALL.html"  #女频

first_url="http://book.zongheng.com/store/c1/c0/b0/u1/p1/v0/s9/t1/u0/i1/ALL.html"  #男奇幻玄幻
novel(first_url)
t3=time()
print("\n\n\n总共用时 ：%.2f秒"%(t3-t0))