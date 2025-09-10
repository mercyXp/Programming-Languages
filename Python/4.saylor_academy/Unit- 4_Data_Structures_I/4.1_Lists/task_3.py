color = ['Red', 'Green', 'Black']

print("Original List: ", color)

color = [v for elt in color for v in ('c', elt)]
print("Updated List: ", color)
