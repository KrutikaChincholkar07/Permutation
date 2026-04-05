# Function to calculate factorial
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i  # multiply numbers
    return fact

# Taking input
n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

# Permutation formula P(n,r) = n!/(n-r)!
result = factorial(n) // factorial(n - r)

# Display result
print("Permutation P(", n, ",", r, ") =", result)
