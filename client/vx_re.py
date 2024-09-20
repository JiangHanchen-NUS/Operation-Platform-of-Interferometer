import os
import time

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
}
num = 1
filenames = []
print("程序接收信息中。。。")
while True:
    dst_dir1 = "F:\project\comp\gene_img\img"
    dst_dir2 = "F:\project\comp\data"
    # dst_dir = "H:\object"
    new_filesnames = [i for i in os.listdir(dst_dir1) if os.path.isfile(i)]
    for new_filesname in new_filesnames:
        if new_filesname not in filenames:
            filenames.append(new_filesname)
            num = 1
            print(filenames)
    resp = requests.get('http://47.94.98.138:4000/vx', headers=headers)
    resp.encoding = "utf-8"
    if resp.text != "":
        print("接受到的信息是：", resp.text)
        with open("{}\data_{}.txt".format(dst_dir2, str(num)), 'w', encoding="utf-8") as f:
            f.write(resp.text + " ")
        num += 1
    time.sleep(3)
