#coding=utf-8
import requests
import json

hua_url="http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList"
hua2_url="http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
}
res_list=[]

def hua2(use_id):
    hua2_url="http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById"
    params={
        "id": use_id
    }

    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }

    res=requests.post(url=hua2_url,params=params,headers=headers)
    return res.json()
    
for page in range(1,6):
    page=str(page)

    params={
        "on": "true",
        "page": page,
        "pageSize": "15",
        "productName":"", 
        "conditionType": "1",
        "applyname":"", 
        "applysn":"" 
    }

    res=requests.post(url=hua_url,params=params,headers=headers)
    r=json.loads(res.text)  #等价于 res.json()  json格式一定要加载为python格式，才可以当作字典去使用
# with open("./huazhuang.json","w",encoding="utf-8") as f:
#     f.write(res.text)



    for i in r['list']:
        for m,n in i.items():
            if m=="ID":
                result=hua2(n)
                res_list.append(result)
                print(n,end=" ")
            if m=="EPS_NAME":
                print(n)
with open("./huainfo.json","w",encoding="utf-8") as fp:
    json.dump(res_list,fp,ensure_ascii=False)
#print(r["list"])
#http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById
#http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById
