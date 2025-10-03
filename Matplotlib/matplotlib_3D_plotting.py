import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D # This import enables 3D projections

print("--- Matplotlib 3D Plotting: All About in Code ---")

# --- 1. Setting up a 3D Axes ---
print("\n--- 1. Setting up a 3D Axes ---")
print("To create 3D plots, you need to tell Matplotlib to use a 3D projection.")

fig = plt.figure(figsize=(10, 8)) # Create a new figure
ax = fig.add_subplot(111, projection='3d') # This is the key: `projection='3d'`

# Basic example: Just an empty 3D axes
ax.set_title("Empty 3D Axes")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()


# --- 2. 3D Scatter Plot (`plot_scatter`) ---
print("\n--- 2. 3D Scatter Plot ---")
print("Visualize data points in a 3D space, showing relationships between three variables.")

np.random.seed(42) # For reproducibility
num_points = 100

# Generate 3D data points
x_scatter = np.random.rand(num_points) * 10
y_scatter = np.random.rand(num_points) * 10
z_scatter = np.random.rand(num_points) * 10

# Add a fourth dimension for color or size
colors = np.random.rand(num_points)
sizes = np.random.rand(num_points) * 200 + 50 # Varying sizes

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the scatter points
scatter_plot = ax.scatter(x_scatter, y_scatter, z_scatter,
                          c=colors,        # Color based on `colors` array
                          cmap='viridis',  # Colormap for the colors
                          s=sizes,         # Size based on `sizes` array
                          alpha=0.7,       # Transparency
                          edgecolors='w',  # White edge around markers
                          depthshade=True) # Shade points according to their depth in the view

ax.set_title("3D Scatter Plot")
ax.set_xlabel("Feature X")
ax.set_ylabel("Feature Y")
ax.set_zlabel("Feature Z")

# Add a color bar for the `c` (color) mapping
fig.colorbar(scatter_plot, ax=ax, shrink=0.5, aspect=10, label='Color Intensity')

plt.show()


# --- 3. 3D Line Plot (`plot`) ---
print("\n--- 3. 3D Line Plot ---")
print("Connects sequential data points in 3D space, often used for trajectories or ordered series.")

# Generate data for a 3D spiral
t = np.linspace(-4 * np.pi, 4 * np.pi, 200)
x_line = np.sin(t)
y_line = np.cos(t)
z_line = t

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x_line, y_line, z_line,
        color='blue',       # Line color
        linestyle='-',      # Line style
        linewidth=2,        # Line width
        alpha=0.8)          # Transparency

ax.set_title("3D Helix (Line Plot)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()

# Multiple 3D lines
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_line, y_line, z_line, color='blue', label='Helix 1')
ax.plot(x_line * 1.2, y_line * 1.2, z_line + 5, color='red', linestyle='--', label='Helix 2')
ax.set_title("Multiple 3D Lines")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.show()


# --- 4. 3D Surface Plot (`plot_surface`) ---
print("\n--- 4. 3D Surface Plot ---")
print("Visualizes a 2D function $Z = f(X, Y)$ as a continuous surface.")

# Create a meshgrid for X and Y values
x_surf = np.arange(-5, 5, 0.25)
y_surf = np.arange(-5, 5, 0.25)
X_surf, Y_surf = np.meshgrid(x_surf, y_surf)

# Define a function for Z (e.g., a "Mexican Hat" function)
R = np.sqrt(X_surf**2 + Y_surf**2)
Z_surf = np.sin(R) / R # Handle division by zero at R=0
Z_surf[R == 0] = 1 # Set Z to 1 at the origin

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(X_surf, Y_surf, Z_surf,
                          cmap='viridis',  # Colormap for the surface
                          edgecolor='none', # No grid lines on the surface
                          alpha=0.9,       # Transparency of the surface
                          rstride=1, cstride=1) # Row and column stride for sampling

ax.set_title("3D Surface Plot (Mexican Hat Function)")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10, label='Function Value')
plt.show()

# Another example: A simple plane
X_plane, Y_plane = np.meshgrid(np.linspace(0, 5, 10), np.linspace(0, 5, 10))
Z_plane = 0.5 * X_plane + 0.3 * Y_plane + 1

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_plane, Y_plane, Z_plane, cmap='plasma', alpha=0.8)
ax.set_title("3D Plane")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()


# --- 5. 3D Wireframe Plot (`plot_wireframe`) ---
print("\n--- 5. 3D Wireframe Plot ---")
print("Similar to a surface plot but only shows the grid lines, useful for dense surfaces.")

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(X_surf, Y_surf, Z_surf,
                  color='green',    # Color of the wireframe lines
                  rstride=5, cstride=5) # Density of the wireframe lines

ax.set_title("3D Wireframe Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.show()


# --- 6. 3D Contour Plot (`contour` and `contourf`) ---
print("\n--- 6. 3D Contour Plot ---")
print("Projects contour lines of a 2D function onto a 3D surface or a 2D plane at the bottom.")

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surface = ax.plot_surface(X_surf, Y_surf, Z_surf, cmap='viridis', alpha=0.7, edgecolor='none')

# Plot contour lines on the 2D plane at the bottom (zdir='z', offset=min(Z_surf))
cset = ax.contour(X_surf, Y_surf, Z_surf,
                  zdir='z',       # Project contours onto the z-plane
                  offset=ax.get_zlim()[0], # At the bottom of the Z-axis
                  cmap='coolwarm',
                  linewidths=1.5)

# Plot filled contours on the 2D plane (optional)
# csetf = ax.contourf(X_surf, Y_surf, Z_surf,
#                      zdir='x', # Project contours onto the x-plane
#                      offset=ax.get_xlim()[0], # At the left of the X-axis
#                      cmap='coolwarm',
#                      alpha=0.5)

ax.set_title("3D Surface with 2D Contours")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10, label='Function Value')
plt.show()


# --- 7. Customizing 3D Plots (View Angle, Axis Labels, Grid) ---
print("\n--- 7. Customizing 3D Plots ---")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x_scatter, y_scatter, z_scatter, c='red', s=50, alpha=0.8)

# 7.1 Setting View Angle
# `elev`: elevation angle (vertical angle from x-y plane)
# `azim`: azimuthal angle (horizontal rotation)
ax.view_init(elev=20, azim=-60) # Rotate the view (default elev=30, azim=-60)

# 7.2 Custom Axis Labels and Limits
ax.set_xlabel("My X-axis", fontsize=12, color='darkblue')
ax.set_ylabel("My Y-axis", fontsize=12, color='darkgreen')
ax.set_zlabel("My Z-axis", fontsize=12, color='darkred')

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

# 7.3 Grid and Background Color
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_facecolor('lightyellow') # Background color of the 3D cube

# Customize pane colors (the planes behind the axes)
ax.xaxis.pane.set_facecolor('lightgray')
ax.yaxis.pane.set_facecolor('lightgray')
ax.zaxis.pane.set_facecolor('lightgray')

ax.set_title("Customized 3D Scatter Plot View", fontsize=14)
plt.show()


# --- 8. Multiple 3D Subplots ---
print("\n--- 8. Multiple 3D Subplots ---")

fig_multi = plt.figure(figsize=(15, 7))

# First subplot: 3D scatter
ax1 = fig_multi.add_subplot(1, 2, 1, projection='3d')
ax1.scatter(x_scatter, y_scatter, z_scatter, c='coral', s=30, alpha=0.8)
ax1.set_title("Scatter Plot")
ax1.set_xlabel("X"); ax1.set_ylabel("Y"); ax1.set_zlabel("Z")
ax1.view_init(elev=10, azim=30)

# Second subplot: 3D surface
ax2 = fig_multi.add_subplot(1, 2, 2, projection='3d')
surface2 = ax2.plot_surface(X_surf, Y_surf, Z_surf, cmap='coolwarm', alpha=0.8, edgecolor='none')
ax2.set_title("Surface Plot")
ax2.set_xlabel("X"); ax2.set_ylabel("Y"); ax2.set_zlabel("Z")
ax2.view_init(elev=20, azim=-120)
fig_multi.colorbar(surface2, ax=ax2, shrink=0.5, aspect=10) # Add colorbar to the second subplot

plt.suptitle("Multiple 3D Plots in a Single Figure", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()


# --- 9. Saving 3D Plots ---
print("\n--- 9. Saving 3D Plots ---")

fig_save = plt.figure(figsize=(10, 8))
ax_save = fig_save.add_subplot(111, projection='3d')
ax_save.plot(x_line, y_line, z_line, color='darkgreen', linewidth=2)
ax_save.set_title("Plot to be Saved")
ax_save.set_xlabel("X"); ax_save.set_ylabel("Y"); ax_save.set_zlabel("Z")

# Saving as PNG (raster image)
plt.savefig("3d_helix_plot.png", dpi=300)
print("Saved: 3d_helix_plot.png")

# Saving as PDF (vector image - good for high quality)
plt.savefig("3d_helix_plot.pdf")
print("Saved: 3d_helix_plot.pdf")

plt.close(fig_save) # Close the figure to free up memory

print("\n--- End of Matplotlib 3D Plotting Practice Code ---")

# Important Notes for 3D Plots:
# - The import `from mpl_toolkits.mplot3d import Axes3D` is crucial.
# - Always create a 3D axes using `fig.add_subplot(111, projection='3d')`.
# - 3D plots can be computationally intensive, especially for very dense surfaces or many points.
# - Interaction: In interactive Matplotlib backends (like the default for Python scripts or Jupyter),
#   you can often rotate 3D plots by clicking and dragging them.