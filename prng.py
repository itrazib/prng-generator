import numpy as np
import matplotlib.pyplot as plt

# Simple LCG function
def lcg(n, seed=42):
    a = 1664525
    c = 1013904223
    m = 2**32
    x = seed
    numbers = []
    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x / m)
    return numbers

# Generate PRNG numbers
rand_nums = lcg(10000)

# Plot histogram
plt.figure(figsize=(12, 5))

# Histogram for uniformity
plt.subplot(1, 2, 1)
plt.hist(rand_nums, bins=50, color='skyblue', edgecolor='black')
plt.title("Histogram (Uniformity Check)")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Scatter plot for dependency
plt.subplot(1, 2, 2)
plt.scatter(rand_nums[:-1], rand_nums[1:], s=1, alpha=0.5)
plt.title("Scatter Plot (Dependency Check)")
plt.xlabel("X[n]")
plt.ylabel("X[n+1]")

plt.tight_layout()
plt.show()