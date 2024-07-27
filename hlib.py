# 此程序适用于https://hlib.cc
import requests
from lxml import etree
from bs4 import BeautifulSoup
url=input("first url(第一章第一页的网址,不用写最后的?P=1):")+"?p=1"
Cookie=input("Cookie(登录网站后复制Cookie信息):")
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Cookie':Cookie
}
oldtitle=''
c=1
while True:
    resp=requests.get(url,headers=headers)
    soup=BeautifulSoup(resp.content,"lxml")
    resp.encoding='utf-8'
    e = etree.HTML(resp.text)
    
    info=''.join(e.xpath('//pre/p/text()'))

    if info:
        title=e.xpath('//h3/text()')[0]
        try:
            filename=e.xpath('//div[@class="stick-tab"]/ul/li[@class="list-group-item text-center"]/a/text()')[0]+".txt"
        except:
            filename=title+".txt"
    try:
        p=e.xpath('//nav/div/button/text()')[-1]
    except:
        p='1'


    with open(filename,'a',encoding='utf-8') as f:
        if oldtitle!=title:
            f.write('\n\n'+title+'\n\n'+info)
        else:
            f.write(info)
    oldtitle=title
    try:
        if url[-1]==p:
            jud=e.xpath('//a[@class="page-link h-100"]/text()')[-1][0]
            if jud=="后":
                url='https://hlib.cc/'+e.xpath('//a[@class="page-link h-100"]/@href')[-1]+'?p=1'
                c=1
            else:
                break
        else:
            c+=1
            url=url[:-1]+str(c)
            
    except:
        break