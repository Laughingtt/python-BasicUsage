import requests
from bs4 import BeautifulSoup
import re
import os

if not os.path.exists('./数据解析1107/adids'):
    os.mkdir('./数据解析1107/adids') 
url="https://list.tmall.com/search_product.htm?q=%B0%A2%B5%CF%B4%EF%CB%B9&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
}

r_text=requests.get(url=url,headers=headers).text.encode("utf-8").decode("utf-8")
# with open("./数据解析1107/adas.json","w",encoding="utf-8") as f:
#      f.write(r_text)
soup=BeautifulSoup(r_text,"html.parser")
name=soup.select("div.product>div.product-iWrap>p.productTitle>a")
price=soup.select("div.product>div.product-iWrap>p.productPrice>em")
picture=soup.select("div.product>div.product-iWrap>div.productImg-wrap>a>img")
for i,l in zip(name,price):
    print(i.attrs['title']+" "+l.attrs['title'])

list_tu=[]
for i in picture:
    path=re.findall(r'//.*?.jpg',str(i))
    path=''.join(path)
    list_tu.append(path)
for tu_url in list_tu:
    tu_url="http:"+tu_url
    tu_r=requests.get(url=tu_url,headers=headers).content
    tu_url_path=tu_url.split('/')[-1]
    tu_path='./数据解析1107/adids/'+tu_url_path
    with open(tu_path,'wb') as f:
        f.write(tu_r)
"""
http://img.alicdn.com/bao/uploaded/i1/369075622/O1CN01IzhAIe1rOvFknnpxn_!!0-item_pic.jpg
//img.alicdn.com/bao/uploaded/i3/320868932/O1CN01RBe3ZC2FquEFYs0M2_!!0-item_pic.jpg
<a href="//detail.tmall.com/item.htm?id=586746930410&amp;skuId=4179007203652&amp;user_id=320868932&amp;cat_id=2&amp;is_b=1&amp;rn=0b150cf8d9ef311edb2deb996e12ca46" class="productImg" target="_blank" data-p="50-10" atpanel="50-10,586746930410,50012043,,spu,1,spu,320868932,,,">
<img src="//img.alicdn.com/bao/uploaded/i4/320868932/O1CN01jc8WV42FquEJZm9Fg_!!0-item_pic.jpg">
</a>
<div class="product  " data-id="41883644764" data-atp="a!,,50012043,,,,,,,,">
<div class="product-iWrap">
 <div class="productImg-wrap">
 <img data-ks-lazyload="//img.alicdn.com/bao/uploaded/i4/848014414/O1CN01zcxkEv1iTenodiyho_!!848014414.jpg"/>
<a href="//detail.tmall.com/item.htm?id=41883644764&amp;skuId=4418642563979&amp;user_id=320868932&amp;cat_id=2&amp;is_b=1&amp;rn=0b150cf8d9ef311edb2deb996e12ca46" class="productImg" target="_blank" data-p="4-10">
<img src="//img.alicdn.com/bao/uploaded/i3/320868932/O1CN01RBe3ZC2FquEFYs0M2_!!0-item_pic.jpg">
</a>
 <img src="//img.alicdn.com/bao/uploaded/i4/320868932/O1CN01jc8WV42FquEJZm9Fg_!!0-item_pic.jpg">
</div>

<div class="productThumb clearfix">
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbPrev proThumb-disable proThumb-prev" title="上一页" style="visibility: visible;">&lt;</a>
<div class="proThumb-wrap">
<p class="ks-switchable-content">
  <b data-sku="1627207:140272657" class="proThumb-img " data-index="4:1">
 <img atpanel="4-1,41883644764,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i3/320868932/O1CN01mEuV7B2FquCP9DQlO_!!320868932.png_30x30.jpg">
 <i></i>
 </b>
  <b data-sku="1627207:2449800632" class="proThumb-img " data-index="4:2">
 <img atpanel="4-2,41883644764,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i1/320868932/O1CN01Rd376r2FquE80z3yj_!!320868932.jpg_30x30.jpg">
 <i></i>
 </b>
  <b data-sku="1627207:2532332715" class="proThumb-img " data-index="4:3">
 <img atpanel="4-3,41883644764,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i3/320868932/O1CN01zekngA2FquEFWOTCa_!!320868932.jpg_30x30.jpg">
 <i></i>
 </b>
  <b data-sku="1627207:2642621532" class="proThumb-img " data-index="4:4">
 <img atpanel="4-4,41883644764,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i3/320868932/O1CN01Z7MGPi2FquE9pTOuN_!!320868932.jpg_30x30.jpg">
 <i></i>
 </b>
  <b data-sku="1627207:2642621533" class="proThumb-img " data-index="4:5">
 <img atpanel="4-5,41883644764,,,spu/shop,20,itemsku," src="//img.alicdn.com/bao/uploaded/i3/320868932/O1CN018pELmo2FquEMkcGXo_!!320868932.jpg_30x30.jpg">
 <i></i>
 </b>
  <b data-sku="1627207:2646016457" class="proThumb-img " data-index="4:6">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i2/320868932/O1CN01lIeyBw2FquE0Un8sl_!!320868932.jpg_30x30.jpg" atpanel="4-6,41883644764,,,spu/shop,20,itemsku,">
 <i></i>
 </b>
  <b data-sku="1627207:2879901453" class="proThumb-img " data-index="4:7">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i2/320868932/O1CN012pVlMI2FquE7gzQK8_!!320868932.jpg_30x30.jpg" atpanel="4-7,41883644764,,,spu/shop,20,itemsku,">
 <i></i>
 </b>
  <b data-sku="1627207:3320162838" class="proThumb-img " data-index="4:8">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i4/320868932/O1CN015VO24H2FquCSC2yPI_!!320868932.jpg_30x30.jpg" atpanel="4-8,41883644764,,,spu/shop,20,itemsku,">
 <i></i>
 </b>
  <b data-sku="1627207:3915655998" class="proThumb-img " data-index="4:9">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i4/320868932/O1CN01Yw6zGo2FquEIRgb2Y_!!320868932.png_30x30.jpg" atpanel="4-9,41883644764,,,spu/shop,20,itemsku,">
 <i></i>
 </b>
  <b data-sku="1627207:4390066197" class="proThumb-img " data-index="4:10">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i1/320868932/O1CN01aZGzsx2FquBh2xqwG_!!320868932.png_30x30.jpg" atpanel="4-10,41883644764,,,spu/shop,20,itemsku,">
 <i></i>
 </b>
  <b data-sku="1627207:4406071039" class="proThumb-img " data-index="4:11">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i3/320868932/O1CN01VH3bjG2FquC6Q27kY_!!320868932.png_30x30.jpg" atpanel="4-11,41883644764,,,spu/shop,20,itemsku,">
 <i></i>
 </b>
  <b data-sku="1627207:5026178843" class="proThumb-img " data-index="4:12">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i4/320868932/O1CN014UPWjJ2FquAwGpWA4_!!320868932.jpg_30x30.jpg" atpanel="4-12,41883644764,,,spu/shop,20,itemsku,">
 <i></i>
 </b>
  <b data-sku="1627207:5112122942" class="proThumb-img " data-index="4:13">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i2/320868932/O1CN01v6tPAA2FquBfRgow0_!!320868932.png_30x30.jpg" atpanel="4-13,41883644764,,,spu/shop,20,itemsku,">
 <i></i>
 </b>
  <b data-sku="1627207:6289222471" class="proThumb-img " data-index="4:14">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i1/3937219703/O1CN016vCgM02LY1b48dpgp_!!3937219703.jpg_30x30.jpg" atpanel="4-14,41883644764,,,spu/shop,20,itemsku,">
 <i></i>
 </b>
  <b data-sku="1627207:6316300363" class="proThumb-img " data-index="4:15">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i1/320868932/O1CN01K7ec2w2FquEKHOSiS_!!320868932.png_30x30.jpg" atpanel="4-15,41883644764,,,spu/shop,20,itemsku,">
 <i></i>
 </b>
  <b data-sku="1627207:706309214" class="proThumb-img " data-index="4:16">
 <img data-ks-lazyload-custom="//img.alicdn.com/bao/uploaded/i4/320868932/O1CN01DLt0UB2FquEJdz6Mf_!!320868932.jpg_30x30.jpg" atpanel="4-16,41883644764,,,spu/shop,20,itemsku,">
 <i></i>
 </b>
</p>
</div>
<a href="javascript:;" class="ui-slide-arrow-s j_ProThumbNext proThumb-next" title="下一页" style="visibility: visible;">&gt;</a>
</div>
  
 <p class="productPrice">
<a class="tag"><img src="http://tmallfans.cn-hangzhou.oss-pub.aliyun-inc.com/pifu/files/788424/20191031101517.png"></a>

<em title="319.00"><b>¥</b>319.00</em>

 </p>

<p class="productTitle">

<a href="//detail.tmall.com/item.htm?id=41883644764&amp;skuId=4418642563979&amp;user_id=320868932&amp;cat_id=2&amp;is_b=1&amp;rn=0b150cf8d9ef311edb2deb996e12ca46" target="_blank" title="Adidas阿迪达斯男鞋秋冬季新款小白鞋NEO帆布运动鞋休闲鞋板鞋男" data-p="4-11">
<span class="H">Adidas</span><span class="H">阿迪达斯</span>男鞋秋冬季新款小白鞋NEO帆布运动鞋休闲鞋板鞋男
</a>

</p>

<div class="productShop" data-atp="b!4-3,{user_id},,,,,,">
 <a class="productShop-name" href="//store.taobao.com/search.htm?user_number_id=320868932&amp;rn=0b150cf8d9ef311edb2deb996e12ca46&amp;keyword=阿迪达斯" target="_blank">
徐氏运动专营店
</a>
</div>
 <p class="productStatus">
<span>月成交 <em>1143笔</em></span>
<span>评价 <a href="//detail.tmall.com/item.htm?id=41883644764&amp;skuId=4418642563979&amp;user_id=320868932&amp;cat_id=2&amp;is_b=1&amp;rn=0b150cf8d9ef311edb2deb996e12ca46&amp;on_comment=1#J_TabBar" target="_blank" data-p="4-1">1.3万</a></span>
<span data-icon="small" class="ww-light ww-small" data-item="41883644764" data-nick="徐氏运动专营店" data-tnick="徐氏运动专营店" data-display="inline" data-atp="a!4-2,,,,,,,320868932"><a href="https://amos.alicdn.com/getcid.aw?v=3&amp;groupid=0&amp;s=1&amp;charset=utf-8&amp;uid=%E5%BE%90%E6%B0%8F%E8%BF%90%E5%8A%A8%E4%B8%93%E8%90%A5%E5%BA%97&amp;site=cntaobao&amp;fromid=cntaobaodBSx1JOVqZreOtvbBOCanurza77OSIRYYuPzaNbMi_5aF6T6zY_OkQ6MlF96VjW5GH8B4cPM8Rp9-etkZHiKFghHtBUqwNtSJXL64" target="_blank" class="ww-inline ww-online" title="点此可以直接和卖家交流选好的宝贝，或相互交流网购体验，还支持语音视频噢。"><span>旺旺在线</span></a></span>
</p>
 </div>


<a class="tag"><img src="http://tmallfans.cn-hangzhou.oss-pub.aliyun-inc.com/pifu/files/110363/20180912021209.png"/></a>, <a class="tag"><img src="http://tmallfans.cn-hangzhou.oss-pub.aliyun-inc.com/pifu/files/788424/20191031101517.png"/></a>, <a class="tag"><img src="http://tmallfans.cn-hangzhou.oss-pub.aliyun-inc.com/pifu/files/788424/20191031101517.png"/></a>

</div>
"""