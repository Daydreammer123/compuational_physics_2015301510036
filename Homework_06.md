## 第六次作业

### 一、摘要
    本次作业是书本43页2.19题：分别在顺风逆风和棒球自身有无自旋角速度的条件下，解析法求出棒球的运动轨迹，对比各种情况。\
    关键词：棒球运动，顺风逆风，角速度，自旋

### 二、背景介绍
- 思路:\
①先考虑下旋球，不考虑左右两个方向，故建立二维xy坐标系。\
![](http://latex.codecogs.com/gif.latex?d_{x}{=}v_{x}dt)\
![](http://latex.codecogs.com/gif.latex?d_{y}{=}v_{y}dt)\
![](http://latex.codecogs.com/gif.latex?dv_{x}{=}\left(\frac{-B_{2}vv_{x}}{m}-\frac{S_{0}v_{x}w}{m}\right)dt)\
![](http://latex.codecogs.com/gif.latex?dv_{y}{=}\left(\frac{-B_{2}vv_{y}}{m}+\frac{S_{0}v_{y}w}{m}\right)dt-gdt)\
其中\
![](http://latex.codecogs.com/gif.latex?\frac{S_{0}}{m}{=}0.00041)\
![](http://latex.codecogs.com/gif.latex?\frac{B_{2}}{m}{=}0.0039+\frac{0.0058}{1+z})\
![](http://latex.codecogs.com/gif.latex?z{=}1+e^{\frac{v-vd}{\bigtriangleup}})\
![](http://latex.codecogs.com/gif.latex?v_{d}{=}35m/s),![](http://latex.codecogs.com/gif.latex?\bigtriangleup{=}5m/s)

②定义一个新的类——ball，其属性是球的运动状态，包括位置、速度、角速度，计算下一刻的状态，只需不断使用该方法，并记录下每次的状态，即可得到轨迹.

```python
class ball:
    def __init__(self,v,theta):
        self.x=0.0
        self.y=1.5
        self.vx=v*math.cos(math.pi*theta/180)
        self.vy=v*math.sin(math.pi*theta/180)
        self.w=2000*2*math.pi/60       
    def fly(self):
        self.x=self.x+self.vx*dt
        self.y=self.y+self.vy*dt
        self.vx=self.vx+(-B2m(abs(self.vx-vwind))*(self.vx-vwind)*math.sqrt((self.vx-vwind)*(self.vx-vwind)+self.vy+self.vy)-S0m*self.vy*self.w)*dt
        self.vy=self.vy+(-B2m(abs(self.vy))*self.vy*math.sqrt((self.vx-vwind)*(self.vx-vwind)+self.vy+self.vy)+S0m*(self.vx-vwind)*self.w-g)*dt
```
③接下来的语句就是循环执行fly方法，记录下每次的位置，即可用plot作图.

```python
S0m=4.1e-4 #backspin
vwind=4.4704 #10mph,tailwind
a=ball(50,35)
x1=[]
y1=[]
x1.append(a.x)
y1.append(a.y)
while a.y>0:
    a.fly()
    x1.append(a.x)
    y1.append(a.y)
x1[-1]=(x1[-2]-y1[-2]*x1[-1]/y1[-1])/(1-y1[-2]/y1[-1])
y1[-1]=0
```


### 三、正文
- 实验代码

```python
import math
import matplotlib.pyplot as plt

g=9.8
dt=0.01

def B2m(v):
    'Calculate air resistance factor'
    B2m=0.0039+0.0058/(1+math.exp((v-35)/5))
    return B2m
        
class ball:
    def __init__(self,v,theta):
        self.x=0.0
        self.y=1.5
        self.vx=v*math.cos(math.pi*theta/180)
        self.vy=v*math.sin(math.pi*theta/180)
        self.w=2000*2*math.pi/60
        
    def fly(self):
        self.x=self.x+self.vx*dt
        self.y=self.y+self.vy*dt
        self.vx=self.vx+(-B2m(abs(self.vx-vwind))*(self.vx-vwind)*math.sqrt((self.vx-vwind)*(self.vx-vwind)+self.vy+self.vy)-S0m*self.vy*self.w)*dt
        self.vy=self.vy+(-B2m(abs(self.vy))*self.vy*math.sqrt((self.vx-vwind)*(self.vx-vwind)+self.vy+self.vy)+S0m*(self.vx-vwind)*self.w-g)*dt

S0m=4.1e-4 #backspin
vwind=4.4704 #10mph,tailwind
a=ball(50,45)
x1=[]
y1=[]
x1.append(a.x)
y1.append(a.y)
while a.y>0:
    a.fly()
    x1.append(a.x)
    y1.append(a.y)
x1[-1]=(x1[-2]-y1[-2]*x1[-1]/y1[-1])/(1-y1[-2]/y1[-1])
y1[-1]=0   

vwind=-4.4704 #10mph,headwind
b=ball(50,45)
x2=[]
y2=[]
x2.append(b.x)
y2.append(b.y)
while b.y>0:
    b.fly()
    x2.append(b.x)
    y2.append(b.y)
x2[-1]=(x2[-2]-y2[-2]*x2[-1]/y2[-1])/(1-y2[-2]/y2[-1])
y2[-1]=0

S0m=0.0 #nospin
vwind=4.4704 #10mph,tailwind
a=ball(50,45)
x3=[]
y3=[]
x3.append(a.x)
y3.append(a.y)
while a.y>0:
    a.fly()
    x3.append(a.x)
    y3.append(a.y)
x3[-1]=(x3[-2]-y3[-2]*x3[-1]/y3[-1])/(1-y3[-2]/y3[-1])
y3[-1]=0   

vwind=-4.4704 #10mph,headwind
b=ball(50,45)
x4=[]
y4=[]
x4.append(b.x)
y4.append(b.y)
while b.y>0:
    b.fly()
    x4.append(b.x)
    y4.append(b.y)
x4[-1]=(x4[-2]-y4[-2]*x4[-1]/y4[-1])/(1-y4[-2]/y4[-1])
y4[-1]=0

plt.plot(x1,y1,color='blue',label='tailwind,backspin')
plt.plot(x2,y2,color='red',label='headwind,backspin')
plt.plot(x3,y3,color='green',label='tailwind,nospin')
plt.plot(x4,y4,color='orange',label='headwind,nospin')
plt.xlabel('x/m')
plt.ylabel('y/m')
plt.xlim(0,180)
plt.legend(loc="upper right", frameon=True,prop={'size':10})
plt.show()
print ('distance with tailwind and backspin=',x1[-1])
print ('distance with headwind and backspin=',x2[-1])
print ('distance with tailwind and nospin=',x3[-1])
print ('distance with headwind and nospin=',x4[-1])
```   
效果图：

![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/6.png)


### 四、总结
   分析图片了可以看出：不考虑自旋，顺风比逆风更高更远。考虑自旋时，逆风条件下下旋球会比无自旋是更高更远
    
### 五、致谢
   谢谢王智麟的指导~
