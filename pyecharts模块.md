# pyecharts模块

> ![image-20221214233538689](E:\Typora\Image\image-20221214233538689.png)

> ​	<img src="E:\Typora\Image\image-20221214234545207.png" alt="image-20221214234545207" style="zoom:50%;" />



## pyecharts模块安装

> ![image-20221214234317386](E:\Typora\Image\image-20221214234317386.png)

## pyecharts快速入门

### 基础折线图	

> ![image-20221215234020823](E:\Typora\Image\image-20221215234020823.png)

注意，line.render()执行后会生成一个html文件，里面就是我们作出的图像，但是它需要用浏览器打开（因为是html网页代码文件）。



## pyecharts的配置选项

> ![image-20221218233150488](E:\Typora\Image\image-20221218233150488.png)

- 全局配置针对整个图像，例如图像标题、图例、工具箱等；
- 系列配置针对图像的坐标轴

### 全局配置

> ![image-20221218233438115](E:\Typora\Image\image-20221218233438115.png)

#### `set_global_opts`方法(标题)

![image-20221218234440950](E:\Typora\Image\image-20221218234440950.png)

-  `TitleOpts`:需要导包`from pyecharts.options import TitleOpts`，

- `title_opts=TitleOpts(title="GDP")`中title参数是图标题名，这里设置为GDP
- `title_opts=TitleOpts(title="GDP", pos_left="center")`中pos_left设置标题的位置距离左边有多远，这里设置为中间
- `title_opts=TitleOpts(title="GDP", pos_left="center", pos_bottom="1%")`中pos_bottom设置标题离底部有多远，这里设置为与底部距离为1%。

