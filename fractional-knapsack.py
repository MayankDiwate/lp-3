def fractional_knapsack(items, capacity):
    # Calculate value-to-weight ratios and sort items by these ratios in descending order
    items.sort(key=lambda x: x[2] / x[1], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    print("\nItems selected for the knapsack:")

    for item in items:
        name, weight, value = item
        if weight <= remaining_capacity:
            print(f"{name} (100%)")
            total_value += value
            remaining_capacity -= weight
        else:
            fraction = remaining_capacity / weight
            print(f"{name} ({fraction * 100:.2f}%)")
            total_value += fraction * value
            break

    print(f"\nMaximum value achievable: {total_value:.2f}")

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    items = []

    for i in range(n):
        name = input(f"Enter the name of item {i + 1}: ")
        weight = float(input(f"Enter the weight of item {i + 1}: "))
        value = float(input(f"Enter the value of item {i + 1}: "))
        items.append((name, weight, value))

    capacity = float(input("Enter the maximum capacity of the knapsack: "))
    fractional_knapsack(items, capacity)





























# Enter the number of items: 3
# Enter the name of item 1: Gold
# Enter the weight of item 1: 10
# Enter the value of item 1: 60
# Enter the name of item 2: Silver
# Enter the weight of item 2: 20
# Enter the value of item 2: 100
# Enter the name of item 3: Diamond
# Enter the weight of item 3: 30
# Enter the value of item 3: 120
# Enter the maximum capacity of the knapsack: 50
