import random

numbers = [random.randint(1,10) for _ in range (10)]

print(numbers)

numbers[2] = 9
numbers[-2] = 0 #replacing the last 2 elements with 0

print(numbers)