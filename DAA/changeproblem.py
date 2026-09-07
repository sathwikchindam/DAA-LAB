import time

# ============================================================
# MAKING CHANGE PROBLEM USING DYNAMIC PROGRAMMING
# ============================================================

def making_change(coins, amount):

    # dp[i] stores the minimum number of coins
    # required to make amount i
    dp = [float('inf')] * (amount + 1)

    # Base condition
    dp[0] = 0

    # Calculate minimum coins for each amount
    for i in range(1, amount + 1):

        for coin in coins:

            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


# Input
coins = list(map(int, input("Enter coin denominations: ").split()))
amount = int(input("Enter the amount: "))

# Measure execution time
start_time = time.perf_counter()

result = making_change(coins, amount)

end_time = time.perf_counter()

execution_time = end_time - start_time


# Output
print("\n--- Making Change Using Dynamic Programming ---")

if result == float('inf'):
    print("Change cannot be made.")
else:
    print("Minimum number of coins =", result)

print("Execution Time =", execution_time, "seconds")


# Time Analysis
print("\nTime Complexity:")
print("Best Case    : O(n * amount)")
print("Average Case : O(n * amount)")
print("Worst Case   : O(n * amount)")
print("Space Complexity: O(amount)")