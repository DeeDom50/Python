import os
import subprocess

# Print student ID
print("Student ID: devdom5222")

# Ask for the picture file from the user
image_path = input("Enter the path to the image: ")

# Open the image with the default image viewer on macOS
try:
    subprocess.run(['open', image_path])
    print(f"Opening {image_path} in the default image viewer...")
except Exception as e:
    print(f"An error occurred: {e}")

