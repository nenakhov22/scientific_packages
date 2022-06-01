import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
ax = axes3d.Axes3D(plt.figure())
i = np.arange(-1,1,0.01)
X,Y=np.meshgrid(i,i)
Z = X**2 + Y**3
ax.plot_wireframe(X,Y,Z,rstride=3,cstride=3)
plt.show()
from matplotlib import projections
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as pit
fig = pit.figure()
ax = fig.add_subplot(111, projection = '3d')
