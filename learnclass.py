import requests

r = requests.get("http://hq.sinajs.cn/list=sh601006", headers =  {'user-agent':"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"})
print(r.json())