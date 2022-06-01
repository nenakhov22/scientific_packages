import numpy as np
data = np.genfromtxt('stockholm_tmp.dat')
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize = [12,12])
y = np.array([1.,2.,1.,2.,1.,2.,1.,2.,1.,2.,1.,2.])
for a in range(12):
  mask_mon = data[:,1] == a+1
  y[a] = (np.mean(data[mask_mon,3]))
ax.bar(np.linspace(1,12,12),y)
ax.axis('tight')
ax.set_xlabel('Mounth')
ax.set_ylabel('Temperature')
print(y)
