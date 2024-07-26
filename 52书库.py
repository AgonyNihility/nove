# 此程序https://www.52shuku.vip/可用
import requests
from lxml import etree
import unicodedata
url=input('first url:')
filename=input("book name:")+'.txt'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
while True:
    resp=requests.get(url,headers=headers)
    resp.encoding='utf-8'
    e = etree.HTML(resp.text)
    info=''.join(e.xpath('//div/article/p/text()')[:-1])
    info=unicodedata.normalize('NFKC',info)
    with open(filename,'a',encoding='utf-8') as f:
            f.write(info)
    try:
        url=e.xpath('//div[@class="pagination2"]//a/@href')[2]
    except:
        break