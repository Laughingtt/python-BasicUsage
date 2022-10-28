import requests
from lxml import etree
import re
import os
import time
from multiprocessing.dummy import Pool

path="./多线程，多进程/li_video/"
if not os.path.exists(path):
    os.mkdir(path)

headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }

def download_video(dic):
    video_url=dic['url']
    video_path=dic['path']
    video_name=dic['name']
    down_time=time.time()
    video_data=requests.get(url=video_url,headers=headers).content
    with open(video_path,"wb") as f:
        f.write(video_data)
    print(video_name+" 下载完成,用时: %.2f秒"%(time.time()-down_time))

def find_url(url):
    res=requests.get(url=url,headers=headers).text
    tree=etree.HTML(res)
    name=tree.xpath('//div[@class="popularem-ath"]/a/h2/text()')
    detail_url=tree.xpath('//li[@class="popularem clearfix"]/div[@class="popularem-ath"]/a/@href')
    video_lis=[]
    for n,d in zip(name,detail_url):
        video_name=n+".mp4"
        video_path=path+video_name
        detail_url="https://www.pearvideo.com/"+d
        res_detail=requests.get(url=detail_url,headers=headers).text
        video_url=re.findall(r'srcUrl="(.*?)",vdoUrl=',res_detail)[0]
        dic={
            "path":video_path,
            "url":video_url,
            "name":video_name
        }
        video_lis.append(dic)
    pool=Pool(len(video_lis))
    pool.map(download_video,video_lis)
    pool.close()
    pool.join()

    
start_time=time.time()
find_url("https://www.pearvideo.com/popular_31")
end_time=time.time()
print("一共用时 %.2f秒"%(end_time-start_time))

"""
with open("./多线程，多进程/li.html","w",encoding="utf-8") as f:
    f.write(res)
var contId="1625088",liveStatusUrl="liveStatus.jsp",liveSta="",playSta="1",autoPlay=!1,isLiving=!1,isVrVideo=!1,hdflvUrl="",sdflvUrl="",hdUrl="",sdUrl="",ldUrl="",srcUrl="https://video.pearvideo.com/mp4/third/20191121/cont-1625088-11315812-181352-hd.mp4",vdoUrl=srcUrl,skinRes="//www.pearvideo.com/domain/skin",videoCDN="//video.pearvideo.com";

<div class="popularem-ath">
                        <a href="video_1624942" class="popularembd actplay" target="_blank">
                            <h2 class="popularem-title">阿勇pr第186课：实例介绍时间插值</h2>
                            <p class="popularem-abs padshow">介绍了时间插值中的帧采样是多出来的帧按现有的帧来生成，播放速度变慢后会让视频看起来不是很流畅，帧混合是上下两帧用不透明的方式......</p>
                        </a>
                        <div class="vercont-auto">
                            <a href="author_13182825" class="column">阿勇PR</a>
                            <span class="fav" data-id="1624942">71</span>
                        </div>
                    </div>
<li class="popularem clearfix">
                    <div class="popularem-sort padshow">01</div>
                    <a href="video_1624942" class="actplay" target="_blank">
                        <div class="popularem-img" style="background-image: url(https://image.pearvideo.com/cont/20191121/cont-1624942-12205959.jpg);">
                            <div class="cm-duration">04:17</div>
                            </div>
                    </a>
                    <div class="popularem-ath">
                        <a href="video_1624942" class="popularembd actplay" target="_blank">
                            <h2 class="popularem-title">阿勇pr第186课：实例介绍时间插值</h2>
                            <p class="popularem-abs padshow">介绍了时间插值中的帧采样是多出来的帧按现有的帧来生成，播放速度变慢后会让视频看起来不是很流畅，帧混合是上下两帧用不透明的方式......</p>
                        </a>
                        <div class="vercont-auto">
                            <a href="author_13182825" class="column">阿勇PR</a>
                            <span class="fav" data-id="1624942">71</span>
                        </div>
                    </div>
		</li>
"""