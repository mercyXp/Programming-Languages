num = int(input("Enter a number: "))

if num > 1:  # Prime numbers must be greater than 1
    is_prime = True  # Assume it's prime until proven otherwise
    for i in range(2, int(num**0.5) + 1): # only check up to the square root of num
        if (num % i) == 0:
            is_prime = False # It's divisible by something other than 1 and itself
            break  # No need to check further

    if is_prime:
        print("prime")
    else:
        print("not prime")
else:
    print("not prime") # 1 and numbers less than 1 are not prime