import turtle

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

square(100)
