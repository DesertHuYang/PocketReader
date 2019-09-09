#-*- coding:utf-8 -*-
import requests
import json
import time
import sys
import imp
imp.reload(sys)
if __name__ == "__main__":
    def TencentReader():
        url = "https://kdy.unisyou.net/yunpan/activity/doSign"
        head = {}
        head['User-Agent'] = 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
        head['Accept'] = "application/json, text/javascript, */*; q=0.01"
        head["Content-Type"] = "application/json"
        head["DNT"] = "1"
        head['Origin'] = "https://kdy.unisyou.net"
		#你自己的口袋阅链接（微信扫码得到的地址，https开头）
        head["Referer"] = "%Url%"
        head["Sec-Fetch-Mode"] = "cors"
        head["X-Requested-With"] = "XMLHttpRequest"
		#自己的Request payload
        req = requests.post(url, data=json.dumps(
            {'userName': "自己注册的手机号", 'deviceNumber': "设备号", 'activityId': '10000',
             'mobile': "iOSNaN --iPad"}), headers=head)
        postmsg = req.content.decode("utf-8")
        print(postmsg)
        translate_results = json.loads(postmsg)
        print(translate_results['resultData'])
        return translate_results['resultData']

    def SendWeChat():
        localtime = u"---\n\n日期：" + time.strftime("%b %d, %Y", time.localtime()) + u"\n\n时间：" + time.strftime("%H:%M:%S", time.localtime()) + " (UTC)"
        #localtimeasc = time.asctime(time.localtime())
        #print(u"本地时间为 :", localtime)
        #自己的Server酱URL
        api = "%Api%"
        title = u"口袋阅签到提醒"
        content =localtime + u"\n\n![poster](http://kdy.yuewen.com/img/201907301-1-2.jpg)\n\n今天好像还没有签到哦！！！\n\n[**尝试手动签到**（可能会失效）](https://www.baidu.com)"
        data = {
            "text": title,
            "desp": content
        }
        #print(data)
        req = requests.post(api, data=data)
    if(TencentReader() is None):
        print(u'已发送签到提醒')
        SendWeChat()
