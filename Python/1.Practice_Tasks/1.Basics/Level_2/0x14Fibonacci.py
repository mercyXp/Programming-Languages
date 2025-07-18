N = int(input("Enter a number: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1
count = 0

print(f"First {N} Fibonacci numbers:")

# Use while loop to print Fibonacci numbers
while count < N:
    print(a)
    a, b = b, a + b
    count += 1