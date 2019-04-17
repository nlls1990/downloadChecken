# -*- coding: UTF-8 -*-
'''
软件名：文件夹整理脚本，通过输入目标文件夹的路径，将其按照文件类型进行分类
输入：绝对路径
输出：新的文件夹，以文件类型为目录分割

主要流程：
1. 获取目录的后缀，加入到字典，键值为数
2. 获取到一个类型， 创建一种文件夹，然后将对应的目录丢进去，键值加1
3. 开启3个线程去进行扫描并且复制
'''

import shutil
import os

def make_path(path):
    if os.path.exists(path):  # 判断文件夹是否存在
        shutil.rmtree(path)  # 删除文件夹
    os.mkdir(path)  # 创建文件夹

def copy_path(srcpath, dstpath):
    if os.path.isfile(srcpath) and os.path.isdir(dstpath):
        shutil.copy2(srcpath, dstpath)
    else:
        print('%s is not a file.' % srcpath)


def os_read():
    if os.access("fulidownload.txt", os.R_OK):
        with open("fulidownload.txt") as fp:
            return fp.read()
    return "some default data"

def list_path(path):
    if os.path.exists(path):  # 判断文件夹是否存在
        return os.listdir(path)

def get_suffix(str):
    return os.path.splitext(str)[-1][1:]


def arrangeFolder(srcDir, dstDir):
    content = list_path(srcDir)
    make_path(dstDir)
    data = {}

    for i in range(len(content)):
        if get_suffix(content[i]) == '':
            continue
        subsrcpath = srcDir + '/' + content[i]
        subdstpath = dstDir + '/' + get_suffix(content[i])
        if get_suffix(content[i]) in data:
            data[get_suffix(content[i])] += 1
        else:
            data[get_suffix(content[i])] = 1
            make_path(subdstpath)
        copy_path(subsrcpath, subdstpath)

if __name__ == "__main__":
    curpath = input('请输入要整理的文件夹路径：\r\n')
    dstpath = input('请输入目标文件夹路径:\r\n')

    arrangeFolder(curpath, dstpath)

    # os.chdir('/Users/lucida/Desktop')
    # print(os.listdir())
    # print(shutil.copyfile('./pullBlog.py', './pullBlog_bk.py'))