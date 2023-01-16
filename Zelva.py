from turtle import exitonclick
from turtle import forward
from turtle import left
from turtle import right
from math import sqrt
import random


def draw_house(a):

    c = (sqrt(2)*a)
    forward(a)
    left(90)
    forward(a)
    left(135)
    forward(c)
    left(225)
    forward(a)
    right(90)
    forward(a)
    left(135)
    forward(c/2)
    left(90)
    forward(c/2)
    left(90)
    forward(c)
    left(135)
    forward(a)
    forward(a/2)
    left(90)
    forward(a/5)
    left(90)
    forward(a/2-a/5)
    left(45)
    forward(c/5)
    right(45)
    forward(a)
    left(90)


for i in range(3):
    cislo = (random.randint(100,300))
    draw_house(cislo)

exitonclick()

