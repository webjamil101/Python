import pandas as pd
import numpy as np

print("--- Pandas Reshaping Data Practice Code ---")

# --- 1. Setup: Create Sample DataFrames for Reshaping ---
print("\n--- 1. Sample Data Setup ---")

# Data for Melt (Wide to Long)
data_melt = {
    'Region': ['East', 'West', 'North', 'South'],
    'Q1_Sales': [100, 150, 120, 80],
    'Q2_Sales': [110, 160, 130, 90],
    'Q3_Sales': [120, 170, 140, 100],
    'Q4_Sales': [130, 180, 150, 110],
    'Q1_Profit': [10, 15, 12, 8],
    'Q2_Profit': [11, 16, 13, 9]
}
df_melt = pd.DataFrame(data_melt)
print("Original DataFrame for Melt (df_melt):\n", df_melt)

# Data for Pivot / Pivot_Table (Long to Wide)
data_pivot = {
    'Date': pd.to_datetime(['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-01']),
    'City': ['New York', 'London', 'New York', 'London', 'Paris'],
    'Metric': ['Temperature', 'Temperature', 'Temperature', 'Temperature', 'Humidity'],
    'Value': [25, 15, 26, 14, 75]
}
df_pivot = pd.DataFrame(data_pivot)
print("\nOriginal DataFrame for Pivot (df_pivot):\n", df_pivot)

# Data for Stack / Unstack (Hierarchical Columns/Index)
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo'],
          ['one', 'two', 'one', 'two', 'one', 'two']]
multi_cols = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
data_stack_unstack = np.random.randn(4, 6) # 4 rows, 6 columns
df_stack_unstack = pd.DataFrame(data_stack_unstack, index=['A', 'B', 'C', 'D'], columns=multi_cols)
print("\nOriginal DataFrame for Stack/Unstack (df_stack_unstack):\n", df_stack_unstack)

# Data for wide_to_long
data_wide_to_long = {
    'ID': ['A', 'B'],
    'Inc_1999': [1000, 1500],
    'Exp_1999': [500, 700],
    'Inc_2000': [1100, 1600],
    'Exp_2000': [600, 800]
}
df_wide_to_long = pd.DataFrame(data_wide_to_long)
print("\nOriginal DataFrame for wide_to_long (df_wide_to_long):\n", df_wide_to_long)


print("\n--- 2. .melt(): Wide to Long Format (Unpivoting) ---")

# 2.1 Basic melt: Convert 'Q1_Sales' through 'Q4_Sales' into two columns: 'variable' and 'value'
df_melt_basic = df_melt.melt(
    id_vars=['Region'], # Columns to keep as identifier variables
    value_vars=['Q1_Sales', 'Q2_Sales', 'Q3_Sales', 'Q4_Sales'] # Columns to unpivot
)
print("\nBasic Melt (Sales only):\n", df_melt_basic.head())

# 2.2 Melt with custom names for 'variable' and 'value' columns
df_melt_named = df_melt.melt(
    id_vars=['Region'],
    value_vars=['Q1_Sales', 'Q2_Sales', 'Q3_Sales', 'Q4_Sales'],
    var_name='Quarter', # Custom name for the new column holding original column names
    value_name='Sales'  # Custom name for the new column holding original values
)
print("\nMelt with custom names (Sales only):\n", df_melt_named.head())

# 2.3 Melt multiple sets of value variables (e.g., Sales and Profit)
# This will create rows for both Sales and Profit, distinguished by 'variable' column
df_melt_all = df_melt.melt(
    id_vars=['Region'],
    var_name='Metric_Quarter', # This will combine 'Q1_Sales', 'Q2_Profit' etc.
    value_name='Value'
)
print("\nMelt with all value variables (combined):\n", df_melt_all.head())

# 2.4 More specific melt to separate 'Sales' and 'Profit' metrics
# This requires a bit more post-processing on the 'Metric_Quarter' column if original columns have patterns
df_melt_structured = df_melt.melt(
    id_vars=['Region'],
    var_name='Quarter_Type',
    value_name='Amount'
)
# Example of splitting 'Quarter_Type' into 'Quarter' and 'Type'
df_melt_structured[['Type', 'Quarter_Num']] = df_melt_structured['Quarter_Type'].str.split('_', expand=True)
df_melt_structured = df_melt_structured.drop(columns=['Quarter_Type']) # Drop the original combined column
print("\nMelt with post-processing to split columns:\n", df_melt_structured.head())


print("\n--- 3. .pivot(): Long to Wide Format (without aggregation) ---")
# Requires unique index-columns pairs in the original long format

# Prepare df_pivot for basic pivot: Date, City, Metric -> Value
df_pivot_ready = df_pivot[df_pivot['Metric'] == 'Temperature'] # Only pivot temperature for unique combinations
df_pivoted_temp = df_pivot_ready.pivot(index='Date', columns='City', values='Value')
print("\nPivot Table (Temperature only - no aggregation):\n", df_pivoted_temp)


print("\n--- 4. .pivot_table(): Long to Wide with Aggregation ---")
# The most flexible pivoting tool; handles duplicate index-columns pairs by aggregating.

# 4.1 Basic pivot_table: Average 'Value' for each 'Date' and 'City', for different 'Metric'
# If multiple values exist for (Date, City, Metric) combination, it will average them.
df_pivot_agg = df_pivot.pivot_table(
    values='Value',
    index='Date',
    columns='City',
    aggfunc='mean' # default is 'mean', can be sum, count, etc.
)
print("\nPivot Table (Avg Value by Date and City):\n", df_pivot_agg)

# 4.2 Pivot_table with multiple value columns
df_pivot_multi_value = df_pivot.pivot_table(
    values='Value',
    index=['Date', 'City'], # MultiIndex for rows
    columns='Metric',       # Columns based on 'Metric'
    aggfunc='sum',          # Aggregate by sum
    fill_value=0            # Fill NaN cells with 0
)
print("\nPivot Table (Sum Value by Date, City, and Metric):\n", df_pivot_multi_value)

# 4.3 Pivot_table with multiple aggregation functions
df_pivot_multi_aggfunc = df_pivot.pivot_table(
    values='Value',
    index='City',
    columns='Metric',
    aggfunc=['mean', 'max', 'count'] # Perform multiple aggregations
)
print("\nPivot Table (Multiple Aggregations):\n", df_pivot_multi_aggfunc)


print("\n--- 5. .stack() and .unstack(): Manipulating MultiIndex ---")
# These are used for reshaping based on MultiIndex (hierarchical index)

print("\nOriginal DataFrame for Stack/Unstack (df_stack_unstack):\n", df_stack_unstack)

# 5.1 .stack(): Pivots the (innermost by default) column level to the row index
df_stacked = df_stack_unstack.stack()
print("\nStacked DataFrame (default: innermost column level 'second' goes to index):\n", df_stacked)
print("Stacked DataFrame info:\n", df_stacked.info())

# 5.2 .stack(level=0): Stack the top column level ('first')
df_stacked_level0 = df_stack_unstack.stack(level=0)
print("\nStacked DataFrame (level=0 'first' goes to index):\n", df_stacked_level0)

# 5.3 .unstack(): Pivots the (innermost by default) row index level to columns
df_unstacked = df_stacked.unstack()
print("\nUnstacked DataFrame (default: innermost index level 'second' goes to columns):\n", df_unstacked)

# 5.4 .unstack(level=0): Unstack the top row index level ('first')
df_stacked_reset = df_stacked.reset_index(level=1, drop=True) # Prepare for unstacking the 'first' level
df_unstacked_level0 = df_stacked_reset.unstack(level=0)
print("\nUnstacked DataFrame (level=0 'first' goes to columns):\n", df_unstacked_level0)


print("\n--- 6. .transpose() (.T): Swapping Rows and Columns ---")

# Transpose the original df_melt DataFrame
df_transposed = df_melt.set_index('Region').T # Set Region as index first for meaningful columns
print("\nTransposed DataFrame (df_melt.set_index('Region').T):\n", df_transposed)

# Transpose a simple DataFrame
df_simple = pd.DataFrame({'ColA': [1,2], 'ColB': [3,4]})
print("\nOriginal Simple DataFrame:\n", df_simple)
print("Transposed Simple DataFrame:\n", df_simple.T)


print("\n--- 7. pd.wide_to_long(): For Specific Column Naming Patterns ---")
# Useful when column names follow a consistent pattern like 'stub_variable' + 'time_variable'

print("\nOriginal DataFrame for wide_to_long (df_wide_to_long):\n", df_wide_to_long)

# Reshape df_wide_to_long to long format
# stubnames: common prefix of the columns to unpivot (e.g., 'Inc_', 'Exp_')
# i: identifier variable(s) (e.g., 'ID')
# j: name for the new column that captures the suffix (e.g., 'Year')
# sep: separator between stub and variable (e.g., '_')
df_long_format = pd.wide_to_long(
    df_wide_to_long,
    stubnames=['Inc', 'Exp'],
    i='ID',
    j='Year',
    sep='_'
)
print("\nDataFrame reshaped using pd.wide_to_long:\n", df_long_format)

# Reset index to make 'Year' and 'ID' regular columns if needed
print("\nDataFrame reshaped (reset index):\n", df_long_format.reset_index())


print("\n--- End of Pandas Reshaping Data Code ---")