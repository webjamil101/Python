import pandas as pd
import numpy as np

print("--- Pandas Grouping Practice Code ---")

# --- 1. Setup: Create a Rich Sample DataFrame ---
print("\n--- 1. Sample DataFrame Setup ---")

# Data for a hypothetical sales company
data = {
    'Region': ['East', 'East', 'West', 'West', 'Central', 'East', 'West', 'Central', 'East', 'West', 'Central', 'East', 'East'],
    'Salesperson': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice', 'Charlie', 'David', 'Bob', 'Alice', 'David', 'Charlie', 'Bob'],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'B', 'A', 'A', 'C', 'B', 'A', 'B'],
    'Sales_Amount': [100, 150, 120, 80, 200, 90, 110, 130, 140, 70, 160, 180, 190],
    'Units_Sold': [10, 15, 12, 8, 20, 9, 11, 13, 14, 7, 16, 18, 19],
    'Order_Date': pd.to_datetime(['2023-01-05', '2023-01-10', '2023-01-15', '2023-01-20', '2023-02-01',
                                  '2023-02-05', '2023-02-10', '2023-02-15', '2023-03-01', '2023-03-05',
                                  '2023-03-10', '2023-03-15', '2023-03-20']),
    'Commission_Rate': [0.1, 0.1, 0.12, 0.1, 0.15, 0.1, 0.12, 0.1, 0.1, 0.1, 0.15, 0.12, 0.1]
}
df = pd.DataFrame(data)

# Introduce some missing values for practice
df.loc[3, 'Units_Sold'] = np.nan
df.loc[7, 'Sales_Amount'] = np.nan
df.loc[10, 'Product'] = np.nan

print("Original DataFrame (df):\n", df)
print("\nDataFrame Info (showing dtypes and non-null counts):\n")
df.info()

print("\n--- 2. Basic Grouping and Single Aggregation ---")

# 2.1 Total Sales Amount by Region
total_sales_by_region = df.groupby('Region')['Sales_Amount'].sum()
print("\nTotal Sales Amount by Region:\n", total_sales_by_region)

# 2.2 Average Units Sold by Product
avg_units_by_product = df.groupby('Product')['Units_Sold'].mean()
print("\nAverage Units Sold by Product:\n", avg_units_by_product)

# 2.3 Count of orders by Salesperson
order_count_by_salesperson = df.groupby('Salesperson').size() # .size() counts all rows in group
print("\nNumber of Orders by Salesperson:\n", order_count_by_salesperson)

# 2.4 Max Sales_Amount by Region (handling NaNs in aggregation)
max_sales_by_region = df.groupby('Region')['Sales_Amount'].max()
print("\nMax Sales Amount by Region (NaNs in original data are ignored by default):\n", max_sales_by_region)


print("\n--- 3. Grouping by Multiple Columns ---")

# 3.1 Total Sales Amount by Region and Product
total_sales_by_region_product = df.groupby(['Region', 'Product'])['Sales_Amount'].sum()
print("\nTotal Sales Amount by Region and Product:\n", total_sales_by_region_product)
# Note: The output has a MultiIndex. You can reset it to get columns:
# print("\n...as DataFrame with reset_index():\n", total_sales_by_region_product.reset_index())

# 3.2 Average Units Sold by Salesperson and Product
avg_units_by_salesperson_product = df.groupby(['Salesperson', 'Product'])['Units_Sold'].mean()
print("\nAverage Units Sold by Salesperson and Product:\n", avg_units_by_salesperson_product)


print("\n--- 4. Multiple Aggregations with .agg() ---")

# 4.1 Aggregate multiple statistics for a single column
region_sales_stats = df.groupby('Region')['Sales_Amount'].agg(['sum', 'mean', 'max', 'min', 'count', 'std'])
print("\nSales Amount Statistics by Region:\n", region_sales_stats)

# 4.2 Aggregate different statistics for different columns
multi_column_agg = df.groupby('Salesperson').agg(
    total_sales=('Sales_Amount', 'sum'),
    avg_units=('Units_Sold', 'mean'),
    num_orders=('Order_Date', 'count'), # Count non-null dates
    min_commission=('Commission_Rate', 'min')
)
print("\nAggregated Salesperson Performance:\n", multi_column_agg)

# 4.3 Using multiple functions on the same column
product_units_stats = df.groupby('Product')['Units_Sold'].agg(['mean', 'sum', 'std', lambda x: x.max() - x.min()])
print("\nUnits Sold Stats by Product (with custom lambda for range):\n", product_units_stats)


print("\n--- 5. Custom Aggregations (using .apply() and .agg() with functions) ---")

# 5.1 Custom function with .apply() on a Series
def get_gpa_category(x):
    """Example custom function to get category based on average GPA."""
    if x.empty:
        return np.nan
    avg_score = x.mean()
    if avg_score >= 150:
        return 'High Performing'
    elif avg_score >= 100:
        return 'Mid Performing'
    else:
        return 'Low Performing'

performance_category = df.groupby('Region')['Sales_Amount'].apply(get_gpa_category)
print("\nSales Performance Category by Region (custom apply):\n", performance_category)

# 5.2 Custom function with .agg()
def sales_range(series):
    return series.max() - series.min()

region_sales_range = df.groupby('Region').agg(
    SalesAmountRange=('Sales_Amount', sales_range),
    UnitsSoldStd=('Units_Sold', 'std')
)
print("\nSales Amount Range and Units Sold Std by Region (custom agg):\n", region_sales_range)


print("\n--- 6. Transformations with .transform() ---")
# .transform() returns a Series/DataFrame with the same index and size as the original,
# with the aggregated value broadcast to each original row.

# 6.1 Normalize Sales_Amount within each Region (subtract mean, divide by std)
df['Sales_Amount_Normalized_by_Region'] = df.groupby('Region')['Sales_Amount'].transform(lambda x: (x - x.mean()) / x.std())
print("\nDataFrame with Sales_Amount Normalized by Region:\n", df[['Region', 'Sales_Amount', 'Sales_Amount_Normalized_by_Region']])

# 6.2 Fill missing 'Units_Sold' with the mean of 'Units_Sold' for that 'Product'
df['Units_Sold_Filled'] = df.groupby('Product')['Units_Sold'].transform(lambda x: x.fillna(x.mean()))
print("\nUnits_Sold with NaNs filled by Product-level Mean:\n", df[['Product', 'Units_Sold', 'Units_Sold_Filled']])

# 6.3 Calculate a region's total sales and add it as a new column to original df
df['Region_Total_Sales'] = df.groupby('Region')['Sales_Amount'].transform('sum')
print("\nDataFrame with Region Total Sales column added:\n", df[['Region', 'Sales_Amount', 'Region_Total_Sales']])


print("\n--- 7. Filtering Groups with .filter() ---")
# .filter() allows you to drop groups based on a condition.
# The condition must return a single True/False value per group.

# 7.1 Keep only regions where the total sales amount is greater than 500
filtered_regions_by_sales = df.groupby('Region').filter(lambda x: x['Sales_Amount'].sum() > 500)
print("\nRegions with total sales > 500:\n", filtered_regions_by_sales)

# 7.2 Keep only salespersons who have more than 3 orders (non-null Sales_Amount)
filtered_salesperson_by_orders = df.groupby('Salesperson').filter(lambda x: x['Sales_Amount'].count() > 3)
print("\nSalespersons with more than 3 non-null orders:\n", filtered_salesperson_by_orders)


print("\n--- 8. Iterating through Groups ---")
# Useful for performing complex operations on each group

# Iterate and print basic info for each group
print("\n--- Iterating through groups (Region) ---")
for region_name, group_df in df.groupby('Region'):
    print(f"\nRegion: {region_name}")
    print(f"Number of orders: {len(group_df)}")
    print(f"Average Sales: {group_df['Sales_Amount'].mean():.2f}")

# You can process each group and store results
processed_groups = []
for salesperson, group_df in df.groupby('Salesperson'):
    if salesperson == 'Alice': # Example: special handling for Alice
        group_df['Adjusted_Sales'] = group_df['Sales_Amount'] * 1.05
    else:
        group_df['Adjusted_Sales'] = group_df['Sales_Amount']
    processed_groups.append(group_df)

df_processed = pd.concat(processed_groups)
print("\nDataFrame after iterating and processing groups (e.g., Alice's sales adjusted):\n", df_processed[['Salesperson', 'Sales_Amount', 'Adjusted_Sales']].head())


print("\n--- 9. Time-based Grouping (Resampling) ---")
# For DataFrames with a DateTimeIndex, resample is a powerful grouping tool.

df_time_series = df.set_index('Order_Date').sort_index()
print("\nDataFrame with Order_Date as index:\n", df_time_series)

# Resample daily data to monthly sum of sales
monthly_sales = df_time_series['Sales_Amount'].resample('M').sum()
print("\nMonthly Total Sales (resample 'M').sum():\n", monthly_sales)

# Resample weekly average of Units_Sold
weekly_avg_units = df_time_series['Units_Sold'].resample('W').mean()
print("\nWeekly Average Units Sold (resample 'W').mean():\n", weekly_avg_units)


print("\n--- 10. Grouping on Categorical vs. Non-Categorical Columns ---")
# While any column can be grouped by, Pandas is often more efficient with 'Categorical' dtype.

df_dtypes_check = df.copy()
# Convert 'Region' to categorical type (good practice for fixed categories)
df_dtypes_check['Region'] = df_dtypes_check['Region'].astype('category')
print("\nDataFrame dtypes after converting 'Region' to 'category':\n")
df_dtypes_check.info()

# Grouping on categorical column
category_group_result = df_dtypes_check.groupby('Region')['Sales_Amount'].sum()
print("\nTotal Sales by Categorical Region:\n", category_group_result)


print("\n--- End of Pandas Grouping Practice Code ---")