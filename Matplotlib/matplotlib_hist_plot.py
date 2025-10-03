import matplotlib.pyplot as plt
import numpy as np

# The `hist()` function in Matplotlib is used to plot a histogram.
# A histogram is a representation of the distribution of a variable.
# It partitions the entire range of values into a series of intervals (bins)
# and counts how many values fall into each interval.

# --- 1. Basic Histogram ---

# Generate some random data from a normal distribution.
data = np.random.randn(1000)

# `hist()` takes a 1D array of data.
# The `bins` argument can be an integer (number of bins) or an array of bin edges.
# The `alpha` argument sets the transparency of the bars.
plt.hist(data, bins=30, alpha=0.7)

# Add a title and labels for clarity.
plt.title("Basic Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


# --- 2. Customizing a Histogram ---

# Generate new data.
data2 = np.random.gamma(2, 2, 1000)

# `color` sets the color of the bars.
# `edgecolor` sets the color of the bar outlines.
# `density=True` normalizes the bins so the total area is 1.
# This makes it a probability density plot.
plt.hist(data2, bins=50, color='skyblue', edgecolor='black', density=True)

plt.title("Customized Histogram (Density Plot)")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.grid(True)
plt.show()


# --- 3. Multiple Histograms on the Same Plot ---

# Generate two different datasets.
data_a = np.random.normal(loc=-2, scale=1, size=1000)
data_b = np.random.normal(loc=2, scale=1, size=1000)

# Plotting two histograms on the same axes.
# `label` is used for the legend.
# `stacked=True` will stack the histograms on top of each other.
# If `stacked=False` (default), they will be overlaid.
plt.hist([data_a, data_b], bins=20, label=['Dataset A', 'Dataset B'], color=['red', 'blue'], alpha=0.6)

plt.title("Multiple Histograms")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()


# --- 4. Using `weights` and a different `histtype` ---

# `histtype='step'` plots a line instead of bars.
# `histtype='stepfilled'` plots a filled line.
# `weights` can be used to assign a weight to each data point.
data3 = np.random.beta(a=0.5, b=0.5, size=1000)

# Create some weights (e.g., all 1s for a standard histogram)
weights = np.ones_like(data3)

plt.hist(data3, bins=50, weights=weights, histtype='stepfilled', color='green', alpha=0.8)

plt.title("Step-filled Histogram with Weights")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()