import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(-20.0, 20.0, 0.001)
#y = np.tan(x)
y = 3.14 ** x
plt.plot(x, y)
plt.ylim([-10, 10])
plt.xlim([-20, 20])
plt.show()
