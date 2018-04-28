

import urllib.request
import requests
import os
import json
import time



baseUrl = 'http://api.5i512.com/v3/search/recommend/1302696161/list?clientid=1302696161&v=1.1&ts=0'
imgpath = 'oftenImage'

response = urllib.request.urlopen(baseUrl)
content = response.read()
data = json.loads(content)

arr = data['list']
n=0

for dic in arr:
    # print(dic['logo'])
    img_url = dic['logo']
    img_name = dic['name']
    img_sort = dic['sort']
    try:
        if not os.path.exists(imgpath):
            print('文件夹', imgpath, '不存在，重新建立')
            os.makedirs(imgpath)
        # 获得图片后缀
        # file_suffix = os.path.splitext(img_url)[1]
        # if int(img_sort) > 1:
            nameArr = img_url.split("/")
            file_name = nameArr[len(nameArr) - 1]
            # 拼接图片名（包含路径）
            filename = '{}'.format(file_name)
            # 下载图片，并保存到文件夹中
            urllib.request.urlretrieve(img_url, filename=filename)
            print('下载第' + str(n) + '张图片' + str(img_name) + str(filename))

            n += 1



    except IOError as e:
        print('文件操作失败', e)

    except Exception as e:
        print('错误 ：', e)





# for i in range(0,94):
