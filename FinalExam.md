## 期末论文

### 一、摘要
   p181-235页 chapter 7：Rndom Systems.\
   关键词：随机游走；扩散；菲克定律；熵。

### 二、背景介绍
- 本文从随机游走出发，先研究了随机游走的一些性质，而后探究了扩散过程和随机游走的联系，并粗略探讨了扩散过程中的熵变。\
      在之前的学习中，我们讨论的所有系统都是确定性的。但是现实中更多的，我们碰到情况往往是随机的，不确定的。\
  其中，一类最简单的随机系统和问题就是随机游走和扩散现象。
  ![image]()
  
- 随机游走：\
    随机游走（random walk）也称随机漫步，随机行走等是指基于过去的表现，无法预测将来的发展步骤和方向。核心概念是指任何无规则行走者所带的守恒量都各自对应着一个扩散运输定律 ，接近于布朗运动，是布朗运动理想的数学状态，现阶段主要应用于互联网链接分析及金融股票市场中。在我们生活中处处都存在着与Random Walk有关的自然现象，例如气体分子的运动，滴入水中的墨水，气味的扩散等。Random Walk是扩散过程的基础，因此它被广泛地用于对物理和化学等扩散现象的模拟上。 
    ![image]()
  
- 无规则行走：\
    无规则行走在任意尺度上都具有相似结构。例如，要想找出第1000 步后你走了多远，我们可以将所有2的N次方 种可能行走一一配对，每一配对由相同的x（N-1 ）；{（N-1)为x的下脚标}的两个可能性相等的行走组成，只是最后一步不同。N 步随机性走的均方位移比N－1 步大a的2次方，后者又比N－2 步大a的2次方，均方位移=Na的2次方。a 为格子间隔，每一个格子点上游动的可能方向有2d 个（d 是格子维数）单位时间内游动的方差为D=a2/(2d)t ，D 为扩散系数。a后面的2为次方，后面凡数字在字母后面都表示指数）。对于一维无规则行走的均方位移随时间线性增加2Kt，扩散常数D=a2/(2Δt)。这个逻辑可以推广到二维和三维。也许行走若干个步后他会回到出发点，但这样的概率非常小。
  
  他离开酒吧的距离满足扩散定律：\
  (a)二维无规则行走；\
  (b)当步骤更多，步幅更低时二维无规则行走；\
  (c)三维无规则行走。
  ![image]()
  
- 扩散定律：\
    扩散以一个初始分布释放大量的无规则行走，观察他们的密度，就会得到分布函数。\
  扩散是一个随机涨落的过程，在本科一年级的物理课程已经提及一个落体最终会达到取决于摩擦的“末速度”。以悬浮颗粒来考虑摩擦，颗粒虽然受随机碰撞，仍获得了一个净漂移速度。v=f/ζ ，ζ=2m/Δt ，其中ζ是黏性摩擦系数，与扩散系数一样可以实验测量。摩擦源于物理实体与周围热致扰动的流体随机碰撞。每一种颗粒当置于不同的溶剂中时都会有相应特征D（扩散系数）和ζ。\
    由于有效步长a 和Δt 无法观察，要想证实扩散与粘滞仅仅是热运动的两个方面，我们还需要第三个关系。爱因斯坦注意到a 和Δt 的关系，按照推到理想气体定律的思路：(a/Δt)2=kBT/m，联合起来就构成爱因斯坦第一扩散公式：ζD=kBT。越小的颗粒受到摩擦阻力越小，但扩散系数会更大，更容易扩散。ζD 的乘积提供了一个可证伪的预言来检验“热即分子的无规则运动”；这个预言提出不久就立刻被佩兰（Jeans Perrin）和其他人的实验所证实。任何无规则行走携带的守恒量都各自对应一个扩散定律。\
     扩散以一个初始分布释放大量的无规则行走，观察他们的密度就会得到分布函数。1855年法国生理学家阿道夫·菲克提出了描述扩散规律的基本公式——菲克定律。   
![image]()\
   
   ①菲克第一定律,假设从高浓度区域往低浓度流的通量大小与浓度梯度（空间导数）成正比，通过这个假设，菲克第一定律把扩散通量与浓度联系起来。在一维空间下的菲克第一定律如下： 
![image]()  
  根据斯托克斯-爱因斯坦关系，D的大小取决于温度、流体黏度与分子大小，并与扩散分子流动的平均速度平方成正比。
  
   ②在二维或以上的情况下，我们必须使用![image]()来把第一导数通用化，得[image]() 
  菲克第二定律预测扩散会如何使得浓度随时间改变：![image]()
  对于二维或以上的扩散，其菲克第二定律为：
![image]()  
  其形式跟热传导方程类似。
 
- 熵: \
    化学及热力学中所指的熵，是一种测量在动力学方面不能做功的能量总数，也就是当总体的熵增加，其做功能力也下降，熵的量度正是能量退化的指标。熵亦被用于计算一个系统中的失序现象，也就是计算该系统混乱的程度。熵是一个描述系统状态的函数，但是经常用熵的参考值和变化量进行分析比较，它在控制论、概率论、数论、天体物理、生命科学等领域都有重要应用，在不同的学科中也有引申出的更为具体的定义，是各领域十分重要的参量。 \
    ![image]()
    1877年，玻尔兹曼发现单一系统中的熵跟构成热力学性质的微观状态数量相关。可以考虑情况如：一个容器内的理想气体。微观状态可以以每个组成的原子的位置及动量予以表达。为了一致性起见，我们只需考虑包含以下条件的微观状态： \
  （i）所有粒子的位置皆在容器的体积范围内；\
  （ii）所有原子的动能总和等于该气体的总能量值。\
    玻尔兹曼提出一个系统的熵和所有可能微观状态的数目满足以下简单关系：
    ![image]()
 
  这个公式称为“玻尔兹曼公式”，根据玻尔兹曼的定义，熵是一则关于状态的函数.根据这个公式，我们可以将熵看作是一个系统“混乱程度”的度量，因为一个系统越混乱，可以看作是微观状态分布越均匀。根据熵的统计学定义，热力学第二定律说明一个孤立系统的倾向于增加混乱程度。

 - 理想状态：无规则行走是布朗运动的理想状态。

  
### 三、正文
* 1、点阵随机游走

一个最流行的随机游走模型就是规则点阵上的随机游走，每一步对象的位置根据某种概率分布从一个阵点跳跃到另一个阵点上。

①其中,最简单的情形就是一个行人以固定步幅在一条直线上等概率地沿两个方向之一行走。
为使结果更具普遍性，我们假设同时有若干人在随机游走，研究他们走完每一步后与原点之间的平均距离。

显然，实现该程序的关键是如何模拟行人们等几率的向两个方向行走。我们可以通过产生一个介于  ![image]()和  ![image]()之间的随机数  ![image]()来实现：若  ![image]()，则行人向右走一步，否则行人向左走一步。

## →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project1-1.py)

②我们取行人人数为10000，模拟三次得如下结果
 ![image]()
可以看出10000名行人的平均位移 ![image]()在 ![image]()附近波动且波动幅度随 ![image]()增大，但 ![image]()的期望值大致为 ![image]()，这是由于

 ![image]()

③下面我们具体研究 ![image]()的波动幅度与步数 ![image]()的关系。

## →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project1-2.py)

下图是一次模拟中 ![image]()随步数的变化
 ![image]()
可以看出， ![image]()的值大致等于步数 ![image]()。接下来我们从理论上具体分析原因：

因为

 ![image]()

而 ![image]()与 ![image]()是相互独立的随机变量，故有

 ![image]()

从而有

 ![image]()

 接下来，我们取消步长为固定值的限制，使每步的位移在 ![image]()间等概率随机取值。

## →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project1-3.py)

 我们同样取行人人数为10000，模拟三次得如下结果
 ![image]()

同样我们可以看出 ![image]()在 ![image]()附近波动，但波动幅度却明显比之前要小。

显然，由于每步的位移 ![image]()服从均匀分布 ![image]()，有

 ![image]()
从而由之前讨论知

 ![image]()


 下面我们具体研究 ![image]()的波动幅度与步数 ![image]()的关系。

 ## →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project1-4.py)


 下图是一次模拟中 ![image]()随步数的变化

 ![image]()

可以看出， ![image]()成正比，但其值要比之前小很多。下面我们从理论上给出解释：

由 ![image]()，有

 ![image]()

故而由前讨论有

 ![image]()

显然，这与模拟所得图像高度一致。

 下面，我们按照**习题7.3**所说，研究当行人向两个方向移动的概率不等时的情况，我们取向左移动的概率 ![image]()，从而向右移动的概率 ![image]()。

 ## →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project1-5.py)

 我们同样取行人人数为10000，模拟三次得如下结果
 ![image]()

不难看出， ![image]()的值约为步数 ![image]()。

又由之前讨论有
 ![image]()

显然，这与模拟结果一致。

 接着我们具体研究 ![image]()与步数 ![image]()>的关系。

 ## →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project1-6.py)

 下图是一次模拟中 ![image]()随步数的变化
 ![image]()


从拟合曲线可知， ![image]()大致是 ![image]()的二次函数。

由于该种情况下， ![image]()，则有

 ![image]()

经验算，所得曲线和该式符合很好。


 为了更直观地理解随机行走的过程，我们可以使用python中的turtle模块绘制二维点阵随机游走示意动画。

 ## →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project2-1.py)

这是 ![image]()网格上的随机游走动画

 ![image]()

 ## →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project2-2.py)

 这是 ![image]()网格上的随机游走动画

 ![image]()

我们可以看出红色箭头会在出发点附近一定大小的区域内游走相当长的时间。事实上，对于一维和二维点阵随机游走，只要步数足够大，任意游动的点必定能返回它的出发点，该定理是著名数学家波利亚在1921年证明的。

 接着，我们模拟在每一步的方向和步幅都随机的情况下的二维随机游走轨迹。

 ## →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project2-3.py)

 下面是三次模拟的轨迹图
 ![image]()
 ![image]()
 ![image]()

 此外，我们还可以较为容易地模拟三维点阵随机游走的轨迹。

 ## →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project2-4.py)

 下面是三次模拟的轨迹图

 ![image]()

 ![image]()

 ![image]()

 我们可以看出多数情况下，动点出发后离原点越来越远，没有返回出发点的迹象。实际上，波利亚也证明了在三维网格中随机游走，最终能回到出发点的概率只有大约 34% ，而且随着维度的增 加，回到出发点的概率将变得越来越低。在四维网格中随机游走，最终能回到出发点 的概率是 19.3% ，而在八维空间中，这个概率只有 7.3% 。 

* 2、扩散
 我们之前曾提到，随机游走和扩散是等价的，宏观上观测到的扩散现象其实就是大量粒子的随机游走行为。下面为了研究扩散问题的处理方法，我们讨论单个粒子在简单立方点阵中的随机游走。

 记* 1、为粒子在<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>时刻（即第<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>步）出现在点<a href="http://www.codecogs.com/eqnedit.php?latex=(i,j,k)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?(i,j,k)" title="(i,j,k)" /></a>处的概率。要使粒子在<a href="http://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n" title="n" /></a>时刻出现在点<a href="http://www.codecogs.com/eqnedit.php?latex=(i,j,k)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?(i,j,k)" title="(i,j,k)" /></a>，则在<a href="http://www.codecogs.com/eqnedit.php?latex=n-1" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n-1" title="n-1" /></a>时刻，粒子必须在与<a href="http://www.codecogs.com/eqnedit.php?latex=(i,j,k)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?(i,j,k)" title="(i,j,k)" /></a>相邻的六个阵点上，又从每个相邻阵点运动到<a href="http://www.codecogs.com/eqnedit.php?latex=(i,j,k)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?(i,j,k)" title="(i,j,k)" /></a>的概率为<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{1}{6}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{1}{6}" title="\frac{1}{6}" /></a>，则有如下递推式


<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=P(i,j,k,n)=\frac{1}{6}[P(i&plus;1,j,k,n-1)&plus;P(i-1,j,k,n-1)&plus;P(i,j&plus;1,k,n-1)\\&plus;P(i,j-1,k,n-1)&plus;P(i,j,k&plus;1,n-1)&plus;P(i,j,k-1,n-1)]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?P(i,j,k,n)=\frac{1}{6}[P(i&plus;1,j,k,n-1)&plus;P(i-1,j,k,n-1)&plus;P(i,j&plus;1,k,n-1)\\&plus;P(i,j-1,k,n-1)&plus;P(i,j,k&plus;1,n-1)&plus;P(i,j,k-1,n-1)]" title="P(i,j,k,n)=\frac{1}{6}[P(i+1,j,k,n-1)+P(i-1,j,k,n-1)+P(i,j+1,k,n-1)\\+P(i,j-1,k,n-1)+P(i,j,k+1,n-1)+P(i,j,k-1,n-1)]" /></a></div>

改写上式，可得

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=P(i,j,k,n)-P(i,j,k,n-1)\\=\frac{1}{6}[P(i&plus;1,j,k,n-1)-2P(i,j,k,n-1)&plus;P(i-1,j,k,n-1)]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?P(i,j,k,n)-P(i,j,k,n-1)\\=\frac{1}{6}[P(i&plus;1,j,k,n-1)-2P(i,j,k,n-1)&plus;P(i-1,j,k,n-1)]" title="P(i,j,k,n)-P(i,j,k,n-1)\\=\frac{1}{6}[P(i+1,j,k,n-1)-2P(i,j,k,n-1)+P(i-1,j,k,n-1)]" /></a></div>

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=&plus;\frac{1}{6}[P(i,j&plus;1,k,n-1)-2P(i,j,k,n-1)&plus;P(i,j-1,k,n-1)]\\&plus;\frac{1}{6}[P(i,j,k&plus;1,n-1)-2P(i,j,k,n-1)&plus;P(i,j,k-1,n-1)]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?&plus;\frac{1}{6}[P(i,j&plus;1,k,n-1)-2P(i,j,k,n-1)&plus;P(i,j-1,k,n-1)]\\&plus;\frac{1}{6}[P(i,j,k&plus;1,n-1)-2P(i,j,k,n-1)&plus;P(i,j,k-1,n-1)]" title="+\frac{1}{6}[P(i,j+1,k,n-1)-2P(i,j,k,n-1)+P(i,j-1,k,n-1)]\\+\frac{1}{6}[P(i,j,k+1,n-1)-2P(i,j,k,n-1)+P(i,j,k-1,n-1)]" /></a></div>

等式两边同乘常量<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{1}{\Delta&space;t}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{1}{\Delta&space;t}" title="\frac{1}{\Delta t}" /></a>，由之前章节对拉普拉斯算子的讨论，可将等式化为

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;P(x,y,z,t)}{\partial&space;t}=D\nabla^{2}P(x,y,z,t)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\partial&space;P(x,y,z,t)}{\partial&space;t}=D\nabla^{2}P(x,y,z,t)" title="\frac{\partial P(x,y,z,t)}{\partial t}=D\nabla^{2}P(x,y,z,t)" /></a></div>

其中<a href="http://www.codecogs.com/eqnedit.php?latex=D=\frac{1}{6}\frac{(\Delta&space;x)^{2}}{\Delta&space;t}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?D=\frac{1}{6}\frac{(\Delta&space;x)^{2}}{\Delta&space;t}" title="D=\frac{1}{6}\frac{(\Delta x)^{2}}{\Delta t}" /></a>

我们发现上式与我们之前提到的扩散方程形式完全一样

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;\rho&space;}{\partial&space;t}=D\nabla^{2}\rho" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\partial&space;\rho&space;}{\partial&space;t}=D\nabla^{2}\rho" title="\frac{\partial \rho }{\partial t}=D\nabla^{2}\rho" /></a></div>

其实，当体系有大量粒子时，他们某一时刻出现在某一位置的概率<a href="http://www.codecogs.com/eqnedit.php?latex=P" target="_blank"><img src="http://latex.codecogs.com/gif.latex?P" title="P" /></a>之和即为该时刻该位置的粒子数密度<a href="http://www.codecogs.com/eqnedit.php?latex=\rho" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\rho" title="\rho" /></a>。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在一维情况下，我们将粒子数密度函数写为<a href="http://www.codecogs.com/eqnedit.php?latex=\rho&space;(x,t)=\rho&space;(i\Delta&space;x,n\Delta&space;t)=\rho&space;(i,n)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\rho&space;(x,t)=\rho&space;(i\Delta&space;x,n\Delta&space;t)=\rho&space;(i,n)" title="\rho (x,t)=\rho (i\Delta x,n\Delta t)=\rho (i,n)" /></a>，则对应的扩散方程为

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;\rho&space;}{\partial&space;t}=D\frac{\partial&space;^{2}\rho&space;}{\partial&space;x^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\partial&space;\rho&space;}{\partial&space;t}=D\frac{\partial&space;^{2}\rho&space;}{\partial&space;x^{2}}" title="\frac{\partial \rho }{\partial t}=D\frac{\partial ^{2}\rho }{\partial x^{2}}" /></a></div>

其有限差分形式如下

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\rho&space;(i,n&plus;1)-\rho&space;(i,n)}{\Delta&space;t}=D\frac{\rho&space;(i&plus;1,n)-2\rho&space;(i,n)&plus;\rho&space;(i-1,n)}{(\Delta&space;x)^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\rho&space;(i,n&plus;1)-\rho&space;(i,n)}{\Delta&space;t}=D\frac{\rho&space;(i&plus;1,n)-2\rho&space;(i,n)&plus;\rho&space;(i-1,n)}{(\Delta&space;x)^{2}}" title="\frac{\rho (i,n+1)-\rho (i,n)}{\Delta t}=D\frac{\rho (i+1,n)-2\rho (i,n)+\rho (i-1,n)}{(\Delta x)^{2}}" /></a></div>

改写为递推形式有

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\rho&space;(i,n&plus;1)=\rho&space;(i,n)&plus;\frac{D\Delta&space;t}{(\Delta&space;x)^{2}}[\rho&space;(i&plus;1,n)&plus;\rho&space;(i-1,n)-2\rho&space;(i,n)]" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\rho&space;(i,n&plus;1)=\rho&space;(i,n)&plus;\frac{D\Delta&space;t}{(\Delta&space;x)^{2}}[\rho&space;(i&plus;1,n)&plus;\rho&space;(i-1,n)-2\rho&space;(i,n)]" title="\rho (i,n+1)=\rho (i,n)+\frac{D\Delta t}{(\Delta x)^{2}}[\rho (i+1,n)+\rho (i-1,n)-2\rho (i,n)]" /></a></div>

可见，如果我们知道粒子的初始分布，就可求得他们之后时刻的分布。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们首先用以上由扩散方程得到的递推式模拟初始时刻粒子全部聚集在原点的情况。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project3-1.py)

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_6-2.png?raw=true" /></div>

如习题**7.9**所说，扩散进行一段时间后，粒子呈正态分布（高斯分布）

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\rho&space;(x,t)=\frac{1}{\sigma&space;}e^{-\frac{x^{2}}{2\sigma&space;^{2}}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\rho&space;(x,t)=\frac{1}{\sigma&space;}e^{-\frac{x^{2}}{2\sigma&space;^{2}}}" title="\rho (x,t)=\frac{1}{\sigma }e^{-\frac{x^{2}}{2\sigma ^{2}}}" /></a></div>


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;既然扩散方程可以由大量粒子的格点随机游走得到，那我们不妨试试模拟初始时刻大量粒子聚集在原点的格点随机游走。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project3-2.py)

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_6-1.png?raw=true" /></div>

可见两种方法所得的粒子分布吻合程度相当高，这恰好印证了两种方法的一致性。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们接下来研究教材提到的奶油在咖啡中溶解的问题。该问题可合理简化为初始时刻在一个正方形区域内均匀分布的粒子的二维扩散问题。我们首先用扩散方程所得递推式进行模拟。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project4-1.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;我们用高度表示某一位置的粒子数密度，初始时刻的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-1%200.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.codecogs.com/eqnedit.php?latex=n=50" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n=50" title="n=50" /></a>时的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-2%2050.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.codecogs.com/eqnedit.php?latex=n=200" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n=200" title="n=200" /></a>时的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-3%20200.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.codecogs.com/eqnedit.php?latex=n=500" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n=500" title="n=500" /></a>时的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-4%20500.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.codecogs.com/eqnedit.php?latex=n=1000" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n=1000" title="n=1000" /></a>时的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-5%201000.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.codecogs.com/eqnedit.php?latex=n=2000" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n=2000" title="n=2000" /></a>时的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-6%202000.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.codecogs.com/eqnedit.php?latex=n=4000" target="_blank"><img src="http://latex.codecogs.com/gif.latex?n=4000" title="n=4000" /></a>时的分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_8-7%204000.png?raw=true" /></div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为了更清楚地理解扩散方程和随机游走的联系，我们再用随机游走的方法模拟这个问题

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project4-2.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;模拟所得不同时刻的粒子分布如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_1-3.png?raw=true" /></div>

可以看出，两种方法所得的粒子分布情况是一致的。

#### Ⅲ 扩散过程中的熵

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如之前所说，熵的统计学定义为

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=S=-k\sum_{s}^{&space;}P_{s}\ln&space;P_{s}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?S=-k\sum_{s}^{&space;}P_{s}\ln&space;P_{s}" title="S=-k\sum_{s}^{ }P_{s}\ln P_{s}" /></a></div>

运用该式，我们就可计算各种过程中的熵。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面我们就按习题**7.12**的要求来模拟计算奶油在咖啡中溶解过程中的熵随时间的变化。

#### →[查看程序](https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/Final%20Project5-1.py)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;模拟所得扩散过程中不同时刻的熵如下

<div align=center><img src="https://github.com/ACGNnsj/compuational_physics_N2014301020001/blob/master/Final%20Project/figure_7-1.png?raw=true" /></div>

可以看出，在奶油溶解的过程中，体系的熵一直在增加，且熵随时间（步数）变化的函数图像大致为一个向左平移后的对数函数。

###4. 结果讨论

* 扩散过程的本质是大量粒子的随机游走，但扩散方程本身却是确定性的。

* 用确定性的扩散方程和大量粒子随机游走模拟得到相同的结果，这昭示了大量在微观上行为服从一定概率分布的粒子在宏观上有确定性的规律来描述其行为。

* 扩散是一个自发行为，而伴随着这个自发行为，系统的熵自发地增加。

---

<h4 align="center">参考文献</h4>

**[1]**Nicholas J. Giordano，Hisao Nakanishi. 计算物理（第2版）[M]. 北京：清华大学出版社，2007.181-206.

**[2]**Y. Daniel Liang.RandomWalk[EB/OL].http://www.cs.armstrong.edu/liang/py/html/RandomWalk.html ，2016.

**[3]**tacaswell.Problems plotting a 2D random walk with Python[EB/OL].http://stackoverflow.com/questions/27282835/problems-plotting-a-2d-random-walk-with-python ，2014.

**[4]**Martin Evans.Plotting 3D random walk in Python[EB/OL].http://stackoverflow.com/questions/34920680/plotting-3d-random-walk-in-python ，2016. 





### 四、总结
1.可以看出α不同时，李雅普诺夫指数截然不同；相同α下，不同的初始距离d可能导致李雅普诺夫指数的些微不同\
2.α越小曲线越密集，这说明系统经历了更多状态，可以预见，当α足够大即台球桌足够长时混沌现象可能会消失
    
### 五、致谢
    感谢彭成铭倪、世杰同学鼎力相助~。
