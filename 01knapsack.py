# 0/1 Knapsack

n = int(input("Enter number of items: "))

weight = []
value = []

for i in range(n):
    w = int(input("Enter weight: "))
    v = int(input("Enter value: "))

    weight.append(w)
    value.append(v)


capacity = int(input("Enter capacity: "))

# Create DP table
dp = []

for i in range(n + 1):
    row = []

    for j in range(capacity + 1):
        row.append(0)

    dp.append(row)


# Fill DP table
for i in range(1, n + 1):

    for j in range(capacity + 1):

        if weight[i - 1] <= j:

            include = value[i - 1] + dp[i - 1][j - weight[i - 1]]
            exclude = dp[i - 1][j]

            if include > exclude:
                dp[i][j] = include
            else:
                dp[i][j] = exclude

        else:
            dp[i][j] = dp[i - 1][j]


print("Maximum Value:", dp[n][capacity])