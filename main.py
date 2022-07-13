#获取token https://webui.mybti.cn/?rd=06091633/#/home/appoint

from subway import Subway
import datetime
import time

if __name__ == '__main__':
    sub=Subway()
    lineName="昌平线"
    stationName="沙河站"
    timeSlot="0700-0710"    # 设置时间段
    while True:
        day = datetime.date.today().day
        month = datetime.date.today().month
        year = datetime.date.today().year
        enterDate = f"{year}{month:02d}{day+1:02d}"    # 设置日期
        begin_time = f'{year}-{month:02d}-{day:02d} 12:00:01.500'  # 设置开抢时间
        print('begin_time', begin_time)
        print('enterDate', enterDate)
        sub.make_reserve_by_time(lineName, stationName, enterDate, timeSlot, begin_time)
        begin_time = f'{year}-{month:02d}-{day:02d} 20:00:01.500'  # 设置开抢时间
        sub.make_reserve_by_time(lineName, stationName, enterDate, timeSlot, begin_time)
        time.sleep(60*60*15)
