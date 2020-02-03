import turtle


def main():
    turtle.hideturtle()
    square(100, 0, 100, "red")
    square(100, -100, 100, "yellow")
    square(100, -200, 100, "green")

# square function draws a square and the x and y parameters
# are the coordinates of the lower-left corner. the width
# parameter is the width of each side. the colour parameter
# is the fill colour, as a string


def square(x, y, width, color):
    turtle.penup()                      # raises pen
    turtle.goto(x, y)                    # move to the specified location
    turtle.fillcolor(color)             # set the fill colour
    turtle.pendown()                    # lowers pen
    turtle.begin_fill()                 # start filling
    for count in range(4):              # draw a square
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()                   # end filling
# call the main function


main()
