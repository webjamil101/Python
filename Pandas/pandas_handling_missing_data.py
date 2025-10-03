import pandas as pd
import numpy as np

print("--- Pandas Handling Missing Data Practice Code ---")

# --- 1. Setup: Create a Sample DataFrame with Various Missing Data Types ---
print("\n--- 1. Sample DataFrame Setup ---")

data = {
    'OrderID': range(101, 111),
    'CustomerID': [1, 2, 3, 1, 4, 5, 2, 6, 7, 8],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Monitor', 'Mouse', 'Keyboard', 'Webcam', 'Laptop', 'Monitor'],
    'Sales_Amount': [1000.0, 50.0, 75.0, np.nan, 300.0, 45.0, 80.0, np.nan, 1200.0, 350.0],
    'Units_Sold': [1, 2, 1, 1, 2, np.nan, 1, 1, 1, np.nan],
    'Region': ['East', 'West', 'North', 'East', 'South', 'West', 'North', 'East', 'South', 'West'],
    'Delivery_Status': ['Delivered', 'Pending', 'Delivered', 'Pending', np.nan, 'Delivered', 'Pending', 'Delivered', 'Pending', np.nan],
    'Customer_Rating': [4, 5, 3, 4, np.nan, 5, 4, 3, 5, 4],
    'Comments': ['Good', '', 'OK', None, 'Fast', 'Great', '', 'Bad', None, 'Awesome'], # Empty string, None
    'Old_Score': [90, 85, -999, 70, 95, 80, -999, 75, 88, 92] # Placeholder for missing
}
df = pd.DataFrame(data)

# Show initial state and info to highlight NaNs
print("Original DataFrame (df):\n", df)
print("\nDataFrame Info (showing non-null counts):\n")
df.info()


print("\n--- 2. Identifying Missing Data ---")

# 2.1 Using .isnull() or .isna() (they are aliases)
print("\nDataFrame.isnull() (Boolean mask):\n", df.isnull().head()) # Show first few rows

# 2.2 Using .notnull()
print("\nDataFrame.notnull() (Boolean mask):\n", df.notnull().head())

# 2.3 Check for any missing values in the entire DataFrame
print("\nAre there any missing values in the DataFrame?", df.isnull().any().any())

# 2.4 Check for missing values in specific columns
print("\nIs 'Sales_Amount' column null?\n", df['Sales_Amount'].isnull())
print("\nIs 'Units_Sold' column not null?\n", df['Units_Sold'].notnull())


print("\n--- 3. Counting Missing Data ---")

# 3.1 Count missing values per column
print("\nNumber of missing values per column (df.isnull().sum()):\n", df.isnull().sum())

# 3.2 Count missing values in the entire DataFrame
print("\nTotal missing values in DataFrame:", df.isnull().sum().sum())

# 3.3 Get percentage of missing values per column
missing_percentage = (df.isnull().sum() / len(df)) * 100
print("\nPercentage of missing values per column:\n", missing_percentage)

# 3.4 Identify columns with ALL missing values
all_nan_cols = df.columns[df.isnull().all()].tolist()
print("\nColumns with all missing values:", all_nan_cols)

# 3.5 Identify columns with ANY missing values
any_nan_cols = df.columns[df.isnull().any()].tolist()
print("Columns with any missing values:", any_nan_cols)


print("\n--- 4. Dropping Missing Data (.dropna()) ---")

# Create a copy to perform destructive operations
df_copy = df.copy()

# 4.1 Drop rows with ANY missing values (default: how='any', axis=0)
df_dropped_any_row = df_copy.dropna()
print("\nDataFrame after dropping rows with ANY NaN:\n", df_dropped_any_row)

# 4.2 Drop rows only if ALL values are missing in that row
# (Not applicable to our df, as no row has all NaNs)
df_dropped_all_row = df_copy.dropna(how='all')
print("\nDataFrame after dropping rows with ALL NaNs (likely no change here):\n", df_dropped_all_row)

# 4.3 Drop columns with ANY missing values (axis=1)
df_dropped_any_col = df_copy.dropna(axis=1)
print("\nDataFrame after dropping columns with ANY NaN:\n", df_dropped_any_col.head())

# 4.4 Drop columns only if ALL values are missing in that column
# Add a column with all NaNs for demonstration
df_copy['All_NaN_Col'] = np.nan
df_dropped_all_col = df_copy.dropna(axis=1, how='all')
print("\nDataFrame after dropping columns with ALL NaNs:\n", df_dropped_all_col.head())

# 4.5 Drop rows that don't have at least 'thresh' non-missing values
df_thresh_rows = df_copy.dropna(thresh=7) # Requires at least 7 non-NaN values
print("\nDataFrame after dropping rows with less than 7 non-NaNs:\n", df_thresh_rows)

# 4.6 Drop rows where specific subset of columns have missing values
df_subset_drop = df_copy.dropna(subset=['Sales_Amount', 'Units_Sold'])
print("\nDataFrame after dropping rows with NaN in 'Sales_Amount' or 'Units_Sold':\n", df_subset_drop)


print("\n--- 5. Filling Missing Data (.fillna()) ---")

# Use df_copy again for fresh fillna demonstrations
df_fill = df.copy()

# 5.1 Fill with a scalar value (e.g., 0)
df_filled_zero = df_fill.fillna(0)
print("\nDataFrame after filling all NaNs with 0:\n", df_filled_zero)

# 5.2 Fill with mean/median/mode of the column
# Fill 'Sales_Amount' with its mean
df_fill['Sales_Amount_Filled_Mean'] = df_fill['Sales_Amount'].fillna(df_fill['Sales_Amount'].mean())
# Fill 'Units_Sold' with its median
df_fill['Units_Sold_Filled_Median'] = df_fill['Units_Sold'].fillna(df_fill['Units_Sold'].median())
# Fill 'Delivery_Status' with its mode
df_fill['Delivery_Status_Filled_Mode'] = df_fill['Delivery_Status'].fillna(df_fill['Delivery_Status'].mode()[0])
print("\nDataFrame after filling specific columns with mean/median/mode:\n",
      df_fill[['Sales_Amount', 'Sales_Amount_Filled_Mean', 'Units_Sold', 'Units_Sold_Filled_Median', 'Delivery_Status', 'Delivery_Status_Filled_Mode']])

# 5.3 Forward fill (ffill) and Backward fill (bfill)
# Note: Data usually needs to be sorted for meaningful ffill/bfill
df_sorted = df.sort_values(by='OrderID').copy() # Ensure chronological order for ffill/bfill

# Forward fill 'Sales_Amount'
df_sorted['Sales_Amount_FFill'] = df_sorted['Sales_Amount'].fillna(method='ffill')
# Backward fill 'Units_Sold'
df_sorted['Units_Sold_BFill'] = df_sorted['Units_Sold'].fillna(method='bfill')
print("\nDataFrame after ffill/bfill (requires sorting):\n",
      df_sorted[['OrderID', 'Sales_Amount', 'Sales_Amount_FFill', 'Units_Sold', 'Units_Sold_BFill']])

# 5.4 Fill different columns with different values using a dictionary
df_fill_dict = df.copy()
fill_values = {
    'Sales_Amount': 0,
    'Units_Sold': 1,
    'Delivery_Status': 'Unknown',
    'Customer_Rating': df_fill_dict['Customer_Rating'].mean()
}
df_filled_with_dict = df_fill_dict.fillna(fill_values)
print("\nDataFrame after filling NaNs with specific values per column (using dict):\n", df_filled_with_dict)


print("\n--- 6. Interpolation (.interpolate()) ---")
# Best for numerical series with some order (like time series)

# Create a Series with more consecutive NaNs for interpolation demo
s_interp = pd.Series([10, 12, np.nan, np.nan, 18, 20, np.nan, 26])
print("\nOriginal Series for interpolation:\n", s_interp)

# 6.1 Linear interpolation (default method)
s_interp_linear = s_interp.interpolate(method='linear')
print("Linear Interpolation:\n", s_interp_linear)

# 6.2 Polynomial interpolation (requires 'order' parameter)
# s_interp_poly = s_interp.interpolate(method='polynomial', order=2)
# print("Polynomial (order 2) Interpolation:\n", s_interp_poly) # Might show warnings for small series

# 6.3 Using 'index' method if index is numeric and represents time/order
s_interp_with_index = pd.Series([10, 12, np.nan, np.nan, 18, 20], index=[1, 2, 4, 5, 7, 8])
s_interp_index_method = s_interp_with_index.interpolate(method='index')
print("\nInterpolation using index method:\n", s_interp_index_method)


print("\n--- 7. Replacing Specific Values as Missing ---")
# Sometimes missing data is represented by placeholders like -999, 0, or empty strings.

df_replace = df.copy()

# Replace -999 in 'Old_Score' with NaN
df_replace['Old_Score'] = df_replace['Old_Score'].replace(-999, np.nan)
print("\n'Old_Score' after replacing -999 with NaN:\n", df_replace[['OrderID', 'Old_Score']])

# Replace empty strings '' in 'Comments' with NaN
df_replace['Comments'] = df_replace['Comments'].replace('', np.nan)
print("\n'Comments' after replacing empty strings with NaN:\n", df_replace[['OrderID', 'Comments']])

# Now you can use standard fillna/dropna on these newly created NaNs
print("\nMissing values after replacing placeholders:\n", df_replace.isnull().sum())


print("\n--- 8. Contextual Filling (Group-based Imputation) ---")
# Fill missing values based on the mean/median/mode of their respective groups.

df_context = df.copy()

# Fill 'Sales_Amount' NaNs with the mean 'Sales_Amount' of their 'Region'
df_context['Sales_Amount_Filled_By_Region'] = df_context.groupby('Region')['Sales_Amount'].transform(lambda x: x.fillna(x.mean()))
print("\nSales_Amount filled by Region's mean:\n", df_context[['Region', 'Sales_Amount', 'Sales_Amount_Filled_By_Region']])

# Fill 'Units_Sold' NaNs with the median 'Units_Sold' of their 'Product'
df_context['Units_Sold_Filled_By_Product'] = df_context.groupby('Product')['Units_Sold'].transform(lambda x: x.fillna(x.median()))
print("\nUnits_Sold filled by Product's median:\n", df_context[['Product', 'Units_Sold', 'Units_Sold_Filled_By_Product']])


print("\n--- End of Pandas Handling Missing Data Code ---")