import turtle;

# Set up the screen
screen = turtle.Screen()
screen.title("Writing to Turtle")

# Set up the turtle
t = turtle.Turtle()
t.hideturtle()

# Customize appearance
t.color("blue")
style = ("Courier", 30, "italic")

# Write text
t.write("Hello, Turtle!", font=style, align="center")

# Keep the window open
screen.mainloop()
