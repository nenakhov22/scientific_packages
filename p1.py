import math

def m_function(t:float) -> float:
  return math.atan(-0.0012*t**3+0.4*t**2+0.616*t+6120) + 0.65*math.sin(0.24*t+1.23) - 0.27*math.cos(0.21*t-0.17)-math.sin(0.34*t+0.16)/(1+0.03*(t-370.5)**2)


import matplotlib as mpl
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

x = range(1000)
plt.plot(x, [m_function(t) for t in x])
