#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }

def book_get(url,book_path,chapter_url_head):
    if os.path.exists(book_path):
        os.remove(book_path)

    r_text=requests.get(url=url,headers=headers).text.encode("utf-8").decode("utf-8")

    soup = BeautifulSoup(r_text,"html.parser")

    text=soup.select("div.book-mulu>ul>li>a")
    for a in text:
        chapter_url=a.attrs['href']
        chapter_title=a.string
        chapter_url=chapter_url_head+chapter_url
        chapter_content=requests.get(url=chapter_url,headers=headers).text.encode('utf-8').decode('utf-8')
        soup_content=BeautifulSoup(chapter_content,"html.parser")
        chapter_text=soup_content.find("div",class_="chapter_content") #节点对象
        chapter_text=chapter_text.text    #节点对象
        with open(book_path,"a",encoding="utf-8") as f:
            f.write(chapter_title+":\n"+chapter_text+"\n")
            print(chapter_title+" 下载完成")

chapter_url_head="http://www.shicimingju.com"
sishu_url="http://www.shicimingju.com/bookmark/sidamingzhu.html"         
r_sishu=requests.get(url=sishu_url,headers=headers).text.encode("utf-8").decode("utf-8")
sishu_soup=BeautifulSoup(r_sishu,"html.parser")
sishu_list=sishu_soup.select("div.bookmark-list>ul>li>h3>a")   #抓到了a标签的内容列表

for a in sishu_list:
    sishu_name=a.string    #取出名字
    sishu_name=sishu_name.replace("《","").replace("》","")  #取出特殊符号
    sishu_url=a.attrs['href']  #从a标签中取出url
    sishu_url=chapter_url_head+sishu_url  #完整url
    sishu_path="./数据解析1107/"+sishu_name+".txt"  #完整存储路径
    book_get(sishu_url,sishu_path,chapter_url_head)  
    print(sishu_name+" 下载完成")



#url_list=["http://www.shicimingju.com/book/sanguoyanyi.html","http://www.shicimingju.com/book/shuihuzhuan.html","http://www.shicimingju.com/book/xiyouji.html","http://www.shicimingju.com/book/hongloumeng.html"]
#book_path="./数据解析1107/三国演义.text"     #用list的方式给予url然后抓取text
# for url in url_list:
#     book_name=url.split('/')[-1].split('.')[0]  #取出书的名称
#     book_path="./数据解析1107/"+book_name+".text"  #还原存入的路径
#     book_get(url,book_path,chapter_url_head)    #定义好的函数
#     print(book_name+"下载完成")
# <div class="book-mulu">
#                 <ul>
"""
http://www.shicimingju.com/book/lunyu.html
<div class="bookmark-list">
                    <ul>
                            <li>
                                <h3><a href="/book/lunyu.html">《论语》</a></h3>
                                <div class="line3"></div>
                            </li>
                            <li>
                                <h3><a href="/book/mengzi.html">《孟子》</a></h3>
                                <div class="line3"></div>
                            </li>
                            <li>
                                <h3><a href="/book/daxue.html">《大学》</a></h3>
                                <div class="line3"></div>
                            </li>
                            <li>
                                <h3><a href="/book/zhongyong.html">《中庸》</a></h3>
                                <div class="line3"></div>
                            </li>
                    </ul>

                </div>
#                     <li><a href="/book/sanguoyanyi/1.html">第一回·宴桃园豪杰三结义  斩黄巾英雄首立功</a></li><li><a href="/book/sanguoyanyi/2.html">第二回·张翼德怒鞭督邮    何国舅谋诛宦竖</a></li><li><a href="/book/sanguoyanyi/3.html">第三回·议温明董卓叱丁原  馈金珠李肃说吕布</a></li><li><a href="/book/sanguoyanyi/4.html">第四回·废汉帝陈留践位    谋董贼孟德献刀</a></li><li><a href="/book/sanguoyanyi/5.html">第五回·发矫诏诸镇应曹公  破关兵三英战吕布</a></li><li><a href="/book/sanguoyanyi/6.html">第六回·焚金阙董卓行凶    匿玉玺孙坚背约</a></li><li><a href="/book/sanguoyanyi/7.html">第七回·袁绍磐河战公孙    孙坚跨江击刘表</a></li><li><a href="/book/sanguoyanyi/8.html">第八回·王司徒巧使连环计  董太师大闹凤仪亭</a></li><li><a href="/book/sanguoyanyi/9.html">第九回·除暴凶吕布助司徒  犯长安李傕听贾诩</a></li><li><a href="/book/sanguoyanyi/10.html">第一十回·勤王室马腾举义    报父仇曹操兴师</a></li><li><a href="/book/sanguoyanyi/11.html">第十一回·刘皇叔北海救孔融  吕温侯濮阳破曹操</a></li><li><a href="/book/sanguoyanyi/12.html">第十二回·陶恭祖三让徐州    曹孟德大战吕布</a></li><li><a href="/book/sanguoyanyi/13.html">第十三回·李傕郭汜大交兵  杨奉董承双救驾</a></li><li><a href="/book/sanguoyanyi/14.html">第十四回·曹孟德移驾幸许都  吕奉先乘夜袭徐郡</a></li><li><a href="/book/sanguoyanyi/15.html">第十五回·太史慈酣斗小霸王  孙伯符大战严白虎</a></li><li><a href="/book/sanguoyanyi/16.html">第十六回·吕奉先射戟辕门    曹孟德败师淯水</a></li><li><a href="/book/sanguoyanyi/17.html">第十七回·袁公路大起七军    曹孟德会合三将</a></li><li><a href="/book/sanguoyanyi/18.html">第十八回·贾文和料敌决胜    夏侯惇拔矢啖睛</a></li><li><a href="/book/sanguoyanyi/19.html">第十九回·下邳城曹操鏖兵    白门楼吕布殒命</a></li><li><a href="/book/sanguoyanyi/20.html">第二十回·曹阿瞒许田打围    董国舅内阁受诏</a></li><li><a href="/book/sanguoyanyi/21.html">第二十一回·曹操煮酒论英雄  关公赚城斩车胄</a></li><li><a href="/book/sanguoyanyi/22.html">第二十二回·袁曹各起马步三军  关张共擒王刘二将</a></li><li><a href="/book/sanguoyanyi/23.html">第二十三回·祢正平裸衣骂贼    吉太医下毒遭刑</a></li><li><a href="/book/sanguoyanyi/24.html">第二十四回·国贼行凶杀贵妃    皇叔败走投袁绍</a></li><li><a href="/book/sanguoyanyi/25.html">第二十五回·屯土山关公约三事  救白马曹操解重围</a></li><li><a href="/book/sanguoyanyi/26.html">第二十六回·袁本初败兵折将    关云长挂印封金</a></li><li><a href="/book/sanguoyanyi/27.html">第二十七回·美髯公千里走单骑  汉寿侯五关斩六将</a></li><li><a href="/book/sanguoyanyi/28.html">第二十八回·斩蔡阳兄弟释疑    会古城主臣聚义</a></li><li><a href="/book/sanguoyanyi/29.html">第二十九回·小霸王怒斩于吉    碧眼儿坐领江东</a></li><li><a href="/book/sanguoyanyi/30.html">第三十回·战官渡本初败绩  劫乌巢孟德烧粮</a></li><li><a href="/book/sanguoyanyi/31.html">第三十一回·曹操仓亭破本初    玄德荆州依刘表</a></li><li><a href="/book/sanguoyanyi/32.html">第三十二回·夺冀州袁尚争锋    决漳河许攸献计</a></li><li><a href="/book/sanguoyanyi/33.html">第三十三回·曹丕乘乱纳甄氏    郭嘉遗计定辽东</a></li><li><a href="/book/sanguoyanyi/34.html">第三十四回·蔡夫人隔屏听密语  刘皇叔跃马过檀溪</a></li><li><a href="/book/sanguoyanyi/35.html">第三十五回·玄德南漳逢隐沧    单福新野遇英主</a></li><li><a href="/book/sanguoyanyi/36.html">第三十六回·玄德用计袭樊城    元直走马荐诸葛</a></li><li><a href="/book/sanguoyanyi/37.html">第三十七回·司马徽再荐名士    刘玄德三顾草庐</a></li><li><a href="/book/sanguoyanyi/38.html">第三十八回·定三分隆中决策    战长江孙氏报仇</a></li><li><a href="/book/sanguoyanyi/39.html">第三十九回·荆州城公子三求计  博望坡军师初用兵</a></li><li><a href="/book/sanguoyanyi/40.html">第四十回·蔡夫人议献荆州    诸葛亮火烧新野</a></li><li><a href="/book/sanguoyanyi/41.html">第四十一回·刘玄德携民渡江    赵子龙单骑救主</a></li><li><a href="/book/sanguoyanyi/42.html">第四十二回·张翼德大闹长坂桥  刘豫州败走汉津口</a></li><li><a href="/book/sanguoyanyi/43.html">第四十三回·诸葛亮舌战群儒    鲁子敬力排众议</a></li><li><a href="/book/sanguoyanyi/44.html">第四十四回·孔明用智激周瑜    孙权决计破曹操</a></li><li><a href="/book/sanguoyanyi/45.html">第四十五回·三江口曹操折兵    群英会蒋干中计</a></li><li><a href="/book/sanguoyanyi/46.html">第四十六回·用奇谋孔明借箭    献密计黄盖受刑</a></li><li><a href="/book/sanguoyanyi/47.html">第四十七回·阚泽密献诈降书    庞统巧授连环计</a></li><li><a href="/book/sanguoyanyi/48.html">第四十八回·宴长江曹操赋诗    锁战船北军用武</a></li><li><a href="/book/sanguoyanyi/49.html">第四十九回·七星坛诸葛祭风    三江口周瑜纵火</a></li><li><a href="/book/sanguoyanyi/50.html">第五十回·诸葛亮智算华容    关云长义释曹操</a></li><li><a href="/book/sanguoyanyi/51.html">第五十一回·曹仁大战东吴兵    孔明一气周公瑾</a></li><li><a href="/book/sanguoyanyi/52.html">第五十二回·诸葛亮智辞鲁肃    赵子龙计取桂阳</a></li><li><a href="/book/sanguoyanyi/53.html">第五十三回·关云长义释黄汉升  孙仲谋大战张文远</a></li><li><a href="/book/sanguoyanyi/54.html">第五十四回·吴国太佛寺看新郎  刘皇叔洞房续佳偶</a></li><li><a href="/book/sanguoyanyi/55.html">第五十五回·玄德智激孙夫人    孔明二气周公瑾</a></li><li><a href="/book/sanguoyanyi/56.html">第五十六回·曹操大宴铜雀台    孔明三气周公瑾</a></li><li><a href="/book/sanguoyanyi/57.html">第五十七回·柴桑口卧龙吊丧    耒阳县凤雏理事</a></li><li><a href="/book/sanguoyanyi/58.html">第五十八回·马孟起兴兵雪恨    曹阿瞒割须弃袍</a></li><li><a href="/book/sanguoyanyi/59.html">第五十九回·许诸裸衣斗马超    曹操抹书问韩遂</a></li><li><a href="/book/sanguoyanyi/60.html">第六十回·张永年反难杨修    庞士元议取西蜀</a></li><li><a href="/book/sanguoyanyi/61.html">第六十一回·赵云截江夺阿斗    孙权遗书退老瞒</a></li><li><a href="/book/sanguoyanyi/62.html">第六十二回·取涪关杨高授首    攻雒城黄魏争功</a></li><li><a href="/book/sanguoyanyi/63.html">第六十三回·诸葛亮痛哭庞统    张翼德义释严颜</a></li><li><a href="/book/sanguoyanyi/64.html">第六十四回·孔明定计捉张任    杨阜借兵破马超</a></li><li><a href="/book/sanguoyanyi/65.html">第六十五回·马超大战葭萌关    刘备自领益州牧</a></li><li><a href="/book/sanguoyanyi/66.html">第六十六回·关云长单刀赴会    伏皇后为国捐生</a></li><li><a href="/book/sanguoyanyi/67.html">第六十七回·曹操平定汉中地    张辽威震逍遥津</a></li><li><a href="/book/sanguoyanyi/68.html">第六十八回·甘宁百骑劫魏营    左慈掷杯戏曹操</a></li><li><a href="/book/sanguoyanyi/69.html">第六十九回·卜周易管辂知机    讨汉贼五臣死节</a></li><li><a href="/book/sanguoyanyi/70.html">第七十回·猛张飞智取瓦口隘  老黄忠计夺天荡山</a></li><li><a href="/book/sanguoyanyi/71.html">第七十一回·占对山黄忠逸待劳  据汉水赵云寡胜众</a></li><li><a href="/book/sanguoyanyi/72.html">第七十二回·诸葛亮智取汉中    曹阿瞒兵退斜谷</a></li><li><a href="/book/sanguoyanyi/73.html">第七十三回·玄德进位汉中王    云长攻拔襄阳郡</a></li><li><a href="/book/sanguoyanyi/74.html">第七十四回·庞令明抬榇决死战  关云长放水淹七军</a></li><li><a href="/book/sanguoyanyi/75.html">第七十五回·关云长刮骨疗毒    吕子明白衣渡江</a></li><li><a href="/book/sanguoyanyi/76.html">第七十六回·徐公明大战沔水    关云长败走麦城</a></li><li><a href="/book/sanguoyanyi/77.html">第七十七回·玉泉山关公显圣    洛阳城曹操感神</a></li><li><a href="/book/sanguoyanyi/78.html">第七十八回·治风疾神医身死    传遗命奸雄数终</a></li><li><a href="/book/sanguoyanyi/79.html">第七十九回·兄逼弟曹植赋诗    侄陷叔刘封伏法</a></li><li><a href="/book/sanguoyanyi/80.html">第八十回·曹丕废帝篡炎刘    汉王正位续大统</a></li><li><a href="/book/sanguoyanyi/81.html">第八十一回·急兄仇张飞遇害    雪弟恨先主兴兵</a></li><li><a href="/book/sanguoyanyi/82.html">第八十二回·孙权降魏受九锡    先主征吴赏六军</a></li><li><a href="/book/sanguoyanyi/83.html">第八十三回·战猇亭先主得仇人  守江口书生拜大将</a></li><li><a href="/book/sanguoyanyi/84.html">第八十四回·陆逊营烧七百里    孔明巧布八阵图</a></li><li><a href="/book/sanguoyanyi/85.html">第八十五回·刘先主遗诏托孤儿  诸葛亮安居平五路</a></li><li><a href="/book/sanguoyanyi/86.html">第八十六回·难张温秦宓逞天辩  破曹丕徐盛用火攻</a></li><li><a href="/book/sanguoyanyi/87.html">第八十七回·征南寇丞相大兴师  抗天兵蛮王初受执</a></li><li><a href="/book/sanguoyanyi/88.html">第八十八回·渡泸水再缚番王    识诈降三擒孟获</a></li><li><a href="/book/sanguoyanyi/89.html">第八十九回·武乡侯四番用计    南蛮王五次遭擒</a></li><li><a href="/book/sanguoyanyi/90.html">第九十回·驱巨善六破蛮兵    烧藤甲七擒孟获</a></li><li><a href="/book/sanguoyanyi/91.html">第九十一回·祭泸水汉相班师    伐中原武侯上表</a></li><li><a href="/book/sanguoyanyi/92.html">第九十二回·赵子龙力斩五将    诸葛亮智取三城</a></li><li><a href="/book/sanguoyanyi/93.html">第九十三回·姜伯约归降孔明    武乡侯骂死王朝</a></li><li><a href="/book/sanguoyanyi/94.html">第九十四回·诸葛亮乘雪破羌兵  司马懿克日擒孟达</a></li><li><a href="/book/sanguoyanyi/95.html">第九十五回·马谡拒谏失街亭    武侯弹琴退仲达</a></li><li><a href="/book/sanguoyanyi/96.html">第九十六回·孔明挥泪斩马谡    周鲂断发赚曹休</a></li><li><a href="/book/sanguoyanyi/97.html">第九十七回·讨魏国武侯再上表  破曹兵姜维诈献书</a></li><li><a href="/book/sanguoyanyi/98.html">第九十八回·追汉军王双受诛    袭陈仓武侯取胜</a></li><li><a href="/book/sanguoyanyi/99.html">第九十九回·诸葛亮大破魏兵    司马懿入寇西蜀</a></li><li><a href="/book/sanguoyanyi/100.html">第一百回·汉兵劫寨破曹真    武侯斗阵辱仲达</a></li><li><a href="/book/sanguoyanyi/101.html">第一百十一回·出陇上诸葛妆神    奔剑阁张郃中计</a></li><li><a href="/book/sanguoyanyi/102.html">第一百十二回·司马懿占北原渭桥  诸葛亮造木牛流马</a></li><li><a href="/book/sanguoyanyi/103.html">第一百十三回·上方谷司马受困    五丈原诸葛禳星</a></li><li><a href="/book/sanguoyanyi/104.html">第一百十四回·陨大星汉丞相归天  见木像魏都督丧胆</a></li><li><a href="/book/sanguoyanyi/105.html">第一百十五回·武侯预伏锦囊计    魏主拆取承露盘</a></li><li><a href="/book/sanguoyanyi/106.html">第一百十六回·公孙渊兵败死襄平  司马懿诈病赚曹爽</a></li><li><a href="/book/sanguoyanyi/107.html">第一百十七回·魏主政归司马氏    姜维兵败牛头山</a></li><li><a href="/book/sanguoyanyi/108.html">第一百十八回·丁奉雪中奋短兵    孙峻席间施密计</a></li><li><a href="/book/sanguoyanyi/109.html">第一百十九回·困司马汉将奇谋    废曹芳魏家果报</a></li><li><a href="/book/sanguoyanyi/110.html">第一百一十回·文鸯单骑退雄兵    姜维背水破大敌</a></li><li><a href="/book/sanguoyanyi/111.html">第一百一十一回·邓士载智败姜伯约  诸葛诞义讨司马昭</a></li><li><a href="/book/sanguoyanyi/112.html">第一百一十二回·救寿春于诠死节    取长城伯约鏖兵</a></li><li><a href="/book/sanguoyanyi/113.html">第一百一十三回·丁奉定计斩孙綝    姜维斗阵破邓艾</a></li><li><a href="/book/sanguoyanyi/114.html">第一百一十四回·曹髦驱车死南阙    姜维弃粮胜魏兵</a></li><li><a href="/book/sanguoyanyi/115.html">第一百一十五回·诏班师后主信谗    托屯田姜维避祸</a></li><li><a href="/book/sanguoyanyi/116.html">第一百一十六回·钟会分兵汉中道    武侯显圣定军山</a></li><li><a href="/book/sanguoyanyi/117.html">第一百一十七回·邓士载偷度阴平    诸葛瞻战死绵竹</a></li><li><a href="/book/sanguoyanyi/118.html">第一百一十八回·哭祖庙一王死孝    入西川二士争功</a></li><li><a href="/book/sanguoyanyi/119.html">第一百一十九回·假投降巧计成虚话  再受禅依样画葫芦</a></li><li><a href="/book/sanguoyanyi/120.html">第一百二十回·荐杜预老将献新谋  降孙皓三分归一统</a></li>
#                 </ul>
#             </div>
"""