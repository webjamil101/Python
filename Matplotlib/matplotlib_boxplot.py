import matplotlib.pyplot as plt
import numpy as np

# A box plot (or box-and-whisker plot) is a standardized way of displaying
# the distribution of data based on a five-number summary: minimum, first quartile (Q1),
# median, third quartile (Q3), and maximum. It can also show outliers.

# --- 1. Basic `boxplot` plot ---

# Generate some random data for a single box plot.
# `numpy.random.rand` generates a uniform distribution between 0 and 1.
data_single = np.random.rand(100)

# Create a figure and axes
fig, ax = plt.subplots()

# `boxplot` takes a single list or array of data.
ax.boxplot(data_single)

ax.set_title("Basic Box Plot")
ax.set_ylabel("Data Values")
ax.set_xlabel("Dataset")
ax.set_xticks([1]) # Set the x-tick to be a single value for a single box plot.
ax.set_xticklabels(['Data 1']) # Label the x-axis tick.

plt.show()


# --- 2. Multiple box plots on the same axes ---

# Generate data for three different datasets.
data_multi = [
    np.random.normal(0, 1, 100),  # Normally distributed data
    np.random.gamma(2, 2, 100),   # Gamma distributed data
    np.random.rand(100) * 10      # Uniformly distributed data scaled
]

fig, ax = plt.subplots()

# `boxplot` can take a list of arrays or a 2D array to plot multiple boxes.
ax.boxplot(data_multi)

ax.set_title("Multiple Box Plots")
ax.set_ylabel("Values")
ax.set_xlabel("Datasets")
ax.set_xticklabels(['Normal', 'Gamma', 'Uniform']) # Label each box plot.

plt.show()


# --- 3. Customizing the box plot appearance ---

# Generate new data with some clear outliers.
data_custom = np.random.normal(50, 10, 200)
data_custom = np.append(data_custom, [90, -10, 100]) # Add outliers

fig, ax = plt.subplots()

# `vert=False` plots the box plot horizontally.
# `patch_artist=True` fills the boxes with colors.
# `notch=True` creates a notched box plot, which can indicate confidence intervals.
# `medianprops` customizes the median line.
# `flierprops` customizes the outlier points (fliers).
# `boxprops` customizes the box.
# `whiskerprops` customizes the whiskers.
# `capprops` customizes the caps.
ax.boxplot(data_custom, vert=False, patch_artist=True, notch=True,
           medianprops={'color': 'red', 'linewidth': 2},
           flierprops={'marker': 'o', 'markerfacecolor': 'green', 'markersize': 8},
           boxprops={'facecolor': 'lightblue', 'edgecolor': 'blue'},
           whiskerprops={'color': 'black', 'linestyle': '--'},
           capprops={'color': 'black'})

ax.set_title("Customized Horizontal Box Plot")
ax.set_xlabel("Values")

plt.show()