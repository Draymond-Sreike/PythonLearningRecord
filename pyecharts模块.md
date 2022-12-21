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

> ![image-20221221192315588](E:\Typora\Image\image-20221221192315588.png)



### 全局配置`set_global_opts`方法

> ![image-20221218233438115](E:\Typora\Image\image-20221218233438115.png)



![image-20221218234440950](E:\Typora\Image\image-20221218234440950.png)

#### 控制标题的方法参数`title_opts`

1. `TitleOpts`一个传给传给参数title_opts的函数/方法:需要导包`from pyecharts.options import TitleOpts`
2. `title_opts=TitleOpts(title="GDP")`中title参数是图标题名，这里设置为GDP
3. `title_opts=TitleOpts(title="GDP", pos_left="center")`中pos_left设置标题的位置距离左边有多远，这里设置为中间
4. `title_opts=TitleOpts(title="GDP", pos_left="center", pos_bottom="1%")`中pos_bottom设置标题离底部有多远，这里设置为与底部距离为1%。

除此还可以控制图例、工具箱等

#### 控制图例的方法参数`legend_opts`

1. `LegendOpts`是一个传给参数legend_opts的函数/方法:需要导包`from pyecharts.options import LegendOpts`
    - (可以与前面已导入的包合并为一个导包语句：`from pyecharts.options import TitleOpts, LegendOpts`即逗号可以使得一条导包语句一次导多个包)
2. `legend_opts=LegendOpts(is_show=True)`中is_show表示是否展示。。。

> ![image-20221221192108750](E:\Typora\Image\image-20221221192108750.png)

#### 工具箱的方法参数`toolbox_opts`

1. 第一点类比同上
2. `toolbox_opts=ToolboxOpts(is_show=True)`中is_show表示是否展示工具箱

> ​	![image-20221221190653717](E:\Typora\Image\image-20221221190653717.png)

#### 视觉映射`visualmap_opts`

1. 第一点类比同上
2. `visualmap_opts=VisualMapOpts(is_show=True)`中is_show表示是否展示工具箱

> ![image-20221221190712165](E:\Typora\Image\image-20221221190712165.png)

#### 其他可以控制参数

上这里找[pyecharts官网-全局配置项](https://pyecharts.org/#/zh-cn/global_options)
