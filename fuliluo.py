# -*- coding: UTF-8 -*-
import os
import shutil
import requests
from bs4 import BeautifulSoup
from collections import namedtuple


header = {'user-agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

def make_path(p):
    if os.path.exists(p):  # 判断文件夹是否存在
        shutil.rmtree(p)  # 删除文件夹
    os.mkdir(p)  # 创建文件夹


def downloadFULI():
    header = {'user-agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    urllist = []
    for page in range(1, 36):
        url = 'https://www.230rr.com/shipin/list-%E4%B8%AD%E6%96%87%E5%AD%97%E5%B9%95' + '-' + str(page) + '.html'
        r = requests.get(url, headers=header)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'lxml')
        for item_url in soup.select('#tpl-img-content a'):
            urllist.append('https://www.230rr.com' + item_url['href'])


    downloadurl = []
    with open("fulidownload.txt", "w") as f:
        for item in urllist:
            r = requests.get(item, headers=header)
            r.encoding = 'utf-8'
            s = BeautifulSoup(r.text, 'lxml')
            download = s.select('.downlink_btn')
            title = s.select('#shipin-detail-content-pull > div.pull-left.text-left.margin_left_10.pull-left-mobile2 > div:nth-child(1) > h2')
            downloadurl.append([download[0]['href'], title])
            f.writelines(download[0]['href'] + '------' + title[0].string + '\r\n')
            print([download[0]['href'], title])



tag = ['shipin', 'xiazai']
# branch = namedtuple('branch', ['shipin', 'xiazai']) #, 'tupian', 'xiaoshuo'
# b = branch(('短视频', '国产精品', '中文字幕', '成人动漫'),  # '女友专辑'
#            ('亚洲电影', '制服丝袜', '强奸乱伦', '变态另类'))
branch = [ ['国产精品', '中文字幕', '成人动漫', '短视频'],['亚洲电影', '制服丝袜', '强奸乱伦', '变态另类']]
page = [ [35, 35, 28, 270], [19, 36, 27, 32]]
ip = "104.19.182.51"

#url = 'https://www.230rr.com/' + tag[i] + '/list-' + tag[i][j] + '-' + str(page) + '.html'

for i in range(len(tag)):
    make_path(tag[i])
    url = 'https://www.230rr.com/' + tag[i] + '/list-'
    #page = # 此处应该获取到所有的页码
    for j in range(len(branch[i])):
        for k in range(page[i][j]):
            full = url + branch[i][j] + '-' + str(k+1) + '.html'
            urllist = []
            header = {'user-agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
            r = requests.get(full, headers=header)
            r.encoding = 'utf-8'
            soup = BeautifulSoup(r.text, 'lxml')
            for item_url in soup.select('#tpl-img-content a'):
                urllist.append('https://www.230rr.com' + item_url['href'])
            print(urllist)
            downloadurl = []
            with open("fulidownload.txt", "w") as f:
                for item in urllist:
                    r = requests.get(item, headers=header)
                    r.encoding = 'utf-8'
                    s = BeautifulSoup(r.text, 'lxml')
                    download = s.select('.downlink_btn')
                    title = s.select(
                        '#shipin-detail-content-pull > div.pull-left.text-left.margin_left_10.pull-left-mobile2 > div:nth-child(1) > h2')
                    downloadurl.append([download[0]['href'], title])
                    f.writelines(download[0]['href'] + '------' + title[0].string + '\r\n')
                    print([download[0]['href'], title])





#if __name__ == "__main__":
    # downloadFULI()
