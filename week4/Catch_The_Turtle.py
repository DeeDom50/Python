import turtle
import random
import colorsys

# Set up turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Initialize a list of 200 turtles
chasers = []
for i in range(200):
    chaser = turtle.Turtle()
    chaser.shape("turtle")
    hue = i / 200
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    chaser.color(color)
    chaser.penup()
    chaser.speed(0)
    x = random.randint(-screen.window_width()//2, screen.window_width()//2)
    y = random.randint(-screen.window_height()//2, screen.window_height()//2)
    chaser.goto(x, y)
    chasers.append(chaser)

# Function to move the 200 turtles
def move_turtles():
    for i in range(len(chasers)):
        if i == 0:
            target = chasers[-1]
        else:
            target = chasers[i - 1]
        chasers[i].setheading(chasers[i].towards(target))
        chasers[i].forward(2)
    screen.update()
    screen.ontimer(move_turtles, 0)

# Call the function
screen.tracer(0)
move_turtles()
screen.mainloop()

