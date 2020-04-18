import requests
from requests.exceptions import RequestException
import re
import json

for i in range(0,100,10):
    url = 'https://maoyan.com/board/4?offset=' + str(i)
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    response = requests.get(url=url, headers = headers).text #得到网页源码
    # print(response)

    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                            + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                            + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)  #使用正则表达式解析数据

    items = re.findall(pattern, response)
    content = items
    for item in items: #写入数据
        with open('demo.txt', 'a', encoding='utf-8') as f:
            # print(type(json.dumps(content)))
            f.write(json.dumps(content,ensure_ascii=False))














# #得到电影排名
# moive_index = re.findall('^<dd>.*?board-index.*?>(.*?</i>)',html)
# #得到电影图片
# moive_img = re.findall('^<dd>.*?board-index.*?board-img.*?src="(.*?)"',html)
# #得到电影的名字
# moive_name = re.findall('^<dd>.*?board-index.*?<p class="name">(.*?)</p>$',html)



