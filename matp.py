import matplotlib.pyplot as plt
import numpy as np
a=[1,2,3,4]
b=[0.1,0.2,0.5,0.8]
plt.plot(a,b)
plt.show()
x=np.arange(0,5,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()
t=np.arange(0.,9.,0.3)
s=np.arange(100,1600,50)
plt.plot(t,t,'b-.',t,s,'m*',t,t**3,'r<')
plt.show()