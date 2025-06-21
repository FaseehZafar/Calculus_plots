import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-6,+6,0.1)
y =[]

for i in x:
f = (np.cos(i))**-1
y.append(f)

plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Question 16(y2)')
plt.show()
