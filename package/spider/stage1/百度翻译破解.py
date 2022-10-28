
import requests
import json

post_url="https://fanyi.baidu.com/sug"
words=input("please input words:")
#words=words.encode("utf-8").decode('unicode_escape')
#print(words)
params={"kw":words}
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}

r=requests.post(url=post_url,params=params,headers=headers)
# p=json.loads(r.text)
# print(p)
# for k,v in p.items():
#     print("word:"+k)
#     print("translation:"+str(v))

j=r.json() #只有网页数据是json文件，才可以使用这种方法
print(j['data'][0]['v'])
# for i in j['data']:
#     for value in i.values():
#         print(value)

filename=words+".json"
with open("./requests_1028/"+filename,"w",encoding="utf-8") as f:
    json.dump(j,f,ensure_ascii=False)

print("over")