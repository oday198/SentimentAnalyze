import matplotlib.pyplot as plt
import numpy as np
names=['grp_a','grp_b','grp_c']
values=[0,10,100]
plt.figure(figsize=(9,3))
plt.subplot(131)
plt.bar(names,values)
plt.subplot(132)
plt.scatter(names,values)
plt.subplot(133)
plt.plot(names,values)
plt.suptitle('Categorical plotting')
plt.show()