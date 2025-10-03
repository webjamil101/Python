import matplotlib.pyplot as plt
import numpy as np

# --- 1. Generate Sample Data ---
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a figure and axes object.
fig, ax = plt.subplots(figsize=(10, 6))


# --- 2. Plot Lines with Customization ---

# Plot the first line: 'y1' (sin wave)
# `color`: sets the line color (e.g., 'blue', 'red', hex codes like '#0000FF').
# `linestyle`: sets the line style ('-', '--', ':', '-.', 'None').
# `linewidth`: sets the thickness of the line.
# `marker`: sets the marker style at each data point ('o', 's', '^', 'D', 'None').
# `markersize`: sets the size of the markers.
# `label`: assigns a label for the legend.
ax.plot(x, y1, color='blue', linestyle='-', linewidth=2, marker='o', markersize=5, label='sin(x)')

# Plot the second line: 'y2' (cos wave)
ax.plot(x, y2, color='red', linestyle='--', linewidth=1.5, marker='s', markersize=4, label='cos(x)')


# --- 3. Set Plot Limits ---

# `ax.set_xlim()`: sets the x-axis limits. The plot will only display data within this range.
# `ax.set_ylim()`: sets the y-axis limits.
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)


# --- 4. Add Titles and Labels ---

# `ax.set_title()`: sets the title of the plot.
# `ax.set_xlabel()`: sets the label for the x-axis.
# `ax.set_ylabel()`: sets the label for the y-axis.
ax.set_title('Matplotlib Plot Customization', fontsize=16)
ax.set_xlabel('X-axis (Time)', fontsize=12)
ax.set_ylabel('Y-axis (Amplitude)', fontsize=12)


# --- 5. Display Legend and Grid ---

# `ax.legend()`: displays the legend using the `label` arguments from the `ax.plot()` calls.
# `loc` argument can be used to set the location of the legend (e.g., 'upper right').
ax.legend(loc='upper right')

# `ax.grid()`: adds a grid to the plot for better readability.
ax.grid(True, linestyle=':', alpha=0.6)


# --- 6. Final Rendering ---
# `plt.show()`: displays the final plot.
plt.show()