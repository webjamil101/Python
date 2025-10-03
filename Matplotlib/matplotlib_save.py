# The `fig.savefig()` method saves the current figure to a file.
# It belongs to the Figure object, which is the top-level container for a plot.

import matplotlib.pyplot as plt
import numpy as np

# --- 1. Basic Plot Setup ---
fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x))
ax.set_title("My Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# --- 2. Saving the Figure ---

# The basic syntax requires only the filename.
# The file extension determines the format (e.g., '.png', '.jpg', '.pdf', '.svg').
# A PNG is a good default for raster graphics.
fig.savefig('my_plot.png')

# --- 3. Common Parameters ---

# You can customize the save process with various parameters:
# - `dpi`: Sets the resolution (dots per inch). Higher DPI means higher quality.
# - `bbox_inches`: Specifies the bounding box. 'tight' automatically crops whitespace.
# - `transparent`: Makes the background transparent.
fig.savefig('my_high_res_plot.png', dpi=300, bbox_inches='tight', transparent=True)

# --- 4. Saving in a Different Format ---

# You can change the format simply by changing the file extension.
# PDF and SVG are vector formats, which are great for scaling without loss of quality.
fig.savefig('my_plot.pdf')

# You can also explicitly specify the format.
fig.savefig('my_plot_explicit_format', format='svg')

# --- 5. Saving a figure with multiple subplots ---

fig_multi, axs = plt.subplots(1, 2)
axs[0].plot(x, x**2)
axs[1].plot(x, np.exp(-x))
fig_multi.suptitle("Subplots")
fig_multi.savefig('my_subplots.png', dpi=200)


'''
Certainly, Jamil! Here's the syntax and usage of `savefig()` in **Matplotlib**, which is used to save a plot as an image file:

---

### 🖼️ **Matplotlib `savefig()` Syntax**

```python
plt.savefig(fname, **kwargs)
```

---

### 📌 **Parameters**

| Parameter     | Description |
|---------------|-------------|
| `fname`       | Filename or path where the figure will be saved (e.g., `'plot.png'`, `'output.pdf'`) |
| `dpi`         | Resolution in dots per inch (e.g., `dpi=300`) |
| `format`      | File format (e.g., `'png'`, `'pdf'`, `'svg'`) |
| `bbox_inches` | `'tight'` trims extra whitespace around the figure |
| `transparent` | If `True`, the background will be transparent |
| `facecolor`   | Background color of the saved figure |
| `edgecolor`   | Edge color of the saved figure |

---

### ✅ **Example Usage**

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Simple Plot")

# Save as PNG with high resolution and tight layout
plt.savefig("my_plot.png", dpi=300, bbox_inches='tight')
```

Absolutely, Jamil! Here's a complete guide to using **grid lines** in Matplotlib — how to enable, customize, and control them for better visualization clarity.

---

## 📊 `plt.grid()` in Matplotlib — Full Syntax & Usage

### 🔧 **Basic Syntax**

```python
plt.grid(True)  # Turns grid on
plt.grid(False) # Turns grid off
```

---

### ⚙️ **Full Parameter List**

```python
plt.grid(
    b=None,               # True/False or None (default: None)
    which='major',        # 'major', 'minor', or 'both'
    axis='both',          # 'x', 'y', or 'both'
    color='gray',         # Grid line color
    linestyle='--',       # Line style: '-', '--', '-.', ':'
    linewidth=0.5,        # Thickness of grid lines
    alpha=0.7             # Transparency (0 to 1)
)
```

---

### ✅ **Examples**

#### 1. **Basic Grid**
```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.grid(True)
```

#### 2. **Custom Grid Style**
```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.grid(color='blue', linestyle=':', linewidth=1.5)
```

#### 3. **Grid Only on X-axis**
```python
plt.grid(axis='x')
```

#### 4. **Minor Grid Lines**
```python
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth=0.5)
```

#### 5. **Both Major and Minor Grids**
```python
plt.minorticks_on()
plt.grid(which='both', color='lightgray', linestyle='--', linewidth=0.7)
```

---

### 📌 **Tips**

- Use `plt.minorticks_on()` to activate minor ticks before using `which='minor'`.
- Combine `grid()` with `tight_layout()` or `bbox_inches='tight'` in `savefig()` to avoid clipping.


'''