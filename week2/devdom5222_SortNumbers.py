# Initialize an empty list
num_list = []
index = 0

print("devdom5222")

# Get 5 numbers from the user
print("Enter 5 numbers:")
while index < 5:
    num_list.append(int(input()))
    index += 1

# Sort the numbers in ascending order
num_list.sort()

# Print the sorted numbers
print("Here are the numbers in order:")
for num in num_list:
    print(num)