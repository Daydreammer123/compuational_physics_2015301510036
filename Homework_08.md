## 第八次作业

### 一、摘要
   p82页3.26题：Show that the Poincare sections in Figure 3.17 are independent of the initial conditions.\
   关键词：欧拉方法，混沌,流体力学，洛伦兹模型，Stokes方程。

### 二、背景介绍
本题的背景是天气现象研究中的洛伦兹模型。\
在研究流体力学的基本方程，Navier-Stokes方程时，我们并将其应用简化成三个方程:\
> ![](http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}x}{\mathrm{d}t}{=}\sigma\left(y-x\right))\
  ![](http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}y}{\mathrm{d}t}{=}-xz+rx-y)\
  ![](http://latex.codecogs.com/gif.latex?\frac{\mathrm{d}z}{\mathrm{d}t}{=}xy-bz)
  
其中x,y,z即Navier-Stokes方程中的温度，密度，速度；而r反映由温差带来的驱动效果，b则反应流体阻尼。

### 三、正文
由欧拉方程得
> ![](http://latex.codecogs.com/gif.latex?x_{i+1}{=}x_{i}+v_{x,i+1})\
  ![](http://latex.codecogs.com/gif.latex?y_{i+1}{=}y_{i}+v_{y,i+1})\
  ![](http://latex.codecogs.com/gif.latex?z_{i+1}{=}z_{i}+v_{z,i+1})\
  ![](http://latex.codecogs.com/gif.latex?v_{x,i+1}{=}\sigma\left(y_{i}-x_{i}\right))\
  ![](http://latex.codecogs.com/gif.latex?v_{y,i+1}{=}-y_{i}+rx_{i}-x_{i}z_{i})\
  ![](http://latex.codecogs.com/gif.latex?v_{z,i+1}{=}-y_{i}x_{i}-bz_{i})

可知Lprenz模型内流体运动显著依赖于驱动r，当改变驱动r的大小时，可观察到混沌的产生和消失。\
取![](http://latex.codecogs.com/gif.latex?\sigma=10,b=8/3),初始值x=1，y=z=0，在不同的r值时画出速度z随时间的变化曲线：

- [x] code①：
```python
import math
import matplotlib.pyplot as plt

a=10
b=8./3.

class Position():
    def __init__(self,_r,_x0=1,_y0=0,_z0=0,_t0=0,_time=60,_dt=0.0001):
        self.x=[_x0]
        self.y=[_y0]
        self.z=[_z0]
        self.t=[_t0]
        self.r=_r
        self.time=_time
        self.dt=_dt
        self.n=int(self.time/self.dt)
    def calculate(self):
        for i in range(self.n):
            self.x.append(self.x[-1]+a*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+self.r*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-b*self.z[-1])*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot(self,color):
        plt.plot(self.t,self.z,color,label='r=$%d$'%self.r)
A=Position(10)
A.calculate()
A.plot('o-')
B=Position(20)
B.calculate()
B.plot('r-')
C=Position(40)
C.calculate()
C.plot('y-')

plt.title('Lorenz model,z vetsus time')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,60)
plt.legend(loc='upper left')
plt.savefig('lorenz1.png')
plt.show()
```

![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/8-1.png)

> 发现，在r值较小时，z出现阻尼衰减的现象，但当r值增大到一定值时出现了复杂的混沌现象.\
于是我们将r值继续增大到160及163.8，作出相空间的图形：

- [x] code②：
```python
import matplotlib.pyplot as plt

a=10
b=8./3.

class Position():
    def __init__(self,_r,_x0=1,_y0=0,_z0=0,_t0=0,_time=60,_dt=0.0001):
        self.x=[_x0]
        self.y=[_y0]
        self.z=[_z0]
        self.t=[_t0]
        self.r=_r
        self.time=_time
        self.dt=_dt
        self.n=int(self.time/self.dt)
    def calculate(self):
        for i in range(self.n):
            self.x.append(self.x[-1]+a*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+self.r*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-b*self.z[-1])*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot(self,color):
        plt.plot(self.t,self.z,color,label='r=$%.1f$'%self.r)
plt.figure(figsize=(8,8))
ax1=plt.subplot(211)
A=Position(160)
A.calculate()
A.plot('k-')
plt.title('Lorenz model,z vetsus time,r=160')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,30)
plt.legend(loc='upper right')

ax2=plt.subplot(212)
B=Position(163.8)
B.calculate()
B.plot('k-')
plt.title('Lorenz model,z vetsus time,r=163.8')
plt.xlabel('time(s)')
plt.ylabel('z')
plt.xlim(0,30)
plt.legend(loc='upper right')

plt.savefig('lorenz2.png')
plt.show()
```

![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/8-2.png)

> 取r=25,初始值x=1，y=z=0：

- [x] code③：
```python
import math
import matplotlib.pyplot as plt

a=10
b=8./3.

class Position():
    def __init__(self,_r,_x0=1,_y0=0,_z0=0,_t0=0,_time=60,_dt=0.0001):
        self.x=[_x0]
        self.y=[_y0]
        self.z=[_z0]
        self.t=[_t0]
        self.r=_r
        self.time=_time
        self.dt=_dt
        self.n=int(self.time/self.dt)
    def calculate(self):
        for i in range(self.n):
            self.x.append(self.x[-1]+a*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+self.r*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-b*self.z[-1])*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot_zx(self,color):
        plt.plot(self.x,self.z,color)
    def plot_zy(self,color):
        plt.plot(self.y,self.z,color)
fig=plt.figure(figsize=(8,12))
ax1=plt.subplot(211)
A=Position(25)
A.calculate()
A.plot_zx('r-')
plt.title('Phase space plot:z vetsus x')
plt.xlabel('x')
plt.ylabel('z')
plt.legend()

ax2=plt.subplot(212)
B=Position(25)
B.calculate()
B.plot_zy('r-')
plt.title('Phase space plot:z vetsus y')
plt.xlabel('y')
plt.ylabel('z')
plt.legend()


plt.show()
```
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/8-3.png)

> 还可以做出相空间的截面图： 

- [x] code④：
```python
import matplotlib.pyplot as plt

a=10
b=8./3.

class Position():
    def __init__(self,_r,_x0=1,_y0=0,_z0=0,_t0=0,_time=500,_dt=0.0001):
        self.x=[_x0]
        self.y=[_y0]
        self.z=[_z0]
        self.t=[_t0]
        self.r=_r
        self.time=_time
        self.dt=_dt
        self.n=int(self.time/self.dt)
    def calculate(self):
        for i in range(self.n):
            self.x.append(self.x[-1]+a*(self.y[-1]-self.x[-1])*self.dt)
            self.y.append(self.y[-1]+(-self.x[-2]*self.z[-1]+self.r*self.x[-2]-self.y[-1])*self.dt)
            self.z.append(self.z[-1]+(self.x[-2]*self.y[-2]-b*self.z[-1])*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot_zy(self):
        y_section=[]
        z_section=[]
        for i in range(len(self.t)):
            if abs(self.x[i]-0.)<4E-3:
                y_section.append(self.y[i])
                z_section.append(self.z[i])
        plt.plot(y_section,z_section,'ok',markersize=2)
    def plot_zx(self):
        x_section=[]
        z_section=[]
        for i in range(len(self.t)):
            if abs(self.y[i]-0.)<4E-3:
                x_section.append(self.x[i])
                z_section.append(self.z[i])
        plt.plot(x_section,z_section,'ok',markersize=2)

plt.figure(figsize=(8,8))
a1=plt.subplot(211)
A=Position(25)
A.calculate()
A.plot_zy()
plt.title('Phase space plot:z vetsus y when x=0')
plt.xlabel('y')
plt.ylabel('z')
plt.ylim(0,30)
plt.xlim(-10,10)
plt.legend()

a2=plt.subplot(212)
B=Position(25)
B.calculate()
B.plot_zx()
plt.title('Phase space plot:z vetsus x when y=0')
plt.xlabel('x')
plt.ylabel('z')
plt.ylim(0,40)
plt.xlim(-20,20)
plt.legend()

plt.savefig('lorenz3.png')
plt.show()
```

![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/8-4.png)

### 四、总结
   随着r的增加，Lorenz模型伴随着混沌现象的产生与消失。
    
### 五、致谢
    感谢张凡同学。


