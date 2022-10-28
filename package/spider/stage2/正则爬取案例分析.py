import requests
import json
import re
import os
if not os.path.exists("./数据解析/actor"): #创建文件夹
    os.mkdir('./数据解析/actor/')

#分页循环遍历
#url=https://movie.douban.com/subject/%d/27119724/
#for i in range(1,10)
#new_url=url%i
url="https://movie.douban.com/subject/27119724/"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
}
r_text=requests.get(url=url,headers=headers).text       #提取网页全部内容

re_actor=re.findall(r'<div class=\"avatar\" style=\"background-image: url\((.*?)\)',r_text) #正则过滤出图片并生成列表

for actor in re_actor:     #遍历
    actor_f=requests.get(url=actor,headers=headers).content #二进制访问图片
    actor_name=actor.split('/')[-1]        #分割
    actor_path="./数据解析/actor/"+actor_name  #编辑图片名称
    with open(actor_path,"wb") as f:     #二进制存储
        f.write(actor_f)          
        print(actor_name+"finished") 