#-*- coding:utf-8 -*-
import requests
import json
import time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
if __name__ == "__main__":
        localtime = u"---\n\n日期：" + time.strftime("%b %d, %Y", time.localtime()) + u"\n\n时间：" + time.strftime("%H:%M:%S", time.localtime()) + " (UTC)"
        #localtimeasc = time.asctime(time.localtime())
        #print(u"本地时间为 :", localtime)
        #自己的Server酱URL
        api = ""
        title = u"口袋阅签到提醒"
        content =localtime + u"\n\n![poster](http://kdy.yuewen.com/img/201907301-1-2.jpg)\n\n今天好像还没有签到哦！！！\n\n[**尝试手动签到**（可能会失效）]()"
        data = {
            "text": title,
            "desp": content
        }
        req = requests.post(api, data=data)
