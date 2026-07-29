# Student ID: devdom5222
# Date: july-21-2024

def computeTotal(scores):
    # Initialize total to 0
    total = 0

    # Use a for loop to accumulate the total score
    for score in scores:
        total += score

    # Return the total score
    return total

# Main program

# Declare an array to store 9 golf scores
scores = [0] * 9

# Use a for loop to get user input for all 9 holes
for i in range(9):
    scores[i] = int(input(f"Enter score for hole {i + 1}: "))

# Call the function to compute the total score and store the result
total_score = computeTotal(scores)

# Use a for loop to display each hole score
print("Scores for each hole:")
for i in range(9):
    print(f"Hole {i + 1}: {scores[i]}")

# Display the total score
print(f"Total score: {total_score}")
