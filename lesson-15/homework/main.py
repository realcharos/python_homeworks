import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-10, 10, 400)  # Generate 400 points from -10 to 10
y = x**2 - 4*x + 4  # Compute function values

plt.plot(x, y, label=r'$f(x) = x^2 - 4x + 4$', color='b')

# Labels and title
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Quadratic Function Plot')

plt.legend()
plt.grid(True)
plt.show()


#Task2
x = np.linspace(0, 2*np.pi, 400)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, linestyle='-', marker='o', color='r', label=r'$\sin(x)$')
plt.plot(x, y_cos, linestyle='--', marker='s', color='b', label=r'$\cos(x)$')

# Labels and title
plt.xlabel('x')
plt.ylabel('Function Value')
plt.title('Sine and Cosine Functions')

plt.legend()
plt.grid(True)
plt.show()

#Task3
x = np.linspace(-2, 2, 400)
x_positive = np.linspace(0, 2, 400)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Top-left
axs[0, 0].plot(x, x**3, 'r')
axs[0, 0].set_title(r'$f(x) = x^3$')

# Top-right
axs[0, 1].plot(x, np.sin(x), 'g')
axs[0, 1].set_title(r'$f(x) = \sin(x)$')

# Bottom-left
axs[1, 0].plot(x, np.exp(x), 'b')
axs[1, 0].set_title(r'$f(x) = e^x$')

# Bottom-right
axs[1, 1].plot(x_positive, np.log(x_positive + 1), 'm')
axs[1, 1].set_title(r'$f(x) = \log(x+1)$')

for ax in axs.flat:
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.grid(True)

plt.tight_layout()
plt.show()

#Task 4
np.random.seed(0)
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.scatter(x, y, c=np.random.rand(100), marker='o', edgecolors='black')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Random Scatter Plot')
plt.grid(True)
plt.show()



data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normally Distributed Data')
plt.grid(True)
plt.show()



x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Surface Plot')

fig.colorbar(surf)
plt.show()



products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

plt.bar(products, sales, color=['red', 'blue', 'green', 'purple', 'orange'])

plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Product Sales')

plt.show()



categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']

data = np.array([[10, 15, 20, 25],  # Category A
                 [5, 10, 15, 20],   # Category B
                 [8, 12, 18, 22]])  # Category C

fig, ax = plt.subplots(figsize=(8, 6))

ax.bar(time_periods, data[0], label=categories[0], color='red')
ax.bar(time_periods, data[1], bottom=data[0], label=categories[1], color='blue')
ax.bar(time_periods, data[2], bottom=data[0]+data[1], label=categories[2], color='green')

ax.set_xlabel('Time Periods')
ax.set_ylabel('Values')
ax.set_title('Stacked Bar Chart')

ax.legend()
plt.show()
