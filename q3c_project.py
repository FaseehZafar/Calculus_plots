import numpy as np
import matplotlib.pyplot as plt

r_max = 0.5
def V(r, c):
return c * (r_max - r) * r**2

r = np.linspace(0, r_max, 100)
c_val = [0.5, 1, 1.5, 2]
plt.figure(figsize=(7, 5))

for c in c_val:
v = V(r, c)

plt.plot(r, v, label=f"c = {c}")
plt.title("Part C")
plt.xlabel("r")
plt.ylabel("V(r)")
plt.legend()
plt.grid(True)
plt.show()
