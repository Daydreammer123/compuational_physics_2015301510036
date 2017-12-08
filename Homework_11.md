## 第十一次作业

### 一、摘要
   p143页5.3题：Show that the Poincare sections in Figure 3.17 are independent of the initial conditions.\
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

可知Lprenz模型内流体运动显著依赖于驱动r，当改变驱动r的大小时，可观察到混沌的产生和消失。
- [ ] 取![](http://latex.codecogs.com/gif.latex?\sigma=10,b=8/3),初始值x=1，y=z=0，在不同的r值时画出速度z随时间的变化曲线：

code1：
```python

```

![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/8-1.png)

- [ ] 发现，在r值较小时，z出现阻尼衰减的现象，但当r值增大到一定值时出现了复杂的混沌现象.\
于是我们将r值继续增大到160及163.8，作出相空间的图形：

code2：
```python

```

![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/8-4.png)

### 四、总结
   随着r的增加，Lorenz模型伴随着混沌现象的产生与消失。
    
### 五、致谢
    感谢张凡同学。

