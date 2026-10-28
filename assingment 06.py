
# 0/1 Knapsack Problem

def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def knapsack_top_down(weights, values, capacity):
    n = len(weights)
    memo = {}

    def solve(i, w):
        if i == n or w == 0:
            return 0

        if (i, w) in memo:
            return memo[(i, w)]

        # Exclude current item
        exclude = solve(i + 1, w)

        # Include current item if it fits
        include = 0
        if weights[i] <= w:
            include = values[i] + solve(
                i + 1, w - weights[i]
            )

        memo[(i, w)] = max(include, exclude)
        return memo[(i, w)]

    return solve(0, capacity)


# Input
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

# Results
print("Bottom-Up Maximum Value:",
      knapsack_bottom_up(weights, values, capacity))

print("Top-Down Maximum Value:",
      knapsack_top_down(weights, values, capacity))
