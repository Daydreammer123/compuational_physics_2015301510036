## 第八次作业

### 一、摘要
   p164页6.6题：Show that two such wavepackets pass through each other without changing shape or speed.\
   关键词：波，频谱，傅里叶展开，边界条件。

### 二、背景介绍
    在经典物理学中，波是波，粒子是粒子.但在量子力学中，我们不得不承认粒子也是波动的.但是自由粒子肯定不是单色波，因为单色波不能归一化. \
    实际上，一个粒子就是一个波包，它的动量就是所有由波包组成的单色波的平均动量。 \
    现在，我们将分析波包的特性。

    在本章中，我们将考虑关于波浪运动的主题。\
    首先，我们假设波在一个完美的无摩擦的弦上运动.然后我们再考虑更加复杂一点的情况。 \
    观察到了一些有趣的现象，例如波浪的半损失和叠加。\
> ![](http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}x}{\mathrm{d}t}{=}\sigma\left(y-x\right))\
  ![](http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}y}{\mathrm{d}t}{=}-xz+rx-y)\
  ![](http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}z}{\mathrm{d}t}{=}xy-bz)


### 三、正文
波浪运动的中心是：
> ![](http://latex.codecogs.com/gif.latex?x_{i+1}{=}x_{i}+v_{x,i+1})\
常规传播模拟波浪上的一个字符串。使用：
  ![](http://latex.codecogs.com/gif.latex?y_{i+1}{=}y_{i}+v_{y,i+1})\
来更新
  ![](http://latex.codecogs.com/gif.latex?z_{i+1}{=}z_{i}+v_{z,i+1})\
设置参数组合
  ![](http://latex.codecogs.com/gif.latex?v_{x,i+1}{=}\sigma\left(y_{i}-x_{i}\right))\
循环内部点i = 1到i = M-1
根据y（i，n + 1）更新
在i = 0和i = M处的末端是固定的，所以y（0，n）= y（M，n）= 0。
  
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
2、刺激两个波包的碰撞如下：
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/8-4.png)

### 四、总结
   From the simulation wave packages' propagate. Then we verify superposition principle of waves that wavepackets are unaffected by collisions.It reveals many intrinsic properties of waves.
   从仿真波包传播。 然后验证波包不受碰撞影响的波叠加原理，揭示了波的许多固有特性。
    
### 五、致谢
    感谢张凡同学。

