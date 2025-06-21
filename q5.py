import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-10, 10, 40)
# Define the function
y = []
	
for i in x:
	  fx = ((i*2)-3)/(i*3)
	  y.append(fx)
	  
# Plot the function
plt.plot(x, y, label='f(x)')

# Label the vertical asymptote
plt.axvline(x=0, color='k', linestyle='--', label='Vertical Asymptote x = 0')

# Label the horizontal asymptote
plt.axhline(y=0, color='g', linestyle='--', label='Horizontal Asymptote y = 0')

# Add labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('24i-2529 M.Faseeh Zafar')
plt.legend()

# Show the plot
plt.show()
