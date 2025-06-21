import numpy as np
import matplotlib.pyplot as plt

r0 = 0.5
c=1

def V(r):
return c * (r0 - r) * r**2

r = np.linspace(0, r0, 500)
v = V(r)
R_Max = (2/3) * r0
V_Max = V(R_Max)

# Plot the graph

plt.figure(figsize=(10, 5))
plt.plot(r, v, label="V(r) = c(r0 - r)r^2", color="black")
plt.axvline(R_Max, color="olive", linestyle="--", label=f"r = (2/3)r0 =
{R_Max:.2f}") plt.scatter(R_Max, V_Max, color="red", label=f"Max V(r) = {V_Max:.2f}
at r = {R_Max:.2f}")

# Labels and title
 plt.title(" Part - B ")
 plt.xlabel("r")
 plt.ylabel("V(r)")
 plt.legend()
 plt.grid(True)
 plt.show()
