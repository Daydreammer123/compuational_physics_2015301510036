from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x2_ave = np.zeros(101)
x_y0 = np.zeros(101)
x_now = np.zeros(10000)
x2_now = np.zeros(10000)

for i in range(100):
    for j in range(10000):
        length = 2*np.random.rand() - 1
        x_now[j] = x_now[j] + length
        x2_now[j] = x_now[j]**2
    average2 = sum(x2_now)/10000
    x2_ave[i+1] = average2
    
para = np.polyfit(steps, x2_ave,1)
poly = np.poly1d(para)
y_fit = poly(steps)

plt.scatter(steps, x2_ave,s=2)
plt.scatter(steps, x2_ave,c='forestgreen',s=15,alpha=0.6)
plt.plot(steps, y_fit, 'coral', label = 'fit line')
plt.legend(loc='upper left')

plt.xlim(0,100)
plt.ylim(0,40)
plt.grid(True)
plt.xlabel('step number')
plt.ylabel('$\overline{x^{2}}$')
plt.title('$\overline{x^{2}}$ of 10000 walkers with random step length')

plt.show()
