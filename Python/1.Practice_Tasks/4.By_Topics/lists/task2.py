import random

numbers = [random.randint(1,10) for _ in range (10)]

print(numbers)
print(numbers[0])
print(numbers[len(numbers)//2])
print(numbers[-1])