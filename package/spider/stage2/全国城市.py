#cording=utf-8

import requests
from lxml import etree

headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    }
    
url="https://www.aqistudy.cn/historydata/"

r_text=requests.get(url=url,headers=headers).text
etree=etree.HTML(r_text)  #实例化xpath
hot_city=etree.xpath('//div[@class="hot"]/div[@class="bottom"]/ul/li/a/text()')   #逐一取抓取
normal_city=etree.xpath('//div[@class="all"]/div[@class="bottom"]/ul/div[2]/li/a/text()')  #逐一抓取
lis=[]
lis=hot_city+normal_city #合并

print(lis,len(lis))
all_city=etree.xpath('//div[@class="hot"]/div[@class="bottom"]/ul/li/a/text() | //div[@class="all"]/div[@class="bottom"]/ul/div[2]/li/a/text()') #可以使用bool进行连接
print(all_city,len(all_city))
"""
<div class="hot">
      <div class="top">
        热门城市：
      </div>
      <div class="bottom">
        <ul class="unstyled">
          <li><a href="monthdata.php?city=北京">北京</a></li>
          <li><a href="monthdata.php?city=上海">上海</a></li>
          <li><a href="monthdata.php?city=广州">广州</a></li>
          <li><a href="monthdata.php?city=深圳">深圳</a></li>
          <li><a href="monthdata.php?city=杭州">杭州</a></li>
          <li><a href="monthdata.php?city=天津">天津</a></li>
          <li><a href="monthdata.php?city=成都">成都</a></li>
          <li><a href="monthdata.php?city=南京">南京</a></li>
          <li><a href="monthdata.php?city=西安">西安</a></li>
          <li><a href="monthdata.php?city=武汉">武汉</a></li>
        </ul>
      </div>
    </div>

    <div class="all">
      <div class="top">
        全部城市：
      </div>
      <div class="bottom">
            <ul class="unstyled">
        <div><b>A.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=阿坝州">阿坝州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=安康">安康</a>
          </li>
                    <li>
            <a href="monthdata.php?city=阿克苏地区">阿克苏地区</a>
          </li>
                    <li>
            <a href="monthdata.php?city=阿里地区">阿里地区</a>
          </li>
                    <li>
            <a href="monthdata.php?city=阿拉善盟">阿拉善盟</a>
          </li>
                    <li>
            <a href="monthdata.php?city=阿勒泰地区">阿勒泰地区</a>
          </li>
                    <li>
            <a href="monthdata.php?city=安庆">安庆</a>
          </li>
                    <li>
            <a href="monthdata.php?city=安顺">安顺</a>
          </li>
                    <li>
            <a href="monthdata.php?city=鞍山">鞍山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=克孜勒苏州">克孜勒苏州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=安阳">安阳</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>B.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=蚌埠">蚌埠</a>
          </li>
                    <li>
            <a href="monthdata.php?city=白城">白城</a>
          </li>
                    <li>
            <a href="monthdata.php?city=保定">保定</a>
          </li>
                    <li>
            <a href="monthdata.php?city=北海">北海</a>
          </li>
                    <li>
            <a href="monthdata.php?city=宝鸡">宝鸡</a>
          </li>
                    <li>
            <a href="monthdata.php?city=北京">北京</a>
          </li>
                    <li>
            <a href="monthdata.php?city=毕节">毕节</a>
          </li>
                    <li>
            <a href="monthdata.php?city=博州">博州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=白山">白山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=百色">百色</a>
          </li>
                    <li>
            <a href="monthdata.php?city=保山">保山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=白沙">白沙</a>
          </li>
                    <li>
            <a href="monthdata.php?city=包头">包头</a>
          </li>
                    <li>
            <a href="monthdata.php?city=保亭">保亭</a>
          </li>
                    <li>
            <a href="monthdata.php?city=本溪">本溪</a>
          </li>
                    <li>
            <a href="monthdata.php?city=巴彦淖尔">巴彦淖尔</a>
          </li>
                    <li>
            <a href="monthdata.php?city=白银">白银</a>
          </li>
                    <li>
            <a href="monthdata.php?city=巴中">巴中</a>
          </li>
                    <li>
            <a href="monthdata.php?city=滨州">滨州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=亳州">亳州</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>C.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=长春">长春</a>
          </li>
                    <li>
            <a href="monthdata.php?city=昌都">昌都</a>
          </li>
                    <li>
            <a href="monthdata.php?city=常德">常德</a>
          </li>
                    <li>
            <a href="monthdata.php?city=成都">成都</a>
          </li>
                    <li>
            <a href="monthdata.php?city=承德">承德</a>
          </li>
                    <li>
            <a href="monthdata.php?city=赤峰">赤峰</a>
          </li>
                    <li>
            <a href="monthdata.php?city=昌吉州">昌吉州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=五家渠">五家渠</a>
          </li>
                    <li>
            <a href="monthdata.php?city=昌江">昌江</a>
          </li>
                    <li>
            <a href="monthdata.php?city=澄迈">澄迈</a>
          </li>
                    <li>
            <a href="monthdata.php?city=重庆">重庆</a>
          </li>
                    <li>
            <a href="monthdata.php?city=长沙">长沙</a>
          </li>
                    <li>
            <a href="monthdata.php?city=常熟">常熟</a>
          </li>
                    <li>
            <a href="monthdata.php?city=楚雄州">楚雄州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=朝阳">朝阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=沧州">沧州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=长治">长治</a>
          </li>
                    <li>
            <a href="monthdata.php?city=常州">常州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=潮州">潮州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=郴州">郴州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=池州">池州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=崇左">崇左</a>
          </li>
                    <li>
            <a href="monthdata.php?city=滁州">滁州</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>D.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=定安">定安</a>
          </li>
                    <li>
            <a href="monthdata.php?city=丹东">丹东</a>
          </li>
                    <li>
            <a href="monthdata.php?city=东方">东方</a>
          </li>
                    <li>
            <a href="monthdata.php?city=东莞">东莞</a>
          </li>
                    <li>
            <a href="monthdata.php?city=德宏州">德宏州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=大理州">大理州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=大连">大连</a>
          </li>
                    <li>
            <a href="monthdata.php?city=大庆">大庆</a>
          </li>
                    <li>
            <a href="monthdata.php?city=大同">大同</a>
          </li>
                    <li>
            <a href="monthdata.php?city=定西">定西</a>
          </li>
                    <li>
            <a href="monthdata.php?city=大兴安岭地区">大兴安岭地区</a>
          </li>
                    <li>
            <a href="monthdata.php?city=德阳">德阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=东营">东营</a>
          </li>
                    <li>
            <a href="monthdata.php?city=黔南州">黔南州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=达州">达州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=德州">德州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=儋州">儋州</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>E.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=鄂尔多斯">鄂尔多斯</a>
          </li>
                    <li>
            <a href="monthdata.php?city=恩施州">恩施州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=鄂州">鄂州</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>F.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=防城港">防城港</a>
          </li>
                    <li>
            <a href="monthdata.php?city=佛山">佛山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=抚顺">抚顺</a>
          </li>
                    <li>
            <a href="monthdata.php?city=阜新">阜新</a>
          </li>
                    <li>
            <a href="monthdata.php?city=阜阳">阜阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=富阳">富阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=抚州">抚州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=福州">福州</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>G.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=广安">广安</a>
          </li>
                    <li>
            <a href="monthdata.php?city=贵港">贵港</a>
          </li>
                    <li>
            <a href="monthdata.php?city=桂林">桂林</a>
          </li>
                    <li>
            <a href="monthdata.php?city=果洛州">果洛州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=甘南州">甘南州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=固原">固原</a>
          </li>
                    <li>
            <a href="monthdata.php?city=广元">广元</a>
          </li>
                    <li>
            <a href="monthdata.php?city=贵阳">贵阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=甘孜州">甘孜州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=赣州">赣州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=广州">广州</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>H.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=淮安">淮安</a>
          </li>
                    <li>
            <a href="monthdata.php?city=海北州">海北州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=鹤壁">鹤壁</a>
          </li>
                    <li>
            <a href="monthdata.php?city=淮北">淮北</a>
          </li>
                    <li>
            <a href="monthdata.php?city=河池">河池</a>
          </li>
                    <li>
            <a href="monthdata.php?city=海东地区">海东地区</a>
          </li>
                    <li>
            <a href="monthdata.php?city=邯郸">邯郸</a>
          </li>
                    <li>
            <a href="monthdata.php?city=哈尔滨">哈尔滨</a>
          </li>
                    <li>
            <a href="monthdata.php?city=合肥">合肥</a>
          </li>
                    <li>
            <a href="monthdata.php?city=鹤岗">鹤岗</a>
          </li>
                    <li>
            <a href="monthdata.php?city=黄冈">黄冈</a>
          </li>
                    <li>
            <a href="monthdata.php?city=黑河">黑河</a>
          </li>
                    <li>
            <a href="monthdata.php?city=红河州">红河州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=怀化">怀化</a>
          </li>
                    <li>
            <a href="monthdata.php?city=呼和浩特">呼和浩特</a>
          </li>
                    <li>
            <a href="monthdata.php?city=海口">海口</a>
          </li>
                    <li>
            <a href="monthdata.php?city=呼伦贝尔">呼伦贝尔</a>
          </li>
                    <li>
            <a href="monthdata.php?city=葫芦岛">葫芦岛</a>
          </li>
                    <li>
            <a href="monthdata.php?city=哈密地区">哈密地区</a>
          </li>
                    <li>
            <a href="monthdata.php?city=海门">海门</a>
          </li>
                    <li>
            <a href="monthdata.php?city=海南州">海南州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=淮南">淮南</a>
          </li>
                    <li>
            <a href="monthdata.php?city=黄南州">黄南州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=衡水">衡水</a>
          </li>
                    <li>
            <a href="monthdata.php?city=黄山">黄山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=黄石">黄石</a>
          </li>
                    <li>
            <a href="monthdata.php?city=和田地区">和田地区</a>
          </li>
                    <li>
            <a href="monthdata.php?city=海西州">海西州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=河源">河源</a>
          </li>
                    <li>
            <a href="monthdata.php?city=衡阳">衡阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=汉中">汉中</a>
          </li>
                    <li>
            <a href="monthdata.php?city=杭州">杭州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=菏泽">菏泽</a>
          </li>
                    <li>
            <a href="monthdata.php?city=贺州">贺州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=湖州">湖州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=惠州">惠州</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>J.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=吉安">吉安</a>
          </li>
                    <li>
            <a href="monthdata.php?city=金昌">金昌</a>
          </li>
                    <li>
            <a href="monthdata.php?city=晋城">晋城</a>
          </li>
                    <li>
            <a href="monthdata.php?city=景德镇">景德镇</a>
          </li>
                    <li>
            <a href="monthdata.php?city=金华">金华</a>
          </li>
                    <li>
            <a href="monthdata.php?city=西双版纳州">西双版纳州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=九江">九江</a>
          </li>
                    <li>
            <a href="monthdata.php?city=吉林">吉林</a>
          </li>
                    <li>
            <a href="monthdata.php?city=即墨">即墨</a>
          </li>
                    <li>
            <a href="monthdata.php?city=江门">江门</a>
          </li>
                    <li>
            <a href="monthdata.php?city=荆门">荆门</a>
          </li>
                    <li>
            <a href="monthdata.php?city=佳木斯">佳木斯</a>
          </li>
                    <li>
            <a href="monthdata.php?city=济南">济南</a>
          </li>
                    <li>
            <a href="monthdata.php?city=济宁">济宁</a>
          </li>
                    <li>
            <a href="monthdata.php?city=胶南">胶南</a>
          </li>
                    <li>
            <a href="monthdata.php?city=酒泉">酒泉</a>
          </li>
                    <li>
            <a href="monthdata.php?city=句容">句容</a>
          </li>
                    <li>
            <a href="monthdata.php?city=湘西州">湘西州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=金坛">金坛</a>
          </li>
                    <li>
            <a href="monthdata.php?city=鸡西">鸡西</a>
          </li>
                    <li>
            <a href="monthdata.php?city=嘉兴">嘉兴</a>
          </li>
                    <li>
            <a href="monthdata.php?city=江阴">江阴</a>
          </li>
                    <li>
            <a href="monthdata.php?city=揭阳">揭阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=济源">济源</a>
          </li>
                    <li>
            <a href="monthdata.php?city=嘉峪关">嘉峪关</a>
          </li>
                    <li>
            <a href="monthdata.php?city=胶州">胶州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=焦作">焦作</a>
          </li>
                    <li>
            <a href="monthdata.php?city=锦州">锦州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=晋中">晋中</a>
          </li>
                    <li>
            <a href="monthdata.php?city=荆州">荆州</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>K.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=库尔勒">库尔勒</a>
          </li>
                    <li>
            <a href="monthdata.php?city=开封">开封</a>
          </li>
                    <li>
            <a href="monthdata.php?city=黔东南州">黔东南州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=克拉玛依">克拉玛依</a>
          </li>
                    <li>
            <a href="monthdata.php?city=昆明">昆明</a>
          </li>
                    <li>
            <a href="monthdata.php?city=喀什地区">喀什地区</a>
          </li>
                    <li>
            <a href="monthdata.php?city=昆山">昆山</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>L.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=临安">临安</a>
          </li>
                    <li>
            <a href="monthdata.php?city=六安">六安</a>
          </li>
                    <li>
            <a href="monthdata.php?city=来宾">来宾</a>
          </li>
                    <li>
            <a href="monthdata.php?city=聊城">聊城</a>
          </li>
                    <li>
            <a href="monthdata.php?city=临沧">临沧</a>
          </li>
                    <li>
            <a href="monthdata.php?city=娄底">娄底</a>
          </li>
                    <li>
            <a href="monthdata.php?city=乐东">乐东</a>
          </li>
                    <li>
            <a href="monthdata.php?city=廊坊">廊坊</a>
          </li>
                    <li>
            <a href="monthdata.php?city=临汾">临汾</a>
          </li>
                    <li>
            <a href="monthdata.php?city=临高">临高</a>
          </li>
                    <li>
            <a href="monthdata.php?city=漯河">漯河</a>
          </li>
                    <li>
            <a href="monthdata.php?city=丽江">丽江</a>
          </li>
                    <li>
            <a href="monthdata.php?city=吕梁">吕梁</a>
          </li>
                    <li>
            <a href="monthdata.php?city=陇南">陇南</a>
          </li>
                    <li>
            <a href="monthdata.php?city=六盘水">六盘水</a>
          </li>
                    <li>
            <a href="monthdata.php?city=拉萨">拉萨</a>
          </li>
                    <li>
            <a href="monthdata.php?city=乐山">乐山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=丽水">丽水</a>
          </li>
                    <li>
            <a href="monthdata.php?city=凉山州">凉山州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=陵水">陵水</a>
          </li>
                    <li>
            <a href="monthdata.php?city=莱芜">莱芜</a>
          </li>
                    <li>
            <a href="monthdata.php?city=莱西">莱西</a>
          </li>
                    <li>
            <a href="monthdata.php?city=临夏州">临夏州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=溧阳">溧阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=辽阳">辽阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=辽源">辽源</a>
          </li>
                    <li>
            <a href="monthdata.php?city=临沂">临沂</a>
          </li>
                    <li>
            <a href="monthdata.php?city=龙岩">龙岩</a>
          </li>
                    <li>
            <a href="monthdata.php?city=洛阳">洛阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=连云港">连云港</a>
          </li>
                    <li>
            <a href="monthdata.php?city=莱州">莱州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=兰州">兰州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=林芝">林芝</a>
          </li>
                    <li>
            <a href="monthdata.php?city=柳州">柳州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=泸州">泸州</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>M.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=马鞍山">马鞍山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=牡丹江">牡丹江</a>
          </li>
                    <li>
            <a href="monthdata.php?city=茂名">茂名</a>
          </li>
                    <li>
            <a href="monthdata.php?city=眉山">眉山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=绵阳">绵阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=梅州">梅州</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>N.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=宁波">宁波</a>
          </li>
                    <li>
            <a href="monthdata.php?city=南昌">南昌</a>
          </li>
                    <li>
            <a href="monthdata.php?city=南充">南充</a>
          </li>
                    <li>
            <a href="monthdata.php?city=宁德">宁德</a>
          </li>
                    <li>
            <a href="monthdata.php?city=内江">内江</a>
          </li>
                    <li>
            <a href="monthdata.php?city=南京">南京</a>
          </li>
                    <li>
            <a href="monthdata.php?city=怒江州">怒江州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=南宁">南宁</a>
          </li>
                    <li>
            <a href="monthdata.php?city=南平">南平</a>
          </li>
                    <li>
            <a href="monthdata.php?city=那曲地区">那曲地区</a>
          </li>
                    <li>
            <a href="monthdata.php?city=南通">南通</a>
          </li>
                    <li>
            <a href="monthdata.php?city=南阳">南阳</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>P.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=平度">平度</a>
          </li>
                    <li>
            <a href="monthdata.php?city=平顶山">平顶山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=普洱">普洱</a>
          </li>
                    <li>
            <a href="monthdata.php?city=盘锦">盘锦</a>
          </li>
                    <li>
            <a href="monthdata.php?city=蓬莱">蓬莱</a>
          </li>
                    <li>
            <a href="monthdata.php?city=平凉">平凉</a>
          </li>
                    <li>
            <a href="monthdata.php?city=莆田">莆田</a>
          </li>
                    <li>
            <a href="monthdata.php?city=萍乡">萍乡</a>
          </li>
                    <li>
            <a href="monthdata.php?city=濮阳">濮阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=攀枝花">攀枝花</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>Q.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=青岛">青岛</a>
          </li>
                    <li>
            <a href="monthdata.php?city=琼海">琼海</a>
          </li>
                    <li>
            <a href="monthdata.php?city=秦皇岛">秦皇岛</a>
          </li>
                    <li>
            <a href="monthdata.php?city=曲靖">曲靖</a>
          </li>
                    <li>
            <a href="monthdata.php?city=齐齐哈尔">齐齐哈尔</a>
          </li>
                    <li>
            <a href="monthdata.php?city=七台河">七台河</a>
          </li>
                    <li>
            <a href="monthdata.php?city=黔西南州">黔西南州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=清远">清远</a>
          </li>
                    <li>
            <a href="monthdata.php?city=庆阳">庆阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=钦州">钦州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=衢州">衢州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=泉州">泉州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=琼中">琼中</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>R.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=荣成">荣成</a>
          </li>
                    <li>
            <a href="monthdata.php?city=日喀则">日喀则</a>
          </li>
                    <li>
            <a href="monthdata.php?city=乳山">乳山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=日照">日照</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>S.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=韶关">韶关</a>
          </li>
                    <li>
            <a href="monthdata.php?city=寿光">寿光</a>
          </li>
                    <li>
            <a href="monthdata.php?city=上海">上海</a>
          </li>
                    <li>
            <a href="monthdata.php?city=绥化">绥化</a>
          </li>
                    <li>
            <a href="monthdata.php?city=石河子">石河子</a>
          </li>
                    <li>
            <a href="monthdata.php?city=石家庄">石家庄</a>
          </li>
                    <li>
            <a href="monthdata.php?city=商洛">商洛</a>
          </li>
                    <li>
            <a href="monthdata.php?city=三明">三明</a>
          </li>
                    <li>
            <a href="monthdata.php?city=三门峡">三门峡</a>
          </li>
                    <li>
            <a href="monthdata.php?city=山南">山南</a>
          </li>
                    <li>
            <a href="monthdata.php?city=遂宁">遂宁</a>
          </li>
                    <li>
            <a href="monthdata.php?city=四平">四平</a>
          </li>
                    <li>
            <a href="monthdata.php?city=商丘">商丘</a>
          </li>
                    <li>
            <a href="monthdata.php?city=宿迁">宿迁</a>
          </li>
                    <li>
            <a href="monthdata.php?city=上饶">上饶</a>
          </li>
                    <li>
            <a href="monthdata.php?city=汕头">汕头</a>
          </li>
                    <li>
            <a href="monthdata.php?city=汕尾">汕尾</a>
          </li>
                    <li>
            <a href="monthdata.php?city=绍兴">绍兴</a>
          </li>
                    <li>
            <a href="monthdata.php?city=三亚">三亚</a>
          </li>
                    <li>
            <a href="monthdata.php?city=邵阳">邵阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=沈阳">沈阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=十堰">十堰</a>
          </li>
                    <li>
            <a href="monthdata.php?city=松原">松原</a>
          </li>
                    <li>
            <a href="monthdata.php?city=双鸭山">双鸭山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=深圳">深圳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=朔州">朔州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=宿州">宿州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=随州">随州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=苏州">苏州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=石嘴山">石嘴山</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>T.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=泰安">泰安</a>
          </li>
                    <li>
            <a href="monthdata.php?city=塔城地区">塔城地区</a>
          </li>
                    <li>
            <a href="monthdata.php?city=太仓">太仓</a>
          </li>
                    <li>
            <a href="monthdata.php?city=铜川">铜川</a>
          </li>
                    <li>
            <a href="monthdata.php?city=屯昌">屯昌</a>
          </li>
                    <li>
            <a href="monthdata.php?city=通化">通化</a>
          </li>
                    <li>
            <a href="monthdata.php?city=天津">天津</a>
          </li>
                    <li>
            <a href="monthdata.php?city=铁岭">铁岭</a>
          </li>
                    <li>
            <a href="monthdata.php?city=通辽">通辽</a>
          </li>
                    <li>
            <a href="monthdata.php?city=铜陵">铜陵</a>
          </li>
                    <li>
            <a href="monthdata.php?city=吐鲁番地区">吐鲁番地区</a>
          </li>
                    <li>
            <a href="monthdata.php?city=铜仁地区">铜仁地区</a>
          </li>
                    <li>
            <a href="monthdata.php?city=唐山">唐山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=天水">天水</a>
          </li>
                    <li>
            <a href="monthdata.php?city=太原">太原</a>
          </li>
                    <li>
            <a href="monthdata.php?city=台州">台州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=泰州">泰州</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>W.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=文昌">文昌</a>
          </li>
                    <li>
            <a href="monthdata.php?city=文登">文登</a>
          </li>
                    <li>
            <a href="monthdata.php?city=潍坊">潍坊</a>
          </li>
                    <li>
            <a href="monthdata.php?city=瓦房店">瓦房店</a>
          </li>
                    <li>
            <a href="monthdata.php?city=威海">威海</a>
          </li>
                    <li>
            <a href="monthdata.php?city=乌海">乌海</a>
          </li>
                    <li>
            <a href="monthdata.php?city=芜湖">芜湖</a>
          </li>
                    <li>
            <a href="monthdata.php?city=武汉">武汉</a>
          </li>
                    <li>
            <a href="monthdata.php?city=吴江">吴江</a>
          </li>
                    <li>
            <a href="monthdata.php?city=乌兰察布">乌兰察布</a>
          </li>
                    <li>
            <a href="monthdata.php?city=乌鲁木齐">乌鲁木齐</a>
          </li>
                    <li>
            <a href="monthdata.php?city=渭南">渭南</a>
          </li>
                    <li>
            <a href="monthdata.php?city=万宁">万宁</a>
          </li>
                    <li>
            <a href="monthdata.php?city=文山州">文山州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=武威">武威</a>
          </li>
                    <li>
            <a href="monthdata.php?city=无锡">无锡</a>
          </li>
                    <li>
            <a href="monthdata.php?city=温州">温州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=吴忠">吴忠</a>
          </li>
                    <li>
            <a href="monthdata.php?city=梧州">梧州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=五指山">五指山</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>X.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=西安">西安</a>
          </li>
                    <li>
            <a href="monthdata.php?city=兴安盟">兴安盟</a>
          </li>
                    <li>
            <a href="monthdata.php?city=许昌">许昌</a>
          </li>
                    <li>
            <a href="monthdata.php?city=宣城">宣城</a>
          </li>
                    <li>
            <a href="monthdata.php?city=襄阳">襄阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=孝感">孝感</a>
          </li>
                    <li>
            <a href="monthdata.php?city=迪庆州">迪庆州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=锡林郭勒盟">锡林郭勒盟</a>
          </li>
                    <li>
            <a href="monthdata.php?city=厦门">厦门</a>
          </li>
                    <li>
            <a href="monthdata.php?city=西宁">西宁</a>
          </li>
                    <li>
            <a href="monthdata.php?city=咸宁">咸宁</a>
          </li>
                    <li>
            <a href="monthdata.php?city=湘潭">湘潭</a>
          </li>
                    <li>
            <a href="monthdata.php?city=邢台">邢台</a>
          </li>
                    <li>
            <a href="monthdata.php?city=新乡">新乡</a>
          </li>
                    <li>
            <a href="monthdata.php?city=咸阳">咸阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=新余">新余</a>
          </li>
                    <li>
            <a href="monthdata.php?city=信阳">信阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=忻州">忻州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=徐州">徐州</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>Y.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=雅安">雅安</a>
          </li>
                    <li>
            <a href="monthdata.php?city=延安">延安</a>
          </li>
                    <li>
            <a href="monthdata.php?city=延边州">延边州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=宜宾">宜宾</a>
          </li>
                    <li>
            <a href="monthdata.php?city=盐城">盐城</a>
          </li>
                    <li>
            <a href="monthdata.php?city=宜昌">宜昌</a>
          </li>
                    <li>
            <a href="monthdata.php?city=宜春">宜春</a>
          </li>
                    <li>
            <a href="monthdata.php?city=银川">银川</a>
          </li>
                    <li>
            <a href="monthdata.php?city=运城">运城</a>
          </li>
                    <li>
            <a href="monthdata.php?city=伊春">伊春</a>
          </li>
                    <li>
            <a href="monthdata.php?city=云浮">云浮</a>
          </li>
                    <li>
            <a href="monthdata.php?city=阳江">阳江</a>
          </li>
                    <li>
            <a href="monthdata.php?city=营口">营口</a>
          </li>
                    <li>
            <a href="monthdata.php?city=榆林">榆林</a>
          </li>
                    <li>
            <a href="monthdata.php?city=玉林">玉林</a>
          </li>
                    <li>
            <a href="monthdata.php?city=伊犁哈萨克州">伊犁哈萨克州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=阳泉">阳泉</a>
          </li>
                    <li>
            <a href="monthdata.php?city=玉树州">玉树州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=烟台">烟台</a>
          </li>
                    <li>
            <a href="monthdata.php?city=鹰潭">鹰潭</a>
          </li>
                    <li>
            <a href="monthdata.php?city=义乌">义乌</a>
          </li>
                    <li>
            <a href="monthdata.php?city=宜兴">宜兴</a>
          </li>
                    <li>
            <a href="monthdata.php?city=玉溪">玉溪</a>
          </li>
                    <li>
            <a href="monthdata.php?city=益阳">益阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=岳阳">岳阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=扬州">扬州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=永州">永州</a>
          </li>
                  </div>
      </ul>
            <ul class="unstyled">
        <div><b>Z.</b></div>
        <div>
                    <li>
            <a href="monthdata.php?city=淄博">淄博</a>
          </li>
                    <li>
            <a href="monthdata.php?city=自贡">自贡</a>
          </li>
                    <li>
            <a href="monthdata.php?city=珠海">珠海</a>
          </li>
                    <li>
            <a href="monthdata.php?city=湛江">湛江</a>
          </li>
                    <li>
            <a href="monthdata.php?city=镇江">镇江</a>
          </li>
                    <li>
            <a href="monthdata.php?city=诸暨">诸暨</a>
          </li>
                    <li>
            <a href="monthdata.php?city=张家港">张家港</a>
          </li>
                    <li>
            <a href="monthdata.php?city=张家界">张家界</a>
          </li>
                    <li>
            <a href="monthdata.php?city=张家口">张家口</a>
          </li>
                    <li>
            <a href="monthdata.php?city=周口">周口</a>
          </li>
                    <li>
            <a href="monthdata.php?city=驻马店">驻马店</a>
          </li>
                    <li>
            <a href="monthdata.php?city=章丘">章丘</a>
          </li>
                    <li>
            <a href="monthdata.php?city=肇庆">肇庆</a>
          </li>
                    <li>
            <a href="monthdata.php?city=中山">中山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=舟山">舟山</a>
          </li>
                    <li>
            <a href="monthdata.php?city=昭通">昭通</a>
          </li>
                    <li>
            <a href="monthdata.php?city=中卫">中卫</a>
          </li>
                    <li>
            <a href="monthdata.php?city=张掖">张掖</a>
          </li>
                    <li>
            <a href="monthdata.php?city=招远">招远</a>
          </li>
                    <li>
            <a href="monthdata.php?city=资阳">资阳</a>
          </li>
                    <li>
            <a href="monthdata.php?city=遵义">遵义</a>
          </li>
                    <li>
            <a href="monthdata.php?city=枣庄">枣庄</a>
          </li>
                    <li>
            <a href="monthdata.php?city=漳州">漳州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=郑州">郑州</a>
          </li>
                    <li>
            <a href="monthdata.php?city=株洲">株洲</a>
          </li>
                  </div>
      </ul>
          </div>
  </div>
"""
