# https://www.52shuku.vip/
import requests
from parsel import Selector
import time
import random
url=input('first url:')

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
    
flag=True
while True:
    resp=requests.get(url,headers=headers)
    resp.encoding='utf-8'
    resp=resp.text
    selector =Selector(text=resp)
    list=selector.xpath('//p/text()').extract()[:-1]
    info='\n'.join(list)
    if flag:
        title=selector.xpath("//h1[@id='nr_title']/text()").extract()[0]
        i=title.find("【")
        title=title[:i]
        flag=False
    with open(title+".txt",'a',encoding='utf-8') as f:
            f.write(info)
    try:
        url=selector.xpath("//a[contains(text(),'下一页')]/@href").extract()[0]
    except:
        break
    secs = random.normalvariate(1, 0.4)
    print(secs)
    if secs <= 0:
        secs = 1
    time.sleep(secs)




