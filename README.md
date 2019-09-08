# PocketReader
口袋阅签到提醒（未签到推送消息到Server酱）

#使用方法

1、利用手机二维码扫码软件获取口袋阅的签到地址，并保存到电脑，地址的格式为
```
http://xxxxxxx...xxx==
```

2、打开Chrome，打开调试模式，选择移动设备界面调试，浏览器粘贴刚刚获取的签到地址，点击`Network`，在`Name`名称一栏找到`doSign`项，从`Header`获取所要填写的`payload`值

3、注册Server酱，获取推送地址（含key）

4、上传代码到服务器或者nas可以定时执行脚本的设备，并设置`crontab`或者计划任务定时执行

#效果展示

![enter description here](https://www.github.com/WANG592154873/LittleBook/raw/master/小书匠/消息页面.jpg)

![enter description here](https://www.github.com/WANG592154873/LittleBook/raw/master/小书匠/详情页面.jpg)