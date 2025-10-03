import pandas as pd
import numpy as np

print("--- Pandas pivot_table() Practice Code ---")

# --- 1. Setup: Create a Rich Sample DataFrame ---
print("\n--- 1. Sample DataFrame Setup ---")

# Data for a hypothetical sales and customer feedback system
data = {
    'Date': pd.to_datetime(['2023-01-01', '2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02',
                            '2023-01-02', '2023-01-03', '2023-01-03', '2023-01-03', '2023-01-04',
                            '2023-01-04', '2023-01-05', '2023-01-05', '2023-01-05', '2023-01-06',
                            '2023-01-06', '2023-01-06', '2023-01-07', '2023-01-07', '2023-01-07']),
    'Region': ['East', 'West', 'East', 'West', 'East', 'East', 'North', 'South', 'North', 'East',
               'West', 'North', 'South', 'North', 'East', 'West', 'East', 'North', 'South', 'North'],
    'ProductType': ['Electronics', 'Electronics', 'Clothing', 'Books', 'Electronics', 'Books',
                    'Clothing', 'Books', 'Electronics', 'Clothing', 'Electronics', 'Books',
                    'Clothing', 'Electronics', 'Books', 'Clothing', 'Electronics', 'Clothing',
                    'Books', 'Electronics'],
    'Salesperson': ['Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Bob', 'David', 'Eve', 'David',
                    'Alice', 'Charlie', 'Eve', 'David', 'Eve', 'Alice', 'Bob', 'Charlie', 'David',
                    'Eve', 'Alice'],
    'Amount': np.random.uniform(20, 1000, 20).round(2),
    'Quantity': np.random.randint(1, 10, 20),
    'CustomerRating': np.random.randint(1, 6, 20), # 1 to 5 stars
    'DiscountGiven': np.random.choice([True, False], 20, p=[0.4, 0.6])
}
df = pd.DataFrame(data)

# Introduce some missing values for more robust testing
df.loc[[3, 7, 12], 'Amount'] = np.nan
df.loc[[1, 8, 11], 'CustomerRating'] = np.nan
df.loc[15, 'ProductType'] = np.nan

print("Original DataFrame (df):\n", df.head(10))
print("\nDataFrame Info:\n")
df.info()


print("\n--- 2. Basic Pivot Table ---")

# 2.1 Calculate the average 'Amount' for each 'Region' and 'ProductType'
# - `values`: Column(s) to aggregate.
# - `index`: Column(s) to form the new index (rows).
# - `columns`: Column(s) to form the new columns.
# - `aggfunc`: Function to aggregate values. Default is 'mean'.
pivot_basic_avg_amount = df.pivot_table(
    values='Amount',
    index='Region',
    columns='ProductType'
)
print("\nAverage Amount by Region and ProductType (default aggfunc='mean'):\n", pivot_basic_avg_amount)

# 2.2 Count the 'Quantity' for each 'Region' and 'Salesperson'
pivot_count_qty = df.pivot_table(
    values='Quantity',
    index='Region',
    columns='Salesperson',
    aggfunc='sum' # Use 'sum' to get total quantity
)
print("\nTotal Quantity by Region and Salesperson:\n", pivot_count_qty)


print("\n--- 3. Multiple Indices and Columns ---")

# 3.1 Use a list for `index` to create a MultiIndex on rows
pivot_multi_index = df.pivot_table(
    values='Amount',
    index=['Region', 'Salesperson'], # Hierarchical index on rows
    columns='ProductType',
    aggfunc='mean'
)
print("\nAverage Amount by Region, Salesperson, and ProductType (MultiIndex rows):\n", pivot_multi_index.head(8))

# 3.2 Use a list for `columns` to create a MultiIndex on columns
pivot_multi_columns = df.pivot_table(
    values='Amount',
    index='Region',
    columns=['ProductType', 'Salesperson'], # Hierarchical index on columns
    aggfunc='mean'
)
print("\nAverage Amount by Region, ProductType, and Salesperson (MultiIndex columns):\n", pivot_multi_columns.head())


print("\n--- 4. Multiple Aggregation Functions ---")

# 4.1 Pass a list of `aggfunc` to apply multiple aggregations to the `values` column(s)
pivot_multi_aggfunc = df.pivot_table(
    values='Amount',
    index='Region',
    columns='ProductType',
    aggfunc=['sum', 'mean', 'count', 'max'] # List of functions
)
print("\nAmount: Sum, Mean, Count, Max by Region and ProductType:\n", pivot_multi_aggfunc)


print("\n--- 5. Aggregating Multiple Value Columns ---")

# 5.1 Aggregate different `values` columns with the same `aggfunc`
pivot_multi_values = df.pivot_table(
    values=['Amount', 'Quantity'], # Aggregate both 'Amount' and 'Quantity'
    index='Region',
    columns='ProductType',
    aggfunc='sum' # Apply sum to both 'Amount' and 'Quantity'
)
print("\nTotal Amount and Total Quantity by Region and ProductType:\n", pivot_multi_values)

# 5.2 Aggregate different `values` columns with different `aggfunc`
# Use a dictionary for `aggfunc` where keys are `values` columns and values are aggregation functions.
pivot_diff_aggfuncs = df.pivot_table(
    values=['Amount', 'Quantity', 'CustomerRating'],
    index='Region',
    columns='ProductType',
    aggfunc={
        'Amount': 'sum',           # Sum of Amount
        'Quantity': 'mean',        # Mean of Quantity
        'CustomerRating': 'median' # Median CustomerRating
    }
)
print("\nMixed Aggregations (Sum Amount, Mean Quantity, Median Rating):\n", pivot_diff_aggfuncs)


print("\n--- 6. Handling Missing Combinations (`fill_value`) ---")

# 6.1 Fill NaN values in the pivot table with a specific value (e.g., 0)
pivot_filled_zero = df.pivot_table(
    values='Quantity',
    index='Salesperson',
    columns='ProductType',
    aggfunc='sum',
    fill_value=0 # Replace NaN with 0
)
print("\nTotal Quantity by Salesperson and ProductType (filled with 0):\n", pivot_filled_zero)


print("\n--- 7. Adding Row and Column Totals (`margins`) ---")

# 7.1 Add row and column totals (named 'All' by default)
pivot_with_margins = df.pivot_table(
    values='Amount',
    index='Region',
    columns='ProductType',
    aggfunc='sum',
    margins=True # Adds row and column totals
)
print("\nTotal Amount by Region and ProductType with 'All' margins:\n", pivot_with_margins)

# 7.2 Customizing the margin name
pivot_custom_margins = df.pivot_table(
    values='Quantity',
    index='Region',
    columns='ProductType',
    aggfunc='sum',
    margins=True,
    margins_name='Grand Total' # Custom name for the total row/column
)
print("\nTotal Quantity by Region and ProductType with 'Grand Total' margins:\n", pivot_custom_margins)


print("\n--- 8. Using Custom Aggregation Functions ---")

# 8.1 Define a custom function to use as `aggfunc`
def sales_range(series):
    """Calculates the range (max - min) of a Series."""
    if series.empty or series.isnull().all():
        return np.nan
    return series.max() - series.min()

pivot_custom_agg = df.pivot_table(
    values='Amount',
    index='Region',
    columns='Salesperson',
    aggfunc=sales_range # Use the custom function
)
print("\nSales Amount Range by Region and Salesperson (custom aggfunc):\n", pivot_custom_agg)

# 8.2 Using a lambda function for a quick custom aggregation
pivot_lambda_agg = df.pivot_table(
    values='Quantity',
    index='ProductType',
    aggfunc=lambda x: x.sum() / x.nunique(), # Example: Sum of quantity per unique customer rating
    columns='CustomerRating'
)
print("\nQuantity Sum / Unique Customer Rating by ProductType (lambda aggfunc):\n", pivot_lambda_agg)


print("\n--- 9. Time-Based Pivoting with pd.Grouper ---")

# 9.1 Grouping by month from 'Date' column
# Requires 'Date' to be in the index or use pd.Grouper on a column.
pivot_monthly_sales = df.pivot_table(
    values='Amount',
    index=pd.Grouper(key='Date', freq='MS'), # Group by month start (MS)
    columns='ProductType',
    aggfunc='sum',
    fill_value=0
)
print("\nMonthly Total Sales by ProductType:\n", pivot_monthly_sales)

# 9.2 Daily average customer rating
pivot_daily_avg_rating = df.pivot_table(
    values='CustomerRating',
    index=pd.Grouper(key='Date', freq='D'), # Group by each day
    columns='Region',
    aggfunc='mean',
    fill_value=np.nan # Keep NaN for days with no data
)
print("\nDaily Average Customer Rating by Region:\n", pivot_daily_avg_rating)


print("\n--- 10. Flattening MultiIndex Columns after pivot_table ---")
# When you use multiple columns in `aggfunc` or multiple `columns` or multiple `values`,
# pivot_table often returns a DataFrame with MultiIndex columns. You might want to flatten them.

# Example from 5.1
pivot_multi_values_flattened = df.pivot_table(
    values=['Amount', 'Quantity'],
    index='Region',
    columns='ProductType',
    aggfunc='sum'
)
print("\nMultiIndex Columns before flattening:\n", pivot_multi_values_flattened.head())

# Flattening Option 1: Join column levels with an underscore
pivot_multi_values_flattened.columns = [
    '_'.join(col).strip() for col in pivot_multi_values_flattened.columns.values
]
print("\nMultiIndex Columns after flattening (Option 1: joining names):\n", pivot_multi_values_flattened.head())

# Example from 4.1
pivot_multi_aggfunc_reset = df.pivot_table(
    values='Amount',
    index='Region',
    columns='ProductType',
    aggfunc=['sum', 'mean'] # Use only two for clearer flatten
)
print("\nMultiIndex Columns (aggfunc and columns) before flattening:\n", pivot_multi_aggfunc_reset.head())

# Flattening Option 2: Using list comprehension or `map` with f-strings
pivot_multi_aggfunc_reset.columns = [
    f"{agg_func}_{product_type}" for agg_func, product_type in pivot_multi_aggfunc_reset.columns
]
print("\nMultiIndex Columns after flattening (Option 2: f-string joining):\n", pivot_multi_aggfunc_reset.head())


print("\n--- End of Pandas pivot_table() Practice Code ---")