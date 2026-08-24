import time

# ============================================================
# FACTORIAL USING ITERATIVE METHOD
# ============================================================

def factorial_iterative(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


# Input
n = int(input("Enter a number: "))

# Measure execution time
start_time = time.perf_counter()

result = factorial_iterative(n)

end_time = time.perf_counter()

execution_time = end_time - start_time

# Output
print("\n--- Iterative Method ---")
print("Factorial =", result)
print("Execution Time =", execution_time, "seconds")

# Time Analysis
print("Time Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n)")
print("Worst Case   : O(n)")
print("Space Complexity: O(1)")


# ============================================================
# FACTORIAL USING RECURSIVE METHOD
# ============================================================

def factorial_recursive(n):
    # Base condition
    if n == 0 or n == 1:
        return 1

    # Recursive call
    return n * factorial_recursive(n - 1)


# Measure execution time
start_time = time.perf_counter()

result = factorial_recursive(n)

end_time = time.perf_counter()

execution_time = end_time - start_time

# Output
print("\n--- Recursive Method ---")
print("Factorial =", result)
print("Execution Time =", execution_time, "seconds")

# Time Analysis
print("Time Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n)")
print("Worst Case   : O(n)")
print("Space Complexity: O(n)")