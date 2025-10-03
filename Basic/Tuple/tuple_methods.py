# --- Python Tuples: All About Methods in Code ---

# Tuples are immutable, which means their elements cannot be changed after creation.
# Due to this immutability, tuples have very few built-in methods compared to lists.
# The methods they do have are for querying information about the tuple's contents,
# not for modifying the tuple itself.

# Let's define a sample tuple for demonstration.
my_tuple = (1, 2, 3, 2, 4, 2, 5)


print("--- 1. `count()` Method ---")

# 1.1 `count(value)`
# - **Purpose:** Returns the number of times a specified `value` appears in the tuple.
# - **Syntax:** `tuple.count(value)`
# - **Parameters:** `value` - The item you want to count its occurrences.
# - **Returns:** An integer representing the count.

print(f"1.1 Original tuple: {my_tuple}")

# Count occurrences of 2
count_of_2 = my_tuple.count(2)
print(f"    Number of times '2' appears: {count_of_2}") # Output: 3

# Count occurrences of 1
count_of_1 = my_tuple.count(1)
print(f"    Number of times '1' appears: {count_of_1}") # Output: 1

# Count occurrences of a value not in the tuple
count_of_99 = my_tuple.count(99)
print(f"    Number of times '99' appears: {count_of_99}") # Output: 0

# Count occurrences of a string in a mixed tuple
mixed_tuple = ("apple", "banana", "apple", "cherry")
count_apple = mixed_tuple.count("apple")
print(f"    Count of 'apple' in {mixed_tuple}: {count_apple}") # Output: 2


print("\n--- 2. `index()` Method ---")

# 2.1 `index(value, start=0, end=len(tuple))`
# - **Purpose:** Returns the index of the *first* occurrence of the specified `value`.
# - **Syntax:** `tuple.index(value, start, end)`
# - **Parameters:**
#     - `value`: The item whose index you want to find.
#     - `start` (optional): The index from where to start searching (inclusive). Default is 0.
#     - `end` (optional): The index where to stop searching (exclusive). Default is the end of the tuple.
# - **Returns:** An integer representing the index.
# - **Raises:** A `ValueError` if the `value` is not found in the specified range.

print(f"2.1 Original tuple: {my_tuple}")

# Find the index of the first occurrence of 1
index_of_1 = my_tuple.index(1)
print(f"    Index of first '1': {index_of_1}") # Output: 0

# Find the index of the first occurrence of 2
index_of_first_2 = my_tuple.index(2)
print(f"    Index of first '2': {index_of_first_2}") # Output: 1

# Find the index of 2, starting the search from index 2
index_of_second_2 = my_tuple.index(2, 2)
print(f"    Index of '2' starting from index 2: {index_of_second_2}") # Output: 3

# Find the index of 2, starting from index 4
index_of_third_2 = my_tuple.index(2, 4)
print(f"    Index of '2' starting from index 4: {index_of_third_2}") # Output: 5

# Attempt to find an element not present in the tuple (raises ValueError)
try:
    print("\n    Attempting to find index of '99'...")
    my_tuple.index(99)
except ValueError as e:
    print(f"    Error: {e} - Value '99' not found in tuple.")

# Attempt to find an element not present in the specified slice (raises ValueError)
try:
    print("\n    Attempting to find index of '1' in slice from index 1 to 3...")
    my_tuple.index(1, 1, 3) # Search for 1 between index 1 (inclusive) and 3 (exclusive)
except ValueError as e:
    print(f"    Error: {e} - Value '1' not found in the specified slice.")


print("\n--- 3. Why So Few Methods? (Immutability) ---")

# The small number of methods for tuples is a direct consequence of their immutability.
# Methods that modify the collection (like `append()`, `remove()`, `insert()`, `sort()`,
# `reverse()`, `pop()`, `extend()`) are not available for tuples because they would
# alter the tuple in place.

# If you need to perform operations that would modify a tuple, you typically:
# 1. Convert the tuple to a list.
# 2. Perform the modifications on the list.
# 3. Convert the list back to a tuple (if a tuple is still desired).

# Example: "Modifying" a tuple by converting to list and back
original_t = (1, 2, 3)
print(f"\n3.1 Original tuple: {original_t}")

# Convert to list
temp_list = list(original_t)
print(f"    Converted to list: {temp_list}")

# Modify the list
temp_list.append(4)
temp_list[0] = 10
print(f"    Modified list: {temp_list}")

# Convert back to tuple
new_t = tuple(temp_list)
print(f"    Converted back to new tuple: {new_t}")
print(f"    Original tuple remains unchanged: {original_t}")
print(f"    ID of original tuple: {id(original_t)}")
print(f"    ID of new tuple: {id(new_t)}") # Note: This is a completely new tuple object.