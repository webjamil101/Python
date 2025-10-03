import matplotlib.pyplot as plt
import numpy as np

# --- 1. Initialize: Setting up the canvas and axes ---
# Create sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a Figure (the window) and an Axes (the plot area) object.
# `plt.subplots()` is the recommended way to create both at once.
fig, ax = plt.subplots(figsize=(8, 6))


# --- 2. Prepare: Adding plot elements ---
# Plot the data on the Axes object
ax.plot(x, y, label='sin(x)', color='blue', linestyle='--')

# Add a title and labels
ax.set_title('My Matplotlib Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Add a legend to identify data series
ax.legend(loc='upper right')

# Add a grid for readability
ax.grid(True, linestyle=':', alpha=0.6)

# Set axis limits
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)


# --- 3. Render: Drawing and displaying the plot ---
# This function displays the plot window.
# It is a blocking call and the program will wait until the window is closed.
plt.show()

# --- 4. Observe: Interaction happens in the displayed window ---
# In the pop-up window, you can use the built-in tools to:
# - Pan and zoom
# - Save the figure to a file
# - Configure subplots