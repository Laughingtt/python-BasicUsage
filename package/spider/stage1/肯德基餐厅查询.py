#coding=utf-8
#阿贾克斯请求：如果url没变，页面发生变化
import requests
import json

ken_url="http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"
params={
    "op":"keyword",
    "cname":"", 
    "pid":"", 
    "keyword": "上海",
    "pageIndex": "1",
    "pageSize": "100"
}
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
}

res=requests.post(url=ken_url,params=params,headers=headers)

print(res.text)

with open("./kendeji.text","w",encoding="utf-8") as f:
    f.write(res.text)