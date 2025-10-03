import numpy as np
import matplotlib.pyplot as plt # For visualizing distributions
import seaborn as sns # For nicer plots

# Configure matplotlib for better display if available
try:
    plt.style.use('seaborn-v0_8-darkgrid')
    sns.set_palette('viridis')
except Exception:
    pass # If seaborn/matplotlib are not available, continue without styling

print("--- NumPy Random Arrays: Practice Code ---")

# --- 1. Introduction to `numpy.random` ---
print("\n--- 1. Introduction to `numpy.random` ---")
print("The `numpy.random` module provides functions for generating pseudo-random numbers.")
print("Pseudo-random means the numbers are generated deterministically from an initial 'seed'.")
print("For most common use cases, these are perfectly fine for simulations and data generation.")

# Setting a seed for reproducibility
# If you run the code multiple times with the same seed, you'll get the same "random" numbers.
np.random.seed(42)
print("\nSet random seed to 42 for reproducibility.")
print(f"First random number after seed(42): {np.random.rand()}")
np.random.seed(42) # Resetting the seed
print(f"First random number after resetting seed(42): {np.random.rand()}")

# --- 2. Basic Random Array Generation ---

# 2.1 `np.random.rand(d0, d1, ..., dn)`: Uniform distribution [0.0, 1.0)
print("\n--- 2.1 `np.random.rand()`: Uniform Distribution (0.0 to 1.0) ---")
# Generates numbers from a uniform distribution over [0, 1).
# Arguments specify the dimensions of the array.

rand_scalar = np.random.rand()
print(f"Single random float (0.0 to 1.0): {rand_scalar}")

rand_1d = np.random.rand(5) # 1D array of 5 random floats
print(f"1D array (5 elements, uniform):\n{rand_1d}")

rand_2d = np.random.rand(2, 3) # 2x3 array of random floats
print(f"2D array (2x3, uniform):\n{rand_2d}")

rand_3d = np.random.rand(2, 2, 2) # 2x2x2 3D array
print(f"3D array (2x2x2, uniform):\n{rand_3d}")

# 2.2 `np.random.randn(d0, d1, ..., dn)`: Standard Normal (Gaussian) Distribution
print("\n--- 2.2 `np.random.randn()`: Standard Normal (Gaussian) Distribution ---")
# Generates numbers from the 'standard normal' distribution (mean=0, variance=1).
# Arguments specify the dimensions of the array.

randn_scalar = np.random.randn()
print(f"Single random float (standard normal): {randn_scalar}")

randn_1d = np.random.randn(5)
print(f"1D array (5 elements, standard normal):\n{randn_1d}")

randn_2d = np.random.randn(3, 2)
print(f"2D array (3x2, standard normal):\n{randn_2d}")

# 2.3 `np.random.randint(low, high=None, size=None, dtype=int)`: Random Integers
print("\n--- 2.3 `np.random.randint()`: Random Integers ---")
# Generates random integers.
# `low`: Inclusive lower bound.
# `high`: Exclusive upper bound (if `high` is None, integers are from 0 to `low-1`).
# `size`: Shape of the output array.

rand_int_scalar = np.random.randint(10) # 0 to 9
print(f"Single random integer (0 to 9): {rand_int_scalar}")

rand_int_range = np.random.randint(5, 15) # 5 to 14
print(f"Single random integer (5 to 14): {rand_int_range}")

rand_int_1d = np.random.randint(0, 100, size=7)
print(f"1D array (7 elements, 0-99): {rand_int_1d}")

rand_int_2d = np.random.randint(1, 10, size=(3, 3))
print(f"2D array (3x3, 1-9):\n{rand_int_2d}")

# 2.4 `np.random.choice(a, size=None, replace=True, p=None)`: Random Selection
print("\n--- 2.4 `np.random.choice()`: Random Selection from an Array/List ---")
# Generates random samples from a given 1-D array or list.
# `a`: The array/list to choose from.
# `size`: Shape of the output array.
# `replace`: Whether to sample with replacement (True, default) or without replacement (False).
# `p`: Probabilities associated with each entry in `a`.

elements = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Elements to choose from: {elements}")

choice_single = np.random.choice(elements)
print(f"Single random choice: {choice_single}")

choice_multiple_replace = np.random.choice(elements, size=3, replace=True)
print(f"Multiple choices (with replacement, size 3): {choice_multiple_replace}")

try:
    choice_multiple_no_replace = np.random.choice(elements, size=5, replace=False)
    print(f"Multiple choices (without replacement, size 5): {choice_multiple_no_replace}")

    # Trying to choose more elements than available without replacement will cause an error
    # choice_error = np.random.choice(elements, size=6, replace=False) # This would raise ValueError
except ValueError as e:
    print(f"Caught expected error when choosing too many without replacement: {e}")

# Choice with probabilities
choice_weighted = np.random.choice(['heads', 'tails'], size=10, p=[0.7, 0.3])
print(f"10 coin flips with 70% heads probability: {choice_weighted}")


# --- 3. More Specific Distributions ---
print("\n--- 3. More Specific Distributions ---")

# 3.1 `np.random.normal(loc=0.0, scale=1.0, size=None)`: Normal (Gaussian) Distribution
print("\n--- 3.1 `np.random.normal()`: Normal (Gaussian) Distribution ---")
# Generates numbers from a normal distribution.
# `loc`: Mean of the distribution.
# `scale`: Standard deviation of the distribution.

normal_dist = np.random.normal(loc=10, scale=2, size=10000) # Mean 10, std dev 2
print(f"Sample from normal distribution (first 5): {normal_dist[:5]}")
print(f"Mean of samples: {np.mean(normal_dist):.2f}")
print(f"Standard deviation of samples: {np.std(normal_dist):.2f}")

# Visualization (if Matplotlib is available)
if plt:
    plt.figure(figsize=(8, 4))
    sns.histplot(normal_dist, bins=50, kde=True)
    plt.title('Histogram of Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()


# 3.2 `np.random.uniform(low=0.0, high=1.0, size=None)`: Uniform Distribution
print("\n--- 3.2 `np.random.uniform()`: Uniform Distribution ---")
# Generates numbers from a uniform distribution over [low, high).

uniform_dist = np.random.uniform(low=-5, high=5, size=10000)
print(f"Sample from uniform distribution [-5, 5) (first 5): {uniform_dist[:5]}")
print(f"Mean of samples: {np.mean(uniform_dist):.2f}")
print(f"Min of samples: {np.min(uniform_dist):.2f}")
print(f"Max of samples: {np.max(uniform_dist):.2f}")

# Visualization (if Matplotlib is available)
if plt:
    plt.figure(figsize=(8, 4))
    sns.histplot(uniform_dist, bins=50, kde=True)
    plt.title('Histogram of Uniform Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()


# 3.3 `np.random.poisson(lam=1.0, size=None)`: Poisson Distribution
print("\n--- 3.3 `np.random.poisson()`: Poisson Distribution ---")
# Generates random samples from a Poisson distribution.
# `lam`: Expectation of interval, must be >= 0.

poisson_dist = np.random.poisson(lam=5, size=10000) # Average rate of 5 events
print(f"Sample from Poisson distribution (first 5): {poisson_dist[:5]}")
print(f"Mean of samples: {np.mean(poisson_dist):.2f} (should be close to lam)")

# Visualization (if Matplotlib is available)
if plt:
    plt.figure(figsize=(8, 4))
    sns.histplot(poisson_dist, bins=np.arange(0, 15), discrete=True, stat='density')
    plt.title('Histogram of Poisson Distribution')
    plt.xlabel('Number of Events')
    plt.ylabel('Probability Density')
    plt.show()


# 3.4 `np.random.binomial(n, p, size=None)`: Binomial Distribution
print("\n--- 3.4 `np.random.binomial()`: Binomial Distribution ---")
# Generates random samples from a binomial distribution.
# `n`: Number of trials.
# `p`: Probability of success in each trial.

binomial_dist = np.random.binomial(n=10, p=0.5, size=10000) # 10 coin flips, 50% chance of heads
print(f"Sample from Binomial distribution (first 5): {binomial_dist[:5]}")
print(f"Mean of samples: {np.mean(binomial_dist):.2f} (should be close to n*p)")

# Visualization (if Matplotlib is available)
if plt:
    plt.figure(figsize=(8, 4))
    sns.histplot(binomial_dist, bins=np.arange(-0.5, 11.5, 1), discrete=True, stat='density')
    plt.title('Histogram of Binomial Distribution (10 flips, p=0.5)')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability Density')
    plt.show()

# --- 4. Permutations and Shuffling ---
print("\n--- 4. Permutations and Shuffling ---")

# 4.1 `np.random.shuffle(x)`: Shuffles an array *in-place*
arr_shuffle = np.array([1, 2, 3, 4, 5])
print(f"\nOriginal array before shuffle: {arr_shuffle}")
np.random.shuffle(arr_shuffle)
print(f"Array after shuffle (in-place): {arr_shuffle}")

# 4.2 `np.random.permutation(x)`: Returns a *new* permuted array (or range)
arr_permute = np.array([10, 20, 30, 40, 50])
permuted_arr = np.random.permutation(arr_permute)
print(f"\nOriginal array before permutation: {arr_permute}")
print(f"New permuted array: {permuted_arr}")

permuted_range = np.random.permutation(5) # Permutation of range(5)
print(f"Permutation of range(5): {permuted_range}")


# --- 5. Random State Management (`np.random.RandomState`) ---
print("\n--- 5. Random State Management (`np.random.RandomState`) ---")
print("For more control and isolated randomness, use a `RandomState` object.")
print("This is useful in functions or classes where you want to ensure reproducibility")
print("without affecting the global NumPy random state.")

rng1 = np.random.RandomState(123)
rng2 = np.random.RandomState(123) # Same seed as rng1

print(f"\nRandom numbers from rng1 (seed 123):")
print(rng1.rand(3))

print(f"Random numbers from rng2 (seed 123, same sequence):")
print(rng2.rand(3))

rng_different = np.random.RandomState(456)
print(f"Random numbers from rng_different (seed 456):")
print(rng_different.rand(3))

# Global random state is unaffected by RandomState instances
print(f"Global random state after using RandomState: {np.random.rand()}")


print("\n--- End of NumPy Random Arrays Practice Code ---")