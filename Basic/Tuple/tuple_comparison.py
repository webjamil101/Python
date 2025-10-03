print("--- Tuple Comparison in Python ---")
print("----------------------------------\n")

# 1. Equality Comparison (== and !=)
print("1. Equality Comparison (== and !=):")
# Tuples are equal if they have the same elements in the same order.
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (3, 2, 1)
tuple4 = (1, 2, 3, 4)
tuple5 = (1, '2', 3) # Different type

print(f"tuple1: {tuple1}")
print(f"tuple2: {tuple2}")
print(f"tuple3: {tuple3}")
print(f"tuple4: {tuple4}")
print(f"tuple5: {tuple5}")

print(f"tuple1 == tuple2: {tuple1 == tuple2}") # True
print(f"tuple1 == tuple3: {tuple1 == tuple3}") # False (order matters)
print(f"tuple1 == tuple4: {tuple1 == tuple4}") # False (different length)
print(f"tuple1 == tuple5: {tuple1 == tuple5}") # False (different element type)
print(f"tuple1 != tuple3: {tuple1 != tuple3}") # True
print(f"tuple1 != tuple1: {tuple1 != tuple1}\n") # False


# 2. Lexicographical Comparison (>, <, >=, <=)
print("2. Lexicographical Comparison (Element-by-Element):")
# Tuples are compared element by element.
# The comparison stops at the first differing element.
# If one tuple is a prefix of another, the longer one is considered greater.

t1 = (1, 2, 3)
t2 = (1, 2, 4)
t3 = (1, 2)
t4 = (1, 3, 0)
t5 = (2, 0, 0)
t6 = (1, 2, 3, 4)

print(f"t1: {t1}, t2: {t2}, t3: {t3}, t4: {t4}, t5: {t5}, t6: {t6}\n")

# Comparing t1 and t2:
# (1, 2, 3) vs (1, 2, 4)
# 1 == 1 (continue)
# 2 == 2 (continue)
# 3 < 4 (t1 is less than t2)
print(f"t1 < t2: {t1 < t2}")   # True
print(f"t1 > t2: {t1 > t2}\n")  # False

# Comparing t1 and t3 (prefix):
# (1, 2, 3) vs (1, 2)
# 1 == 1 (continue)
# 2 == 2 (continue)
# t3 runs out of elements, so t1 (the longer one) is greater
print(f"t1 > t3: {t1 > t3}")   # True
print(f"t1 < t3: {t1 < t3}\n")  # False

# Comparing t1 and t4:
# (1, 2, 3) vs (1, 3, 0)
# 1 == 1 (continue)
# 2 < 3 (t1 is less than t4)
print(f"t1 < t4: {t1 < t4}")   # True
print(f"t1 > t4: {t1 > t4}\n")  # False

# Comparing t1 and t5:
# (1, 2, 3) vs (2, 0, 0)
# 1 < 2 (t1 is less than t5)
print(f"t1 < t5: {t1 < t5}\n") # True

# Comparing t1 and t6:
# (1, 2, 3) vs (1, 2, 3, 4)
# All elements match up to t1's length. t6 is longer.
print(f"t1 < t6: {t1 < t6}")   # True (t1 is a prefix of t6)
print(f"t1 <= t6: {t1 <= t6}") # True
print(f"t1 == t6: {t1 == t6}\n") # False

# 3. Mixed Data Types in Tuples during Comparison
print("3. Mixed Data Types in Tuples during Comparison:")
# Elements are compared using their standard comparison rules.
# If types are incomparable, a TypeError will be raised.
tuple_mixed_1 = (1, 'apple', 3)
tuple_mixed_2 = (1, 'banana', 2)
tuple_mixed_3 = (1, 2, 'zebra') # Incomparable int and str at second element

print(f"tuple_mixed_1: {tuple_mixed_1}")
print(f"tuple_mixed_2: {tuple_mixed_2}")
print(f"tuple_mixed_3: {tuple_mixed_3}\n")

# (1, 'apple', 3) vs (1, 'banana', 2)
# 1 == 1
# 'apple' < 'banana' (lexicographical string comparison)
print(f"tuple_mixed_1 < tuple_mixed_2: {tuple_mixed_1 < tuple_mixed_2}\n") # True

# (1, 'apple', 3) vs (1, 2, 'zebra')
# 1 == 1
# 'apple' and 2 are incomparable types
try:
    print(f"tuple_mixed_1 < tuple_mixed_3: {tuple_mixed_1 < tuple_mixed_3}")
except TypeError as e:
    print(f"Caught TypeError: {e}")
    print("Cannot compare 'str' and 'int' directly within tuple comparison.\n")


# 4. Empty Tuples
print("4. Empty Tuples:")
empty_tuple = ()
print(f"() == (): {empty_tuple == ()}")    # True
print(f"() < (1,): {empty_tuple < (1,)}") # True (empty tuple is less than any non-empty tuple)
print(f"(1,) > (): {(1,) > empty_tuple}\n") # True


# 5. Nested Tuples
print("5. Nested Tuples:")
nested_t1 = (1, (2, 3), 4)
nested_t2 = (1, (2, 4), 4)
nested_t3 = (1, (2, 3), 5)

print(f"nested_t1: {nested_t1}")
print(f"nested_t2: {nested_t2}")
print(f"nested_t3: {nested_t3}\n")

# (1, (2, 3), 4) vs (1, (2, 4), 4)
# 1 == 1
# (2, 3) < (2, 4) (inner tuple comparison: 3 < 4)
print(f"nested_t1 < nested_t2: {nested_t1 < nested_t2}\n") # True

# (1, (2, 3), 4) vs (1, (2, 3), 5)
# 1 == 1
# (2, 3) == (2, 3)
# 4 < 5
print(f"nested_t1 < nested_t3: {nested_t1 < nested_t3}\n") # True


print("--- End of Tuple Comparison Demonstration ---")



import operator
from collections import namedtuple

print("--- Advanced Use Cases of Tuple Comparison in Python ---\n")

# 1. Multi-level Sorting (Lexicographical Sorting by Default)
print("1. Multi-level Sorting (Lexicographical Sorting by Default):")
# This is arguably the most common and powerful advanced use case.
# When you sort a list of tuples, Python automatically uses lexicographical
# comparison. This means it sorts by the first element, then by the second
# for ties, and so on.

students = [
    ('Alice', 25, 'Math', 90),
    ('Bob', 30, 'Physics', 85),
    ('Alice', 22, 'Chemistry', 95), # Different age, same name as first Alice
    ('Charlie', 22, 'Biology', 88),
    ('Bob', 30, 'Chemistry', 92)  # Same name and age as first Bob, different subject
]

print("Original student data:")
for student in students:
    print(student)

# Sort by name (primary), then by age (secondary), then by score (tertiary, descending)
# For descending sort on a numeric field, you can negate the value.
sorted_students = sorted(students, key=lambda s: (s[0], s[1], -s[3]))
print("\nSorted by name (ASC), then age (ASC), then score (DESC):")
for student in sorted_students:
    print(student)

# Using operator.itemgetter for performance and readability (often preferred over lambda for simple key extraction)
from operator import itemgetter
# Sort by subject (ASC), then by score (DESC), then by name (ASC)
sorted_students_2 = sorted(students, key=itemgetter(2, 3, 0), reverse=False) # reverse only applies to the first key if not using negation
print("\nSorted by subject (ASC), then score (ASC), then name (ASC):")
for student in sorted_students_2:
    print(student)

# To achieve descending on score with itemgetter, you might need a more complex key or a two-pass sort
# A common idiom for stable sort (sort by primary, then sort by secondary in place)
# Note: list.sort() is stable, so subsequent sorts preserve relative order of equal keys.
students_for_complex_sort = list(students) # Create a copy to avoid modifying original
students_for_complex_sort.sort(key=itemgetter(3), reverse=True) # Sort by score (DESC)
students_for_complex_sort.sort(key=itemgetter(0)) # Then by name (ASC) - stable sort preserves score order for same names
print("\nComplex Sort: By Name (ASC), then Score (DESC) (using two-pass stable sort):")
for student in students_for_complex_sort:
    print(student)
print("-" * 30)


# 2. Custom Comparison Functions (Less Common with sorted/sort, but tuple comparison is fundamental)
print("2. Custom Comparison Functions (Leveraging tuple comparison for custom logic):")

class Version:
    def __init__(self, version_string):
        self.parts = tuple(map(int, version_string.split('.')))

    def __lt__(self, other):
        # Define how one Version object is less than another
        # This implicitly uses tuple comparison for self.parts and other.parts
        return self.parts < other.parts

    def __eq__(self, other):
        return self.parts == other.parts

    def __le__(self, other):
        return self.parts <= other.parts

    # Define other comparison operators if needed for full rich comparison
    def __gt__(self, other):
        return self.parts > other.parts

    def __ge__(self, other):
        return self.parts >= other.parts

    def __ne__(self, other):
        return self.parts != other.parts

    def __repr__(self):
        return f"Version('{'.'.join(map(str, self.parts))}')"

versions = [
    Version("1.0.5"),
    Version("1.2.0"),
    Version("1.0.10"),
    Version("2.0.0"),
    Version("1.1.0"),
    Version("1.0.5")
]

print("Original versions:")
for v in versions:
    print(v)

sorted_versions = sorted(versions) # Uses the __lt__ method we defined
print("\nSorted versions (using custom __lt__ based on tuple comparison):")
for v in sorted_versions:
    print(v)

v1 = Version("1.5.0")
v2 = Version("1.10.0")
v3 = Version("1.5.0")
print(f"\n{v1} < {v2}: {v1 < v2}") # True because (1, 5, 0) < (1, 10, 0)
print(f"{v1} == {v3}: {v1 == v3}") # True
print("-" * 30)


# 3. Using Tuples as Dictionary Keys for Multi-criteria Lookup
print("3. Using Tuples as Dictionary Keys for Multi-criteria Lookup:")
# Tuples are hashable (if all their elements are hashable), making them
# excellent candidates for dictionary keys when you need to look up data
# based on a combination of values.

sales_data = {}
sales_data[('Electronics', 'Laptop', 'Q1')] = 150000
sales_data[('Electronics', 'Mouse', 'Q1')] = 5000
sales_data[('Clothing', 'Shirt', 'Q1')] = 20000
sales_data[('Electronics', 'Laptop', 'Q2')] = 180000

print(f"Sales data for ('Electronics', 'Laptop', 'Q1'): {sales_data.get(('Electronics', 'Laptop', 'Q1'))}")
print(f"Sales data for ('Clothing', 'Shirt', 'Q1'): {sales_data.get(('Clothing', 'Shirt', 'Q1'))}")
print(f"Sales data for ('Electronics', 'Keyboard', 'Q1'): {sales_data.get(('Electronics', 'Keyboard', 'Q1'), 'N/A')}\n")

# This allows for structured keying where the order of elements in the tuple key matters
# (e.g., ('Electronics', 'Laptop', 'Q1') is distinct from ('Laptop', 'Electronics', 'Q1'))
print("-" * 30)


# 4. Range Checking and Filtering with Tuples
print("4. Range Checking and Filtering with Tuples:")
# Tuple comparison can be used to check if a point falls within a range,
# especially useful for multi-dimensional data or versions.

# Define a 2D bounding box
min_point = (10, 20)
max_point = (50, 60)

points = [(15, 25), (5, 30), (45, 55), (70, 10)]

print(f"Points to check: {points}")
print(f"Bounding box: from {min_point} to {max_point}")

points_in_box = []
for p in points:
    # A point (x, y) is in the box if min_x <= x <= max_x AND min_y <= y <= max_y
    # This can be simplified with tuple comparison if the order of dimensions matches
    # (min_x, min_y) <= (x, y) <= (max_x, max_y)
    # This works because the comparison is lexicographical:
    # (min_x <= x) AND (if min_x == x then min_y <= y)
    # AND (x <= max_x) AND (if x == max_x then y <= max_y)
    # This is a good approximation for rectangular bounds.
    if min_point <= p <= max_point: # This is a shorthand for (min_point <= p) and (p <= max_point)
        points_in_box.append(p)

print(f"Points inside the box: {points_in_box}\n")

# More precise check (often necessary for clear boundaries):
points_in_box_precise = []
for x, y in points:
    if min_point[0] <= x <= max_point[0] and min_point[1] <= y <= max_point[1]:
        points_in_box_precise.append((x, y))
print(f"Points inside the box (precise check): {points_in_box_precise}\n")

# The shorthand `min_point <= p <= max_point` works for rectangular bounds IF
# the dimensions are independent and compared in the same order.
# For example, (10, 20) <= (15, 25) evaluates True:
# (10 <= 15) is True, then (20 <= 25) is True.
# And (15, 25) <= (50, 60) evaluates True:
# (15 <= 50) is True, then (25 <= 60) is True.

# However, be careful with non-rectangular or complex ranges.
# Example where direct tuple comparison might mislead:
# Is (5, 50) between (10, 20) and (50, 60)?
p_test = (5, 50)
print(f"Checking if {p_test} is between {min_point} and {max_point} (tuple comparison): {min_point <= p_test <= max_point}")
# This evaluates to False because (10, 20) <= (5, 50) is False (10 is not <= 5)
# This is correct for the lexicographical interpretation.

# Is (10, 5) between (10, 20) and (50, 60)?
p_test_2 = (10, 5)
print(f"Checking if {p_test_2} is between {min_point} and {max_point} (tuple comparison): {min_point <= p_test_2 <= max_point}")
# This evaluates to False because (10, 20) <= (10, 5) is False (20 is not <= 5)
# This highlights that tuple comparison is *lexicographical*, not a simple component-wise "all within range" check.
# For general bounding box checks, the precise `and` logic is usually clearer and safer.
print("-" * 30)

# 5. Prioritization Queues or Custom Ordering
print("5. Prioritization Queues or Custom Ordering:")
# Tuples are often used to define custom sorting keys for items in queues
# or when you need a compound sort order that prioritizes certain attributes.
# Python's `heapq` module, for instance, uses tuple comparison for its priority queue.

# Task: Sort events by priority (High > Medium > Low), then by timestamp (earliest first), then by event name.
# Represent priority as an integer for comparison: High=3, Medium=2, Low=1
priority_map = {'High': 3, 'Medium': 2, 'Low': 1}

events = [
    ('Low', '2025-06-05 10:30:00', 'Backup Data'),
    ('High', '2025-06-05 10:00:00', 'Critical Alert'),
    ('Medium', '2025-06-05 10:15:00', 'Process Report'),
    ('High', '2025-06-05 10:00:05', 'Another Critical Alert'), # Slightly later timestamp
    ('Low', '2025-06-05 10:30:00', 'Cleanup Temp Files') # Same priority and timestamp as first Low
]

# When sorting, higher priority should come first, so negate the priority map value.
# Timestamps should be sorted ascending naturally.
# Event name should be sorted ascending naturally for ties.
sorted_events = sorted(events, key=lambda event: (-priority_map[event[0]], event[1], event[2]))

print("Events sorted by (Priority DESC, Timestamp ASC, Event Name ASC):")
for event in sorted_events:
    print(event)
print("-" * 30)

print("--- End of Advanced Tuple Comparison Demonstration ---")