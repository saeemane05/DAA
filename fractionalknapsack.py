# Fractional Knapsack

n = int(input("Enter number of items: "))

weight = []
value = []
ratio = []

for i in range(n):
    w = int(input("Enter weight: "))
    v = int(input("Enter value: "))

    weight.append(w)
    value.append(v)

    r = v / w
    ratio.append(r)


capacity = int(input("Enter knapsack capacity: "))

# Sort items by ratio
for i in range(n):
    for j in range(i + 1, n):

        if ratio[i] < ratio[j]:

            ratio[i], ratio[j] = ratio[j], ratio[i]
            weight[i], weight[j] = weight[j], weight[i]
            value[i], value[j] = value[j], value[i]


total = 0

for i in range(n):

    if capacity == 0:
        break

    if weight[i] <= capacity:
        total = total + value[i]
        capacity = capacity - weight[i]

    else:
        total = total + ratio[i] * capacity
        capacity = 0


print("Maximum Value:", total)