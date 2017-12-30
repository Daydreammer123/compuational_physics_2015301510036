## 期末论文

### 一、摘要
   p181-235页 chapter 7：Rndom Systems.\
   关键词：随机游走；SAW；SAP；扩散；菲克定律；熵。

### 二、背景介绍
- 本文从随机游走出发，先研究了随机游走的一些性质，而后探究了扩散过程和随机游走的联系，并粗略探讨了扩散过程中的熵变。
  在之前的学习中，我们讨论的所有系统都是确定性的。但是现实中更多的，我们碰到情况往往是随机的，不确定的。
  其中，一类最简单的随机系统和问题就是随机游走和扩散现象。
- 台球动力系统拥有哈密顿系统从可积性到混沌运动的所有复杂性，无须对运动方程进行困难的积分就可确定其庞加莱截面。乔治·大卫·比尔霍夫证明一个椭圆边界的台球动力系统是可积的。

### 三、正文
* 1、思路：\
① 台球动力系统示意图：
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/911.jpg)

② 一个混沌台球动力系统中粒子的轨迹：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/912.jpg)

③ 在完美的台球桌上，我们考虑一个没有摩擦的球移动的问题，碰撞速度是恒定的，所以我们有\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/913.png)\
确定一个碰撞点，我们得到在碰撞点处垂直于墙的单位向量\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/914.png)\
我们对速度进行分解可得\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/916.png)\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/917.png)\
当粒子撞击边界时有\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/918.png)\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/919.png)\

* 2、代码:
```python

```
①T = 50，单位圆下反弹\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/921.png)\
②T = 100，单位圆下反弹\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/922.png)\
③相空间情节\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/923.png)

3.考虑到在两半圆间增加宽为2α的矩形，并得到动画，代码如下:\
```python

```
①α= 0.1\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/931.png)\
②动图：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/932.gif)

4.用欧拉法进行数值模拟\
```python

```

如图：\
![image](https://github.com/lilyechoC/compuational_physics_2015301510036/blob/master/pictures/971.gif)\


### 四、总结
1.可以看出α不同时，李雅普诺夫指数截然不同；相同α下，不同的初始距离d可能导致李雅普诺夫指数的些微不同\
2.α越小曲线越密集，这说明系统经历了更多状态，可以预见，当α足够大即台球桌足够长时混沌现象可能会消失
    
### 五、致谢
    感谢彭成铭倪、世杰同学鼎力相助~。
