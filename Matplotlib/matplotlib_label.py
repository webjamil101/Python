# In Matplotlib, 'labels' are essential for making plots readable and informative.
# They are used for titles, axis labels, and legends.

import matplotlib.pyplot as plt
import numpy as np

# --- 1. Generate Sample Data ---
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(8, 6))

# --- 2. Axis Labels and Title ---

# `ax.set_xlabel()`: Sets the label for the x-axis.
# `ax.set_ylabel()`: Sets the label for the y-axis.
# `ax.set_title()`: Sets the title for the plot.
# You can customize these labels with parameters like `fontsize`, `fontweight`, and `color`.
ax.set_xlabel("X-axis: Time (s)", fontsize=12, fontweight='bold', color='darkblue')
ax.set_ylabel("Y-axis: Amplitude", fontsize=12, color='darkgreen')
ax.set_title("Two Sine Waves Plot", fontsize=16, fontweight='bold')


# --- 3. Legend Labels ---

# The `label` parameter inside a plotting function (e.g., `ax.plot()`)
# assigns a name to that data series. This name will be used by the legend.
ax.plot(x, y1, color='blue', linestyle='--', label='sin(x)')
ax.plot(x, y2, color='red', linestyle='-', label='cos(x)')

# `ax.legend()`: Displays the legend on the plot using the labels provided above.
# The `loc` parameter specifies the location of the legend (e.g., 'upper right').
# `fontsize` and `frameon` are other common customization options.
ax.legend(loc='upper right', fontsize=10, frameon=True, framealpha=0.8)


# --- 4. Adding Labels for Individual Points (Annotations) ---

# `ax.text(x, y, text)`: Adds text to an arbitrary location on the plot.
# This is useful for annotating specific points or areas.
ax.text(np.pi, np.sin(np.pi), "  Peak", fontsize=10, verticalalignment='bottom')


# --- 5. Final Display ---
ax.grid(True, linestyle=':', alpha=0.6)
plt.show()