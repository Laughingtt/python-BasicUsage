#coding=utf-8
import requests
import json

dou_url="https://movie.douban.com/j/chart/top_list"
params={
    "type": "25", #5动作 #11剧情 24喜剧 20恐怖 10悬疑 19惊悚
    "interval_id": "100:90",
    "action": "",
    "start": "0", #从第几部电影去取
    "limit": "1000" #一次取多少部电影
}
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
}
response=requests.get(url=dou_url,params=params,headers=headers)
for i in response.json():
    if float(i['score']) >= 9:
        print(i['title']+" : "+str(i['score']))
        

# with open("./douban.json","w",encoding="utf-8") as f:
#     json.dump(response.json(),f,ensure_ascii=False)  #ensure_ascii 默认为True,会将中文进行ascii编码，写为False会显示中文

