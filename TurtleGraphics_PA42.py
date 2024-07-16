import turtle

def square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def circle():
    turtle.circle(50)

def triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

# Print student ID
print("devdom5222")

# Draw shapes
square()
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()
circle()
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()
triangle()

# Keep the window open
turtle.done()
