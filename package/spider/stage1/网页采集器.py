import requests

url="https://www.sogou.com/web?"
kw=input("input keywords :\n")
params={"query":kw}
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}
r=requests.get(url=url,params=params,headers=headers)
print(r.text)
filename=kw+".html"
with open(filename,"w",encoding="utf-8") as f:
    f.write(r.text)