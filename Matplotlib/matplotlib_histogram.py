import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("--- Matplotlib Histogram: All About in Code ---")

# --- 1. Basic Histogram ---
print("\n--- 1. Basic Histogram ---")
print("A histogram divides the data into bins and shows the number of observations (frequency) in each bin.")

# Generate some sample data: 1000 random numbers from a standard normal distribution
data_norm = np.random.randn(1000)

plt.figure(figsize=(8, 6)) # Create a new figure
plt.hist(data_norm)       # Create the histogram
plt.title("Basic Histogram of Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.75, linestyle='--') # Add horizontal grid lines
plt.show()


# --- 2. Customizing Histograms ---
print("\n--- 2. Customizing Histograms ---")

# 2.1 Number of Bins (`bins` parameter)
print("\n--- 2.1 Customizing Bins ---")
# 'bins' can be an integer (number of bins), a sequence (bin edges), or 'auto'/'fd'/'sturges'/'rice'
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1) # First subplot
plt.hist(data_norm, bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram with 10 Bins")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.75, linestyle=':')

plt.subplot(1, 2, 2) # Second subplot
plt.hist(data_norm, bins=50, color='lightgreen', edgecolor='black')
plt.title("Histogram with 50 Bins")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.75, linestyle=':')

plt.tight_layout() # Adjust subplots to fit in figure area.
plt.show()

# Custom bin edges (e.g., specific ranges)
bins_custom = [-3, -2, -1, 0, 1, 2, 3]
plt.figure(figsize=(7, 5))
plt.hist(data_norm, bins=bins_custom, color='lightsalmon', edgecolor='darkred')
plt.title("Histogram with Custom Bin Edges")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.xticks(bins_custom) # Set x-ticks to bin edges
plt.grid(axis='y', alpha=0.75, linestyle=':')
plt.show()

# 2.2 `density=True` (Normalized Histogram)
print("\n--- 2.2 Normalized Histogram (`density=True`) ---")
print("When `density=True`, the area under the histogram sums to 1. This is useful for comparing distributions.")
plt.figure(figsize=(8, 6))
plt.hist(data_norm, bins=30, density=True, color='violet', edgecolor='purple', alpha=0.7)
plt.title("Normalized Histogram (Probability Density)")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.grid(axis='y', alpha=0.75, linestyle='--')
plt.show()

# Overlaying a probability density function (PDF)
from scipy.stats import norm
x_pdf = np.linspace(-4, 4, 100)
pdf_values = norm.pdf(x_pdf, loc=0, scale=1) # PDF for standard normal distribution

plt.figure(figsize=(8, 6))
plt.hist(data_norm, bins=30, density=True, color='skyblue', edgecolor='black', alpha=0.6, label='Histogram')
plt.plot(x_pdf, pdf_values, color='red', linestyle='--', linewidth=2, label='Normal PDF')
plt.title("Histogram with Overlaid Normal PDF")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()


# 2.3 Color, Edge Color, Alpha
print("\n--- 2.3 Colors, Edges, Transparency ---")
plt.figure(figsize=(7, 5))
plt.hist(data_norm, bins=20,
         color='green',       # Fill color of bars
         edgecolor='darkgreen', # Border color of bars
         alpha=0.6,           # Transparency (0.0 to 1.0)
         label='Data Distribution')
plt.title("Histogram with Custom Colors")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(axis='y', alpha=0.75, linestyle='--')
plt.show()


# --- 3. Multiple Histograms on One Plot ---
print("\n--- 3. Multiple Histograms on One Plot ---")

# Generate two different datasets
data_set1 = np.random.normal(loc=0, scale=1, size=500)
data_set2 = np.random.normal(loc=2, scale=1.5, size=500) # Different mean and std dev

plt.figure(figsize=(10, 7))

# 3.1 Overlayed Histograms (transparent for comparison)
plt.hist(data_set1, bins=30, alpha=0.5, label='Dataset 1 (Mean=0, Std=1)', color='blue', edgecolor='black')
plt.hist(data_set2, bins=30, alpha=0.5, label='Dataset 2 (Mean=2, Std=1.5)', color='red', edgecolor='black')
plt.title("Overlayed Histograms")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

# 3.2 Stacked Histograms
# Histograms are stacked on top of each other. Requires a list of arrays.
plt.figure(figsize=(10, 7))
plt.hist([data_set1, data_set2],
         bins=30,
         stacked=True, # Stack the histograms
         color=['skyblue', 'lightcoral'],
         edgecolor='black',
         label=['Dataset 1', 'Dataset 2'])
plt.title("Stacked Histograms")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()


# --- 4. Using `histtype` Parameter ---
print("\n--- 4. Using `histtype` Parameter ---")
print("`histtype` controls the type of histogram to draw: 'bar' (default), 'barstacked', 'step', 'stepfilled'.")

plt.figure(figsize=(12, 5))

# 'step' - unfilled line plot
plt.subplot(1, 2, 1)
plt.hist(data_norm, bins=30, histtype='step', color='darkblue', linewidth=2, label='Step Histogram')
plt.title("`histtype='step'`")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

# 'stepfilled' - filled step plot
plt.subplot(1, 2, 2)
plt.hist(data_norm, bins=30, histtype='stepfilled', color='darkgreen', alpha=0.7, label='Stepfilled Histogram')
plt.title("`histtype='stepfilled'`")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

plt.tight_layout()
plt.show()


# --- 5. Histogram with Pandas DataFrame Column ---
print("\n--- 5. Histogram with Pandas DataFrame Column ---")
print("Pandas `df.hist()` method is a convenient wrapper around Matplotlib's `plt.hist()`.")

# Create a sample DataFrame
df = pd.DataFrame({
    'Feature_A': np.random.normal(loc=10, scale=2, size=500),
    'Feature_B': np.random.exponential(scale=1.5, size=500), # Exponential distribution
    'Category': np.random.choice(['X', 'Y', 'Z'], size=500)
})
print(f"\nDataFrame head:\n{df.head()}")

# Plotting a histogram for a specific column
plt.figure(figsize=(8, 6))
df['Feature_A'].hist(bins=20, color='purple', edgecolor='black', alpha=0.7)
plt.title("Histogram of 'Feature_A' (from Pandas)")
plt.xlabel("Feature A Value")
plt.ylabel("Frequency")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Plotting histograms for multiple numerical columns
# This automatically creates a subplot for each numerical column
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
df[['Feature_A', 'Feature_B']].hist(ax=axes, bins=25, color='orange', alpha=0.8, edgecolor='black')
fig.suptitle("Histograms of Features A and B", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to make space for suptitle
plt.show()


print("\n--- End of Matplotlib Histogram Practice Code ---")

# Reminder:
# - `plt.show()` displays the plot.
# - Adjust `bins` to reveal details or broad trends.
# - `density=True` for probability distributions.
# - `alpha` is useful for overlaying multiple distributions.