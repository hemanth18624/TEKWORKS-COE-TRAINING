# Sample list of tuples
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sort the list by the last element of each tuple
sorted_list = sorted(sample_list, key=lambda x: x[-1])

# Print the result
print("Sorted List:", sorted_list)
