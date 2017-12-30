## 期末论文

### 一、摘要
   p181-235页 chapter 7：Rndom Systems.\
   关键词：随机游走；扩散；菲克定律；熵。

### 二、背景介绍
- 本文从随机游走出发，先研究了随机游走的一些性质，而后探究了扩散过程和随机游走的联系，并粗略探讨了扩散过程中的熵变。/
  在之前的学习中，我们讨论的所有系统都是确定性的。但是现实中更多的，我们碰到情况往往是随机的，不确定的。/
  其中，一类最简单的随机系统和问题就是随机游走和扩散现象。
- 随机游走：/
  随机游走（random walk）也称随机漫步，随机行走等是指基于过去的表现，无法预测将来的发展步骤和方向。核心概念是指任何无规则行走者所带的守恒量都各自对应着一个扩散运输定律 ，接近于布朗运动，是布朗运动理想的数学状态，现阶段主要应用于互联网链接分析及金融股票市场中。在我们生活中处处都存在着与Random Walk有关的自然现象，例如气体分子的运动，滴入水中的墨水，气味的扩散等。Random Walk是扩散过程的基础，因此它被广泛地用于对物理和化学等扩散现象的模拟上。 
  
- 无规则行走：/
  无规则行走在任意尺度上都具有相似结构。例如，要想找出第1000 步后你走了多远，我们可以将所有2的N次方 种可能行走一一配对，每一配对由相同的x（N-1 ）；{（N-1)为x的下脚标}的两个可能性相等的行走组成，只是最后一步不同。N 步随机性走的均方位移比N－1 步大a的2次方，后者又比N－2 步大a的2次方，均方位移=Na的2次方。a 为格子间隔，每一个格子点上游动的可能方向有2d 个（d 是格子维数）单位时间内游动的方差为D=a2/(2d)t ，D 为扩散系数。a后面的2为次方，后面凡数字在字母后面都表示指数）。对于一维无规则行走的均方位移随时间线性增加2Kt，扩散常数D=a2/(2Δt)。这个逻辑可以推广到二维和三维。
  也许行走若干个步后他会回到出发点，但这样的概率非常小。他离开酒吧的距离满足扩散定律：
  (a)二维无规则行走；
  (b)当步骤更多，步幅更低时二维无规则行走；
  (c)三维无规则行走。
  
- 扩散定律：/  
  扩散以一个初始分布释放大量的无规则行走，观察他们的密度，就会得到分布函数。
  扩散是一个随机涨落的过程，在本科一年级的物理课程已经提及一个落体最终会达到取决于摩擦的“末速度”。以悬浮颗粒来考虑摩擦，颗粒虽然受随机碰撞，仍获得了一个净漂移速度。v=f/ζ ，ζ=2m/Δt ，其中ζ是黏性摩擦系数，与扩散系数一样可以实验测量。摩擦源于物理实体与周围热致扰动的流体随机碰撞。每一种颗粒当置于不同的溶剂中时都会有相应特征D（扩散系数）和ζ。
  由于有效步长a 和Δt 无法观察，要想证实扩散与粘滞仅仅是热运动的两个方面，我们还需要第三个关系。爱因斯坦注意到a 和Δt 的关系，按照推到理想气体定律的思路：(a/Δt)2=kBT/m，联合起来就构成爱因斯坦第一扩散公式：ζD=kBT。越小的颗粒受到摩擦阻力越小，但扩散系数会更大，更容易扩散。ζD 的乘积提供了一个可证伪的预言来检验“热即分子的无规则运动”；这个预言提出不久就立刻被佩兰（Jeans Perrin）和其他人的实验所证实。任何无规则行走携带的守恒量都各自对应一个扩散定律。
  
   扩散以一个初始分布释放大量的无规则行走，观察他们的密度就会得到分布函数。1855年法国生理学家阿道夫·菲克提出了描述扩散规律的基本公式——菲克定律。
<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/DiffusionMicroMacro.gif?raw=true" /></div>
<div align=center>不同尺度下观察到的扩散过程</div>
   ①菲克第一定律假设从高浓度区域往低浓度流的通量大小与浓度梯度（空间导数）成正比，通过这个假设，菲克第一定律把扩散通量与浓度联系起来。在一维空间下的菲克第一定律如下：
<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=J=-D\frac{\partial&space;\phi&space;}{\partial&space;x}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?J=-D\frac{\partial&space;\phi&space;}{\partial&space;x}" title="J=-D\frac{\partial \phi }{\partial x}" /></a></div>

  根据斯托克斯-爱因斯坦关系，<a href="http://www.codecogs.com/eqnedit.php?latex=D" target="_blank"><img src="http://latex.codecogs.com/gif.latex?D" title="D" /></a>的大小取决于温度、流体黏度与分子大小，并与扩散分子流动的平均速度平方成正比。

  ②在二维或以上的情况下，我们必须使用<a href="http://www.codecogs.com/eqnedit.php?latex=\nabla" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\nabla" title="\nabla" /></a>来把第一导数通用化，得
<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=J=-D\nabla\phi" target="_blank"><img src="http://latex.codecogs.com/gif.latex?J=-D\nabla\phi" title="J=-D\nabla\phi" /></a></div>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;菲克第二定律预测扩散会如何使得浓度随时间改变：
<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;\phi&space;}{\partial&space;t}=D\frac{\partial&space;^{2}\varphi&space;}{\partial&space;x^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\partial&space;\phi&space;}{\partial&space;t}=D\frac{\partial&space;^{2}\varphi&space;}{\partial&space;x^{2}}" title="\frac{\partial \phi }{\partial t}=D\frac{\partial ^{2}\varphi }{\partial x^{2}}" /></a></div>
  对于二维或以上的扩散，其菲克第二定律为：
<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;\phi&space;}{\partial&space;t}=D\nabla^{2}\varphi" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\partial&space;\phi&space;}{\partial&space;t}=D\nabla^{2}\varphi" title="\frac{\partial \phi }{\partial t}=D\nabla^{2}\varphi" /></a></div>
其形式跟热传导方程类似。
  
- 熵：/  
  化学及热力学中所指的熵，是一种测量在动力学方面不能做功的能量总数，也就是当总体的熵增加，其做功能力也下降，熵的量度正是能量退化的指标。熵亦被用于计算一个系统中的失序现象，也就是计算该系统混乱的程度。熵是一个描述系统状态的函数，但是经常用熵的参考值和变化量进行分析比较，它在控制论、概率论、数论、天体物理、生命科学等领域都有重要应用，在不同的学科中也有引申出的更为具体的定义，是各领域十分重要的参量。
  1877年，玻尔兹曼发现单一系统中的熵跟构成热力学性质的微观状态数量相关。可以考虑情况如：一个容器内的理想气体。微观状态可以以每个组成的原子的位置及动量予以表达。为了一致性起见，我们只需考虑包含以下条件的微观状态：
  （i）所有粒子的位置皆在容器的体积范围内；
  （ii）所有原子的动能总和等于该气体的总能量值。
  玻尔兹曼提出一个系统的熵和所有可能微观状态的数目满足以下简单关系：
<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=S=k\ln\Omega" target="_blank"><img src="http://latex.codecogs.com/gif.latex?S=k\ln\Omega" title="S=k\ln\Omega" /></a></div>
  这个公式称为“玻尔兹曼公式”，根据玻尔兹曼的定义，熵是一则关于状态的函数。并且因为<a href="http://www.codecogs.com/eqnedit.php?latex=\Omega" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\Omega" title="\Omega" /></a>是一个自然数（1,2,3,...），熵必定是个非负数。
根据这个公式，我们可以将熵看作是一个系统“混乱程度”的度量，因为一个系统越混乱，可以看作是微观状态分布越均匀。根据熵的统计学定义，热力学第二定律说明一个孤立系统的倾向于增加混乱程度。

 - 理想状态：无规则行走是布朗运动的理想状态。

  
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