import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y = []

for i in x:
sx = 7*np.sin(np.pi*1/5 * i)
y.append(sx)

plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Question 15')
plt.show()
