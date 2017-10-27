## 第七次作业

### 一、摘要
   p65页3.12题：Construct the Poineare sections for these cases and compare them with Ficture 3.9.\
   关键词：摆，混沌，相位空间，非线性，阻尼。

### 二、背景介绍
- 混沌现象是一个发生在确定性系统中的看似随机的不规则运动，其实它的系统是被确定的理论定义的。它的行为是非确定性的。这是非线性动力系统的固有特征和常见现象。
- 而在研究物理摆动时，如果我们增加上一个驱动力，我们就会看到混沌摆，也就是看似随机的振荡。

### 三、正文
* 1、思路
考虑驱动力和耗散力的摆的微分方程：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/7-1.png)\
其中：g=9.8m/s l=9.8m ![](http://latex.codecogs.com/gif.latex?q=0.5s^{-1})\
q是耗散参数，![](http://latex.codecogs.com/gif.latex?F_{D})和![](http://latex.codecogs.com/gif.latex?\Omega _{D})分别是驱动力的幅度和角频率。

混乱，意味着你改变了初始条件，终点的差异就失之千里。但这并不意味着它是不可预知的，相反，由于我们有ODE和初始条件，我们可以预测摆锤的轨迹。\
Eular-Cromer方法执行如下：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/7-2.png)\
使![](http://latex.codecogs.com/gif.latex?\theta_{i+1})在![](http://latex.codecogs.com/gif.latex?\left[-\pi\right\pi])间取值\
取![](http://latex.codecogs.com/gif.latex?F_{D}{=}0,0.5,1.2)，计算，有图：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/71.png)\
当![](http://latex.codecogs.com/gif.latex?F_{D}{=}0,0.5)时，没有混沌出现。\
如图\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/72.png)\
但是当![](http://latex.codecogs.com/gif.latex?F_{D}{=}1.2)时，我们发现混沌。\
如图\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/73.png)\
当我们选择一些特殊的点：![](http://latex.codecogs.com/gif.latex?\Omega_{D}t_{i}{=}2\pin)，其中n为任意整数，我们看到如Figure3.9的图，看到attractor。

* 2、代码
```python
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:44:35 2017

@author: qmcqi
"""

import numpy as np
import math
import matplotlib.pyplot as plt

g=9.8
l=9.8
class CHAOS():
    def __init__(self,_omg0,_theta0,_t0,_q,_FD,_Omega,_size=100.,_timelim=400.):
        self.omg=[_omg0]
        self.theta=[_theta0]
        self.t=[_t0]
        self.q=_q
        self.FD=_FD
        self.Omega=_Omega
        self.timelim=int(round(_timelim))
        self.size=int(round(_size))
        self.dt=(2.*math.pi/self.Omega)/self.size
        self.time=(2.*math.pi/self.Omega)*self.timelim
        self.n=int(round(self.time/self.dt))
    def calculate(self):
        global g,l
        for i in range(self.n):
            self.omg.append(self.omg[-1]-g/l*math.sin(self.theta[-1])*self.dt-self.q*self.omg[-1]*self.dt+self.FD*math.sin(self.Omega*self.t[-1])*self.dt)
            if self.theta[-1]+self.omg[-1]*self.dt>math.pi:
                self.theta.append(self.theta[-1]+self.omg[-1]*self.dt-2*math.pi)
            elif self.theta[-1]+self.omg[-1]*self.dt<-math.pi:
                self.theta.append(self.theta[-1]+self.omg[-1]*self.dt+2*math.pi)
            else: 
                self.theta.append(self.theta[-1]+self.omg[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
            
    def plot_Poincare(self,_ax):        # the Poincare section plot    
        self.theta_Poincare=[]
        self.omg_Poincare=[]
        self.t_Poincare=[]
        for i in range(int(np.round(self.timelim))):
            self.t_Poincare.append(self.t[(i+1)*self.size])
            self.omg_Poincare.append(self.omg[(i+1)*self.size])
            self.theta_Poincare.append(self.theta[(i+1)*self.size])
        _ax.plot(self.theta_Poincare,self.omg_Poincare,'ob',markersize=2,label=r'$F_d = $'+' %.1f'%self.FD)
a=CHAOS(0,0.2,0,0.5,1.2,2./3.,100.,400.)
a.calculate()
ax=plt.subplot(111)
a.plot_Poincare(ax)
plt.xlabel(r"$\theta$(radians)")
plt.ylabel("$\omega$(radians/s)")
plt.title(r'$\omega$'+'   versus   '+r'$\theta$'+'   FD=1.2')

plt.savefig('chaos4.png')
plt.show()
```

效果图：

![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/74.png)


### 四、总结
   混乱的制度似乎是无序的，但如果我们在驱动力的每一个周期内选择一个点，我们可以看到吸引力，而这个特征只出现在一些特殊的情况下。如果我改变驱动力的幅度，attractor消失。
    
### 五、致谢
    感谢王泽。

