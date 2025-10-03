# --- Python Tuples: All About "Tuple Comprehensions" (and why they're not) ---

# This topic often leads to confusion because Python has list comprehensions,
# set comprehensions, and dictionary comprehensions, but *not* a direct
# "tuple comprehension" syntax.

# --- 1. The "Tuple Comprehension" Misconception ---
import random
print("--- 1. The 'Tuple Comprehension' Misconception ---")

# If you try to create a tuple using parentheses `()` like you would for a list
# comprehension with square brackets `[]`, you actually create a **generator expression**.

# Example of what looks like a tuple comprehension:
generator_expression = (num * 2 for num in range(5))

print(f"1.1 Result of (num * 2 for num in range(5)): {generator_expression}")
print(f"    Type of the result: {type(generator_expression)}")
# Output: <generator object <genexpr> at 0x...>
# This is NOT a tuple. It's a generator object.


# --- 2. What a Generator Expression Is ---

print("\n--- 2. What a Generator Expression Is ---")

# A generator expression is a lightweight way to create iterators.
# It evaluates its elements *lazily* (on demand), meaning it generates values
# one by one as they are requested, rather than creating all values in memory
# at once. This makes them very memory efficient for large sequences.

# 2.1 Iterating over a generator expression
print(f"2.1 Iterating over the generator expression:")
for val in generator_expression:
    print(val, end=" ")
print()

# Note: A generator expression can only be iterated over once.
# If you try to iterate again, it will be exhausted.
print(f"    Attempting to iterate again (will produce nothing):")
for val in generator_expression:
    print(val, end=" ")
print("(No output here as generator is exhausted)")


# --- 3. How to Create a Tuple using a Generator Expression ---

print("\n--- 3. Creating a Tuple from a Generator Expression ---")

# To get a tuple from a comprehension-like syntax, you must explicitly pass
# the generator expression to the `tuple()` constructor.

# 3.1 Creating a tuple from a generator expression
my_tuple = tuple(num * 2 for num in range(5))
print(f"3.1 Tuple created from generator expression: {my_tuple}")
print(f"    Type of the result: {type(my_tuple)}")
# Output: (0, 2, 4, 6, 8)

# Example 3.2: Tuple of strings with a condition
words = ["apple", "banana", "cherry", "date", "fig"]
tuple_of_long_words = tuple(word.upper() for word in words if len(word) > 4)
print(f"3.2 Tuple of long words (uppercase): {tuple_of_long_words}")
# Output: ('APPLE', 'BANANA', 'CHERRY')

# Example 3.3: Tuple of tuples (nested structure)
nested_data = tuple((i, i**2) for i in range(3))
print(f"3.3 Tuple of tuples: {nested_data}")
# Output: ((0, 0), (1, 1), (2, 4))


# --- 4. Benefits of Using Generator Expressions for Tuple Creation ---

print("\n--- 4. Benefits of Generator Expressions for Tuples ---")

# The primary benefit is memory efficiency, especially for large datasets.

# 4.1 Memory Efficiency (Lazy Evaluation)
# When you create a list using a list comprehension, all elements are generated
# and stored in memory immediately.
import sys

large_list = [i for i in range(1_000_000)] # 1 million elements
print(f"4.1 Size of large list: {sys.getsizeof(large_list)} bytes")

# When you create a generator expression, it doesn't store all elements.
large_generator = (i for i in range(1_000_000))
print(f"    Size of large generator expression: {sys.getsizeof(large_generator)} bytes")
# Notice the generator's size is much smaller, as it only stores the logic to generate.

# If you then convert the large generator to a tuple, it will consume memory
# for all elements, but the intermediate step of the generator is efficient.
large_tuple = tuple(large_generator)
print(f"    Size of large tuple (after conversion): {sys.getsizeof(large_tuple)} bytes")
# The tuple itself will be large, but the generator was memory-efficient *before* conversion.


# --- 5. Comparison: List Comprehension vs. Generator Expression (for Tuples) ---

print("\n--- 5. Comparison: List Comp vs. Gen Expr (for Tuples) ---")

# 5.1 List Comprehension (uses `[]`)
# - Creates a list immediately.
# - Stores all elements in memory.
# - Good when you need the entire list for further operations or random access.
list_result = [num * 2 for num in range(5)]
print(f"5.1 List Comprehension: {list_result}, Type: {type(list_result)}")

# 5.2 Generator Expression (uses `()` and then `tuple()`)
# - Creates a generator object.
# - Generates elements one by one (lazy).
# - Good when you need to iterate once or process a very large sequence without
#   storing it all in memory, then convert to tuple if needed.
tuple_result = tuple(num * 2 for num in range(5))
print(f"5.2 Generator Expression to Tuple: {tuple_result}, Type: {type(tuple_result)}")


# --- 6. Practical Scenarios for Using Generator Expressions with `tuple()` ---

print("\n--- 6. Practical Scenarios ---")

# 6.1 Creating immutable records from a large data stream
# Imagine processing millions of sensor readings and wanting to store them
# as tuples for immutability, but not wanting to build a huge list first.
def get_sensor_readings(count):
    for i in range(count):
        yield (f"Sensor_{i}", random.uniform(20.0, 30.0))

# Instead of `list(get_sensor_readings(1_000_000))`, which would build a huge list,
# you can process parts or convert directly to tuple if memory is a concern.
# For example, if you only need the first 100 readings as a tuple:
first_100_readings_tuple = tuple(next(get_sensor_readings(1_000_000)) for _ in range(100))
print(f"6.1 First 100 sensor readings as tuple: {first_100_readings_tuple[:5]}...") # Print first 5

# 6.2 When a function or API specifically requires a tuple as input
# You can generate the data efficiently and then convert it.
def process_coordinates(coords_tuple):
    print(f"    Processing coordinates: {coords_tuple}")
    # ... do something with the tuple ...

# Generate coordinates efficiently and convert to tuple
generated_coords = tuple((i, i*i) for i in range(5))
process_coordinates(generated_coords)