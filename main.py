import turtle
from turtle import Turtle
from turtle import Screen
import random
turtle.colormode(255)

# import colorgram
#
# colors = colorgram.extract("image.jpg", 84)
# color_list = []
#
# for color in colors:
#     current_color = color
#     current_item = (current_color.rgb[0], current_color.rgb[1], current_color.rgb[2])
#     color_list.append(current_item)
#
# print(color_list)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

tim = Turtle()
tim.penup()
tim.goto(-225, -250)
tim.pendown()
tim.speed("fastest")
tim.hideturtle()


def print_line():
    for _ in range(10):
        rgb = random.choice(color_list)
        tim.dot(20, rgb)
        tim.penup()
        tim.forward(50)
        tim.pendown()


def next_line():
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)

for _ in range(10):
    print_line()
    next_line()

my_screen = Screen()
my_screen.exitonclick()
