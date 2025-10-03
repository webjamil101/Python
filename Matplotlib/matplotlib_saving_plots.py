import matplotlib.pyplot as plt
import numpy as np

print("--- Matplotlib Saving Plots: All About in Code ---")

# --- 1. Basic Saving (`plt.savefig()`) ---
print("\n--- 1. Basic Saving (`plt.savefig()`) ---")
print("The simplest way to save a plot is to call `plt.savefig()` before `plt.show()` (or instead of it).")

# Create a sample plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(8, 5))
plt.plot(x, y, color='blue', linewidth=2)
plt.title("My First Saved Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True, linestyle='--', alpha=0.7)

# 1.1 Saving as PNG (Portable Network Graphics - Raster Image)
# Good for web, presentations, or when you need a fixed-resolution image.
filename_png = "my_first_plot.png"
plt.savefig(filename_png)
print(f"Plot saved as '{filename_png}'")

# 1.2 Saving as PDF (Portable Document Format - Vector Image)
# Excellent for publications, print, and when you need scalable, high-quality output.
filename_pdf = "my_first_plot.pdf"
plt.savefig(filename_pdf)
print(f"Plot saved as '{filename_pdf}'")

# 1.3 Saving as SVG (Scalable Vector Graphics - Vector Image)
# Good for web and situations where you might want to edit the graphic in vector editors.
filename_svg = "my_first_plot.svg"
plt.savefig(filename_svg)
print(f"Plot saved as '{filename_svg}'")

# 1.4 Other common formats: JPG, TIFF, EPS
# plt.savefig("my_first_plot.jpg")
# plt.savefig("my_first_plot.tiff")
# plt.savefig("my_first_plot.eps")

# IMPORTANT: After `plt.savefig()`, it's often good practice to close the figure
# if you are generating many plots in a loop to avoid memory issues.
plt.close() # Closes the current figure


# --- 2. Customizing Saved Plots ---
print("\n--- 2. Customizing Saved Plots ---")

# Create another sample plot for customization
x_custom = np.linspace(0, 5, 50)
y_custom = np.exp(-x_custom) * np.cos(5 * x_custom)
plt.figure(figsize=(7, 5))
plt.plot(x_custom, y_custom, color='darkgreen', marker='o', markersize=4, linestyle='-')
plt.title("Customized Saved Plot")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True, alpha=0.6)

# 2.1 Setting DPI (Dots Per Inch) for Raster Images
print("\n--- 2.1 Setting DPI (for Raster Images) ---")
# Higher DPI means higher resolution. Default is often 100 or 72.
# For print, 300 DPI or 600 DPI are common.
filename_high_dpi = "custom_plot_300dpi.png"
plt.savefig(filename_high_dpi, dpi=300)
print(f"Plot saved as '{filename_high_dpi}' with 300 DPI")

filename_low_dpi = "custom_plot_50dpi.png"
plt.savefig(filename_low_dpi, dpi=50) # Noticeable pixelation
print(f"Plot saved as '{filename_low_dpi}' with 50 DPI (lower quality)")


# 2.2 Transparent Background (`transparent=True`)
print("\n--- 2.2 Transparent Background ---")
# Useful for overlaying plots on different backgrounds in presentations.
filename_transparent = "custom_plot_transparent.png"
plt.savefig(filename_transparent, transparent=True, dpi=200)
print(f"Plot saved as '{filename_transparent}' with transparent background")


# 2.3 Setting Facecolor (`facecolor`)
print("\n--- 2.3 Setting Facecolor ---")
# Change the background color of the saved figure.
filename_custom_facecolor = "custom_plot_blue_bg.png"
plt.savefig(filename_custom_facecolor, facecolor='lightblue', dpi=150)
print(f"Plot saved as '{filename_custom_facecolor}' with lightblue background")


# 2.4 Bounding Box (`bbox_inches='tight'`)
print("\n--- 2.4 Bounding Box (`bbox_inches='tight'`) ---")
# This option attempts to trim any extra white space around the plot,
# making the saved image "tight" to the plot content. Very useful!
filename_tight = "custom_plot_tight.png"
plt.savefig(filename_tight, bbox_inches='tight', dpi=200)
print(f"Plot saved as '{filename_tight}' with tight bounding box")

# You can also specify specific padding around the tight box
filename_tight_pad = "custom_plot_tight_pad.png"
plt.savefig(filename_tight_pad, bbox_inches='tight', pad_inches=0.1, dpi=200)
print(f"Plot saved as '{filename_tight_pad}' with tight bounding box and 0.1 inch padding")

plt.close()


# --- 3. Saving Multiple Subplots ---
print("\n--- 3. Saving Multiple Subplots ---")

fig_multi, axes_multi = plt.subplots(1, 2, figsize=(10, 5))
x_multi = np.linspace(0, 10, 50)

axes_multi[0].plot(x_multi, np.sin(x_multi), color='red')
axes_multi[0].set_title("Subplot 1 (Sine)")
axes_multi[0].grid(True)

axes_multi[1].scatter(x_multi, np.cos(x_multi), color='green')
axes_multi[1].set_title("Subplot 2 (Cosine)")
axes_multi[1].grid(True)

plt.suptitle("Figure with Multiple Subplots", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust for super title

filename_subplots = "multiple_subplots.png"
plt.savefig(filename_subplots, dpi=250, bbox_inches='tight')
print(f"Saved: '{filename_subplots}' (containing multiple subplots)")
plt.close(fig_multi) # Close the figure object


# --- 4. Using `figure.savefig()` (Object-Oriented Approach) ---
print("\n--- 4. Using `figure.savefig()` (Object-Oriented Approach) ---")
print("When using `fig, ax = plt.subplots()`, you should save using the figure object.")

fig_oo, ax_oo = plt.subplots(figsize=(7, 5))
ax_oo.plot(x, x**2, color='darkviolet')
ax_oo.set_title("Object-Oriented Plot")
ax_oo.set_xlabel("X")
ax_oo.set_ylabel("Y-squared")

filename_oo = "object_oriented_plot.pdf"
fig_oo.savefig(filename_oo, dpi=200, bbox_inches='tight')
print(f"Saved: '{filename_oo}' using figure object's savefig method.")
plt.close(fig_oo)


# --- 5. Saving Before or After `plt.show()` ---
print("\n--- 5. Saving Before or After `plt.show()` ---")
print("Important: `plt.savefig()` should typically be called before `plt.show()` when running a script.")
print("If `plt.show()` is called first, it might clear the figure, resulting in an empty saved file.")

# Example: Saving *before* show
plt.figure(figsize=(6, 4))
plt.bar(['A', 'B', 'C'], [10, 20, 15], color='skyblue')
plt.title("Save Before Show Example")
plt.savefig("save_before_show.png") # Save
print("Saved: 'save_before_show.png' (before plt.show())")
plt.show() # Then show

# Example: Saving *after* show (might not work as expected in all environments)
# In some interactive environments (like Jupyter), it might still work because the figure
# state is retained. In a standalone script, it often won't save anything or an empty plot.
plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3], [1, 4, 9], 'ro-')
plt.title("Save After Show Example (Caution!)")
plt.show() # Display the plot
# plt.savefig("save_after_show_caution.png") # This line might save an empty plot in a script!
# print("Attempted to save 'save_after_show_caution.png' (after plt.show()) - check if it worked.")
plt.close()


print("\n--- End of Matplotlib Saving Plots Practice Code ---")

# Summary of Key Parameters for `plt.savefig()`:
# - `fname`: The filename (e.g., "my_plot.png", "my_plot.pdf"). Matplotlib infers format from extension.
# - `dpi`: Resolution for raster formats (PNG, JPG, etc.). Higher = more pixels.
# - `transparent`: If True, background is transparent.
# - `facecolor`: Background color of the figure canvas.
# - `bbox_inches`: 'tight' often desired to trim whitespace.
# - `pad_inches`: Padding around the tight bounding box.




import matplotlib.pyplot as plt
import numpy as np
import os # For managing directories and file paths

print("--- Matplotlib Saving Plots: More Advanced Code ---")

# Create some consistent data for all plots
x_data = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x_data)
y_cos = np.cos(x_data)

# --- 1. Supported File Formats Revisited ---
print("\n--- 1. Supported File Formats Revisited ---")
print("Matplotlib supports a wide range of output formats. The format is typically inferred from the filename extension.")

# Create a sample plot
plt.figure(figsize=(9, 6))
plt.plot(x_data, y_sin, label='Sine', color='darkblue')
plt.plot(x_data, y_cos, label='Cosine', color='darkred', linestyle='--')
plt.title("Various Output Formats")
plt.xlabel("Angle (radians)")
plt.ylabel("Value")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)

# 1.1 Postscript / EPS (Encapsulated Postscript)
# Vector format, common in scientific publishing, especially LaTeX.
filename_eps = "plot_output.eps"
plt.savefig(filename_eps)
print(f"Saved: '{filename_eps}' (Vector - EPS)")

# 1.2 TIFF (Tagged Image File Format)
# Raster format, often used in professional printing due to its lossless compression.
filename_tiff = "plot_output.tiff"
plt.savefig(filename_tiff)
print(f"Saved: '{filename_tiff}' (Raster - TIFF)")

# 1.3 JPG (Joint Photographic Experts Group - Raster Image)
# Lossy compression, good for web/email where file size is critical.
# You can control quality.
filename_jpg = "plot_output.jpg"
plt.savefig(filename_jpg, quality=90, optimize=True) # quality (0-100), optimize for file size
print(f"Saved: '{filename_jpg}' (Raster - JPG, quality=90)")

plt.close() # Close current figure


# --- 2. Saving to a Specific Directory ---
print("\n--- 2. Saving to a Specific Directory ---")
print("You can specify a full path, including a directory, to save your plots.")

output_directory = "my_plots_output"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Created directory: '{output_directory}'")

plt.figure(figsize=(7, 5))
plt.bar(['Item X', 'Item Y', 'Item Z'], [100, 150, 120], color='skyblue')
plt.title("Plot in a Specific Directory")
plt.xlabel("Items")
plt.ylabel("Count")

full_path_filename = os.path.join(output_directory, "bar_chart_in_folder.png")
plt.savefig(full_path_filename, dpi=200, bbox_inches='tight')
print(f"Saved: '{full_path_filename}'")
plt.close()


# --- 3. Including External Artists with `bbox_extra_artists` ---
print("\n--- 3. Including External Artists with `bbox_extra_artists` ---")
print("`bbox_inches='tight'` usually tries to include all axes elements, but if you add custom text or annotations outside the default bounding box, you might need this.")

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x_data, y_sin, color='blue')
ax.set_title("Plot with External Text")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)

# Add some text far outside the plot area, using figure coordinates
fig_text_obj = fig.text(0.01, 0.99, "This is a Note Outside Axes",
                        fontsize=10, color='gray', ha='left', va='top')

# Add an annotation that might go slightly out of bounds
annot_obj = ax.annotate('Max Point', xy=(np.pi/2, 1), xytext=(np.pi/2 + 2, 1.2),
                        arrowprops=dict(facecolor='black', shrink=0.05),
                        fontsize=12, color='darkgreen')

filename_extra_artists_no_bbox = os.path.join(output_directory, "extra_artists_no_bbox.png")
plt.savefig(filename_extra_artists_no_bbox, dpi=150) # May cut off text
print(f"Saved: '{filename_extra_artists_no_bbox}' (Might cut off external text)")

# Now, save again, explicitly including the external text objects
filename_extra_artists_with_bbox = os.path.join(output_directory, "extra_artists_with_bbox.png")
plt.savefig(filename_extra_artists_with_bbox, dpi=150, bbox_inches='tight',
            bbox_extra_artists=(fig_text_obj, annot_obj)) # Include the artists here
print(f"Saved: '{filename_extra_artists_with_bbox}' (With external text included)")

plt.close(fig)


# --- 4. Adding Metadata to Vector Files (PDF, SVG) ---
print("\n--- 4. Adding Metadata to Vector Files ---")
print("You can embed information like author, title, creation date, etc., in the file.")

fig_meta, ax_meta = plt.subplots(figsize=(7, 5))
ax_meta.hist(np.random.randn(500), bins=30, color='purple', edgecolor='black', alpha=0.7)
ax_meta.set_title("Histogram with Metadata")
ax_meta.set_xlabel("Value")
ax_meta.set_ylabel("Frequency")

metadata_dict = {
    'Author': 'Your Name',
    'Title': 'Analysis of Random Data',
    'Subject': 'Data Distribution',
    'Keywords': 'Python, Matplotlib, Histogram, Data Science'
}

filename_pdf_meta = os.path.join(output_directory, "plot_with_metadata.pdf")
fig_meta.savefig(filename_pdf_meta, metadata=metadata_dict, bbox_inches='tight')
print(f"Saved: '{filename_pdf_meta}' (with custom metadata)")
plt.close(fig_meta)


# --- 5. Setting Orientation for PDF/PS Output (`orientation`) ---
print("\n--- 5. Setting Orientation for PDF/PS Output ---")
print("For formats like PDF or Postscript, you can specify 'portrait' (default) or 'landscape'.")

fig_orient, ax_orient = plt.subplots(figsize=(6, 9)) # Taller than wide for portrait
ax_orient.plot(y_sin, x_data, color='brown') # Swapping x,y to make it vertical
ax_orient.set_title("Portrait Plot (Tall)")
ax_orient.set_xlabel("Value")
ax_orient.set_ylabel("Data Index")

filename_portrait = os.path.join(output_directory, "portrait_plot.pdf")
fig_orient.savefig(filename_portrait, orientation='portrait', bbox_inches='tight')
print(f"Saved: '{filename_portrait}' (Portrait orientation)")
plt.close(fig_orient)

fig_orient_land, ax_orient_land = plt.subplots(figsize=(9, 6)) # Wider than tall for landscape
ax_orient_land.plot(x_data, y_sin, color='darkorange')
ax_orient_land.set_title("Landscape Plot (Wide)")
ax_orient_land.set_xlabel("Data Index")
ax_orient_land.set_ylabel("Value")

filename_landscape = os.path.join(output_directory, "landscape_plot.pdf")
fig_orient_land.savefig(filename_landscape, orientation='landscape', bbox_inches='tight')
print(f"Saved: '{filename_landscape}' (Landscape orientation)")
plt.close(fig_orient_land)


# --- 6. Using a Context Manager for Saving (More Robust) ---
print("\n--- 6. Using a Context Manager for Saving (More Robust) ---")
print("This pattern ensures the figure is closed automatically, even if errors occur during plotting.")

with plt.io.BytesIO() as buffer: # A BytesIO object to simulate a file
    fig_buffer, ax_buffer = plt.subplots(figsize=(7, 5))
    ax_buffer.scatter(np.random.rand(50), np.random.rand(50), color='teal', alpha=0.7)
    ax_buffer.set_title("Context Manager Plot")
    ax_buffer.set_xlabel("X")
    ax_buffer.set_ylabel("Y")

    fig_buffer.savefig(buffer, format='png', dpi=150, bbox_inches='tight') # Save to buffer
    print("Plot saved to an in-memory buffer (can then write buffer to actual file or send)")

    # Example: How to write the buffer content to a file
    with open(os.path.join(output_directory, "context_manager_plot.png"), 'wb') as f:
        f.write(buffer.getvalue())
    print(f"Saved from buffer to '{os.path.join(output_directory, 'context_manager_plot.png')}'")

    # The figure `fig_buffer` is automatically closed when exiting the `with` block
    # No explicit `plt.close(fig_buffer)` is needed here.

print("\n--- End of Matplotlib Saving Plots: More Advanced Code ---")

# Reminder of good practices:
# - Always use `plt.close(fig)` or work within a context manager if generating many plots.
# - For vector formats (PDF, SVG, EPS), DPI primarily affects rasterized elements (like alpha transparency or image overlays).
# - For raster formats (PNG, JPG, TIFF), DPI directly controls the pixel dimensions.
# - `bbox_inches='tight'` is almost always recommended to prevent excess whitespace.
# - Consider `bbox_extra_artists` if labels or annotations extend beyond the typical plot boundaries.