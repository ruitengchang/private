# image_process

image_process.py
程序针对情景1进行，（情景1：背景为白色，拼接图片之间有缝隙 (如果是图片和文字拼接而成，比如，图片左边配上了文字，只需要分割出图片部分，文字部分需要过滤掉)
整体思路：
原图：

![Image text](https://github.com/ruitengchang/image_process/blob/master/white.jpg)

1.读取图片，讲图片中所有非背景区域设为黑色，背景区域设为白色

![Image text](https://github.com/ruitengchang/image_process/blob/master/white.jpg)

2.利用边缘检测和霍夫变换检测图片中的黑色区域，并画出黑色部分的边界

![Image text](https://github.com/ruitengchang/image_process/blob/master/result.jpg)

3.通过黑色部分的边界得到矩形顶点，使用顶点讲图片切割出来

![Image text](https://github.com/ruitengchang/image_process/blob/master/new1.jpg)

![Image text](https://github.com/ruitengchang/image_process/blob/master/new0.jpg)


该方法不能用在庆幸2上，因为算法中是通过白素背景进行区分照片的，情形而当中没有白色背景，无法区分。
对于情形3，不是拼接图片的情况，也能够使用该算法。



问题1.如何在视频中嵌入观看者感兴趣的广告（不是插播），提出思路和实现技术方案
1.确定观众的兴趣点在哪里，这个需要手机观众的历史信息，以及观众本身的信息（年龄，性别，消费习惯等），越详细越好，形成用户画像，确定用户感兴趣的商品，
2.在视频中的右下右上等位置嵌入广告，具体可以在直接对视频进行处理，在视频中嵌入，或者在播放器，浏览器中嵌入。

问题2.为了实现设计案例重用（参考之前的设计范例），如何对Photoshop设计稿进行检索（有PSD和jpeg两种格式)，试阐述技术方案
1.读取文件夹下所有文件，文件名为string，
2.正则匹配“.*\.[(PSD)(jpeg)]”


