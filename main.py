import turtle as t
import random

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
rows = 10
columns = 10
distance = 50
radius = 20

pen = t.Turtle()
t.colormode(255)
pen.hideturtle()
pen.penup()
pen.setposition(-335,300)
pen.speed(15)


def next_row(pen):
    x_pos = pen.position()[0]
    y_pos = pen.position()[1]
    pen.setposition(x_pos-700, y_pos-70)


def paint_row(pen):
    pen.pendown()
    pen.color(random.choice(color_list))
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()
    pen.penup()
    pen.forward(70)
    pass


for _ in range(rows):
    for _ in range(columns):
        paint_row(pen)
    next_row(pen)


screen = t.Screen()
screen.exitonclick()