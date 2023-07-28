def findMaxCarrots(field):
    rows = len(field)
    cols = len(field[0])

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    dp[0][0] = field[0][0]

    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + field[0][j]

    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + field[i][0]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + field[i][j]

    maxCarrots = dp[rows-1][cols-1]

    return maxCarrots

# Example usage with the sample input
field = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

maxCarrots = findMaxCarrots(field)
print("Maximum carrots the rabbit can eat:", maxCarrots)