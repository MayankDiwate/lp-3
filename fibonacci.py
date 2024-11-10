# Recursive Fibonacci Calculation
def recfib(n, s):
    s[0] += 1
    if n <= 1:
        return n
    return recfib(n - 1, s) + recfib(n - 2, s)

# Non-Recursive Fibonacci Calculation
def nonrecfib(n, s):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        s[0] += 1
        a, b = b, a + b
    return b

# Generate a List of Fibonacci Numbers using Recursive Calculation
def reclist(n):
    f = []
    s = [0]  # To track the number of recursive calls
    for i in range(n):
        s[0] = 0
        f.append(recfib(i, s))
    return f

# Generate a List of Fibonacci Numbers using Non-Recursive Calculation
def nonreclist(n):
    f = []
    s = [0]  # To track the number of recursive calls
    for i in range(n):
        s[0] = 0
        f.append(nonrecfib(i, s))
    return f

# Main function
if __name__ == "__main__":
    count = int(input("Enter the number of Fibonacci numbers to generate: "))
    print("Choose the Fibonacci calculation method:")
    print("1. Recursive")
    print("2. Non-Recursive")
    
    choice = int(input("Enter 1 or 2: "))
    
    if choice == 1:
        recursive_fib_list = reclist(count)
        print("\nRecursive Fibonacci Numbers:", recursive_fib_list)
    elif choice == 2:
        non_recursive_fib_list = nonreclist(count)
        print("\nNon-Recursive Fibonacci Numbers:", non_recursive_fib_list)
    else:
        print("Invalid choice! Please enter 1 for Recursive or 2 for Non-Recursive.")
