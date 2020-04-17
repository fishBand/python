import requests
from lxml import etree

#确定地址
url = 'https://music.163.com/playlist?id=4910420313'
base_url = 'https://link.hhtjim.com/163/'

#请求
headers = {
     'User-Agent' : 'Mozilla/5.0 (Windows NT 99.0; Win32; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
 }
result = requests.get(url,headers = headers).text
# print(result)

#筛选
dom = etree.HTML(result)
ids = dom.xpath('//a[contains(@href,"song?")]/@href')
# print(ids)
#
for song_id in ids:
    count_id = song_id.strip('/song?id=')
    # print(count_id)

    #剔除不需要的信息
    if('$' in count_id) == False:
        # print(count_id)
        #确定歌曲的url
        song_url = base_url + '%s'%count_id + '.mp3'
        # print(song_url)
        song_name = song_url.split('/')[-1]
        # print(song_name)
        #爬取并写入
        music = requests.get(song_url).content
        with open('./MusicWangYiYun/%s'%song_name,'wb' ) as file:
            file.write(music)
