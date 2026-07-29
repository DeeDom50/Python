import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Say HI with Turtle")

# Set up the turtle
t = turtle.Turtle()
## t.hideturtle()

# Function to draw the letter H
def draw_H():
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.backward(100)

# Function to draw the letter I
def draw_I():
    t.penup()
    t.goto(0, 0)  # Start position for I
    t.pendown()
    t.forward(100)  # Draw vertical line
    t.backward(100)  # Move back to top
    t.right(90)  # Turn right to draw top and bottom lines
    t.forward(25)  # Draw top line
    t.backward(50)  # Move back to the middle
    t.forward(25)  # Draw bottom line
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(25)
    t.backward(50)
    t.forward(25)
    t.right(90)
    
# Draw letters "H" and "I" to spell "HI"
draw_H()
t.penup()
t.forward(100)  # Move forward to add space between letters
t.pendown()
draw_I()

# Keep the window open
screen.mainloop()
