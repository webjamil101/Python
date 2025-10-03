import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

print("--- Matplotlib 3D Scatter Plot: All About in Code ---")

# Generate 3D data points
np.random.seed(42)  # For reproducibility
num_points = 100
x_scatter = np.random.rand(num_points) * 10
y_scatter = np.random.rand(num_points) * 10
z_scatter = np.random.rand(num_points) * 10

# Add a fourth dimension for color or size
colors = np.random.rand(num_points)
sizes = np.random.rand(num_points) * 200 + 50  # Varying sizes

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the scatter points
scatter_plot = ax.scatter(
    x_scatter,
    y_scatter,
    z_scatter,
    c=colors,  # Color based on `colors` array
    cmap='viridis',  # Colormap for the colors
    s=sizes,  # Size based on `sizes` array
    alpha=0.7,  # Transparency
    edgecolors='w',  # White edge around markers
    depthshade=True,  # Shade points according to their depth in the view
)

ax.set_title("3D Scatter Plot")
ax.set_xlabel("Feature X")
ax.set_ylabel("Feature Y")
ax.set_zlabel("Feature Z")

# Add a color bar for the `c` (color) mapping
fig.colorbar(scatter_plot, ax=ax, shrink=0.5, aspect=10, label='Color Intensity')

plt.show()