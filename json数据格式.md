# json数据格式

## 什么是json

> ![image-20221212235334992](E:\Typora\Image\image-20221212235334992.png)

## json的用途

> ![image-20221212235449604](E:\Typora\Image\image-20221212235449604.png)

## json格式数据转化

> ![image-20221212235615316](E:\Typora\Image\image-20221212235615316.png)

- 简单理解：
    1. json就是把我们Python中的字典转换为字符串
    2. 又或者说把Python中的一个元素都是字典的列表转换为字符串

​	这两种类型就完全直接json数据了

- 而json又可以反过来转换为字典或内嵌字典的列表

- 关键在于**字典 **

    

## Python数据和Json数据的相互转化	

> ![image-20221213214938453](E:\Typora\Image\image-20221213214938453.png)

### 应用案例

> 案例1：Python数据转json
>
> ![image-20221213215145712](E:\Typora\Image\image-20221213215145712.png)
>
> 注意到json实际上也是str类型，且出现了编码，为了解决这个编码的呈现，我们作如下改进：
>
> ![image-20221213215321053](E:\Typora\Image\image-20221213215321053.png)
>
> 此时即可输出正常结果，这是因为输出`ensure_ascii=False`表明不使用ASCII来转换，而是把内容直接输出，若为True则中文会转换为Unicode，也就是上述见到的编码。
>
> ![image-20221213215344394](E:\Typora\Image\image-20221213215344394.png)
>
> 总体案例：
>
> ![image-20221213215639001](E:\Typora\Image\image-20221213215639001.png)

> 案例2：json转Python
>
> ![image-20221213215924892](E:\Typora\Image\image-20221213215924892.png)

# json总结

> ![image-20221213220104844](E:\Typora\Image\image-20221213220104844.png)