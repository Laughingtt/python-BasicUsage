#coding=utf-8
import requests
from lxml import etree
import json
import os

filepath="C:\\Users\\TianJian\\Desktop\\python\\数据解析1107\\music\\"
# for tu_file in os.listdir(filepath):    #删除文件夹内的文件
#     os.remove(filepath+str(tu_file))
if not os.path.exists(filepath):
    os.mkdir(filepath)

url="http://music.taihe.com/top/dayhot"
base_url="http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&songid="
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }
r=requests.get(url=url,headers=headers).content.decode()

f_etree=etree.HTML(r)
music_name=f_etree.xpath('//div[@class="song-item"]/span[@class="song-title "]/a[contains(@href,"/song/")]/text()')
music_id=f_etree.xpath('//li/div[@class="song-item"]/span[@class="song-title "]/a[contains(@href,"/song/")]/@href')
#print(len(music_id))

for id,name in zip(music_id,music_name):
    second_url=base_url+id.split('/')[-1]
    #print(second_url,name)
    sec_r=requests.get(url=second_url,headers=headers).text
    sec_etree=etree.HTML(sec_r)
    three_url=sec_etree.xpath('//body//text()')[0]
    three_u=json.loads(three_url)
    three_ur=three_u['bitrate']['show_link']
    three_r=requests.get(url=three_ur,headers=headers).content
    if '/' in name:
        name=name.replace('/','')
    downloadpath=filepath+name+".mp3"
    with open(downloadpath,'wb') as f:
        f.write(three_r)
        print(name+" 下载完成")

"""
http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&songid=242078437
http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&callback=jQuery1720539299930388321_1573571577655&songid=265715650&from=web&_=1573571580444
<div class="song-item"><span class="index-num index-hook" style="width: 30px;">2</span><span class="status" style="width:30px;"><i class="fair"></i></span><span class="songlist-album-cover"><a href="/album/670254951" target="_self" title="我和我的祖国"><img src="http://qukufile2.qianqian.com/data2/pic/a9d6f5be2f2ec036f8033a415873b80c/670254991/670254991.jpg@s_2,w_90,h_90" width="41" height="41"></a></span><!-- 设置截断长度，考虑到有热门歌曲后会跟一个hot标签，需要做相应处理 --><span class="fun-icon"><a class="icon-lossless" title="无损资源" target="_blank" href="javascript:;"></a>
    

    
            
    <!-- yuting添加下架歌曲按钮置灰 -->
                
    <!-- yuting添加下架歌曲按钮置灰  end -->

    
        
        
    
                                                                                                                                    
                                                            
                                                                            <span class="music-icon-hook" data-musicicon="{&quot;id&quot;:&quot;670254953&quot;,&quot;type&quot;:&quot;song&quot;,&quot;iconStr&quot;:&quot; play add download collect&quot;,&quot;moduleName&quot;:&quot;songListIcon&quot;,&quot;searchValue&quot;:null,&quot;yyr_song_id&quot;:0,&quot;pay_type&quot;:&quot;2&quot;,&quot;kr_top&quot;:0,&quot;is_jump&quot;:0,&quot;playFee&quot;:false,&quot;albumId&quot;:&quot;670254951&quot;,&quot;siPresaleFlag&quot;:null,&quot;downFee&quot;:true,&quot;songPic&quot;:null,&quot;songTitle&quot;:&quot;\u6211\u548c\u6211\u7684\u7956\u56fd&quot;,&quot;songPublishTime&quot;:null}">
                                        
                                                        
                                                                        
                            <a class="list-micon icon-play" data-action="play" title="播放我和我的祖国" href="javascript:;" c-tj="{&quot;page&quot;:&quot;search_detail&quot;,&quot;pos&quot;:&quot;list_song&quot;,&quot;sub&quot;:&quot;down_to_phone&quot;}"></a>
                                                                                                                        
                                                        
                                                                        
                            <a class="list-micon icon-add" data-action="add" title="添加我和我的祖国" href="javascript:;" c-tj="{&quot;page&quot;:&quot;search_detail&quot;,&quot;pos&quot;:&quot;list_song&quot;,&quot;sub&quot;:&quot;down_to_phone&quot;}"></a>
                                                                                                                        
                                                        
                                                                        <a c-tj="{&quot;page&quot;:&quot;search_detail&quot;,&quot;pos&quot;:&quot;list_song&quot;,&quot;sub&quot;:&quot;down&quot;}" class="list-micon icon-download song-down-vip" data-action="download" title="下载我和我的祖国" href="javascript:;"></a>
                                                                                            
                                                        
                                                                        
                            <a class="list-micon icon-collect" data-action="collect" title="收藏我和我的祖国" href="javascript:;" c-tj="{&quot;page&quot;:&quot;search_detail&quot;,&quot;pos&quot;:&quot;list_song&quot;,&quot;sub&quot;:&quot;down_to_phone&quot;}"></a>
                                                                                                                                    </span></span><span class="song-title " style="width: 240px;"><a href="/song/670254953" target="_blank" title="尹相杰,谢东我和我的祖国" data-film="null" c-tj="{&quot;page&quot;:&quot;songlist_detail&quot;,&quot;pos&quot;:&quot;list&quot;,&quot;sub&quot;:&quot;song&quot;}">我和我的祖国</a></span><span class="singer" style="width: 240px;">							<span class="author_list" title="尹相杰,谢东">
																<a hidefocus="true" href="/artist/1465">尹相杰</a><span class="artist-line">/</span><a hidefocus="true" href="/artist/1523">谢东</a>        	</span>
</span></div>
<span class="song-title " style="width: 240px;"><a href="/song/670254953" target="_blank" title="尹相杰,谢东我和我的祖国" data-film="null" c-tj="{&quot;page&quot;:&quot;songlist_detail&quot;,&quot;pos&quot;:&quot;list&quot;,&quot;sub&quot;:&quot;song&quot;}">我和我的祖国</a></span>
"""