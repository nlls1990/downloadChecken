# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import os

# 读取要分析的内容
# with open('./abc.txt', 'r') as f:
#     html = f.read()
#
# soup = BeautifulSoup(html, "lxml")
#
# titles = []
# for title in soup.select('.post_title a'):
#     titles.append([title.get_text(), "https://nlls1990.github.io"+str(title['href'])])
# print(titles)


def pullBlog(url):
    '''
    :param url: 输入的博客的地址
    :return: blog标题和访问链接组成的list
    '''
    fullurl = url
    headers = {'user-agent':"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    r = requests.get(fullurl,headers=headers)
    r.encoding = "utf-8"

    soup = BeautifulSoup(r.text, "lxml")
    titles = []
    for title in soup.select('.post_title a'):
        titles.append([title.get_text(), "https://nlls1990.github.io"+str(title['href'])])

    return titles

def saveInfo(array):
    if array == None:
        print("There is no data to save.")
        return -1
    with open("BlogArchive.txt", "w") as f:
        for i in range(len(array)):
            f.writelines("%s - %s" % (array[i][0],  array[i][1]))
        return 0



if __name__ == "__main__":
    retBlog = pullBlog('https://nlls1990.github.io/archive')
    saveInfo(retBlog)
    print(retBlog)