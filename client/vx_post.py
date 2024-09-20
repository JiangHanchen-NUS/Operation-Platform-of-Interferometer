import os
import time

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
}

while True:
    data_num = input("请输入你想上传的数字：")
    data = {
        "num": data_num
    }
    resp = requests.post('http://47.94.98.138:4000/vx', data=data, headers=headers)
    print("数据提交成功！")
    time.sleep(3)
