from turtle import *
from math import *
from random import *

bgcolor('black')

color = ['gold2','peru','lawngreen','sienna1','seagreen1','blue','purple','green']
speed(0)
pensize(5)

def body(follow,like,share,kreggs,code,love,me):
    pu()
    poss(follow,like)
    pd()
    for i in range(love):
        fillcolor(color[i%7])
        begin_fill()
        rt(kreggs)
        fd(share)
        circle(me,180+(kreggs*2))
        fd(share)
        rt(180-kreggs)
        end_fill()
    pu()
    poss(follow,like)
    pd()
    dot((code*1.3)+10, 'black')
    dot((code*1.3), 'gold2')
    pu()

def poss(follow,like):
    home()
    goto(follow,like)

def eye(r):
    lt(45)
    for i in range(2):
        fillcolor('black')
        begin_fill()
        circle(r,90)
        circle(r/2,90)
        end_fill()
    lt(45)
    fd(r/5)
    dot(r/2,'white')
    pu()
    lt(30)
    fd(r)
    pd()
    dot(r,'white')

def eyes(follow,like,code):
    poss(follow,like)
    fd(code/3.6)
    lt(90)
    fd(code/5)
    rt(90)
    pd()
    eye(code/12)
    pu()
    poss(follow,like)
    bk(code/3.6)
    lt(90)
    fd(code/5)
    rt(90)
    pd()
    eye(code/12)

def mouth(follow,like,r):
    pu()
    poss(follow,like)
    pd()
    fillcolor('lawngreen')
    begin_fill()
    pu()
    fd(r)
    pd()
    lt(165)
    circle(r*4,30)
    lt(90+15)
    fd(r)
    circle(r*0.60,120)
    fd(r)
    end_fill()

def kreggscode(x1,y1,code):
    me = code/3.75
    follow=100
    like=100
    share = sqrt(pow(me,2) + pow(code,2))
    kreggs = int(round(degrees(atan2(me, code))))
    love = ceil(360/(kreggs*2))
    body(x1,y1,share,kreggs,code,love,me)
    eyes(x1,y1,code)
    mouth(x1,y1,code/2.25)

min = -500
max = 500
love = 70

for i in range(love):
    kreggscode(randint(min, max),randint(min, max),randint(30,150))