# image_process

image_process.py
程序针对情景1进行，（情景1：背景为白色，拼接图片之间有缝隙 (如果是图片和文字拼接而成，比如，图片左边配上了文字，只需要分割出图片部分，文字部分需要过滤掉)
整体思路：
原图：

![Image text](https://github.com/ruitengchang/image_process/blob/master/test.jpg)

1.读取图片，讲图片中所有非背景区域设为黑色，背景区域设为白色

![Image text](https://github.com/ruitengchang/image_process/blob/master/white.jpg)

2.利用边缘检测和霍夫变换检测图片中的黑色区域，找出所有直线（红色），并找到黑色区域的边界（绿色）

![Image text](https://github.com/ruitengchang/image_process/blob/master/hough.jpg)

![Image text](https://github.com/ruitengchang/image_process/blob/master/result.jpg)

3.通过黑色部分的边界得到矩形顶点，使用顶点讲图片切割出来
得到图片1如下：

![Image text](https://github.com/ruitengchang/image_process/blob/master/new1.jpg)

得到图片2如下：
![Image text](https://github.com/ruitengchang/image_process/blob/master/new0.jpg)

该方法不能用在情形2上，因为算法中是通过白素背景进行区分照片的，情形而当中没有白色背景，无法区分。
对于情形3，不是拼接图片的情况，也能够使用该算法。
注意，该方法还没有经过完备的测试，并且在所给的数据上测试的结果也有好有坏，以上现实的是切分效果最好的一张。在其他数据上测试还有一些缺陷：

1.识别出所有直线后并不能正确确定黑色区域的边界，可能代码中参数还需要调试

2.并不能识别出所有直线，hough变换的参数可能需要调试

3.识别出所有黑色区域之后，区域之间的合并机制并不完备，可能会出现吧一张图片切成两张的情况



下面回答邮件中的其他问题：

问题1.如何在视频中嵌入观看者感兴趣的广告（不是插播），提出思路和实现技术方案

1.确定观众的兴趣点在哪里，这个需要手机观众的历史信息，以及观众本身的信息（年龄，性别，消费习惯等），越详细越好，形成用户画像，确定用户感兴趣的商品

2.在视频中的右下右上等位置嵌入广告，具体可以在直接对视频进行处理，在视频中嵌入，或者在播放器，浏览器中嵌入。


问题2.为了实现设计案例重用（参考之前的设计范例），如何对Photoshop设计稿进行检索（有PSD和jpeg两种格式)，试阐述技术方案

1.读取文件夹下所有文件，文件名为string，

2.正则匹配“.*\.[(PSD)(jpeg)]”

备注：问题的回答：

a. 平时阅读哪些技术类书籍 ：

平时看的书有：《正则表达式》，《linux bash编程与脚本应用》，《c++沉思录》，《c++ primier》以及一些学校的课程的书籍等等，除了看书之外其实我还会看一些教程视频，bilibili和慕课网上的视频等

b. 当遇到技术问题时，常去哪些网站寻找帮助：

遇到技术困难查询网站：百度，知乎，stackoverflow，谷歌等。

其中百度信息比较杂，但是优点在于都是中文的，也能找到一些不错的技术博客，缺点就是信息太杂，且不一定准确。

知乎上面如果有比较好的回答，也能给人很多信息，但是好的回答比较少

stackoverflow上面基本能解决所有程序中遇到的环境配置，bug，报错之类的，回答的人都是大牛，缺点在于英文读起来比较慢。

谷歌要科学上网，现在抓得比较紧，好多都挂了。

