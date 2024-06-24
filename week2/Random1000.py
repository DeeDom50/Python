import random

# Initialize an empty list
num_list = []
index = 0

print("devdom5222")

# Generate and append 1000 random numbers to the list
print("Adding 1000 random numbers to the list:")
while index < 1000:
    num_list.append(random.randint(1, 100))
    index += 1

# Sort the list of numbers
num_list.sort()

# Print the sorted numbers using a for loop
print("Here are the sorted numbers:")
for num in num_list:
    print(num)