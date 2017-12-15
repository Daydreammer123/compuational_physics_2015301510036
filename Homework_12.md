## 第十二次作业

### 一、摘要
   p164页6.6题：Show that two such wavepackets pass through each other without changing shape or speed.\
   关键词：波，频谱，傅里叶展开，边界条件。

### 二、背景介绍
   在经典物理学中，波是波，粒子是粒子.\
   但在量子力学中，我们不得不承认粒子也是波动的.但是自由粒子肯定不是单色波，因为单色波不能归一化. \
   实际上，一个粒子就是一个波包，它的动量就是所有由波包组成的单色波的平均动量。 \
   现在，我们将分析波包的特性。

   在本章中，我们将考虑关于波浪运动的主题。\
   首先，我们假设波在一个完美的无摩擦的弦上运动.然后我们再考虑更加复杂一点的情况。 \
   观察到了一些有趣的现象，例如波浪的半损失和叠加。

### 三、正文
   中央波运动方程为：
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/12-1.png)\
   波动方程可以写成有限差分形式,例如,：
![](http://latex.codecogs.com/gif.latex?y\left(i,n+1\right)=2\left[1-r^{2}\right]y\left(i,n\right)-y\left(i,n-1\right)+r^{2}\left[y\left(i+1,n\right)+y\left(i-1,n\right)\right])\
   我们设参数![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/12-2.png)\
   并使i从i=1依次取整数到i=M-1
   然后我们取所有端![](http://latex.codecogs.com/gif.latex?xy\left(0,n\right)=y\left(m,n\right)=0)，边界条件就固定了。

1、code：
```python
from matplotlib import animation
from pylab import*
import numpy as np
c=25.0
dx=0.01
dt=0.01
t=0.0

y=[]
l=np.linspace(0,1,100)#x-axis
y0=np.exp(-1000*(l-0.3)**2)#y-axis it's a wave package locates at x=0.3
y0_2=np.exp(-1000*(l-0.7)**2)+np.exp(-700*(l-0.7)**2)    

def w():
    global t,dt
    y.append(y0_2)
    y.append(y0_2)
    while t<100.0:
        y_next=np.zeros(100)
       
        for i in range(1,98):
            y_next[i]=-y[-2][i]+y[-1][i+1]+y[-1][i-1]
       
        y.append(y_next)
        t=t+dt
    return y, t
#print w()[0] ,w()[1]

def w2():
    global t,dt
    y.append(y0)
    y.append(y0)
    while t<100.0:
        y_next=np.zeros(100)
       
        for i in range(1,98):
            if i<50:
                y_next[i]=-y[-2][i]+y[-1][i+1]+y[-1][i-1]
            else: 
                y_next[i]=2*(1-0.5)*y[-1][i]-y[-2][i]+0.5*(y[-1][i+1]+y[-1][i-1])
        y.append(y_next)
        t=t+dt
    return y, t
#print w()[0] ,w()[1]

a=w()[0]
a=w()[0]
f=figure()
ax=axes(xlim=(0,1),ylim=(-1.2,1.2))
line, =ax.plot([],[],lw=2)

def animate(i):
    line.set_data(l,a[i])
    return line,
def init():
    line.set_data([],[])
    return line,
anim=animation.FuncAnimation(f,animate,init_func=init,frames=200,interval=50,blit=True)#frames mean zhenshu,interval mean each frame last how long
show()
```
2、效果：\
①设波长为1m，波速为300/s，r=1.\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/1201.gif)

②叠加原理：在①的基础上加一个波包。\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/1202.gif)

③半波损失：设波在两个介质中的传播速度分别是：v1=300/s,v2=150m/s，在介质分界面发生半波损失.
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/1203.gif)

④假设③中第二介质密度更高,v3=125m/s
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/1204.gif)

### 四、总结
   从波包传播的仿真，然后验证波包不受碰撞影响的波叠加原理，揭示了波的许多固有特性。\
   ①一个波包会自动分解为两个波包,它们沿反向传播，而且当波传播到尽头时,它在垂直方向返现，水平速度也会反向。\
   ②由于波函数是线性的，满足线性叠加原则，所以两个波包重叠时速度互不影响，形状线性叠加，但本质不变。\
   ③第二介质密度越大，振幅越小，即半波损失。由于入射角是零,当波从一个稀疏介质传播到密介质,反射波的相位突变π,损失了波长的一半。所以反射波的传播方向改变,但透射波不变。
    
### 五、致谢
    感谢王智霖同学的指导。

