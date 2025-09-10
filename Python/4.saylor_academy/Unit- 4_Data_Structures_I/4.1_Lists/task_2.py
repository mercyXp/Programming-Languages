import collections # for counting hashable objects

list = [10, 7, 9, 10, 14, 5, 5, 6, 7, 10]
print("Original list:", list)

count = collections.Counter(list)
print("Frequency of elements in the list:", count)