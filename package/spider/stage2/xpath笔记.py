"""
1 导入库
from lxml import etree

2实例化etree对象
    本地导入：
    r=etree.parse(filepath)
    互联网获取的数据：
    r=etree.HTML("page_text")

3.xpath表达式
-r.xpath('表达式')
    定位：
    -/ 表示从跟节点开始定位
    -// 表示多个层级或者从任意位置开始定位
    -//div[@class="song"]  属性定位
    -//div[@class="song"]/p[3]  索引定位，索引是从1开始
    取文本：
    -//p/text()    获取直系的文本
    -//p//text()   获取p节点下的所有内容
    取属性
    /@attrs  取属性文本
"""
from lxml import etree
import requests

headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }

url="http://huayu.zongheng.com/rank/details.html?rt=8&d=1"

r_text=requests.get(url=url,headers=headers).text.encode('utf-8').decode('utf-8')
r_xpath=etree.HTML(r_text)
#title=r_xpath.xpath('//div[@class="rank_d_list borderB_c_dsh clearfix"]/div[@class="rank_d_book_img fl"]/@title')  取属性值
content=r_xpath.xpath('//div[@class="rank_d_list borderB_c_dsh clearfix"]//div[@class="rank_d_b_info"]/text()')

#print(title)
print(content)

"""
<div class="rank_d_list borderB_c_dsh clearfix" bookname="早安继承者" bookid="821099">
	                    <div class="rank_d_book_img fl" title="早安继承者">
	                        <a href="http://huayu.zongheng.com/book/821099.html" data-sa-d="{&quot;page_module&quot;:&quot;rankPage&quot;,&quot;click_name&quot;:&quot;rankBook&quot;,&quot;rank_type&quot;:&quot;完结榜&quot;,&quot;rank_pos&quot;:&quot;0&quot;,&quot;book_id&quot;:&quot;821099&quot;}" target="_blank"><img src="http://static.zongheng.com/upload/cover/shucheng/44/14194245.jpg" alt="早安继承者"></a>
	                    </div>
	                    <div class="rank_d_book_intro fl">
	                        <div class="rank_d_b_name" title="早安继承者">
	                            <a href="http://huayu.zongheng.com/book/821099.html" data-sa-d="{&quot;page_module&quot;:&quot;rankPage&quot;,&quot;click_name&quot;:&quot;rankBook&quot;,&quot;rank_type&quot;:&quot;完结榜&quot;,&quot;rank_pos&quot;:&quot;0&quot;,&quot;book_id&quot;:&quot;821099&quot;}" target="_blank">早安继承者</a>
	                        </div>
	                        <div class="rank_d_b_cate" title="月儿">
	                            <a href="http://home.zongheng.com/show/userInfo/50720332.html" data-sa-d="{&quot;page_module&quot;:&quot;rankPage&quot;,&quot;click_name&quot;:&quot;rankBook&quot;,&quot;rank_type&quot;:&quot;完结榜&quot;,&quot;rank_pos&quot;:&quot;0&quot;,&quot;book_id&quot;:&quot;821099&quot;}" target="_blank">月儿</a>|<a target="_blank">豪门</a>|<a target="_blank">完结</a>
	                        </div>
	                        <div class="rank_d_b_info">一次危险驾驶，林小米悲催的将一个帅哥撞得失去了记忆，而更悲催的是，这帅哥竟然赖在她家里不走了，从那天开始，林小米唯一目标就是轰他！轰他！轰走他！
冷奕煌失去记忆后见到的第一个人就是林小米，她还没长眼的撞了他，人美胸大智商低，不赖上她赖上谁？
可林小米万万想不到，这混蛋竟然吃完就跑。
她发誓，天涯海角也要追杀那个混蛋。
当一整排的劳斯莱斯停在她面前，一大群带枪警卫恭敬的喊她“少奶奶”时，林小米直接被吓傻了。
谁能想到，那个穷光蛋摇身一变竟成了权倾S国的大人物。
他一脸邪魅的将她抵在墙角：“小心肝，你哭什么？”
林小米泣不成声：“呜呜呜，不带这么玩的，我落到你手上，你还不得像我欺负你一样的欺负我呀！”
他珍而重之的吻上她的眼角：“绝对不会。”
可事实证明，混蛋的话从来不可信。</div>
	                        <div class="rank_d_b_last" title="正文_第1943章　唐家小公主最漂亮了">
	                            <a href="http://huayu.zongheng.com/chapter/821099/51055647.html" data-sa-d="{&quot;page_module&quot;:&quot;rankPage&quot;,&quot;click_name&quot;:&quot;rankBook&quot;,&quot;rank_type&quot;:&quot;完结榜&quot;,&quot;rank_pos&quot;:&quot;0&quot;,&quot;book_id&quot;:&quot;821099&quot;}" class="fl" target="_blank"><span class="rank_d_lastchapter">最新章节</span>正文_第1943章　唐家小公主最漂亮了</a>
	                            <span class="rank_d_b_time">03-13 13:01</span>
	                        </div>
	                    </div>
	                    <div class="rank_d_book_manage fr">
	                        <div class="rank_d_b_rank">
	                            <div class="rank_d_icon rank_d_b_num rank_d_b_num1 fr">1</div>
	                            <div class="rank_d_b_ticket"><span></span></div>
	                        </div>
	                        <a href="http://huayu.zongheng.com/toread/821099.html" data-sa-d="{&quot;page_module&quot;:&quot;rankPage&quot;,&quot;click_name&quot;:&quot;rankBook&quot;,&quot;rank_type&quot;:&quot;完结榜&quot;,&quot;rank_pos&quot;:&quot;0&quot;,&quot;book_id&quot;:&quot;821099&quot;}" target="_blank"><span class="rank_d_btn_donate">立即阅读</span></a>
	                        <button type="button" class="rank_d_btn_favor" data-sa-d="{&quot;page_module&quot;:&quot;rankPage&quot;,&quot;click_name&quot;:&quot;rankBook&quot;,&quot;rank_type&quot;:&quot;完结榜&quot;,&quot;rank_pos&quot;:&quot;0&quot;,&quot;book_id&quot;:&quot;821099&quot;}">加入书架</button>
	                        
	                    </div>
	                </div>
"""