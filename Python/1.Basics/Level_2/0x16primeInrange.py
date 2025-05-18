# Program to print all prime numbers in a given range using nested loops

# Get the range from user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Prime numbers between {start} and {end} are:")

# Outer loop: check each number in the range
for num in range(start, end + 1):
    # Prime numbers are greater than 1
    if num > 1:
        # Assume number is prime initially
        is_prime = True
        
        # Inner loop: check for factors
        for i in range(2, num):
            if num % i == 0:
                # Found a factor, not a prime number
                is_prime = False
                break  # No need to check further
        
        # If no factors found, it's a prime number
        if is_prime:
            print(num, end=' ')

print()  # For new line after output