import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10,10,0.1)
y = []

for i in x:
fx = 2.5+(3/20*i)
y.append(fx)

plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Question 14')
plt.show()
