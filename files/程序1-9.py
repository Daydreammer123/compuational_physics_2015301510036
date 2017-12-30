from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt      
from matplotlib import animation 

def show_trajectory(self):
fig = plt.figure()
ax =Axes3D(fig)
line1=ax.plot([],[],'b:')
point1=ax.plot([],[],'bo',markersize=10)
images=[]

def init():
line1 = ax.plot([], [], 'b', markersize=8)
point1 = ax.plot([], [], 'ro', markersize=10)
return line1, point1

def anmi(i):
ax.clear()
line1 = ax.plot(self.x[0:(1 * i)], self.y[0:(1 * i)], self.z[0:1*i],'b', markersize=8)
point1 = ax.plot(self.x[(1 * i - 1):(1 * i)], self.y[(1 * i - 1):(1 * i)], self.z[1 * i -1:1 * i],'ro', markersize=10)
return line1, point1

anmi = animation.FuncAnimation(fig, anmi, init_func=init, frames=100, interval=1,blit=False,repeat=False)
 plt.show()
