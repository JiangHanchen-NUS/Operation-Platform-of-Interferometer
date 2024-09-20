import os
import threading
import time

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0"
}


def upload_object():
    dst_dir = "F:\project\comp\init_img\object"
    filenames = []
    while True:
        new_filesnames = [dst_dir+"\\"+i for i in os.listdir(dst_dir) if os.path.isfile(dst_dir+"\\"+i)]
        print("obj new_filesnames:",str(new_filesnames))
        for new_filesname in new_filesnames:
            if new_filesname not in filenames:
                filenames.append(new_filesname)
                requests.post("http://47.94.98.138:5000/obj", headers=headers, files={"objfile": open(new_filesname, 'rb')})
        time.sleep(2)


def upload_img():
    dst_dir = "F:\project\comp\gene_img\img"
    # dst_dir = "H:\img"
    filenames = []
    while True:
        new_filesnames = [dst_dir+"\\"+i for i in os.listdir(dst_dir) if os.path.isfile(dst_dir+"\\"+i)]
        print("img new_filesnames:", str(new_filesnames))
        for new_filesname in new_filesnames:
            if new_filesname not in filenames:
                filenames.append(new_filesname)
                requests.post("http://47.94.98.138:5000/img", headers=headers, files={"imgfile": open(new_filesname, 'rb')})
            time.sleep(1)
        time.sleep(2)


def upload_background():
    dst_dir = r"F:\project\comp\init_img\background"
    filenames = []
    while True:
        new_filesnames = [dst_dir+"\\"+i for i in os.listdir(dst_dir) if os.path.isfile(dst_dir+"\\"+i)]
        print("bg new_filesnames:",str(new_filesnames))
        for new_filesname in new_filesnames:
            if new_filesname not in filenames:
                filenames.append(new_filesname)
                requests.post("http://47.94.98.138:5000/bg", headers=headers, files={"bgfile": open(new_filesname, 'rb')})
        time.sleep(2)


def main():
    # t1 = threading.Thread(target=upload_object)
    # t1.start()
    # time.sleep(6)
    # t1 = threading.Thread(target=upload_background)
    # t1.start()
    # time.sleep(6)
    t1 = threading.Thread(target=upload_img)
    t1.start()


main()
