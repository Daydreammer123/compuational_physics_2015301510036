## 第五次作业

### 一、摘要
本次作业是书本第二单元2.9及其扩展。 \
关键词：炮弹轨迹，欧拉法，空气阻力，最大发射角

### 二、背景介绍
　1.　不考虑空气阻力对物体的影响时，抛体运动方程可分解成两个垂直方向的二阶常微分方程。\
　2.　考虑空气阻力，但不考虑空气密度的变化。 \
　3.　考虑绝热近似，用欧拉法求出个轨迹曲线，用图像进行分析并给出实际情况下的最大发射角度。

### 三、正文
* 1、当不考虑空气阻力时，数值求解二阶线性常微分方程组:\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/511.png)

可以把它化为四个一阶常微分方程: \
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/512.png)

式中vx和vy分别为速度的水平和垂直分量。使用欧拉法，将每个方程写为有限小量形式，以计算每隔dt炮弹位置和速度的变化，给定位置和速度的初始值，计算此后的运动状态。当dt足够小时，用欧拉法数值计算的结果趋近于真实（解析）解。 \

无阻力情况代码：
```python
g = 9.8
b2m = 1e-5

class flight_state:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.t = _t

class cannon:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt
        #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
        next_t = current_state.t + self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, next_t)

    def shoot(self):
        while not(self.cannon_flight_state[-1].y < 0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0
        #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy


    def show_trajectory(self):
        global x,y        
        x = []
        y = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)



a = cannon(flight_state(0, 0, 700*cos(pi*30/180), 700*sin(pi*30/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'r',label = r'$\theta=30^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
a_final = x[-1]


a = cannon(flight_state(0, 0, 700*cos(pi*35/180), 700*sin(pi*35/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'b',label=r'$\theta=35^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]


a = cannon(flight_state(0, 0, 700*cos(pi*40/180), 700*sin(pi*40/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'y',label=r'$\theta=40^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]


a = cannon(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'c',label=r'$\theta=45^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]


a = cannon(flight_state(0, 0, 700*cos(pi*50/180), 700*sin(pi*50/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'g',label=r'$\theta=50^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]



a = cannon(flight_state(0, 0, 700*cos(pi*55/180), 700*sin(pi*55/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,color='m',label=r'$\theta=55^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]



title('trajectory of cannon shell')
xlabel('x(km)')
ylabel('y(km)')
show()
```

无阻力情况效果图：

![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/5-1.png)
 
由图可以看出：45度角是无阻力情况的最大发射角；而且相加为90度的射程相同。

* 2、当考虑空气阻力时:\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/521.png)

化为微分表达式:\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/522.png)

有阻力情况代码:
```python
g = 9.8
b2m = 1e-5

class flight_state:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.t = _t

class cannon:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt
        #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
        next_t = current_state.t + self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, next_t)

    def shoot(self):
        while not(self.cannon_flight_state[-1].y < 0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0
        #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy


    def show_trajectory(self):
        global x,y        
        x = []
        y = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)

class drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

class adiabatic_drag_cannon(cannon):
    def next_state(self, current_state):
        pass


a = cannon(flight_state(0, 0, 900*cos(pi*30/180), 900*sin(pi*30/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'r',label = r'$\theta=30^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
a_final = x[-1]

b = drag_cannon(flight_state(0, 0, 900*cos(pi*30/180), 900*sin(pi*30/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'r--', label = r'$drag\theta=30^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = cannon(flight_state(0, 0, 900*cos(pi*35/180), 900*sin(pi*35/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'b',label=r'$\theta=35^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

b = drag_cannon(flight_state(0, 0, 900*cos(pi*35/180), 900*sin(pi*35/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'b--', label = r'$drag\theta=35^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = cannon(flight_state(0, 0, 900*cos(pi*40/180), 900*sin(pi*40/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'y',label=r'$\theta=40^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

b = drag_cannon(flight_state(0, 0, 900*cos(pi*40/180), 900*sin(pi*40/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'y--', label = r'$drag\theta=40^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = cannon(flight_state(0, 0, 900*cos(pi*45/180), 900*sin(pi*45/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'c',label=r'$\theta=45^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

b = drag_cannon(flight_state(0, 0, 900*cos(pi*45/180), 900*sin(pi*45/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'c--', label = r'$drag\theta=45^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = cannon(flight_state(0, 0, 900*cos(pi*50/180), 900*sin(pi*50/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'g',label=r'$\theta=50^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

b = drag_cannon(flight_state(0, 0, 900*cos(pi*50/180), 900*sin(pi*50/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'g--', label = r'$drag\theta=50^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = cannon(flight_state(0, 0, 900*cos(pi*60/180), 900*sin(pi*60/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,color='m',label=r'$\theta=60^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]

b = drag_cannon(flight_state(0, 0, 900*cos(pi*60/180), 900*sin(pi*60/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'m--', label = r'$drag\theta=60^\circ$')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

title('trajectory of cannon shell')
xlabel('x(km)')
ylabel('y(km)')
show()
```
无阻力情况效果图:\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/5-2.png)

可以看出：还是45度为最大发射角，但是“相加为90的射程相同”不成立。
* 3、考虑绝热模型:\
空气密度随高度变化的关系为:\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/531.png)

故微分方程的修改项变为:\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/532.png)

绝热模型代码:
```python
g = 9.8
b2m = 1e-5

class flight_state:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.t = _t

class cannon:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt
        #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
        next_t = current_state.t + self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, next_t)

    def shoot(self):
        while not(self.cannon_flight_state[-1].y < 0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0
        #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy


    def show_trajectory(self):
        global x,y        
        x = []
        y = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)

class drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)


class adiabatic_drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
        factor = (1 - 6.5e-3 * current_state.y / 288.15) ** 2.5
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt * factor
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

b = drag_cannon(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
b.shoot()
b.show_trajectory()
plot(x,y,'c', label = 'with drag')
legend(loc = 'best', prop = {'size':11}, frameon = False)
b_final = x[-1]

a = cannon(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
a.shoot()
a.show_trajectory()
plot(x,y,'m',label='no drag')
legend(loc='best',prop={'size':11},frameon=False)
a_final=x[-1]


d = adiabatic_drag_cannon(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
d.shoot()
d.show_trajectory()
plot(x,y,'y',label='adiabatic approximation')
legend(loc='best',prop={'size':11},frameon=False)
d_final=x[-1]

text(10000,16000,r'$\theta=45^\circ$')
title('trajectory of cannon shell with different drag')
xlabel('x(km)')
ylabel('y(km)')
xlim(0,60000)
ylim(0,18000)
show()

```
绝热模型效果图 ：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/5-3.png)

* 4、绝热情况下的最大发射角:\

绝热模型最大发射角代码：
```python
g = 9.8
b2m = 1e-5

class flight_state:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.t = _t

class cannon:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt
        #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
        next_t = current_state.t + self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, next_t)

    def shoot(self):
        while not(self.cannon_flight_state[-1].y < 0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0
        #print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy


    def show_trajectory(self):
        global x,y        
        x = []
        y = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)


class adiabatic_drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
        factor = (1 - 6.5e-3 * current_state.y / 288.15) ** 2.5
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt * factor
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

d = adiabatic_drag_cannon(flight_state(0, 0, 700*cos(pi*35/180), 700*sin(pi*35/180), 0), _dt = 0.1)
d.shoot()
d.show_trajectory()
plot(x,y,'y',label=r'$\theta=35^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
d_final=x[-1]

d = adiabatic_drag_cannon(flight_state(0, 0, 700*cos(pi*40/180), 700*sin(pi*40/180), 0), _dt = 0.1)
d.shoot()
d.show_trajectory()
plot(x,y,'c',label=r'$\theta=40^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
d_final=x[-1]

d = adiabatic_drag_cannon(flight_state(0, 0, 700*cos(pi*42.5/180), 700*sin(pi*42.5/180), 0), _dt = 0.1)
d.shoot()
d.show_trajectory()
plot(x,y,'r--',label=r'$\theta=42.5^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
d_final=x[-1]

d = adiabatic_drag_cannon(flight_state(0, 0, 700*cos(pi*45/180), 700*sin(pi*45/180), 0), _dt = 0.1)
d.shoot()
d.show_trajectory()
plot(x,y,'r',label=r'$\theta=45^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
d_final=x[-1]

d = adiabatic_drag_cannon(flight_state(0, 0, 700*cos(pi*50/180), 700*sin(pi*50/180), 0), _dt = 0.1)
d.shoot()
d.show_trajectory()
plot(x,y,'m',label=r'$\theta=50^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
d_final=x[-1]



d = adiabatic_drag_cannon(flight_state(0, 0, 700*cos(pi*55/180), 700*sin(pi*55/180), 0), _dt = 0.1)
d.shoot()
d.show_trajectory()
plot(x,y,'g',label=r'$\theta=55^\circ$')
legend(loc='best',prop={'size':11},frameon=False)
d_final=x[-1]


title('trajectory of cannon shell with adiabatic_drag')
xlabel('x(km)')
ylabel('y(km)')
xlim(0,60000)
ylim(0,18000)
show()
```
绝热模型最大发射角效果图：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/5-4.png)

可以看出：最大发射角可能不再是45度，随参数的变化而变化。

### 四、总结
1、不考虑空气阻力时，45度角是无阻力情况的最大发射角；而且相加为90度的射程相同。
2、考虑空气阻力时，仍然是45度为最大发射角，但是“相加为90的射程相同”不成立。
3、绝热模型下，最大发射角可能不再是45度，随参数的变化而变化。

### 五、致谢
    感谢王智麟同学~
