## 第九次作业

### 一、摘要
   p88页3.30题：Investigate the Lyapunov exponent of the stadium billiard for several values of ![](http://latex.codecogs.com/gif.latex?q=0.5s^{-1}).\
   关键词：哈密顿，混沌，庞加莱截面。

### 二、背景介绍
- 台球动力系统是一个粒子沿直线匀速运动并在边界发生镜面反射的动力系统。当粒子击中边界发生反射时它不会损失动能。台球动力系统是哈密顿理想化的台球游戏，但其边界可以是矩形等其他形状，甚至可以是多维的。台球动力系统也可以被用于研究非欧几何。
- 台球动力系统拥有哈密顿系统从可积性到混沌运动的所有复杂性，无须对运动方程进行困难的积分就可确定其庞加莱截面。乔治·大卫·比尔霍夫证明一个椭圆边界的台球动力系统是可积的。

### 三、正文
* 1、思路
① 台球动力系统示意图：
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/7-1.png)

② 一个混沌台球动力系统中粒子的轨迹：
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/7-1.png)

③ 在完美的台球桌上，我们考虑一个没有摩擦的球移动的问题，碰撞速度是恒定的，所以我们有
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/7-1.png)
确定一个碰撞点，我们得到在碰撞点处垂直于墙的单位向量
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/7-1.png)
我们对速度进行分解可得
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/7-1.png)
当粒子撞击边界时有
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/7-1.png)


![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/7-1.png)
![](http://latex.codecogs.com/gif.latex?q=0.5s^{-1})\

* 2、代码：
```python
import pylab as pl
import numpy as np
import math


class tabel:
    def __init__(self, x0=0.2, y0=0, vx0=-0.2, vy0=-0.5, dtstep=0.001, total_time=50):
        self.x = [x0]
        self.y = [y0]
        self.vx = [vx0]
        self.vy = [vy0]
        self.time = total_time
        self.t = [0]
        self.dt = dtstep
        self.xbound=[-1]
        self.y1bound=[0]
        self.y2bound=[0]


    def run(self):
        for i in range(int(self.time / self.dt)):
            self.x.append(self.x[i]+self.vx[i]*self.dt)
            self.y.append(self.y[i] + self.vy[i] * self.dt)
            self.vx.append(self.vx[i])
            self.vy.append(self.vy[i])
            if (self.x[i+1]**2+self.y[i+1]**2>1):
                xtry=(self.x[i]+self.x[i+1])/2
                ytry=(self.y[i]+self.y[i+1])/2
                cos=xtry/(xtry**2+ytry**2)**0.5
                sin=ytry/(xtry**2+ytry**2)**0.5
                verticalx=-(self.vx[i]*cos+self.vy[i]*sin)*cos
                verticaly=-(self.vx[i]*cos+self.vy[i]*sin)*sin
                #parallelx=self.vx*sin**2-sin*cos*self.vy
               # parallely=self.vy*cos**2-self.vx*cos*sin
                parallelx=self.vx[i]+verticalx
                parallely=self.vy[i]+verticaly
                self.vx[i+1]=verticalx+parallelx
                self.vy[i+1]=verticaly+parallely
                #利用向量变换得到反弹后的速度vx和vy

                if (xtry**2+ytry**2>1):
                    self.x[i+1]=xtry
                    self.y[i+1]=ytry
                    continue
                else:
                    self.x[i]=xtry
                    self.x[i]=ytry
                    continue

    def bound(self):
        self.xbound= [-1]
        self.y1bound = [0]
        self.y2bound = [0]
        dx = 0.001
        for i in range (2000):
            self.xbound.append(self.xbound[i]+dx)
            self.y1bound.append((1-self.xbound[i+1]**2)**0.5)
            self.y2bound.append(-(1-self.xbound[i+1]**2)**0.5)
    def show(self):
        pl.plot(self.x,self.y,'.',label='tra')
        pl.plot(self.xbound,self.y1bound,'--',label='bound')
        pl.plot(self.xbound,self.y2bound,'--',label='bound')
        pl.xlabel(u'x')
        pl.ylabel(u'y')
a=tabel()
a.run()
a.bound()
a.show()
pl.show()
```
①T = 50，单位圆下反弹
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/74.png)
②T = 100，单位圆下反弹
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/74.png)
③相空间情节
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/74.png)

3.考虑到在两半圆间增加宽为2α的矩形，并得到动画，代码如下
```python
import pylab as pl
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import animation
#用于制作动画
class tabel:
    def __init__(self, x0=0.2, y0=0, vx0=0.1, vy0=0.3, dtstep=0.01, total_time=300,alpha=0.1):
        self.x = [x0]
        self.y = [y0]
        self.vx = [vx0]
        self.vy = [vy0]
        self.time = total_time
        self.t = [0]
        self.dt = dtstep
        self.xbound=[-1]
        self.y1bound=[0]
        self.y2bound=[0]
        self.alpha=alpha
    def run(self):
        for i in range(int(self.time / self.dt)):
            self.x.append(self.x[i]+self.vx[i]*self.dt)
            self.y.append(self.y[i] + self.vy[i] * self.dt)
            self.vx.append(self.vx[i])
            self.vy.append(self.vy[i])
            self.t.append(self.t[i]+self.dt)
            if( self.y[i]>=self.alpha):
                if (self.x[i+1]**2+(self.y[i+1]-self.alpha)**2>1):
                    xtry = self.x[i] + self.vx[i]*self.dt/200
                    ytry= self.y[i]+self.vy[i]*self.dt/200
                    dtrebound=self.dt/200
                    while(xtry**2+(ytry-self.alpha)**2<=1):
                        xtry = xtry + self.vx[i] * self.dt / 200
                        ytry = ytry + self.vy[i] * self.dt / 200
                        dtrebound=dtrebound+self.dt/100
                    self.t.append(self.t[-1]+dtrebound)
                    cos=xtry/(xtry**2+(ytry-self.alpha)**2)**0.5
                    sin=(ytry-self.alpha)/(xtry**2+(ytry-self.alpha)**2)**0.5
                    verticalx=-(self.vx[i]*cos+self.vy[i]*sin)*cos
                    verticaly=-(self.vx[i]*cos+self.vy[i]*sin)*sin
                    parallelx=self.vx[i]+verticalx
                    parallely=self.vy[i]+verticaly
                    self.vx[i + 1] = verticalx + parallelx
                    self.vy[i + 1] = verticaly + parallely#利用向量变换得到反弹后的速度vx和vy
                    self.x[i+1]=xtry
                    self.y[i+1]=ytry
            elif(self.y[i]<self.alpha and self.y[i]>-self.alpha):
                if (abs(self.x[i+1])>1):
                    xtry = self.x[i] + self.vx[i]*self.dt/100
                    ytry= self.y[i]+self.vy[i]*self.dt/100
                    dtrebound=self.dt/100
                    while(abs(xtry)<=1):
                        xtry = xtry + self.vx[i] * self.dt / 200
                        ytry = ytry + self.vy[i] * self.dt / 200
                        dtrebound=dtrebound+self.dt/100
                    self.vx[i+1]=-self.vx[i]
                    self.vy[i+1]=self.vy[i]
            elif(self.y[i]<-self.alpha ):
                if(self.x[i+1]**2+(self.y[i+1]+self.alpha)**2>1):
                    xtry = self.x[i] + self.vx[i] * self.dt / 200
                    ytry = self.y[i] + self.vy[i] * self.dt / 200
                    dtrebound = self.dt / 100
                    while (xtry ** 2 + (ytry + self.alpha) ** 2 <=1):
                        xtry = xtry + self.vx[i] * self.dt / 200
                        ytry = ytry + self.vy[i] * self.dt / 200
                        dtrebound = dtrebound + self.dt / 200
                    cos = xtry / (xtry ** 2 + (ytry+self.alpha) ** 2) ** 0.5
                    sin = (ytry+self.alpha)/ (xtry ** 2 + (ytry+self.alpha) ** 2) ** 0.5
                    verticalx = -(self.vx[i] * cos + self.vy[i] * sin) * cos
                    verticaly = -(self.vx[i] * cos + self.vy[i] * sin) * sin
                    parallelx = self.vx[i] + verticalx
                    parallely = self.vy[i] + verticaly
                    self.vx[i + 1] = verticalx + parallelx
                    self.vy[i + 1] = verticaly + parallely
                    self.x[i + 1] = xtry
                    self.y[i + 1] = ytry
    def bound(self):
        self.xbound= [-1]
        self.y1bound = [self.alpha]
        self.y2bound = [-self.alpha]
        dx = 0.001
        for i in range (2000):
            self.xbound.append(self.xbound[i]+dx)
            self.y1bound.append(self.alpha+(1-self.xbound[i+1]**2)**0.5)
            self.y2bound.append(-self.alpha-(1-self.xbound[i+1]**2)**0.5)
    def show(self):
        pl.plot(self.x,self.y,'-',label='tra',linewidth=0.1)
        pl.plot(self.xbound,self.y1bound,'--')
        pl.plot(self.xbound,self.y2bound,'--')
        pl.xlabel(u'x')
        pl.ylabel(u'y')
        pl.ylim(-1.1,1.1)
        pl.xlim(-1.1,1.1)
        pl.axis('equal')
        pl.show()

    def drawtrajectory(self):

        fig = plt.figure()
        ax = plt.axes(title=('Stadium with $\\alpha$ = 0.1, - divergence of two trajectories'),
                      aspect='equal', autoscale_on=False, xlim=(-1.1, 1.1), ylim=(-1.1, 1.1),
                      xlabel=('x'),
                      ylabel=('y'))


        line1 = ax.plot([], [], 'b:')  # 初始化数据，line是轨迹，point是轨迹的头部
        point1 = ax.plot([], [], 'bo', markersize=10)

        images = []

        def init():  # 该函数用于初始化动画

            line1 = ax.plot([], [], 'b:', markersize=8)
            point1 = ax.plot([], [], 'bo', markersize=10)
            bound1 = ax.plot([], [], 'k.', markersize=1)
            bound2 = ax.plot([], [], 'k.', markersize=1)
            return line1, point1, bound1, bound2

        def anmi(i):  # anmi函数用于每一帧的数据更新，i是帧数。
            ax.clear()
            bound1 = ax.plot(self.xbound, self.y1bound, 'k.', markersize=1)
            bound2 = ax.plot(self.xbound, self.y2bound, 'k.', markersize=1)
            line1 = ax.plot(self.x[0:20* i], self.y[0:20 * i], 'b:', markersize=8)
            point1 = ax.plot(self.x[20 * i - 1:20 * i], self.y[20 * i - 1:20 * i], 'bo', markersize=10)
            return line1, point1, bound1, bound2

        anmi = animation.FuncAnimation(fig, anmi, init_func=init, frames=500, interval=1, blit=False, repeat=False, )
        plt.show()


a=tabel()
a.run()
a.bound()
a.show
a.drawtrajectory()
```
①α= 0.1
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/74.png)
②动图：
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/74.png)

4.用欧拉法进行数值模拟
```python
import math

class stadium_billiard:
    def __init__(self, vx_initial, vy_initial, x_initial, y_initial, time_interval, total_time, alpha):
        self.vx = [vx_initial]
        self.vy = [vy_initial]
        self.x = [x_initial]
        self.y = [y_initial]
        self.t = [0]
        self.dt = time_interval
        self.alpha = alpha
        self.steps = int(total_time // time_interval) + 1
    def calculate(self):
        for i in range(self.steps):
            new_y = self.y[i] + self.vy[i] * self.dt
            new_x = self.x[i] + self.vx[i] * self.dt
            if new_y <= self.alpha and new_y >= -self.alpha:
                if new_x > 1 :
                    new_x = self.x[i] + self.vx[i] * self.dt / 100
                    new_y = self.y[i] + self.vy[i] * self.dt / 100
                    time_interval_revised = self.dt / 100
                    while new_x < 1:
                        new_x = new_x + self.vx[i] * self.dt / 100
                        new_y = new_y + self.vy[i] * self.dt / 100
                        time_interval_revised = time_interval_revised + self.dt / 100
                    v_vertical_in_x = self.vx[i]
                    v_vertical_in_y = 0
                    v_parallel_in_x = 0
                    v_parallel_in_y = self.vy[i]
                    v_vertical_out_x = -self.vx[i]
                    v_vertical_out_y = 0
                    v_parallel_out_x = 0
                    v_parallel_out_y = self.vy[i]
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(v_vertical_out_x + v_parallel_out_x)
                    self.vy.append(v_vertical_out_y + v_parallel_out_y)
                    self.t.append(self.t[i] + time_interval_revised)
                elif new_x < -1:
                    new_x = self.x[i] + self.vx[i] * self.dt / 100
                    new_y = self.y[i] + self.vy[i] * self.dt / 100
                    time_interval_revised = self.dt / 100
                    while new_x > -1:
                        new_x = new_x + self.vx[i] * self.dt / 100
                        new_y = new_y + self.vy[i] * self.dt / 100
                        time_interval_revised = time_interval_revised + self.dt / 100
                    v_vertical_in_x = self.vx[i]
                    v_vertical_in_y = 0
                    v_parallel_in_x = 0
                    v_parallel_in_y = self.vy[i]
                    v_vertical_out_x = -self.vx[i]
                    v_vertical_out_y = 0
                    v_parallel_out_x = 0
                    v_parallel_out_y = self.vy[i]
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(v_vertical_out_x + v_parallel_out_x)
                    self.vy.append(v_vertical_out_y + v_parallel_out_y)
                    self.t.append(self.t[i] + time_interval_revised)
                else:
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(self.vx[i])
                    self.vy.append(self.vy[i])
                    self.t.append(self.t[i] + self.dt)
            elif new_y > self.alpha:
                if (new_x ** 2 + (new_y - self.alpha) ** 2) > 1:
                    new_x = self.x[i] + self.vx[i] * self.dt / 100
                    new_y = self.y[i] + self.vy[i] * self.dt / 100
                    time_interval_revised = self.dt / 100
                    while (new_x) ** 2 + (new_y - self.alpha) ** 2 < 1:
                        new_x = new_x + self.vx[i] * self.dt / 100
                        new_y = new_y + self.vy[i] * self.dt / 100
                        time_interval_revised = time_interval_revised + self.dt / 100
                    r = math.sqrt((new_x) ** 2 + (new_y - self.alpha) ** 2)
                    dot_product = self.vx[i] * (-new_x / r) + self.vy[i] * (self.alpha - new_y) / r
                    v_vertical_in_x = dot_product * (-new_x) / r
                    v_vertical_in_y = dot_product * (self.alpha - new_y) / r
                    v_parallel_in_x = self.vx[i] - v_vertical_in_x
                    v_parallel_in_y = self.vy[i] - v_vertical_in_y
                    v_vertical_out_x = -v_vertical_in_x
                    v_vertical_out_y = -v_vertical_in_y
                    v_parallel_out_x = v_parallel_in_x
                    v_parallel_out_y = v_parallel_in_y
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(v_vertical_out_x + v_parallel_out_x)
                    self.vy.append(v_vertical_out_y + v_parallel_out_y)
                    self.t.append(self.t[i] + time_interval_revised)
                else:
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(self.vx[i])
                    self.vy.append(self.vy[i])
                    self.t.append(self.t[i] + self.dt)
            elif new_y < -self.alpha:
                if (new_x ** 2 + (new_y - self.alpha) ** 2) > 1:
                    new_x = self.x[i] + self.vx[i] * self.dt / 100
                    new_y = self.y[i] + self.vy[i] * self.dt / 100
                    time_interval_revised = self.dt / 100
                    while new_x ** 2 + (new_y - self.alpha) ** 2 < 1:
                        new_x = new_x + self.vx[i] * self.dt / 100
                        new_y = new_y + self.vy[i] * self.dt / 100
                        time_interval_revised = time_interval_revised + self.dt / 100
                    r = math.sqrt((new_x) ** 2 + (new_y - self.alpha) ** 2)
                    dot_product = self.vx[i] * (-new_x / r) + self.vy[i] * (-self.alpha - new_y) / r
                    v_vertical_in_x = dot_product * (-new_x) / r
                    v_vertical_in_y = dot_product * (-self.alpha - new_y) / r
                    v_parallel_in_x = self.vx[i] - v_vertical_in_x
                    v_parallel_in_y = self.vy[i] - v_vertical_in_y
                    v_vertical_out_x = -v_vertical_in_x
                    v_vertical_out_y = -v_vertical_in_y
                    v_parallel_out_x = v_parallel_in_x
                    v_parallel_out_y = v_parallel_in_y
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(v_vertical_out_x + v_parallel_out_x)
                    self.vy.append(v_vertical_out_y + v_parallel_out_y)
                    self.t.append(self.t[i] + time_interval_revised)
                else:
                    self.x.append(new_x)
                    self.y.append(new_y)
                    self.vx.append(self.vx[i])
                    self.vy.append(self.vy[i])
                    self.t.append(self.t[i] + self.dt)


t1 = stadium_billiard(vx_initial = 0.1, vy_initial = 0.2, x_initial = 0.01, y_initial = 0.02, time_interval = 0.01, total_time = 1500, alpha = 0.05)
t2 = stadium_billiard(vx_initial = 0.1, vy_initial = 0.2, x_initial = 0.01006, y_initial = 0.02, time_interval = 0.01, total_time = 1500, alpha = 0.05)
t1.calculate()
t2.calculate()

d = []
for i in range(len(t1.x)):
    d.append(math.sqrt((t1.x[i]-t2.x[i]) ** 2) + (t1.y[i] - t2.y[i]) ** 2)

d_log = []
for i in range(len(t1.x)):
    d_log.append(math.log(d[i]))
```

如图：
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/74.png)

### 四、总结
1.可以看出α不同时，李雅普诺夫指数截然不同；相同α下，不同的初始距离d可能导致李雅普诺夫指数的些微不同

2.α越小曲线越密集，这说明系统经历了更多状态，可以预见，当α足够大即台球桌足够长时混沌现象可能会消失
    
### 五、致谢
    感谢彭成铭倪世杰同学鼎力相助~。


