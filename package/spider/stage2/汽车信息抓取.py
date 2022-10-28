import requests
import json
from bs4 import BeautifulSoup

url="https://www.chebaba.com/car?smartcode=g2019-2818529-90-12446454&&renqun_youhua=1814814&bd_vid=9588359745841161786&smtid=573139219z2vwjz2670oz8jz0zNDUwOQ%3D%3D"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
}
r_text=requests.get(url=url,headers=headers).text
# with open("./douban.json","w",encoding="utf-8") as f:
#     f.write(r_text)
soup=BeautifulSoup(r_text,"html.parser")
car_name=soup.select("li>a>div.car-index__text-box>h4")
car_price=soup.select("li>a>div.car-index__text-box>p>span.car-type__price")
for car,price in zip(car_name,car_price):
    print(car.string.strip(),price.string.strip())
"""
<li class="m-car-series__type-item m-car-series__hover-active" data-brand-id="1" data-extra-level="13" data-series-id="54" data-track="click:gtm|cbb_car_carlist_54" style="display: list-item;">
    			 	 	<a href="https://www.chebaba.com/car/54/242147.html">
    			 	 		<div class="new-car-presell">新车预售</div>
    			 	 		<div class="car-index__pic-box">
    			 	 			<img class="lazyload" src="//upload.chebaba.com/shop/goods_class/2019-07-16-13-41-34-5d2d638e8737b.jpg@450w" data-original="//upload.chebaba.com/shop/goods_class/2019-07-16-13-41-34-5d2d638e8737b.jpg@450w" alt="第14代轩逸" style="display: inline-block;">
    			 	 		</div>
    			 	 		<div class="car-index__text-box">
    			 	 			<h4 class="car-type__name">第14代轩逸</h4>
    			 	 										<p class="car-type__price-box">
									<span class="car-type__price">10.90万起</span>
									<span class="price_reduce">
										<i class="price_reduce-sign cbb-iconfont" style="display:none"></i>
																				<span class="reductionPrice"></span>
									</span>
								</p>
								<div class="car_content__label">
									<span class="car_content__label__class">新车上市</span>
									<span class="car_content__label__num">6款在售车型</span>
								</div>
														
    			 	 		</div>
    			 	 	</a>
    			 	 </li>
                      """