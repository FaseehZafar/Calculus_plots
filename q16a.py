import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-6,+6,0.1)
y =[]

for i in x:
fx = np.sin(np.pi*1/2+i)
y.append(fx)

plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Question 16(y1)')
plt.show()
