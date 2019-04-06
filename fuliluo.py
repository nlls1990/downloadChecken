# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import os



ip = "104.19.182.51"

def downloadFULI():
    header = {'user-agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    urllist = []
    for page in range(1, 36):
        url = 'https://www.ai737.com/shipin/list-%E4%B8%AD%E6%96%87%E5%AD%97%E5%B9%95' + '-' + str(page) + '.html'
        r = requests.get(url, headers=header)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'lxml')
        for item_url in soup.select('#tpl-img-content a'):
            urllist.append('https://www.ai737.com' + item_url['href'])


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

if __name__ == "__main__":
    downloadFULI()

