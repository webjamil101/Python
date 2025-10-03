import pandas as pd
import numpy as np

print("--- Pandas Summary Functions Practice Code ---")

# --- 1. Setup: Create a Comprehensive Sample DataFrame ---
print("\n--- 1. Sample DataFrame Setup ---")

data = {
    'OrderID': np.arange(1001, 1021),
    'CustomerID': np.random.randint(100, 105, 20),
    'ProductCategory': np.random.choice(['Electronics', 'Books', 'Clothing', 'Food'], 20),
    'Product': np.random.choice(['Laptop', 'Keyboard', 'T-Shirt', 'Milk', 'Book A', 'Mouse', 'Pants', 'Cereal', 'Book B'], 20),
    'Quantity': np.random.randint(1, 10, 20),
    'Price_Per_Unit': np.random.uniform(5.0, 1500.0, 20).round(2),
    'OrderDate': pd.to_datetime(pd.date_range(start='2024-01-01', periods=20, freq='D')),
    'Discount_Applied': np.random.choice([0.05, 0.1, 0.0, np.nan], 20, p=[0.25, 0.25, 0.4, 0.1]),
    'CustomerRating': np.random.randint(1, 6, 20), # 1 to 5 stars
    'IsExpressShipping': np.random.choice([True, False], 20),
    'ReturnReason': np.random.choice(['Damaged', 'Wrong Size', 'No Reason', np.nan], 20, p=[0.1, 0.1, 0.3, 0.5])
}
df = pd.DataFrame(data)

# Introduce some more NaNs for demonstration
df.loc[[3, 7, 12], 'Quantity'] = np.nan
df.loc[[1, 8, 11], 'CustomerRating'] = np.nan
df.loc[[5, 14], 'ProductCategory'] = np.nan # Example of NaN in categorical

# Calculate Total Price for later use
df['Total_Price'] = df['Quantity'] * df['Price_Per_Unit'] * (1 - df['Discount_Applied'].fillna(0))

print("Original DataFrame (df):\n", df.head(10))
print("\nDataFrame Info:\n")
df.info()


print("\n--- 2. General DataFrame Summaries ---")

# 2.1 .describe(): Provides descriptive statistics for numerical columns
print("\nDataFrame.describe():\n", df.describe())

# 2.2 .describe(include='all'): Includes descriptive stats for all columns (numerical and categorical)
print("\nDataFrame.describe(include='all'):\n", df.describe(include='all'))

# 2.3 .info(): Concise summary, including Dtypes, non-null values, and memory usage
# Already printed above, but useful to remember it's a "summary" function
# df.info()


print("\n--- 3. Series-Specific Summaries (on individual columns) ---")

# 3.1 .value_counts(): Counts unique values in a Series (good for categorical/discrete)
print("\nValue counts for 'ProductCategory':\n", df['ProductCategory'].value_counts())
print("\nValue counts for 'CustomerRating' (including NaNs):\n", df['CustomerRating'].value_counts(dropna=False))

# 3.2 .unique(): Returns an array of unique values
print("\nUnique 'ProductCategory' values:", df['ProductCategory'].unique())
print("Unique 'CustomerID' values:", df['CustomerID'].unique())

# 3.3 .nunique(): Returns the number of unique values
print("\nNumber of unique 'ProductCategory' values:", df['ProductCategory'].nunique())
print("Number of unique 'Product' values:", df['Product'].nunique())
print("Number of unique 'CustomerID' values (excluding NaNs):", df['CustomerID'].nunique())

# 3.4 .mode(): Returns the most frequent value(s) in a Series
print("\nMode of 'ProductCategory':\n", df['ProductCategory'].mode())
print("Mode of 'Quantity' (might return multiple if tied):\n", df['Quantity'].mode())

# 3.5 .quantile(): Calculates quantiles (percentiles)
print("\nMedian (0.5 quantile) of 'Price_Per_Unit':", df['Price_Per_Unit'].quantile(0.5))
print("25th and 75th percentiles of 'Total_Price':\n", df['Total_Price'].quantile([0.25, 0.75]))


print("\n--- 4. Basic Aggregation Functions ---")
# These can be applied to entire DataFrames (numerical columns) or specific Series

# 4.1 .sum(): Sum of values
print("\nTotal sum of 'Total_Price':", df['Total_Price'].sum())
print("Sum of 'Quantity' per column (NaNs are skipped by default):\n", df[['Quantity', 'CustomerRating']].sum())

# 4.2 .mean(): Mean of values
print("\nAverage 'Price_Per_Unit':", df['Price_Per_Unit'].mean())

# 4.3 .median(): Median of values
print("\nMedian 'CustomerRating':", df['CustomerRating'].median())

# 4.4 .min() / .max(): Minimum and Maximum values
print("\nMinimum 'Total_Price':", df['Total_Price'].min())
print("Maximum 'Total_Price':", df['Total_Price'].max())

# 4.5 .std() / .var(): Standard Deviation and Variance
print("\nStandard Deviation of 'Total_Price':", df['Total_Price'].std())
print("Variance of 'CustomerRating':", df['CustomerRating'].var())

# 4.6 .count(): Count of non-NA/null observations
print("\nNon-null count for 'Quantity':", df['Quantity'].count())
print("Non-null count for 'ReturnReason':", df['ReturnReason'].count())


print("\n--- 5. Correlation and Covariance ---")

# 5.1 .corr(): Pairwise correlation of columns
# Only works on numerical columns by default
print("\nCorrelation matrix (numerical columns):\n", df.corr(numeric_only=True))

# 5.2 .cov(): Pairwise covariance of columns
print("\nCovariance matrix (numerical columns):\n", df.cov(numeric_only=True))

# 5.3 Correlation between two specific series
print("\nCorrelation between 'Quantity' and 'Price_Per_Unit':", df['Quantity'].corr(df['Price_Per_Unit']))


print("\n--- 6. Grouped Summaries (using .groupby() with aggregations) ---")

# 6.1 Total Quantity Sold by ProductCategory
qty_by_category = df.groupby('ProductCategory')['Quantity'].sum()
print("\nTotal Quantity Sold by ProductCategory:\n", qty_by_category)

# 6.2 Average Price_Per_Unit and Total_Price by CustomerID
customer_avg_spend = df.groupby('CustomerID').agg(
    Avg_Price_Per_Unit=('Price_Per_Unit', 'mean'),
    Total_Spend=('Total_Price', 'sum'),
    Num_Orders=('OrderID', 'count')
)
print("\nCustomer Spending Summary:\n", customer_avg_spend)

# 6.3 Customer Rating distribution by Product Category
# Nested aggregation or pivot_table can show this
rating_by_category = df.groupby('ProductCategory')['CustomerRating'].value_counts(normalize=True).unstack(fill_value=0)
print("\nCustomer Rating Distribution by ProductCategory (Normalized):\n", rating_by_category)


print("\n--- 7. Pivot Tables and Crosstab ---")
# Powerful for summarizing data in a spreadsheet-like format

# 7.1 .pivot_table(): Summarize data by one or more keys on the rows, columns, and values
# Average 'Total_Price' for each 'ProductCategory' per 'CustomerID'
pivot_avg_price = df.pivot_table(
    values='Total_Price',
    index='CustomerID',
    columns='ProductCategory',
    aggfunc='mean',
    fill_value=0 # Fill NaN values in the pivot table with 0
)
print("\nPivot Table: Avg Total_Price by CustomerID and ProductCategory:\n", pivot_avg_price)

# Count of unique OrderIDs for each CustomerID and ProductCategory
pivot_count_orders = df.pivot_table(
    values='OrderID',
    index='CustomerID',
    columns='ProductCategory',
    aggfunc='count', # Aggregates non-null values
    fill_value=0
)
print("\nPivot Table: Count of Orders by CustomerID and ProductCategory:\n", pivot_count_orders)


# 7.2 pd.crosstab(): Compute a frequency table of two (or more) factors
# Frequency of ProductCategory by ReturnReason
cross_tab_prod_return = pd.crosstab(df['ProductCategory'], df['ReturnReason'], margins=True, dropna=False)
print("\nCrosstab: ProductCategory vs ReturnReason (with totals and NaNs):\n", cross_tab_prod_return)

# Normalized crosstab (proportions)
cross_tab_normalized = pd.crosstab(df['ProductCategory'], df['IsExpressShipping'], normalize='index') # normalize by row
print("\nCrosstab (Normalized by row): ProductCategory vs IsExpressShipping:\n", cross_tab_normalized)


print("\n--- End of Pandas Summary Functions Code ---")