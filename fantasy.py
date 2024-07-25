import requests
from lxml import etree
import unicodedata
# 发送给谁
url='https://www.52shuku.vip/gl/21_b/bjUAr_79.html'
# 发送请求
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
oldtitle=''
while True:
    resp=requests.get(url,headers=headers)

    resp.encoding='utf-8'

    e = etree.HTML(resp.text)
    info=''.join(e.xpath('//div/article/p/text()')[:-1])
    info=unicodedata.normalize('NFKC',info)
    title=e.xpath('//h1/text()')[0]
    with open('天降女友.txt','a',encoding='utf-8') as f:
        if oldtitle!=title:
            f.write('\n\n'+title+'\n\n'+info)
        else:
            f.write(info)
    oldtitle=title
    try:
        url=e.xpath('//div[@class="pagination2"]//a/@href')[2]
    except:
        break