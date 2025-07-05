from turtle import*
import colorsys
bgcolor('black')
pensize(3)
speed(0.2)

for i in range(15):
    color=colorsys.hsv_to_rgb(1,0,1)
    circle(i)
    right(90)
    left(35)
    circle(120,220)
    backward(360-i)
