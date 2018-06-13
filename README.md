# QR-Code Server

## 概述

基于 https://github.com/sylnsfar/qrcode 进行开发，修复多进程下tempdir的问题，并将该工具制作成http服务。

与原项目不同，本项目生成的二维码**不填充背景图**，直接返回**透明背景的二维码**。生成的二维码为PNG格式，你可以使用PS等工具自行添加背景图，或者制作动图。与直接返回成品二维码相比，返回PNG格式的素材在使用上更加灵活和自由。

由于原项目使用GPLv3协议，所以本项目也根据GPLv3协议进行开源。

## 例子
生成的透明背景图片：

![](https://github.com/tiaod/qrcode-art-server/blob/master/example/newqr.png)

自行**使用PS**叠加背景图：

![](https://github.com/tiaod/qrcode-art-server/blob/master/example/avatar1.jpg)
![](https://github.com/tiaod/qrcode-art-server/blob/master/example/avatar2.jpg)

甚至制作海报：

![](https://github.com/tiaod/qrcode-art-server/blob/master/example/poster3.jpg)
![](https://github.com/tiaod/qrcode-art-server/blob/master/example/poster1.jpg)

你也可以手动调节二维码的透明度，让海报看起来更自然：

![](https://github.com/tiaod/qrcode-art-server/blob/master/example/poster2.jpg)

## 部署服务
首先安装依赖
```
$ pip install -r requirements.txt
```
然后启动服务器
```
$ python app.py
```

## http接口调用
运行`python app.py`之后，会在本地运行一个http服务器，端口为5000，可以直接发送http请求：
```
http://localhost:5000/?words=https%3A%2F%2Fgithub.com%2Ftiaod%2Fqrcode-art-server&scale=2
```
相应内容为生成的二维码。

参数：
- words: 二维码的内容。必填
- scale: 缩放倍数，只支持整数。默认为 1
- level: 纠错等级，默认为 L
- version: 支持1~40的整数，用于调节二维码尺寸。默认为自适应，根据内容长度调整

返回：
- PNG格式的二维码图片

## 编程调用
由于生成的是透明背景二维码，所以和原项目相比，大量的参数可以精简:
```python
qr = myqr.run(
	words,
    scale=8, #缩放倍数
    version=1,
    level='L')
qr.save('qrcode.png')
```

## 使用docker部署
```
$ docker run -p 5000:5000 tiaod/qrcode-art-server
```

## 赞赏
如果你觉得项目对你有帮助，欢迎赞赏我

![](https://github.com/tiaod/qrcode-art-server/blob/master/example/微信.png)
![](https://github.com/tiaod/qrcode-art-server/blob/master/example/支付宝.png)
![](https://github.com/tiaod/qrcode-art-server/blob/master/example/微信赞赏码.png)
​
## 协议
* GPLv3
