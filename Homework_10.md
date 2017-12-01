## 第十次作业

### 一、摘要
  p118页4.16题：利用欧拉克罗默的方法，研究三体问题。\
  关键词：三体问题，木星。

### 二、背景介绍
- 三体系统是一个值得研究的问题，它有一个混沌的行为，因此不能被解析解。但是在三体系统中，行星运动有许多有趣的的现象。
- 现在考虑一个假设的理想太阳、地球和一个伪木星组成的天体系统，我们研究了其在不同初始条件下地球的运动模型。

### 三、正文
思路：
> 已知太阳质量为：![](http://latex.codecogs.com/gif.latex?M_{S}=2.0\times10^{30}kg) \
地球质量为：![](http://latex.codecogs.com/gif.latex?M_{E}=6.0\times10^{24}kg) \
木星质量为：![](http://latex.codecogs.com/gif.latex?M_{J}=1.9\times10^{27}kg) \
由受力公式可知，每个天体的总受力为每个其他天体对它的力的矢量和，为：![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/101.png)，这里只计算太阳，地球和木星。 
接下来讨论各种情形：
* 1、在质心系下。太阳保持不动，木星与地球绕太阳做圆周运动，三者保持稳定运动状态。这是由于太阳的质量相对其余二者而言相当大，木星对地球的影响可以忽略\
①代码：
```python
import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d

#Determine the initial value
def initial(a,e):
    x0=a*(1+e)
    v_y0=2*pi*sqrt((1-e)/(a*(1+e)))
    return [x0,v_y0]

def three_orbits(m_e,m_j,m_s):
#Earth
    x_e0=initial(1,0.023)[0]
    x_e=[]
    x_e.append(x_e0)
    
    v_ex0=0
    v_ex=[]
    v_ex.append(v_ex0)

    y_e0=0
    y_e=[]
    y_e.append(y_e0)
    
    v_ey0=initial(1,0.023)[1]
    v_ey=[]
    v_ey.append(v_ey0)
#Jupiter
    x_j0=initial(5.2,0.3)[0]
    x_j=[]
    x_j.append(x_j0)
    
    v_jx0=0
    v_jx=[]
    v_jx.append(v_jx0)

    y_j0=0
    y_j=[]
    y_j.append(y_j0)
    
    v_jy0=initial(5.2,0.3)[1]
    v_jy=[]
    v_jy.append(v_jy0)
#Sun
    x_s0=0
    x_s=[]
    x_s.append(x_s0)
    
    v_sx0=0
    v_sx=[]
    v_sx.append(v_sx0)

    y_s0=0
    y_s=[]
    y_s.append(y_s0)
    
    v_sy0=-(m_e*v_ey0+m_j*v_jy0)/m_s
    v_sy=[]
    v_sy.append(v_sy0)
#r
    r_es=[]
    r_es.append(sqrt((x_e0-x_s0)**2+(y_e0-y_s0)**2))
    r_js=[]
    r_js.append(sqrt((x_j0-x_s0)**2+(y_j0-y_s0)**2))
    r_ej=[]
    r_ej.append(sqrt((x_e0-x_j0)**2+(y_e0-y_j0)**2))

    t=[]
    t.append(0)
    time=40.0
    dt=0.001

    
    for i in range(int(time/dt)):
#Earth
        v_ex.append(v_ex[i]+dt*(4*pi**2*(x_s[i]-x_e[i])/(r_es[i]**3)+4*pi**2*m_j/m_s*(x_j[i]-x_e[i])/(r_ej[i]**3)))
        x_e.append(x_e[i]+v_ex[i+1]*dt)
        v_ey.append(v_ey[i]+dt*(4*pi**2*(y_s[i]-y_e[i])/(r_es[i]**3)+4*pi**2*m_j/m_s*(y_j[i]-y_e[i])/(r_ej[i]**3)))
        y_e.append(y_e[i]+v_ey[i+1]*dt)
#Jupiter
        v_jx.append(v_jx[i]+dt*(4*pi**2*(x_s[i]-x_j[i])/(r_js[i]**3)+4*pi**2*m_e/m_s*(x_e[i]-x_j[i])/(r_ej[i]**3)))
        x_j.append(x_j[i]+v_jx[i+1]*dt)
        v_jy.append(v_jy[i]+dt*(4*pi**2*(y_s[i]-y_j[i])/(r_js[i]**3)+4*pi**2*m_e/m_s*(y_e[i]-y_j[i])/(r_ej[i]**3)))
        y_j.append(y_j[i]+v_jy[i+1]*dt)
#Sun
        v_sx.append(v_sx[i]+dt*(4*pi**2*m_e/m_s*(x_e[i]-x_s[i])/(r_es[i]**3)+4*pi**2*m_j/m_s*(x_j[i]-x_s[i])/(r_js[i]**3)))
        x_s.append(x_s[i]+v_sx[i+1]*dt)
        v_sy.append(v_sy[i]+dt*(4*pi**2*m_e/m_s*(y_e[i]-y_s[i])/(r_es[i]**3)+4*pi**2*m_j/m_s*(y_j[i]-y_s[i])/(r_js[i]**3)))
        y_s.append(y_s[i]+v_sy[i+1]*dt)

        r_es.append(sqrt((x_e[i+1]-x_s[i+1])**2+(y_e[i+1]-y_s[i+1])**2))
        r_js.append(sqrt((x_j[i+1]-x_s[i+1])**2+(y_j[i+1]-y_s[i+1])**2))
        r_ej.append(sqrt((x_e[i+1]-x_j[i+1])**2+(y_e[i+1]-y_j[i+1])**2))

        t.append(t[i]+dt)
    return [x_e,y_e,x_j,y_j,x_s,y_s,t]
m_e=1.0
m_j=316.7
m_s=333333.3
thr=three_orbits(m_e,m_j,m_s)
x_e=thr[0]
y_e=thr[1]
x_j=thr[2]
y_j=thr[3]
x_s=thr[4]
y_s=thr[5]
t=thr[6]

#plot
plt.figure(figsize=[9,9])
plt.plot(x_e,y_e,color='yellow',label='Earth')
plt.plot(x_j,y_j,color='black',label='Jupiter')
plt.plot(x_s,y_s,color='red',label='Sun')
plt.legend(loc='upper right')
plt.title('three-body,change the initial condition',fontsize=15)
plt.xlabel('x/AU')
#xlim(-6,6)
plt.ylabel('y/AU')
#ylim(-6,6)
plt.show()
#3D plot
fig = figure(figsize=[9,9])
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_e,y_e,t,color='yellow',label='Earth')
ax.plot(x_j,y_j,t,color='black',label='Jupiter')
ax.plot(x_s,y_s,t,color='red',label='Sun')
legend(loc='upper right')
ax.set_xlabel('x/Au')
ax.set_ylabel('y/AU')
ax.set_zlabel('t/yr')
show()
```
②截面图：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/102.png)\
3D图：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/103.png)\

③改变初始条件有\
截面图:\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/104.png)\
3D图：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/105.png)\


* 2、在质心系下。同样可以得出木星质量变大10倍，100倍，1000倍的截面图和三维图：\
①木星质量变大10倍:
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/107.png)\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/108.png)\
②木星质量变大100倍:
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/109.png)\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/1010.png)\
③木星质量变大1000倍:
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/1011.png)\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/1012.png)\


### 四、总结
    1、改变初始条件时：可以发现，质心系下，保持总动量为0，在木星初始速度变大的条件下，地球绕太阳做圆周，但是太阳的位置偏离了中心。\
    2、改变木星的质量时：①当木星质量改为10倍时，太阳受影响很小。\
                       ②当木星质量改为100倍时，太阳做圆周运动，地球绕地球做圆周，木星不变。\
                       ③当木星质量改为1000倍时，木星偏离太阳。\
    3、不同的条件下，三体问题会产生不同的运动。
   
### 五、致谢
    感谢郭潇同学。
