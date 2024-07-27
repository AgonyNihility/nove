# 此程序适用于https://hlib.cc
import requests
from lxml import etree
# url=input('first url:')
url="https://hlib.cc/n/14397616?p=1"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Cookie':'connect.sid=s%3Ai_ImZ4qnFAYSdT1Qs2kRGkym4La3fOjh.g17sx1BqRGNJ88Bd4zHA3iJ%2BEYyaI2Ruu7e3w9ptsIw; cf_clearance=5erP4zeU.uk2WxEk2TAJSXD0dPyxuY6bBpdZUbfygiE-1721984495-1.0.1.1-0eXlKE0uRmNF5cSKK0rI.zVCwEwGtLYRZYq7dQ5EzY64ID3fjsimtUw_rgJB4el0lnfcoZjWIpqzhj8dAq8jdw; ts_popunder-cnt=0; ts_popunder=Fri%20Jul%2026%202024%2017%3A12%3A05%20GMT%2B0800%20(%E9%A6%99%E6%B8%AF%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)'
}
oldtitle=''
while True:
    resp=requests.get(url,headers=headers)
    
    resp.encoding='utf-8'

    e = etree.HTML(resp.text)
    p=e.xpath('//div[@class="btn-group"]')[0]
    a=e.xpath('//li[@class="list-group-item text-center"][1]/a/text()')
    filename=e.xpath('//li[@class="list-group-item text-center"][1]/a/text()')[0]+".txt"
    info=''.join(e.xpath('//pre/p/text()'))
    if info:
        title=e.xpath('//h3/text()')[0]
        with open(filename,'a',encoding='utf-8') as f:
            if oldtitle!=title:
                f.write('\n\n'+title+'\n\n'+info)
            else:
                f.write(info)
        oldtitle=title
        try:
            if url[-1]=="2":
                url='https://hlib.cc/'+e.xpath('//a[@class="page-link h-100"]/@href')[-1]+'?p=1'
            else:
                url=url[:-1]+'2'
        except:
            break
    else:
        break