import pandas as pd
import numpy as np

print("--- Pandas Statistical Analysis Code ---")

# --- 1. Setup: Create Sample DataFrames ---
print("\n--- 1. Sample Data Setup ---")

# Create a DataFrame with numerical and categorical data
data = {
    'Student_ID': np.arange(101, 111),
    'Age': [20, 21, 20, 22, 21, 23, 20, 22, 21, 20],
    'Score_Math': [85, 90, 78, 92, 88, 75, 95, 80, 89, 87],
    'Score_Science': [70, 85, 90, 75, 80, 92, 88, 78, 95, 82],
    'Grade': ['A', 'A', 'B', 'A', 'A', 'C', 'A', 'B', 'A', 'B'],
    'City': ['NY', 'LA', 'NY', 'SF', 'LA', 'NY', 'SF', 'NY', 'LA', 'SF'],
    'Attendance_Days': [25, 28, 24, 29, 27, np.nan, 26, 28, 25, 29] # With missing value
}
df = pd.DataFrame(data)
print("Sample DataFrame (df):\n", df)

# Create a second DataFrame for correlation/covariance examples
data_econ = {
    'Year': np.arange(2010, 2020),
    'GDP': np.random.normal(100, 10, 10).cumsum() + 1000, # Simulating increasing GDP
    'Inflation': np.random.normal(3, 1, 10),
    'Unemployment_Rate': np.random.normal(6, 0.5, 10)
}
df_econ = pd.DataFrame(data_econ)
print("\nSample Economic DataFrame (df_econ):\n", df_econ)


# --- 2. Descriptive Statistics for entire DataFrame ---
print("\n--- 2. Descriptive Statistics (DataFrame) ---")

# Generates descriptive statistics for numerical columns
print("\nDataFrame.describe():\n", df.describe())

# Includes all data types (numerical and object/categorical)
print("\nDataFrame.describe(include='all'):\n", df.describe(include='all'))


# --- 3. Descriptive Statistics for Series (Columns) ---
print("\n--- 3. Descriptive Statistics (Series/Columns) ---")

# Mean
print("\nMean of 'Age':", df['Age'].mean())
print("Mean of 'Score_Math':", df['Score_Math'].mean())

# Median
print("\nMedian of 'Age':", df['Age'].median())

# Mode (can return multiple modes)
print("\nMode of 'Age':\n", df['Age'].mode())
print("Mode of 'City':\n", df['City'].mode())

# Standard Deviation
print("\nStandard Deviation of 'Score_Science':", df['Score_Science'].std())

# Variance
print("\nVariance of 'Score_Math':", df['Score_Math'].var())

# Minimum and Maximum
print("\nMin 'Score_Math':", df['Score_Math'].min())
print("Max 'Score_Math':", df['Score_Math'].max())

# Count of non-null values
print("\nCount of 'Attendance_Days' (non-null):", df['Attendance_Days'].count())
print("Count of 'Age' (non-null):", df['Age'].count())

# Sum
print("\nSum of 'Score_Math':", df['Score_Math'].sum())

# Quantiles (0.25 for Q1, 0.50 for Q2/Median, 0.75 for Q3)
print("\n25th percentile (Q1) of 'Score_Math':", df['Score_Math'].quantile(0.25))
print("75th percentile (Q3) of 'Score_Math':", df['Score_Math'].quantile(0.75))
print("All quartiles of 'Score_Science':\n", df['Score_Science'].quantile([0.25, 0.5, 0.75]))

# Value Counts (for categorical or discrete data)
print("\nValue counts for 'Grade':\n", df['Grade'].value_counts())
print("\nNormalized value counts for 'City':\n", df['City'].value_counts(normalize=True)) # as proportions


# --- 4. Correlation and Covariance ---
print("\n--- 4. Correlation and Covariance ---")

# Correlation matrix for numerical columns in df_econ
# Pearson correlation is default
print("\nCorrelation Matrix (df_econ.corr()):\n", df_econ.corr(numeric_only=True))

# Covariance matrix for numerical columns in df_econ
print("\nCovariance Matrix (df_econ.cov()):\n", df_econ.cov(numeric_only=True))

# Correlation between two specific Series (e.g., Score_Math and Score_Science)
print("\nCorrelation between 'Score_Math' and 'Score_Science':",
      df['Score_Math'].corr(df['Score_Science']))

# Covariance between two specific Series
print("Covariance between 'Score_Math' and 'Score_Science':",
      df['Score_Math'].cov(df['Score_Science']))


# --- 5. Aggregations with GroupBy ---
print("\n--- 5. Aggregations with GroupBy ---")

# Group by 'Major' and calculate mean GPA for each major
avg_gpa_by_major = df.groupby('Major')['GPA'].mean()
print("\nAverage GPA by Major:\n", avg_gpa_by_major)

# Group by 'City' and get max score for both Math and Science
max_scores_by_city = df.groupby('City')[['Score_Math', 'Score_Science']].max()
print("\nMax Scores by City:\n", max_scores_by_city)

# Group by 'Grade' and get multiple statistics
grade_stats = df.groupby('Grade').agg(
    Avg_Math_Score=('Score_Math', 'mean'),
    Min_Science_Score=('Score_Science', 'min'),
    Num_Students=('Student_ID', 'count')
)
print("\nStatistics by Grade:\n", grade_stats)

# Group by multiple columns and apply custom aggregation
# Using .apply() with a lambda to calculate score range
score_range_by_major_city = df.groupby(['Major', 'City'])[['Score_Math', 'Score_Science']].apply(
    lambda x: x.max() - x.min()
)
print("\nScore Range by Major and City:\n", score_range_by_major_city)


# --- 6. Rolling and Expanding Statistics (Time Series/Ordered Data) ---
print("\n--- 6. Rolling and Expanding Statistics ---")

# Ensure 'Year' is sorted for rolling/expanding
df_econ_sorted = df_econ.sort_values('Year').set_index('Year')
print("\nEconomic Data (indexed by Year):\n", df_econ_sorted)

# Rolling mean (e.g., 3-year rolling mean of GDP)
# min_periods=1 allows calculation even if fewer than 3 periods are available at the start
df_econ_sorted['Rolling_Mean_GDP'] = df_econ_sorted['GDP'].rolling(window=3, min_periods=1).mean()
print("\nGDP with 3-year Rolling Mean:\n", df_econ_sorted[['GDP', 'Rolling_Mean_GDP']])

# Expanding sum (cumulative sum from start)
df_econ_sorted['Expanding_Sum_Inflation'] = df_econ_sorted['Inflation'].expanding(min_periods=1).sum()
print("\nInflation with Expanding Sum:\n", df_econ_sorted[['Inflation', 'Expanding_Sum_Inflation']])


# --- 7. Sampling Data ---
print("\n--- 7. Sampling Data ---")

# Random sample of 3 rows
sample_3_rows = df.sample(n=3)
print("\nRandom Sample of 3 rows:\n", sample_3_rows)

# Random sample of 50% of rows
sample_50_percent = df.sample(frac=0.5)
print("\nRandom Sample of 50% of rows:\n", sample_50_percent)

# Sample with replacement
sample_with_replacement = df.sample(n=5, replace=True)
print("\nSample with replacement (5 rows, duplicates possible):\n", sample_with_replacement)


# --- 8. Unique Values and Frequencies ---
print("\n--- 8. Unique Values and Frequencies ---")

# Number of unique values
print("\nNumber of unique 'Major' values:", df['Major'].nunique())

# List of unique values
print("Unique 'City' values:", df['City'].unique())

# Frequency counts of unique values (as seen in Section 3)
# print("\nValue counts for 'City':\n", df['City'].value_counts()) # Already demonstrated


# --- 9. Skewness and Kurtosis ---
print("\n--- 9. Skewness and Kurtosis ---")

# Skewness (measure of asymmetry of the probability distribution)
print("\nSkewness of 'Score_Math':", df['Score_Math'].skew())

# Kurtosis (measure of 'tailedness' of the probability distribution)
print("Kurtosis of 'Score_Science':", df['Score_Science'].kurt())


print("\n--- End of Pandas Statistical Analysis Code ---")