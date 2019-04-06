'''
设置高考倒计时，每分钟更新状态
'''
import time
from datetime import datetime


gaokaotime = datetime(2019, 6, 7, 9, 0)
now = datetime.now()
timedelta = gaokaotime - now

print(type(timedelta))
print("距离2019年高考还有:",timedelta.days, "天")

while True:
    time.sleep(2)
    print("还有5分钟")
