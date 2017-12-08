## 第十一次作业

### 一、摘要
   p143页5.3题：Use the symmetry of the capacitor problem to write a program that obtains the results by calculating the potential in     only one quadrant of x-y plane.\
   关键词：雅克比方法，电容器，势场。

### 二、背景介绍
用电容器问题的对称性来编写程序，通过计算x-y平面的一个象限中的电势来获得结果。\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/112.png)

### 三、正文
分析题意，列出二维有限差分形式如下：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/111.png)\
在每一步更新的过程中，由于所求势场存在对称性，因此只需计算其中的对称部分，然后根据对称性直接对其他部分赋值即可。\
下面我们利用Jacobi方法计算具有两固定势能的金属条的方形势场中电势能的分布情况\
1、code：
```python
import math
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import pyplot
from matplotlib import numpy


X = numpy.arange(-1, 1, 0.05)
Y = numpy.arange(-1, 1, 0.05)
V = []
detV = 10000
end_detV = 1e-5 * len(X)


def update_V():
    global detV
    detV = 0
    for i in xrange(1, len(X) - 1):
        for j in xrange(1, len(Y) - 1):
            if (i==len(X)/3 or i==len(X)*2/3) and len(Y)/3<j<len(Y)*2/3:
                continue
            tmp = (V[i-1][j] + V[i+1][j] + V[i][j-1] + V[i][j+1]) / 4
            detV += numpy.abs(tmp - V[i][j])
            V[i][j] = tmp


# initialize V
V.append([0. for i in xrange(len(X))])
for i in xrange(1, len(X) - 1):
    tmp = [0.]
    for j in range(1, len(Y) - 1):
        if i==len(X)/3 and len(Y)/3<j<len(Y)*2/3:
            tmp.append(1.)
        elif i==len(X)*2/3 and len(Y)/3<j<len(Y)*2/3:
            tmp.append(-1.)
        else:
            tmp.append(0.)
    tmp.append(0.)
    V.append(tmp)
V.append([0. for i in xrange(len(X))])

while detV > end_detV:
    update_V()

X, Y = numpy.meshgrid(X, Y)

fig = pyplot.figure()
ax = fig.gca(projection='3d')
ax.set_title(r"Electric potential near two metal plates")
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_zlabel(r'$V$')
surf = ax.plot_surface(X, Y, V, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
pyplot.show()
```
2、效果：
①电场：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/113.png)\
②电势：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/114.png)

### 四、总结
   方法是先计算第一象限中的情况，然后用对称性，镜面和旋转对称到第二第三第四象限中，最后得到效果图。
   
### 五、致谢
    感谢王智麟同学的指导。

