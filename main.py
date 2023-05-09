from turtle import *
from colorsys import *
bgcolor("Black")
tracer(78)
pensize(2)
h = 0
for i in range(200):
    c = hsv_to_rgb(h, 1, 1)
    h += 0.005
    color(c)
    up()
    goto(-8, 25)
    down()
    penup()
    fd(i)
    rt(89)
    pendown()
    fillcolor(c)
    begin_fill()
    circle(90, 100)
    end_fill()
    lt(179)
    penup()
    bk(i/2)
    pendown()
    lt(6)
done()
