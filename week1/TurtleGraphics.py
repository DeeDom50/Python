import turtle

turtle.write("devdom5222") 

# Create a square of length 100 (blue color)
turtle.color("blue")
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

# Create a circle of size 50 (green color)
turtle.color("green")
turtle.circle(50)

# Create an octagon (stop sign shape) with sides of length 50 (red color)
turtle.color("red")
for _ in range(8):
    turtle.forward(50)
    turtle.right(45)

# Ensures the window stays open until manually closed
turtle.done()