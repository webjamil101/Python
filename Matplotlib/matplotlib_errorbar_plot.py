# `errorbar` is a Matplotlib function used to create plots with error bars.
# Error bars are graphical representations of the variability of data,
# and are used on graphs to indicate the error, or uncertainty, in a reported measurement.

import matplotlib.pyplot as plt
import numpy as np

# --- 1. Basic `errorbar` plot ---

# Define some sample data
x = np.arange(1, 5) # x-coordinates of the data points
y = x * 2          # y-coordinates of the data points

# Define the error values. This can be a single number (symmetric error)
# or an array/list of values for each point.
# Here, we use symmetric error bars of size 0.5.
y_error = 0.5

# Create the plot
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=y_error, fmt='-o', capsize=5, label='Symmetric Error')

# `fmt='-o'` specifies the format of the plot: '-' for a line, 'o' for circle markers.
# `yerr` is for vertical error bars. You can also use `xerr` for horizontal error bars.
# `capsize` controls the size of the caps on the error bars.

ax.set_title('Basic `errorbar` Plot with Symmetric Error')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
plt.show()


# --- 2. Asymmetric error bars ---

# Create new data
x_asym = np.arange(1, 5)
y_asym = [2, 4.5, 5, 8]

# Asymmetric errors are given as a 2xN array, where the first row
# is the negative error and the second row is the positive error.
y_error_asym = [[0.5, 1, 0.7, 0.2],  # Negative error values
                [0.8, 0.5, 0.9, 0.4]] # Positive error values

fig, ax = plt.subplots()
ax.errorbar(x_asym, y_asym, yerr=y_error_asym, fmt='--s', capsize=3, label='Asymmetric Error')

# `fmt='--s'` specifies a dashed line with square markers.

ax.set_title('`errorbar` Plot with Asymmetric Error')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
plt.show()


# --- 3. Horizontal and vertical error bars ---

# Create new data
x_both = [1, 2, 3]
y_both = [2, 5, 6]

# Define errors for both x and y directions
x_error = 0.2
y_error_both = [0.5, 0.8, 0.4]

fig, ax = plt.subplots()
ax.errorbar(x_both, y_both, xerr=x_error, yerr=y_error_both,
            fmt='-o', color='red', ecolor='blue', capsize=5, label='Both X and Y Errors')

# `xerr` and `yerr` are used together for both horizontal and vertical errors.
# `ecolor` sets the color of the error bars themselves, separate from the main line/markers.

ax.set_title('`errorbar` with Both X and Y Error Bars')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
plt.show()


# --- 4. Customizing the appearance of error bars ---

# Create new data
x_custom = np.arange(5)
y_custom = x_custom**2

# `errorevery` can be used to plot error bars only on a subset of the points.
# Here, we plot error bars on every 2nd point.
# `elinewidth` controls the thickness of the error bar lines.
# `capthick` controls the thickness of the caps.
fig, ax = plt.subplots()
ax.errorbar(x_custom, y_custom, yerr=1.5, fmt='-p', capsize=5,
            errorevery=2, elinewidth=2, capthick=2, label='Custom Appearance')

# `fmt='-p'` specifies a line with pentagon markers.

ax.set_title('Customized `errorbar` Appearance')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
plt.show()