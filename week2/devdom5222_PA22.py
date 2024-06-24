import random

# Initialize an empty list
num_list = []

# Append 100 random numbers to the list
for i in range(1000):
    num_list.append(random.randint(1, 100))

# Print the original list of numbers
print("Original List:")
print(num_list)

# Sort the list
num_list.sort()

# Print the sorted list of numbers
print("\nSorted List:")
print(num_list)