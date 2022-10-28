#coding=utf-8

import os
import re
import json
import requests
from lxml import etree
from bs4 import BeautifulSoup

filepath="C:\\Users\\TianJian\\Desktop\\python\\数据解析1107\\top_music\\"  #定义存储路径

if not os.path.exists(filepath):   #创建路径
    os.mkdir(filepath)

headers={          #定义headers
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }

def down_song(song_url,song_path,name,headers):   #获得song_url后，下载歌曲
    song_r=requests.get(url=song_url,headers=headers).content
    with open(song_path,"wb") as f:
        f.write(song_r)
        print(name+" : 下载完成 ")


def down_lyric(lrc_url,lyric_path,name,headers):  #获得lyric_url后，下载歌词
    r=requests.get(url=lrc_url,headers=headers).text
    try:                                              #有些歌曲歌词不存在，需要用try过度
        lyric=json.loads(r)['lrc']['lyric']           #歌词url是一个json格式的文件，我们需要加载才可以使用
        lyric_r=re.sub(r'\[.*\]','',lyric)            #正则取剔除无用的信息
        with open(lyric_path,"w",encoding="utf-8") as f:
            f.write(lyric_r)
            print(name+" : 歌词 下载完成 ")
    except:
        print(name+"的歌词不存在~~~")
        pass

    
#url="http://music.163.com/song/media/outer/url?id=1400256289.mp3"    #外链播放地址
#lrc_url="http://music.163.com/api/song/lyric?id=3932159&lv=1&kv=1&tv=-1"   #外链歌词地址

#url="https://music.163.com/discover/toplist?id=3779629"   #top榜
#url="https://music.163.com/discover/toplist?id=1978921795"  #电音榜
url="https://music.163.com/discover/toplist?id=2250011882"  #抖音榜
song_base_url="http://music.163.com/song/media/outer/url?id="  
lrc_base_url = 'http://music.163.com/api/song/lyric?id='

s = requests.session()
r=s.get(url=url,headers=headers).content        #需要content来提取信息

etree=etree.HTML(r)
title=etree.xpath('//a[contains(@href,"song?")]/text()')[:-3]   #抓取歌名，后三位无用信息，切片拿掉
id=etree.xpath('//ul[@class="f-hide"]/li/a/@href')  #抓取歌id

for name,i in zip(title,id):        #遍历
    song_id=i.split('=')[-1]       #分割，取得id
    song_url=song_base_url+song_id+".mp3"   #歌url加工
    song_path=filepath+name+".mp3"   #歌存储路径加工

    lrc_url=lrc_base_url+song_id+'&lv=1&kv=1&tv=-1'  #词url加工
    lyric_path=filepath+name+".txt"  #词存储路径加工

    down_song(song_url,song_path,name,headers)   #分别调用
    down_lyric(lrc_url,lyric_path,name,headers)

    
    


# import requests

# from bs4 import BeautifulSoup

# import urllib.request

# headers = {   
#     'Referer':'http://music.163.com/',  
#     'Host':'music.163.com',   
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',  
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',  
#             }

# play_url = 'http://music.163.com/playlist?id=2182968685'
# url="https://music.163.com/playlist?id=2983892338"
# s = requests.session()
# response=s.get(url=play_url,headers = headers).content
# print(response)
# s = BeautifulSoup(response,'lxml')
# main = s.find('ul',{'class':'f-hide'})
# print(main)
# for music in main.find_all('a'):
#     print('{} : {}'.format(music.text, music['href']))