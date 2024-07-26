#此程序http://www.biqugie.com/ 可用
import requests
from lxml import etree


url=input('first url:')
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
filename=input("book name:")+'.txt'
ht=url[:url.find(".com")+4]
oldtitle=''


while True:
    resp=requests.get(url,headers=headers)
    resp.encoding='utf-8'
    e = etree.HTML(resp.text)
    info=''.join(e.xpath('//div/p/text()')[5:-6])
    title=e.xpath('//h1/text()')[0]
    url=ht+e.xpath('//a[@class="label label-default"][2]/@href')[0]


    with open(filename,'a',encoding='utf-8') as f:
        if oldtitle!=title:
            f.write('\n\n'+title+'\n\n'+info)
        else:
            f.write(info)
    oldtitle=title