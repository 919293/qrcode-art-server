# QR-Code Server

## 概述

基于 https://github.com/sylnsfar/qrcode 进行开发，修复多进程下tempdir的问题，并将该工具制作成http服务。
与原项目不同，本项目生成的二维码不填充背景图，直接按最小尺寸返回透明背景的二维码。也可以指定缩放倍数。
由于原项目使用GPLv3协议，所以本项目也根据GPLv3协议进行开源。

## 例子
生成的透明背景图片：

![](https://github.com/tiaod/qrcode-art-server/blob/master/example/newqr.png)

自行使用PS叠加背景图：

![](https://github.com/tiaod/qrcode-art-server/blob/master/example/avatar1.jpg)
![](https://github.com/tiaod/qrcode-art-server/blob/master/example/avatar2.jpg)

甚至制作海报：

![](https://github.com/tiaod/qrcode-art-server/blob/master/example/poster3.jpg)
![](https://github.com/tiaod/qrcode-art-server/blob/master/example/poster1.jpg)

你也可以手动调节二维码的透明度，让海报看起来更自然：

![](https://github.com/tiaod/qrcode-art-server/blob/master/example/poster2.jpg)


## http接口调用
运行`python app.py`之后，会在本地运行一个http服务器，端口为5000，可以直接发送http请求：
```
http://localhost:5000/?words=https%3A%2F%2Fgithub.com%2Ftiaod%2Fqrcode-art-server&scale=2
```
相应内容为生成的二维码。

支持参数：
- words: 二维码的内容
- scale: 缩放倍数，只支持整数。默认为 1
- level: 纠错等级，默认为 L
- version: 支持1~40的整数，用于调节二维码尺寸。默认为自适应，根据长度调整


## 编程调用
由于生成的是透明背景二维码，所以大量的参数可以精简:
```python
qr = myqr.run(
	words,
    scale=8, #缩放倍数
    version=1,
    level='L')
qrcode.save('qrcode.png')
```

## 使用docker部署
项目提供了Dockerfile，但暂未发布到docker hub

## 赞赏
如果你觉得项目对你有帮助，欢迎赞赏我

![](https://github.com/tiaod/qrcode-art-server/blob/master/example/微信.png)
![](https://github.com/tiaod/qrcode-art-server/blob/master/example/支付宝.png)
![](https://github.com/tiaod/qrcode-art-server/blob/master/example/微信赞赏码.png)
​
## 协议
* GPLv3
