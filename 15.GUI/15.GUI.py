import random
from turtle import Turtle, Screen

# johnny_the_turtle = Turtle()
# johnny_the_turtle.shape("turtle")
# johnny_the_turtle.color("red")
# johnny_the_turtle.forward(100)
# johnny_the_turtle.right(90)
#
# for _ in range(15):
#     johnny_the_turtle.forward(10)
#     johnny_the_turtle.penup()
#     johnny_the_turtle.forward(10)
#     johnny_the_turtle.pendown()
tim = Turtle()

color = [ "medium aquamarine",  "DarkOrchid", "DeepSkyBlue", "wheat", "SlateGrey", "SeaGreen"]

def draw_shape(num_side):
    for _ in range(num_side):
        angle = 360 / num_side
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(color))
    draw_shape(shape_side_n)
screen = Screen()
screen.exitonclick()
