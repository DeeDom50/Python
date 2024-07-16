import turtle

def square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

def circle(size):
    turtle.circle(size)

def triangle(size):
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

def display_student_id(student_id):
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.write(f"Your student ID is {student_id}", align="center", font=("Arial", 16, "normal"))

# Get user input
student_id = input("Enter your student ID: ")
square_size = int(input("Enter the size of the square: "))
circle_size = int(input("Enter the size of the circle: "))
triangle_size = int(input("Enter the size of the triangle: "))

# Print student ID
print(student_id)

# Draw shapes
square(square_size)
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()
circle(circle_size)
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()
triangle(triangle_size)

# Display student ID
display_student_id(student_id)

# Keep the window open
turtle.done()
