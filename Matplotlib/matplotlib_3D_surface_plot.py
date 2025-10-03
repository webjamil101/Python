import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D # This import enables 3D projections

print("--- Matplotlib 3D Surface Plot: All About in Code ---")

# --- 1. Basic 3D Surface Plot ---
print("\n--- 1. Basic 3D Surface Plot ---")
print("A surface plot visualizes a 2D function Z = f(X, Y) as a continuous surface.")

# 1.1 Data Preparation: Create a Meshgrid
# We need 2D arrays for X, Y, and Z. `np.meshgrid` is perfect for this.
x_values = np.arange(-5, 5, 0.25) # Array of x values
y_values = np.arange(-5, 5, 0.25) # Array of y values
X, Y = np.meshgrid(x_values, y_values) # Creates 2D arrays from 1D arrays

# Define a function for Z (e.g., a simple parabolic shape)
Z = X**2 + Y**2

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d') # Key for 3D plotting

# Plot the surface
surface = ax.plot_surface(X, Y, Z,
                          cmap='viridis') # Colormap to color the surface based on Z values

ax.set_title("Basic 3D Surface Plot ($Z = X^2 + Y^2$)")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# Add a color bar to explain the colormap
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10, label='Z Value')

plt.show()


# --- 2. Customizing 3D Surface Plots ---
print("\n--- 2. Customizing 3D Surface Plots ---")

# 2.1 Changing Colormaps, Transparency, and Edge Lines
print("\n--- 2.1 Colormaps, Transparency, Edges ---")

# Define a more interesting function (e.g., a "Mexican Hat" or sinc function)
R = np.sqrt(X**2 + Y**2)
Z_sinc = np.sin(R) / R
Z_sinc[R == 0] = 1.0 # Handle the singularity at R=0

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

surface_custom = ax.plot_surface(X, Y, Z_sinc,
                                 cmap='coolwarm', # Another popular colormap
                                 edgecolor='black', # Add black lines between facets
                                 linewidth=0.5,     # Thickness of edge lines
                                 alpha=0.9,         # Transparency of the surface (0.0 to 1.0)
                                 rstride=1,         # Row stride: frequency of sampled rows
                                 cstride=1)         # Column stride: frequency of sampled columns

ax.set_title("Customized 3D Surface Plot (Sinc Function)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
fig.colorbar(surface_custom, ax=ax, shrink=0.5, aspect=10, label='Sinc(R) Value')
plt.show()

# Experiment with different `rstride` and `cstride`
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z_sinc,
                cmap='plasma',
                edgecolor='gray',
                linewidth=0.2,
                rstride=10, # Higher stride means fewer sampled points (coarser mesh)
                cstride=10)
ax.set_title("Coarser Surface Plot (rstride=10, cstride=10)")
ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
plt.show()


# 2.2 Setting View Angle (`view_init`)
print("\n--- 2.2 Setting View Angle ---")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z_sinc, cmap='magma', edgecolor='none')

ax.set_title("3D Surface Plot with Custom View Angle")
ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")

# `elev`: elevation angle in the z-plane (vertical angle from x-y plane).
# `azim`: azimuthal angle in the x-y plane (horizontal rotation).
ax.view_init(elev=30, azim=-120) # Default is elev=30, azim=-60

plt.show()


# --- 3. Combining Surface with Contour/Wireframe ---
print("\n--- 3. Combining Surface with Contour/Wireframe ---")
print("You can add projections of the surface onto the planes, or overlay a wireframe.")

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surface_combo = ax.plot_surface(X, Y, Z_sinc, cmap='viridis', alpha=0.8) # Slightly transparent

# Add a contour plot projected onto the x-y plane (zdir='z')
# The offset determines where on the z-axis the contour is drawn.
cset_xy = ax.contourf(X, Y, Z_sinc,
                       zdir='z', # Project onto the z-plane
                       offset=Z_sinc.min() - 0.5, # Offset below the surface
                       cmap='viridis',
                       alpha=0.8)

# Add a contour plot projected onto the y-z plane (zdir='x')
cset_yz = ax.contourf(X, Y, Z_sinc,
                       zdir='x', # Project onto the x-plane
                       offset=X.min() - 1, # Offset to the left of the surface
                       cmap='viridis',
                       alpha=0.8)

# Add a contour plot projected onto the x-z plane (zdir='y')
cset_xz = ax.contourf(X, Y, Z_sinc,
                       zdir='y', # Project onto the y-plane
                       offset=Y.max() + 1, # Offset to the right of the surface
                       cmap='viridis',
                       alpha=0.8)

ax.set_title("Surface Plot with Plane Projections")
ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
fig.colorbar(surface_combo, ax=ax, shrink=0.5, aspect=10, label='Z Value')

# Set explicit limits to make space for projections
ax.set_zlim(Z_sinc.min() - 1, Z_sinc.max() + 0.5)
ax.set_xlim(X.min() - 1.5, X.max() + 0.5)
ax.set_ylim(Y.min() - 0.5, Y.max() + 1.5)

plt.show()


# --- 4. Wireframe Overlay on Surface ---
print("\n--- 4. Wireframe Overlay on Surface ---")

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface (usually with some transparency)
surface_overlay = ax.plot_surface(X, Y, Z_sinc,
                                  cmap='GnBu',
                                  alpha=0.6, # Make it transparent to see wireframe
                                  edgecolor='none')

# Overlay a wireframe on top of the surface
ax.plot_wireframe(X, Y, Z_sinc,
                  color='black', # Color of the wireframe lines
                  linewidth=0.8,
                  rstride=5, cstride=5) # Adjust stride for desired wireframe density

ax.set_title("Surface Plot with Wireframe Overlay")
ax.set_xlabel("X"); ax.set_ylabel("Y"); ax.set_zlabel("Z")
fig.colorbar(surface_overlay, ax=ax, shrink=0.5, aspect=10, label='Z Value')
plt.show()


# --- 5. Saving 3D Surface Plots ---
print("\n--- 5. Saving 3D Surface Plots ---")

fig_save = plt.figure(figsize=(10, 8))
ax_save = fig_save.add_subplot(111, projection='3d')
ax_save.plot_surface(X, Y, Z_sinc, cmap='viridis', edgecolor='none')
ax_save.set_title("Plot to be Saved")
ax_save.set_xlabel("X"); ax_save.set_ylabel("Y"); ax_save.set_zlabel("Z")

# Saving as PNG (raster image)
plt.savefig("3d_surface_plot.png", dpi=300)
print("Saved: 3d_surface_plot.png")

# Saving as PDF (vector image - good for high quality publications)
plt.savefig("3d_surface_plot.pdf")
print("Saved: 3d_surface_plot.pdf")

plt.close(fig_save) # Close the figure to free up memory

print("\n--- End of Matplotlib 3D Surface Plot Practice Code ---")

# Important Considerations:
# - Data Structure: Surface plots require Z values corresponding to a 2D grid of X and Y values.
#   `np.meshgrid` is crucial for creating these X and Y grids from 1D arrays.
# - Performance: For very large datasets or very fine `rstride`/`cstride` values, rendering can be slow.
# - Interactivity: In many Matplotlib backends (especially in interactive environments like Jupyter),
#   you can click and drag the 3D plot to rotate it and examine it from different angles.