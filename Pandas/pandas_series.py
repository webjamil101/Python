import pandas as pd
import numpy as np

print("--- Pandas Series Practice Code ---")
print("\n--- 1. Series Creation ---")

# 1.1 Create a Series from a list
data_list = [10, 20, 30, 40, 50, 60]
s_from_list = pd.Series(data_list)
print("\nSeries from list:\n", s_from_list)

# 1.2 Create a Series with a custom index
data_fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
index_ids = ['f1', 'f2', 'f3', 'f4', 'f5']
s_fruits = pd.Series(data_fruits, index=index_ids)
print("\nSeries with custom index (fruits):\n", s_fruits)

# 1.3 Create a Series from a NumPy array
np_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
s_from_numpy = pd.Series(np_array)
print("\nSeries from NumPy array:\n", s_from_numpy)

# 1.4 Create a Series from a dictionary (keys become index)
data_dict = {'Math': 95, 'Science': 88, 'English': 72, 'History': 91}
s_scores = pd.Series(data_dict, name='Student Scores') # 'name' attribute
print("\nSeries from dictionary (student scores):\n", s_scores)
print(f"Series name: {s_scores.name}")

# 1.5 Create an empty Series
empty_series = pd.Series(dtype=float)
print("\nEmpty Series:\n", empty_series)

# 1.6 Create a Series with a scalar value (index must be provided)
s_scalar = pd.Series(5, index=['a', 'b', 'c'])
print("\nSeries from scalar:\n", s_scalar)

print("\n--- 2. Accessing Series Elements & Slicing ---")

# Using positional index
print("\nFirst element of s_from_list:", s_from_list[0])
print("Last element of s_from_list:", s_from_list[len(s_from_list) - 1]) # Or s_from_list.iloc[-1]

# Using label index
print("\nScore for 'Math' in s_scores:", s_scores['Math'])
print("Fruit with id 'f3' in s_fruits:", s_fruits['f3'])

# Accessing multiple elements by position
print("\nElements at positions 1, 3, 5 from s_from_list:\n", s_from_list[[1, 3, 5]])

# Accessing multiple elements by label
print("\nScores for 'Science' and 'History':\n", s_scores[['Science', 'History']])

# Slicing by position
print("\nSlice (first 3 elements) of s_from_list:\n", s_from_list[:3])
print("Slice (elements from index 2 to 4) of s_from_list:\n", s_from_list[2:5]) # Exclusive of 5

# Slicing by label (inclusive of end label)
print("\nSlice from 'banana' to 'date' (inclusive) of s_fruits:\n", s_fruits['f2':'f4'])


print("\n--- 3. Series Attributes & Methods ---")

# Attributes
print("\nData type of s_from_list:", s_from_list.dtype)
print("Index of s_fruits:", s_fruits.index)
print("Values of s_scores (NumPy array):", s_scores.values)
print("Shape of s_from_numpy:", s_from_numpy.shape)
print("Number of dimensions of s_scores:", s_scores.ndim)
print("Size of s_from_list:", s_from_list.size)
print("Is s_from_list empty?", s_from_list.empty)

# Basic methods
print("\nSum of s_from_list:", s_from_list.sum())
print("Mean of s_from_numpy:", s_from_numpy.mean())
print("Maximum value in s_scores:", s_scores.max())
print("Minimum value in s_scores:", s_scores.min())
print("Standard deviation of s_from_list:", s_from_list.std())
print("Count of non-null values in s_from_list:", s_from_list.count())


print("\n--- 4. Conditional Selection & Filtering ---")

# Select elements greater than a value
print("\nElements in s_from_list > 30:\n", s_from_list[s_from_list > 30])

# Select elements based on a condition applied to index
print("\nFruits with 'e' in their name:\n", s_fruits[s_fruits.str.contains('e')])

# Select elements where score is even
print("\nScores that are even:\n", s_scores[s_scores % 2 == 0])

# Using multiple conditions
print("\nScores > 80 AND < 95:\n", s_scores[(s_scores > 80) & (s_scores < 95)])


print("\n--- 5. Handling Missing Data ---")

# Create a Series with missing values
s_with_nan = pd.Series([10, 20, np.nan, 40, 50, np.nan, 70])
print("\nSeries with NaNs:\n", s_with_nan)

# Check for null values
print("\nIs null (boolean Series):\n", s_with_nan.isnull())

# Check for non-null values
print("\nIs not null (boolean Series):\n", s_with_nan.notnull())

# Drop null values
s_dropped_nan = s_with_nan.dropna()
print("\nSeries after dropping NaNs:\n", s_dropped_nan)

# Fill null values with a specific value
s_filled_zero = s_with_nan.fillna(0)
print("\nSeries after filling NaNs with 0:\n", s_filled_zero)

# Fill null values with the mean of the Series
s_filled_mean = s_with_nan.fillna(s_with_nan.mean())
print("\nSeries after filling NaNs with mean:\n", s_filled_mean)

# Forward fill (ffill)
s_ffill = s_with_nan.fillna(method='ffill')
print("\nSeries after forward fill:\n", s_ffill)

# Backward fill (bfill)
s_bfill = s_with_nan.fillna(method='bfill')
print("\nSeries after backward fill:\n", s_bfill)


print("\n--- 6. Applying Functions & Mapping ---")

# Apply a simple lambda function
s_squared = s_from_list.apply(lambda x: x**2)
print("\nSeries with elements squared:\n", s_squared)

# Apply a more complex function
def classify_score(score):
    if score >= 90:
        return 'Excellent'
    elif score >= 70:
        return 'Good'
    else:
        return 'Needs Improvement'

s_score_classification = s_scores.apply(classify_score)
print("\nScores classified:\n", s_score_classification)

# Using .map() for element-wise mapping with a dictionary
country_map = {
    'apple': 'USA',
    'banana': 'Ecuador',
    'cherry': 'Turkey',
    'date': 'Egypt'
}
s_fruit_origin = s_fruits.map(country_map)
print("\nFruit origins using .map() with dict:\n", s_fruit_origin)

# Using .map() with a function (similar to .apply() for Series)
s_fruit_upper = s_fruits.map(lambda x: x.upper())
print("\nFruit names in uppercase using .map() with lambda:\n", s_fruit_upper)


print("\n--- 7. Reindexing and Aligning Series ---")

s_a = pd.Series([1, 2, 3], index=['x', 'y', 'z'])
s_b = pd.Series([4, 5, 6], index=['y', 'z', 'w'])

print("\nSeries A:\n", s_a)
print("\nSeries B:\n", s_b)

# Addition aligns by index, fills NaN where no match
s_add = s_a + s_b
print("\nSeries A + Series B (aligned by index):\n", s_add)

# Reindexing to a new index (fills NaN for missing labels)
new_index = ['x', 'y', 'z', 'k']
s_reindexed = s_a.reindex(new_index)
print("\nSeries A reindexed to ['x', 'y', 'z', 'k']:\n", s_reindexed)

# Reindexing with a fill value
s_reindexed_fill = s_a.reindex(new_index, fill_value=0)
print("\nSeries A reindexed with fill_value=0:\n", s_reindexed_fill)


print("\n--- 8. Sorting Series ---")

# Sort by values
s_unsorted_values = pd.Series([30, 10, 50, 20, 40])
print("\nUnsorted Series by values:\n", s_unsorted_values)
s_sorted_values = s_unsorted_values.sort_values()
print("Series sorted by values (ascending):\n", s_sorted_values)
s_sorted_values_desc = s_unsorted_values.sort_values(ascending=False)
print("Series sorted by values (descending):\n", s_sorted_values_desc)

# Sort by index
s_unsorted_index = pd.Series([1, 2, 3], index=['c', 'a', 'b'])
print("\nUnsorted Series by index:\n", s_unsorted_index)
s_sorted_index = s_unsorted_index.sort_index()
print("Series sorted by index:\n", s_sorted_index)


print("\n--- End of Pandas Series Practice ---")