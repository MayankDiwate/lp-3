def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Initialize the dynamic programming table
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    weights = []
    values = []

    print("Enter the weights of items:")
    for _ in range(n):
        weights.append(int(input()))

    print("Enter the values of items:")
    for _ in range(n):
        values.append(int(input()))

    capacity = int(input("Enter the knapsack capacity: "))

    max_value = knapsack(weights, values, capacity)
    print(f"Maximum value that can be obtained: {max_value}")































# Enter the number of items: 3
# Enter the weights of items:
# 2
# 3
# 4
# Enter the values of items:
# 3
# 4
# 5
# Enter the knapsack capacity: 5
