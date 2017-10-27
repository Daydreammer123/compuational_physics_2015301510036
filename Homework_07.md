## 第七次作业

### 一、摘要
   p65页3.12题：Construct the Poineare sections for these cases and compare them with Ficture 3.9.
   关键词：摆，混沌，相位空间，非线性，阻尼。

### 二、背景介绍
- 混沌现象是一个发生在确定性系统中的看似随机的不规则运动，其实它的系统是被确定的理论定义的。它的行为是非确定性的。这是非线性动力系统的固有特征和常见现象。
- 而在研究物理摆动时，如果我们增加上一个驱动力，我们就会看到混沌摆，也就是看似随机的振荡。

### 三、正文
* 1、思路
考虑驱动力和耗散力的摆的微分方程：
![](http://latex.codecogs.com/gif.latex?\frac{\mathrm{d^2}\theta}{\mathrm{d}t^2}{=}-\frac{g}{l}sin\theta-q\frac{\mathrm{d}\theta}{\mathrm{d}t}+F_{D}sin\left (t\Omega_{D}\right) )\






```python
print("   # # #      #           #     #  #  # ")
print(" #        #   # #       # #   #         ")
print(" #        #   #   #   #   #  #          ")
print(" #      # #   #     #     #   #         ")
print("   # # # # #  #           #     #  #  # ")
```
效果图：

![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/02-1.png)

* 2、进阶版
```python
>>> a="qiaominchen"
>>> for i in range(len(a)):
    print(a[i])
```   
效果图：

![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/02-2.png)


### 四、总结
    刚开始因为文件名没有加“.md”，以及周五晚上的发烧走了很多弯路。\
    心得就是要多花时间，多问多找教程吧！\
    其实还想弄个点阵第三版的，没搞出来还，勉强奉上以上吧。\
    
### 五、致谢
    **非常感谢 曾梓龙学长！！**，在我快崩溃时指出了文件名的错误。\
    另谢谢，我的好友赵展艺，方昕，李震宇，在与他们的讨论中受益匪浅。

